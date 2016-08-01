---
layout: post
title:  "Atom을 Julia 개발 툴로 사용하기"
categories: julia
---

지금까지 Julia로 프로그래밍시 주로 Jupyter를 이용하였습니다.
Jupyter는 있는 모듈을 사용해서 간단히 보여주는 용도로는 훌륭하지만,
실제 프로그래밍을 하기에는 아쉬운 것이 사실 이었습니다.

이 점이 항상 아쉬웠는데 Atom 에디터에 Julia 개발 툴 패키지가 올라왔습니다.

http://junolab.org/

설치는 간단합니다.

Julia에 Atom 패키지를 설치하면 의존성 패키지가 모두 설치됩니다.

```
> julia
_
_       _ _(_)_     |  A fresh approach to technical computing
(_)     | (_) (_)    |  Documentation: http://docs.julialang.org
_ _   _| |_  __ _   |  Type "?help" for help.
| | | | | | |/ _` |  |
| | |_| | | | (_| |  |  Version 0.4.2 (2015-12-06 21:47 UTC)
_/ |\__'_|_|_|\__'_|  |  Official http://julialang.org release
|__/                   |  x86_64-linux-gnu

julia> Pkg.add("Atom")
julia> Pkg.update()
```

그 다음에 Atom 에디터에서 Preference -> Install 메뉴에 들어가서 uber-juno 패키지를 설치합니다.

* uber-juno (https://github.com/JunoLab/uber-juno/blob/master/setup.md)

이후 Atom 에디터에서 확장자가 .jl 을 가지는 파일을 생성하고
Ctrl + \` 키를 이용하여 Julia Console 을 띄워 결과를 바로 확인해가면서
개발이 가능합니다.

![ink demo](https://github.com/JunoLab/atom-ink/raw/readme/demos/full.gif)
