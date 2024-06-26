#!/bin/bash
sudo docker run -dit --name server01 --network lamport-network -p 50051:50051 grpc-server1
sudo docker run -dit --name server02 --network lamport-network -p 50052:50052 grpc-server2
sudo docker run -dit --name server03 --network lamport-network -p 50053:50053 grpc-server3
sudo docker run -dit --name server04 --network lamport-network -p 50054:50054 grpc-server4
sudo docker run -dit --name server05 --network lamport-network -p 50055:50055 grpc-server5