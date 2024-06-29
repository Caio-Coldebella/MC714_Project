from argparse import ArgumentParser

import grpc
import time
import threading
from concurrent import futures
import leader_election_pb2
import leader_election_pb2_grpc


class Node(leader_election_pb2_grpc.ElectionServicer):
    def __init__(self, node_ip, node_ips, port):
        self.port = port
        self.node_ip = node_ip
        self.node_ips = node_ips
        self.leader_id = None
        self.is_participating = False
        self.is_leader = False
        self.heartbeat_interval = 2
        self.heartbeat_timeout = 5
        self.last_heartbeat = time.time()

    def start(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        leader_election_pb2_grpc.add_ElectionServicer_to_server(self, server)
        server.add_insecure_port(f'{self.node_ip}:{port}')
        server.start()
        threading.Thread(target=self.send_heartbeat).start()
        threading.Thread(target=self.check_leader).start()
        self.initiate_election()
        server.wait_for_termination()

    def Elect(self, request, context):
        sender_id = request.node_id
        if sender_id < self.node_ip:
            self.initiate_election()
            return leader_election_pb2.ElectionResponse(ok=True)
        return leader_election_pb2.ElectionResponse(ok=False)

    def AnnounceLeader(self, request, context):
        self.leader_id = request.leader_id
        self.is_leader = self.node_ip == self.leader_id
        self.last_heartbeat = time.time()
        print(f"Node {self.node_ip} recognizes {self.leader_id} as leader")
        return leader_election_pb2.LeaderResponse(ok=True)

    def initiate_election(self):
        self.is_participating = True
        print(f"Node {self.node_ip} initiating election")
        higher_nodes = [node for node in self.node_ips if node > self.node_ip]
        if not higher_nodes:
            self.declare_victory()
        else:
            for node in higher_nodes:
                with grpc.insecure_channel(f'{node}:{port}') as channel:
                    stub = leader_election_pb2_grpc.ElectionStub(channel)
                    try:
                        response = stub.Elect(leader_election_pb2.ElectionRequest(node_id=self.node_ip))
                        if response.ok:
                            self.is_participating = True
                    except grpc.RpcError:
                        continue
            time.sleep(1)
            if not self.leader_id:
                self.declare_victory()

    def declare_victory(self):
        self.leader_id = self.node_ip
        self.is_leader = True
        for node in self.node_ips:
            if node != self.node_ip:
                with grpc.insecure_channel(f'{node}:{port}') as channel:
                    stub = leader_election_pb2_grpc.ElectionStub(channel)
                    try:
                        stub.AnnounceLeader(leader_election_pb2.LeaderRequest(leader_id=self.leader_id))
                    except grpc.RpcError:
                        continue
        print(f"Node {self.node_ip} is the new leader")

    def send_heartbeat(self):
        while True:
            if self.is_leader:
                for node in self.node_ips:
                    if node != self.node_ip:
                        with grpc.insecure_channel(f'{node}:{port}') as channel:
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
                    print(f"Node {self.node_ip} detected leader failure")
                    self.leader_id = None
                    self.initiate_election()
            time.sleep(1)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-i', '--ip')
    parser.add_argument('-a', '--address')
    args = parser.parse_args()

    node_ips = [
        "10.158.0.6",
        "10.158.0.5",
        "10.158.0.7"
    ]
    node_ip = args.ip
    port = args.address
    node = Node(node_ip, node_ips, port)
    node.start()
