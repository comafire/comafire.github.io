---
layout: post
title: "OSX에 Cuda사용 가능하도록 Tensorflow 소스 컴파일 설치 Cuda"
tags:
    - tensorflow
    - python
---

## Macbook Pro 에서 Cuda 사용 가능하도록 Tensorflow 설치

### Macbook Pro 2014-Mid
* CPU: 2.5 GHz Intel Core i7
* RAM: 16GB 1600 MHz DDR3
* GPU: NVIDIA GeForce GT 750M 2048 MB
* OSX: El Capitan 10.11.5

### Tensorflow Source Compile Install with Cuda on OSX
OSX 에서는 기본적으로 Cuda 를 지원하는 바이너리 패키지가 없이 때문에 컴파일을 통해서 패키지를 만들어 설치합니다.

소스컴파일을 위한 의존성 패키지, python 은 2.7 사용을 권장합니다.

```
> brew install bazel swig coreutils
> sudo easy_install -U six
> sudo easy_install -U numpy
> sudo easy_install wheel
> sudo easy_install ipython
```

brew 를 통해 cuda 7.5 버전 설치

```
> brew update
> brew tap caskroom/cask
> brew cask install cuda
> brew cask info cuda
cuda: 7.5.27
Nvidia CUDA
https://developer.nvidia.com/cuda-zone
/usr/local/Caskroom/cuda/7.5.27 (23 files, 1.0G)
https://github.com/caskroom/homebrew-cask/blob/master/Casks/cuda.rb
No Artifact Info
```

tensorflow 0.9 컴파일 후 실행시 tensorflow 는 libcuda.1.dylib 라이브러리를 찾는데, 실제 cuda 패키지의 cuda 라이브러리 이름은 libcuda.dylib 이라서 segmentation fault 11 에러를 내면서 실행이 되지 않습니다. 이 에러를 방지하기 위해 심볼릭 링크를 추가로 걸어줍니다.

```
> cd /usr/local/cuda/lib
> sudo ln -s libcuda.dylib libcuda.1.dylib
```

다음으로 Nvidia 에서 제공하는 cudnn (https://developer.nvidia.com/cudnn)을 설치합니다.(다운로드시에 로그인이 필요)

```
> cd ~/Downloads
> tar -zvxf cudnn-7.5-osx-x64-v5.1-rc.tgz
> cd cuda
> sudo mv include/cudnn.h /Developer/NVIDIA/CUDA-7.5/include/
> sudo mv lib/libcudnn* /Developer/NVIDIA/CUDA-7.5/lib
> sudo ln -s /Developer/NVIDIA/CUDA-7.5/lib/libcudnn* /usr/local/cuda/lib/
```

설치 후 cudnn 라이브러리를 사용하기 위하여 shell 환경 변수 등록

```
> vi ~/.bash_profile

export CUDA_HOME=/usr/local/cuda
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:$CUDA_HOME/lib"
export PATH="$CUDA_HOME/bin:$PATH"

> source ~/.bash_profile
```

Cuda 사용 가능을 검증하기 위해 Cuda 패키지에서 제공되는 Sample 을 컴파일해서 실행 시켜봅니다.

```
> cd /usr/local/cuda/samples
> sudo make -C 1_Utilities/deviceQuery
> ./bin/x86_64/darwin/release/deviceQuery

./bin/x86_64/darwin/release/deviceQuery Starting...

CUDA Device Query (Runtime API) version (CUDART static linking)

Detected 1 CUDA Capable device(s)

Device 0: "GeForce GT 750M"
  CUDA Driver Version / Runtime Version          7.5 / 7.5
  CUDA Capability Major/Minor version number:    3.0
  Total amount of global memory:                 2048 MBytes (2147024896 bytes)
  ( 2) Multiprocessors, (192) CUDA Cores/MP:     384 CUDA Cores
  GPU Max Clock rate:                            926 MHz (0.93 GHz)
  Memory Clock rate:                             2508 Mhz
  Memory Bus Width:                              128-bit
  L2 Cache Size:                                 262144 bytes
...
deviceQuery, CUDA Driver = CUDART, CUDA Driver Version = 7.5, CUDA Runtime Version = 7.5, NumDevs = 1, Device0 = GeForce GT 750M
Result = PASS
```

tensorflow 소스 다운로드, 패키지 빌드 및 설치

```
> git clone https://github.com/tensorflow/tensorflow
> cd tensorflow
> ./configure
Please specify the location of python. [Default is /usr/local/bin/python]:
Do you wish to build TensorFlow with Google Cloud Platform support? [y/N]
No Google Cloud Platform support will be enabled for TensorFlow
Do you wish to build TensorFlow with GPU support? [y/N] y
GPU support will be enabled for TensorFlow
Please specify which gcc nvcc should use as the host compiler. [Default is /usr/bin/gcc]:
Please specify the Cuda SDK version you want to use, e.g. 7.0. [Leave empty to use system default]: 7.5
Please specify the location where CUDA 7.5 toolkit is installed. Refer to README.md for more details. [Default is /usr/local/cuda]:
Please specify the Cudnn version you want to use. [Leave empty to use system default]: 5
Please specify the location where cuDNN 5 library is installed. Refer to README.md for more details. [Default is /usr/local/cuda]:
Please specify a list of comma-separated Cuda compute capabilities you want to build with.
You can find the compute capability of your device at: https://developer.nvidia.com/cuda-gpus.
Please note that each additional compute capability significantly increases your build time and binary size.
[Default is: "3.5,5.2"]: 3.5
Setting up Cuda include
Setting up Cuda lib
Setting up Cuda bin
Setting up Cuda nvvm
Setting up CUPTI include
Setting up CUPTI lib64
Configuration finished
> bazel build -c opt --config=cuda //tensorflow/tools/pip_package:build_pip_package
> bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg
> sudo pip install /tmp/tensorflow_pkg/tensorflow-0.9.0-py2-none-any.whl
```

tensorflow 샘플 테스트

```
> cd tensorflow/models/image/mnist
> python convolutional.py
...
I tensorflow/core/common_runtime/gpu/gpu_init.cc:102] Found device 0 with properties:
name: GeForce GT 750M
major: 3 minor: 0 memoryClockRate (GHz) 0.9255
pciBusID 0000:01:00.0
Total memory: 2.00GiB
Free memory: 64.40MiB
I tensorflow/core/common_runtime/gpu/gpu_init.cc:126] DMA: 0
I tensorflow/core/common_runtime/gpu/gpu_init.cc:136] 0:   Y
I tensorflow/core/common_runtime/gpu/gpu_device.cc:813] Ignoring gpu device (device: 0, name: GeForce GT 750M, pci bus id: 0000:01:00.0) with Cuda compute capability 3.0. The minimum required Cuda capability is 3.5.
Initialized!
Step 0 (epoch 0.00), 3.5 ms
Minibatch loss: 12.054, learning rate: 0.010000
Minibatch error: 90.6%
Validation error: 84.6%
...
```
