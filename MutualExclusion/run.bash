#!/bin/bash
sudo docker build -t lock-client -f ./client/Dockerfile .
sudo docker run -d --name lock-client1 --network distributed-net lock-client
sudo docker run -d --name lock-client2 --network distributed-net lock-client
sudo docker run -d --name lock-client3 --network distributed-net lock-client
sudo docker run -d --name lock-client4 --network distributed-net lock-client
