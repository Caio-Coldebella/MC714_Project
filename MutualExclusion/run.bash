#!/bin/bash
sudo docker build --build-arg ID=client-1 -t lock-client1 -f ./client/Dockerfile .
sudo docker build --build-arg ID=client-2 -t lock-client2 -f ./client/Dockerfile .
sudo docker build --build-arg ID=client-3 -t lock-client3 -f ./client/Dockerfile .

sudo docker run -d --name lock-client1 --network distributed-net lock-client1
sudo docker run -d --name lock-client2 --network distributed-net lock-client2
sudo docker run -d --name lock-client3 --network distributed-net lock-client3
