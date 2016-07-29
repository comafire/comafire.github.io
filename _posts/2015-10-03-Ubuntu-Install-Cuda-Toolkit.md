---
layout: post
title:  "Ubuntu 14.04 에 cuda toolkit 설치하기"
categories: linux
---

우부투에서 Nvidia 그래픽 카드의 Cuda Toolkit 설치하기

Cuda 툴킷 저장소 파일 받기

```
> wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1404/x86_64/cuda-repo-ubuntu1404_7.5-18_amd64.deb
2015-10-03 07:51:47 (252 MB/s) - ‘cuda-repo-ubuntu1404_7.5-18_amd64.deb’ saved
```

Cuda 툴킷 저장소 우분투에 등록

```
> sudo dpkg -i cuda-repo-ubuntu1404_7.5-18_amd64.deb
Selecting previously unselected package cuda-repo-ubuntu1404.
...
OK

> sudo apt-get update
...
Hit http://security.ubuntu.com trusty-security/universe Translation-en         
Fetched 1,222 kB in 7s (169 kB/s)                                              
Reading package lists... Done
```

Cuda 설치

```
> sudo apt-get install cuda
...
After this operation, 2,195 MB of additional disk space will be used.
Do you want to continue? [Y/n] Y
...
done.
```

쉘에 환경 설정 추가

```
> vi ~/.bashrc
export CUDA_HOME=/usr/local/cuda
export LD_LIBRARY_PATH=$CUDA_HOME/lib64  
export PATH=$CUDA_HOME/bin:$PATH
> source ~/.basrc
```

설치확인

```
> nvidia-smi
+------------------------------------------------------+                       
| NVIDIA-SMI 352.39     Driver Version: 352.39         |                       
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX TIT...  Off  | 0000:06:00.0     Off |                  N/A |
|  0%   50C    P0    59W / 250W |     23MiB / 12284MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
```
