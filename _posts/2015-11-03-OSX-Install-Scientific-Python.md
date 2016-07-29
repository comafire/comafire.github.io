---
layout: post
title:  "OSX에서 Scientific Python 설치"
categories: OSX
---

OSX에 Data Scientific을 위한 Python 설치 스크립트 메모

참조: https://joernhees.de/blog/2014/02/25/scientific-python-on-mac-os-x-10-9-with-homebrew/

### Homebrew 설치
http://brew.sh 를 방문하여 ruby 스크립트를 복사해서 실행합니다.

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### Scientific Python Package 설치

```
# set up some taps and update brew
brew tap homebrew/science # a lot of cool formulae for scientific tools
brew tap homebrew/python # numpy, scipy, matplotlib, ...
brew update && brew upgrade

# install a brewed python
brew install python

# install PIL, imagemagick, graphviz and other
# image generating stuff
brew install libtiff libjpeg webp little-cms2
pip install Pillow
brew install imagemagick --with-fftw --with-librsvg --with-x11
brew install graphviz --with-librsvg --with-x11
brew install cairo
brew install py2cairo # this will ask you to download xquartz and install it
brew install qt pyqt

# install virtualenv, nose (unittests & doctests on steroids)
pip install virtualenv
pip install nose

# install numpy and scipy
# there are two ways to install numpy and scipy now: via pip or via brew.
# PICK ONE, i prefer pip for proper virtualenv support and more up-to-date versions.
pip install numpy
pip install scipy
# OR:
# (if you want to run numpy and scipy with openblas also remove comments below:)
#brew install openblas
brew install numpy # --with-openblas
brew install scipy # --with-openblas

# test the numpy & scipy install
python -c 'import numpy ; numpy.test();'
python -c 'import scipy ; scipy.test();'

# some cool python libs (if you don't know them, look them up)
# matplotlib: generate plots
# pandas: time series stuff
# nltk: natural language toolkit
# sympy: symbolic maths in python
# q: fancy debugging output
# snakeviz: cool visualization of profiling output (aka what's taking so long?)
#brew install Caskroom/cask/mactex  # if you want to install matplotlib with tex support and don't have mactex installed already
brew install matplotlib --with-cairo --with-tex  # cairo: png ps pdf svg filetypes, tex: tex fonts & formula in plots
pip install pandas
pip install nltk
pip install sympy
pip install q
pip install snakeviz
pip install scikit-learn

# ipython with parallel and notebook support
brew install zmq
pip install ipython[all]

# html stuff (parsing)
pip install html5lib cssselect pyquery lxml BeautifulSoup

# webapps / apis (choose what you like)
pip install Flask Django tornado

# semantic web stuff: rdf & sparql
pip install rdflib SPARQLWrapper

# graphs (graph metrics, social network analysis, layouting)
pip install networkx

# maintenance: updating of pip libs
pip list --outdated  # see Updating section below
```

### Scientific Python Package 업데이트

설치 후 최신 패키지로 유지하기

brew update

```
brew update && brew outdated && brew upgrade --all
```

pip update

--outdated 옵션으로 리스트 확인 후에 -U 옵션으로 업그레이드

```
pip list --outdated
pip install -U package1 package2 ...
```
