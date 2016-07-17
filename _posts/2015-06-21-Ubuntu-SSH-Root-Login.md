---
layout: post
title:  "Ubuntu 14.04 SSH Root Login"
categories: linux
---

우분투에 SSH를 통해 root로 접속하기

## Root 계정 활성화
일반 계정으로 접속뒤 아래와 같이 root 계정의 passwd 를 설정하여 계정을 활성화합니다.

```
> sudo passwd root
```

## SSH 인증 설정
기본적으로 root 접속은 보안상 막혀있으므로 아래와 같이 풀어주고 SSH를 다시 실행시켜 줍니다.

```
> sudo vi /etc/ssh/sshd_config

...

LoginGraceTime 120
PermitRootLogin without-password
StrictModes yes
without-password를 yes로 변경하고 ssh를 다시 시작합니다.

...

> sudo service ssh restart
```
