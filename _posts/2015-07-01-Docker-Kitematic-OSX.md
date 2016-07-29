---
layout: post
title:  "Mac OSX에서 Kitematic으로 Docker편하게 쓰기"
categories: docker
---

## Kitematic
Docker는 Host OS로 Linux만 지원합니다.
OSX에서 Docker를 사용하기 위해서는 Virtual Box위에 Docker를 실행시키기 위한 최소한의 기능만을 담고 있는 Linux인 CoreOS를 Boot2Docker라는 툴을 이용하여 사용합니다.

Boot2Docker가 command기반이고 Linux에서 Docker를 사용하는 것과 달리 Virtual Box라는 하나의 층이 더 있기 때문에 OSX의 로컬 스토리지 및 네트워크 포트를 맵핑해주는 것이 귀찮은 것이 사실입니다.

Docker에서 인수한 Kitematic은 OSX에서 Docker의 설치 및 설정을 GUI를 통해서 간단하게 할수 있도록 해줍니다.

HomePage: https://kitematic.com/

### Install
설치는 OSX용 package를 다운받아 압축을 푼 후에 Application 폴더에 떨구면 끝입니다.
실행하면 Docker 실행에 필요한 모든 것들을 자동으로 설치합니다.

![screen shot 01 ](https://raw.githubusercontent.com/reachlab-kr/reachlab-kr.github.io/master/_images/2015-07-01-Docker-Kitematic-OSX-01.png)

설치가 끝나고 Docker Hub를 통해 계정 생성을 마치면 바로 Docker 컨테이너 실행이 가능합니다.

![screen shot 02 ](https://raw.githubusercontent.com/reachlab-kr/reachlab-kr.github.io/master/_images/2015-07-01-Docker-Kitematic-OSX-02.png)

### Docker Tutorial
Docker 자체에 대한 개념 및 내용은 [가장 빨리 만나는 Docker (이재홍)](http://pyrasis.com/docker.html)을 참조하세요.

### Kitematic Tutorial
Kitematic에 대한 상세 내용은 [Kitematic Document](https://kitematic.com/docs/)를 참조하세요.
Tutorial 섹션에서 Nginx, Minecraft, RethinkDB 에 대한 예제를 자세히 볼수 있습니다.

여기서는 Ubuntu 14.04 + Torch7 + iTorch 를 가지는 이미지를 Kitematic으로 만들어 보겠습니다.
필요한 모든 파일은 Github [reachlab-kr/docker-itorch](https://github.com/reachlab-kr/docker-itorch)에 있으므로 해당 프로젝트를 clone해 사용해봅니다.

Docker Client 콘솔에서 스크립트를 수행하면 Kitematic에서 itorch 컨테이너가 생성된 것을 볼수 있습니다.

```
> git clone https://github.com/reachlab-kr/docker-itorch
> cd docker-itorch
> ./build.sh
> ./create.sh
```

![screen shot 03 ](https://raw.githubusercontent.com/reachlab-kr/reachlab-kr.github.io/master/_images/2015-07-01-Docker-Kitematic-OSX-03.png)

브라우저를 통한 접속은 ACCESS URL을 통해 iTorch에 접속이 가능하게 됩니다.

![screen shot 04 ](https://raw.githubusercontent.com/reachlab-kr/reachlab-kr.github.io/master/_images/2015-07-01-Docker-Kitematic-OSX-04.png)

해당 이미지는 Docker Hub에도 올라가 있으므로 Hub에서 직접 CREATE 하여 사용하는 것도 가능합니다.

![screen shot 05 ](https://raw.githubusercontent.com/reachlab-kr/reachlab-kr.github.io/master/_images/2015-07-01-Docker-Kitematic-OSX-05.png)
