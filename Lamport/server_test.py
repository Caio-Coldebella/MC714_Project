from concurrent import futures
import grpc
import lamport_pb2
import lamport_pb2_grpc
from argparse import ArgumentParser
import threading
import time
import random

process = None

class LamportProcess(lamport_pb2_grpc.LamportServiceServicer):
    def __init__(self, frequency, address):
        self.logical_clock = 0
        self.frequency = frequency
        self.address = address

    def increment_clock(self):
        self.logical_clock += self.frequency

    def update_clock(self, received_clock):
        self.logical_clock = max(self.logical_clock, received_clock) + 1

    def ResolveEvent(self, request, context):
        self.update_clock(request.logical_clock)
        print(f"Received message: {request.message} with logical clock {request.logical_clock} in address {self.address}")
        return lamport_pb2.EventResponse(logical_clock=self.logical_clock)

    def SendMessage(self, message, address):
        self.channel = grpc.insecure_channel(address)
        self.stub = lamport_pb2_grpc.LamportServiceStub(self.channel)

        self.increment_clock()

        request = lamport_pb2.EventRequest(logical_clock=self.logical_clock, message=message)
        response = self.stub.ResolveEvent(request)

        self.update_clock(response.logical_clock)

        print(f"Sent message: {message} with logical clock {self.logical_clock} to address {address}")
        print(f"Updated logical clock after response: {self.logical_clock}")

def serve(address, frequency):
    global process
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    process = LamportProcess(frequency, address)
    lamport_pb2_grpc.add_LamportServiceServicer_to_server(process, server)
    server.add_insecure_port(f'[::]:{address}')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-f', '--frequency', type=int)
    parser.add_argument('-a', '--address', type=int)
    args = parser.parse_args()

    # Lista de portas para os servidores locais
    ports = [50051, 50052, 50053]

    # Remover a porta atual da lista de servidores
    current_port = args.address
    servers = [f"localhost:{port}" for port in ports if port != current_port]

    grpc_thread = threading.Thread(target=serve, args=(current_port, args.frequency))
    grpc_thread.start()

    request_time = int(random.random() * 30) + 5
    while True:
        time.sleep(request_time)
        if process is not None:
            server_to_send_message = random.choice(servers)
            try:
                print(f"Sending message to {server_to_send_message}")
                process.SendMessage('Event', server_to_send_message)
            except Exception as e:
                print(f"Failed to send message to {server_to_send_message}: {e}")
