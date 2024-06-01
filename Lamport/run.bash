#!/bin/bash
END=$1
for i in $(seq 1 $END);
do 
	python3 client.py
done

