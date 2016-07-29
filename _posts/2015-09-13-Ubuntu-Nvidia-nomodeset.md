---
layout: post
title:  "Ubuntu 설치시 Nvidia 그래픽카드 충돌문제 해결법"
categories: linux
---

Ubuntu 설치 이미지가 대부분의 그래픽 드라이버를 잘 지원하기는 하지만, 때때로 Nvidia 그래픽카드가 내장된
컴퓨터에 설치시 이미지안에 들어있는 커널 드라이버와 호환성이 좋지 않아 그래픽이 깨져보이는 현상을 겪을 수 있습니다.

이럴때는 설치 후 Nvidia에서 제공하는 드라이버를 설치하면 해결되지만, 아예 부팅시 먹통이 되는 경우가 생기면
난감하게 됩니다.

이럴때는 부팅시 커널에서 사용하는 그래픽 모드를 사용하지 않도록 해주면 낮은 해상도로 부팅이 가능하게 됩니다.
Ubuntu 부팅시에 왼쪽 shift 키를 누르고 있으면 부팅 메뉴 모드로 들어갈 수 있습니다.

이제 2가지 방법중 하나를 통해서 부팅하고 최신 Nvidia 그래픽 드라이버를 찾아서 설치해주면 됩니다.

#### 부팅 커널의 옵션 바로 수정
메뉴에서 화살표로 부팅할 커널로 옮긴다음 'e' 문자를 누르면 부팅 옵션 수정이 가능합니다.

```
linux /boot/vmlinuz-linux ..... quiet splash nomodeset
```

여기서 맨끝에 nomodeset 추가 후 부팅

#### Grub 설정 수정
메뉴에서 아예 복구 모드로 들어가 root shell 를 띄운다음에 grub 부팅 옵션을 아래와 같이 수정해 줍니다.

```
> sudo vi /etc/default/grub

GRUB_CMDLINE_LINUX_DEFAULT="quiet splash nomodeset"

> sudo update-grub2
```
