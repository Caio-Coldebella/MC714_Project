#!/bin/bash
sudo docker stop $(docker ps -a -q)
sudo docker rm $(docker ps -a -q)
sudo docker rmi lock-client
sudo docker rmi mutualexclusion-lock-manager