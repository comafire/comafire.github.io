---
layout: post
title:  "OSX에서 GO개발환경 만들기"
categories: jekyll update
---

## Brew 설치

Brew는 OSX 에서는 제공하지 않지만, Unix/Linux 환경에서 돌아가는 많은 유용한 유틸들을 설치 할 수 있는 패키지 매니저라 할수 있습니다.
http://brew.sh/index_ko.html

터미널 상에서 아래 명령으로 설치 가능

```
> ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
```

## Brew 상에서 Go 설치

```
> brew install go
```

문서 작성 당시 Go 버전은 1.2 이고 brew 를 통해 설치하면 /usr/local/Cellar/go/1.2 해당 디렉토리에 설치가 된다. go 바이너리는 /usr/local/bin 에 심볼릭 링크로 처리됩니다.

## Go 환경 변수 설정

Go 를 이용하여 컴파일을 하기 위한 환경 설정, 계정의 .profile 파일에서 환경 설정을 해줍니다.

```
> vi ~/.bash_profile
```

```
export GO=/usr/local/Cellar/go/1.2/libexec
export PATH=$GO/bin:$PATH

export GOROOT=$GO
export GOPATH=/Users/comafire/Development/go/workspace/Sopark
export PATH=$PATH:$GOPATH/bin
```

Brew 를 통해 go 를 설치할 경우 package 들이 libexec 밑에 설치되므로 GO 환경 변수의 Path 는 libexec 밑이 됩니다. GOPATH 의 경우 자신이 수행할 개발 디렉토리 Path 를 지정해주면 됩니다.

위에서 설정한 것들을 현재 적용시키기 위해서 아래 명령을 수행해줍니다.

```
> source ~/.bash_profile
```

## Go 개발을 위한 vim 설정

Go 를 개발하는데 있어 2-3 종류의 IDE 들이 나와있기는 하지만, 거의 기능이 제한적이라 Command 기반의 개발에 익숙해져야 합니다. Go 에서는 vim 과 emacs 의 플러인을 제공하는데 vim 이 익숙하여 vim 기반으로 설정하기로 하였습니다.

### Vim 플러그인 관리자 Vundle 설치

기존에 Vim 플러그인 설치에는 많은 노력이 들어갔었지만, 지금은 이 프로젝트 때문에 편해졌습니다.
https://github.com/gmarik/vundle
사용법 참조: http://kldp.org/node/125263
Go 설정에 필요한 플러그인들을 편하게 설치하기 위해 우선 설치합니다.

```
> git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle
> vi ~/.vimrc
```

```
set nocompatible              " be iMproved
filetype off                  " required!

set rtp+=~/.vim/bundle/vundle/
call vundle#rc()

" let Vundle manage Vundle
" required!
Bundle 'gmarik/vundle'

" My bundles here:
"
" original repos on GitHub
Bundle 'tpope/vim-fugitive'
Bundle 'Lokaltog/vim-easymotion'
Bundle 'rstacruz/sparkup', {'rtp': 'vim/'}
Bundle 'tpope/vim-rails.git'
" vim-scripts repos
Bundle 'L9'
Bundle 'FuzzyFinder'
" non-GitHub repos
Bundle 'git://git.wincent.com/command-t.git'
" Git repos on your local machine (i.e. when working on your own plugin)

filetype plugin indent on     " required!
"
" Brief help
" :BundleList          - list configured bundles
" :BundleInstall(!)    - install (update) bundles
" :BundleSearch(!) foo - search (or refresh cache first) for foo
" :BundleClean(!)      - confirm (or auto-approve) removal of unused bundles
"
" see :h vundle for more details or wiki for FAQ
" NOTE: comments after Bundle commands are not allowed.
```

위와 같이 .vimrc 에 설정을 추가하면 설치가 끝난것이다.

## Go 언어의 공식 Vim  플러그인

Go 언어 설치 디렉토리의 misc 에는 Go 언어에서 제공하는 vim 플러그인이 있습니다.

```
> cd /usr/local/Cellar/go/1.2/libexec/misc/vim
> vi ~/.vimrc
```

```
set tabstop=2

filetype off
filetype plugin indent off
set runtimepath+=$GOROOT/misc/vim
filetype plugin indent on
syntax on

autocmd FileType go autocmd BufWritePre <buffer> Fmt
```

.vimrc 파일에 위부분을 추가하면 Go 에서 제공하는 모든 플러그인을 사용하고 추가적으로 Go 언어 소스를 수정하고 vim 을 닫을 때 자동으로 gofmt 를 수정하여 소스를 Go 언어의 문법에 맞게 수정해주게 됩니다.

### Gocode + SuperTab

Gocode: https://github.com/nsf/gocode
Go code 는 Daemon 기반으로 Go 언어의 함수 자동완성 기능을 vim 에서 쓸수 있게 해주는 유용한 플러그인입니다.

![enter image description here][1]

![enter image description here][2]

이를 설치하기 위해서 GOPATH 환경 변수로 설정한 프로젝트 디렉토리로 이동합니다.

```
> cd $GOPATH
> mkdir src
> mkdir bin
> go get -u github.com/nsf/gocode
> cd ./src/github.com/nsf/gocode/vim
> ./update.sh
```

위 명령을 수행하면 bin 디렉토리안에 gocode 가 빌드되 설치되고 vim 플러그인이 설치됩니다.
다음으로 .vimrc 에 아래 구문을 추가해 줍니다.

```
> vi ~/.vimrc
```

```
filetype plugin on
```

이제 ctrl+x 후 ctrl+o 를 누르면 스크린 샷과 같은 함수 자동 완성 기능을 사용할 수 있습니다. 매번 함수정의를 보기 위해서는 ctrl+x 누른 후 ctrl+o 를 눌러야 하는데 여간 불편하지 않습니다.

그래서 SuperTab 플러그인을 통해 Tab 키를 누르면 위 두 동작을 자동으로 수행하게 해주도록 합니다.
SuperTab: https://github.com/ervandew/supertab

설치는 Vundle 에서 할수 있습니다. .vimrc 파일을 열고 명령 모드에서 :Bundle SuperTab 을 입력하여 플러그인을 설치하고 .vimrc 중간과 끝에 아래 구문을 추가해주면 됩니다.

```
> vi ~/.vimrc
```

```
...
...
" My bundles here:
Bundle 'SuperTab'
...
...
" for SuperTab
let g:SuperTabDefaultCompletionType = "<c-x><c-o>"
```

이제 부터는 Go 자동 완성 기능을 Tab 키로 사용할 수 있습니다.

### NERD Tree
https://github.com/scrooloose/nerdtree
이 플러그인은 IDE 의 소스트리를 보여주는 창처럼 vi 의 왼쪽에 소스트리 창을 띄워주는 플러그인입니다.
여러 소스를 옮겨가면서 작업할때 유용한 플러그인으로 <F3> 에 맵핑합니다.

설치는 Vundle 로..

```
> vi ~/.vimrc
```

```
…
…
" My bundles here:
Bundle 'SuperTab'
Bundle 'The-NERD-tree'
…
...
" for NERDTree
" "au VimEnter * NERDTreeToggle
nmap <F3> :NERDTreeToggle<CR>
```

위와 같이 설정하면 아래와 같이 소스트리를 볼수 있습니다.

![enter image description here][3]

### gotags and Tagbar
vim 을 통해서 Go 소스 탐색을 쉽게 하기 위한 설정. $GOPATH 로 이동하여 gotags 를 설지합니다.

```
> cd $GOPATH
> go get -u github.com/jstemmer/gotags
```

.vimrc 를 열고 Vundle 을 통해서 Tagbar 를 설치후 아래와 같이 설정을 추가해줍니다.

```
> vi ~/.vimrc
```

```
…
" My bundles here:
Bundle 'SuperTab'  
Bundle 'The-NERD-tree'
Bundle 'Tagbar'
…
" for gotags
let g:tagbar_type_go = {
    \ 'ctagstype' : 'go',
    \ 'kinds'     : [
        \ 'p:package',
        \ 'i:imports:1',
        \ 'c:constants',
        \ 'v:variables',
        \ 't:types',
        \ 'n:interfaces',
        \ 'w:fields',
        \ 'e:embedded',
        \ 'm:methods',
        \ 'r:constructor',
        \ 'f:functions'
    \ ],
    \ 'sro' : '.',
    \ 'kind2scope' : {
        \ 't' : 'ctype',
        \ 'n' : 'ntype'
    \ },
    \ 'scope2kind' : {
        \ 'ctype' : 't',
        \ 'ntype' : 'n'
    \ },
    \ 'ctagsbin'  : 'gotags',
    \ 'ctagsargs' : '-sort -silent'
    \ }

" for tagbar
"au VimEnter * TagbarToggle
nmap <F4> :TagbarToggle<CR>
```

이렇게 설정하면 아래와 같이 함수 tag 를 볼수 있습니다.

![enter image description here][4]

### vim-godef
함수가 정의된 파일을 vim 편집창을 분할하여 보여주는 아주 유용한 플러그인입니다.
https://github.com/dgryski/vim-godef

설치는 아래와 같이 합니다.

```
> cd $GOPATH
> go get -v code.google.com/p/rog-go/exp/cmd/godef
> go install -v code.google.com/p/rog-go/exp/cmd/godef
> git clone https://github.com/dgryski/vim-godef ~/.vim/bundle/vim-godef
> vi ~/.vimrc
```

```
…
…
" My bundles here:
Bundle 'SuperTab'  
Bundle 'The-NERD-tree'
Bundle 'Tagbar'
Bundle 'vim-godef'
...
```

vim-godef 의 경우 Vundle  을 이용해서 설치할 수는 없지만 사용은 가능 하므로 위와 같이 설정해 줍니다.
Go 소스를 편집중 명령모드에서 보고 싶은 함수 위에 커서를 두고 g 와 d 키를 치면 아래 화면과 같이 새로은 분할 vim 창이 열리면서 함수가 정의된 파일을 자동으로 열어줍니다.
아래는 명령모드에서 NewScreenWriter() 함수 위에 커서를 위치한 상태에서 g 와 d 키를 누른 결과입니다.

![enter image description here][5]

위에서 설정하였던 .vimrc 파일의 전체 내용은 아래와 같습니다.

```
set nocompatible              " be iMproved
filetype off                  " required!

set rtp+=~/.vim/bundle/vundle/
call vundle#rc()

" let Vundle manage Vundle
" required!
Bundle 'gmarik/vundle'

" My bundles here:
Bundle 'SuperTab'
Bundle 'The-NERD-tree'
Bundle 'Tagbar'
Bundle 'vim-godef'

" original repos on GitHub
Bundle 'tpope/vim-fugitive'
Bundle 'Lokaltog/vim-easymotion'
Bundle 'rstacruz/sparkup', {'rtp': 'vim/'}
Bundle 'tpope/vim-rails.git'
" vim-scripts repos
Bundle 'L9'
Bundle 'FuzzyFinder'
" non-GitHub repos
Bundle 'git://git.wincent.com/command-t.git'

filetype plugin indent on     " required!
"
" Brief help
" :BundleList          - list configured bundles
" :BundleInstall(!)    - install (update) bundles
" :BundleSearch(!) foo - search (or refresh cache first) for foo
" :BundleClean(!)      - confirm (or auto-approve) removal of unused bundles
"
" see :h vundle for more details or wiki for FAQ
" NOTE: comments after Bundle commands are not allowed.

set tabstop=2

" for go plugin
filetype off
```

  [1]: https://docs.google.com/drawings/d/1jZwpWWDvfXYiEYOXTQ7NM7YNXj-0Zfsxtm53l2ntBEA/pub?w=600&h=500 "screenshot_01"
  [2]: https://docs.google.com/drawings/d/1qBVOOZvRFZrLVaVh7RUDEG5vv0w-QzTNkdjKe_MI_QY/pub?w=600&h=500 "screenshot_02"
  [3]: https://docs.google.com/drawings/d/1CecqAdtjw882B6AHgMAY-x1Pb04FcA0Q4saawQfAXjM/pub?w=600&h=500 "screenshot_03"
  [4]: https://docs.google.com/drawings/d/1aPhUocY3_nOTL0D-aTW7Nj_5200CU1ga6cLcrSDbHu4/pub?w=600&h=500 "screenshot_04"
  [5]: https://docs.google.com/drawings/d/1zc_xQxIqDjyMrIC5PXyZUx5VqJGZf3OVgK4GEjthvpg/pub?w=600&h=500 "screenshot_05"
