#!/bin/bash
pip install -r requirements.txt
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. lamport.proto
sudo docker network create lamport-network
sudo docker build --build-arg ADDRESS=50051 --build-arg FREQUENCY=1 -t grpc-server1 .
sudo docker build --build-arg ADDRESS=50052 --build-arg FREQUENCY=2 -t grpc-server2 .
sudo docker build --build-arg ADDRESS=50053 --build-arg FREQUENCY=3 -t grpc-server3 .
sudo docker build --build-arg ADDRESS=50054 --build-arg FREQUENCY=4 -t grpc-server4 .
sudo docker build --build-arg ADDRESS=50055 --build-arg FREQUENCY=5 -t grpc-server5 .