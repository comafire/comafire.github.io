#!/bin/bash

CWD=$(pwd)

cd docker && docker build --tag comafire/jupyter:1 .

cd $CWD
