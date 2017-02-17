#!/bin/bash

CWD=$(pwd)

#docker run -i -t --name jupyter -d -p 8888:8888 -v $CWD/volume:/root/volume comafire/jupyter:1
docker rm -f jupyter
docker run -i -t --name jupyter -d -p 7777:8888 -v $CWD:/root/volume comafire/jupyter:1
docker rm -f tensorboard 
docker run -i -t --name tensorboard -d -p 7007:6006 -v $CWD:/root/volume comafire/jupyter:1 tensorboard --logdir /root/volume/logs


cd $CWD
