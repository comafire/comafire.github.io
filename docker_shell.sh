#!/bin/sh

docker rm -f shell
docker run -i -t --name shell comafire/jupyter:1 /bin/bash
