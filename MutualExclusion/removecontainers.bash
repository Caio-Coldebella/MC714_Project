#!/bin/bash
sudo docker stop $(docker ps -a -q)
sudo docker rm $(docker ps -a -q)
sudo docker rmi lock-client1
sudo docker rmi lock-client2
sudo docker rmi lock-client3
sudo docker rmi mutualexclusion-lock-manager