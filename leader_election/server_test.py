import grpc
import time
import threading
from concurrent import futures
import leader_election_pb2
import leader_election_pb2_grpc


class Node(leader_election_pb2_grpc.ElectionServicer):
    def __init__(self, node_id, nodes):
        self.node_id = node_id
        self.nodes = nodes
        self.leader_id = None
        self.is_participating = False
        self.is_leader = False
        self.heartbeat_interval = 2
        self.heartbeat_timeout = 5
        self.last_heartbeat = time.time()

    def start(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        leader_election_pb2_grpc.add_ElectionServicer_to_server(self, server)
        server.add_insecure_port(f'[::]:{5000 + self.node_id}')
        server.start()
        threading.Thread(target=self.send_heartbeat).start()
        threading.Thread(target=self.check_leader).start()
        self.initiate_election()
        server.wait_for_termination()

    def Elect(self, request, context):
        sender_id = request.node_id
        if sender_id < self.node_id:
            self.initiate_election()
            return leader_election_pb2.ElectionResponse(ok=True)
        return leader_election_pb2.ElectionResponse(ok=False)

    def AnnounceLeader(self, request, context):
        self.leader_id = request.leader_id
        self.is_leader = self.node_id == self.leader_id
        self.last_heartbeat = time.time()
        print(f"Node {self.node_id} recognizes {self.leader_id} as leader")
        return leader_election_pb2.LeaderResponse(ok=True)

    def initiate_election(self):
        self.is_participating = True
        print(f"Node {self.node_id} initiating election")
        higher_nodes = [node for node in self.nodes if node > self.node_id]
        if not higher_nodes:
            self.declare_victory()
        else:
            for node in higher_nodes:
                with grpc.insecure_channel(f'localhost:{5000 + node}') as channel:
                    stub = leader_election_pb2_grpc.ElectionStub(channel)
                    try:
                        response = stub.Elect(leader_election_pb2.ElectionRequest(node_id=self.node_id))
                        if response.ok:
                            self.is_participating = True
                    except grpc.RpcError:
                        continue
            time.sleep(1)
            if not self.leader_id:
                self.declare_victory()

    def declare_victory(self):
        self.leader_id = self.node_id
        self.is_leader = True
        for node in self.nodes:
            if node != self.node_id:
                with grpc.insecure_channel(f'localhost:{5000 + node}') as channel:
                    stub = leader_election_pb2_grpc.ElectionStub(channel)
                    try:
                        stub.AnnounceLeader(leader_election_pb2.LeaderRequest(leader_id=self.leader_id))
                    except grpc.RpcError:
                        continue
        print(f"Node {self.node_id} is the new leader")

    def send_heartbeat(self):
        while True:
            if self.is_leader:
                for node in self.nodes:
                    if node != self.node_id:
                        with grpc.insecure_channel(f'localhost:{5000 + node}') as channel:
                            stub = leader_election_pb2_grpc.ElectionStub(channel)
                            try:
                                stub.AnnounceLeader(leader_election_pb2.LeaderRequest(leader_id=self.leader_id))
                            except grpc.RpcError:
                                continue
            time.sleep(self.heartbeat_interval)

    def check_leader(self):
        while True:
            if not self.is_leader and self.leader_id:
                if time.time() - self.last_heartbeat > self.heartbeat_timeout:
                    print(f"Node {self.node_id} detected leader failure")
                    self.leader_id = None
                    self.initiate_election()
            time.sleep(1)


if __name__ == "__main__":
    import sys
    nodes = [1, 2, 3]
    node_id = int(sys.argv[1])
    node = Node(node_id, nodes)
    node.start()
