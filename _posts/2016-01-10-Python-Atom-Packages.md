---
layout: post
title:  "Atom을 Python 개발 툴로 사용하기"
categories: python
---

Python로 프로그래밍시 주로 Pycharm이나 Jupyter(iPython)를 사용하였지만,
Pycharm은 강력한 기능대비 개인 사용자가 아니면 유료라는 점이 아쉬웠고,
Jupyter는 있는 모듈을 사용하여 간단한 데모용으로는 아주 훌륭하였지만 긴 프로그램을 짜기에는 뭔가 아쉬운
부분이 있는 것이 사실 이었습니다.

이런 부분에 있어 개발자용 에디터 Atom 은 많은 기능을 제공하는 데 그 중 Python 개발 툴로 활용해 보겠습니다.

설치는 간단합니다.

Atom 에디터에서 Preference -> Install 메뉴에 들어가서 아래 2개의 패키지를 설치합니다.

* autocomplete-python (https://atom.io/packages/autocomplete-python)
* script (https://atom.io/packages/script)

OSX 에서는 script 패키지에서 python 명령을 찾기 못하기때문에 꼭 콘솔 상에서 아래 명령으로 실행해 줘야
환경 변수 내에 python 명령을 인식하게 됩니다. 이부분은 좀 귀찮은 부분입니다.

```
> atom .
```

이제 Atom 에디터에서 test.py 파일을 하나 만들어 보겠습니다.

```
import sys

for i in range(len(sys.argv)):
  print "sys.argv[%d] = '%s'" % (i, sys.argv[i])
```

간단하게 명령행 옵션을 받아서 출력해 보는 프로그램입니다.
해당 파일을 저장하고 해당 파일을 Atom 에디터 상에서 단축키로 바로 실행 시켜 볼 수 있습니다.
단축키는 아래 웹페이지를 참고하세요
https://atom.io/packages/script

저는 OSX를 사용하고 있기 때문에 cmd + i 단축키를 사용하였습니다.

![screen shot](https://raw.githubusercontent.com/reachlab-kr/reachlab-kr.github.io/master/_images/2016-01-10-Python-Atom-Packages-01.png)

cmd + i 는 명령행 옵션을 줄 수 없으므로 명령행 옵션을 주고 실행시키키 위해서는 shift + cmd + i 단축키를
이용하면 여려 옵션들을 넣을 수 있는 창이 뜨고 넣고 싶은 값을 넣고 Run 버튼을 누르면 실행됩니다.

![screen shot](https://raw.githubusercontent.com/reachlab-kr/reachlab-kr.github.io/master/_images/2016-01-10-Python-Atom-Packages-02.png)
