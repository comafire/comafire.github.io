#!/bin/bash

CWD=$(pwd)

docker rm -f tensorboard 
docker run -i -t --name tensorboard -d -p 7007:6006 -v $CWD:/root/volume comafire/jupyter:1 tensorboard --logdir /root/volume/logs


cd $CWD
