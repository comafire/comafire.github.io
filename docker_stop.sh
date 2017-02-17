#!/bin/bash

CWD=$(pwd)

docker rm -f jupyter
docker rm -f tensorboard 

cd $CWD
