---
layout: post
title:  "Docker에서 Proxy 및 SSL Certificates 설정"
categories: docker
---

Docker 사용시 네트워크에 Proxy 및 Self Signed SSL Certification 을 사용하도록 되어 있는 곳에서는 Docker Hub에서 Docker 이미지를 검색하고 내려받을때 접속 에러와 'x509: certificate signed by unknown authority' 에러를 만나게 됩니다.

이럴때는 proxy 및 SSL Certification 아래와 같이 설정합니다.

## Proxy 설정
/etc/default/docker.io 파일에서 proxy 설정 후에 docker service 를 재실행합니다.

```
> sudo vi /etc/default/docker.io
...
export http_proxy="http://<proxy_ip>:<proxy_port>"
export https_proxy="https://<proxy_ip>:<proxy_port>"
...
> sudo service docker.io restart
```

## SSL Certification 설정
Self Signed Certification 파일을 예를 들어 Self.crt 라고 한다면, 해당 파일을 /usr/local/share/ca-certificates 에 복사하고 update-ca-certificates 명령으로 업데이트 해줍니다.

```
> sudo cp ./Self.crt /usr/local/share/ca-certificates/
> sudo update-ca-certificates
> sudo service docker.io restart
```
