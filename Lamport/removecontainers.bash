#!/bin/bash
sudo docker stop $(docker ps -a -q)
sudo docker rm $(docker ps -a -q)
sudo fuser -k 50051/tcp
sudo fuser -k 50052/tcp
sudo fuser -k 50053/tcp
sudo fuser -k 50054/tcp
sudo fuser -k 50055/tcp