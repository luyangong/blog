Title: Vim配置文件.Vimrc
Date: 2019-12-22 23:40
Category: article

```vimscript
" 底部操作指令Tab自动补全

set wildmenu
set wildmode=longest:list,full

set smarttab
set showmode
set number
set nocompatible

" 设置tab符长度为4个空格
set tabstop=4

" 设置换行自动缩进长度为4个空格
set shiftwidth=4

" 设置tab符自动转换为空格
set expandtab

" 设置智能缩进，其他可选缩进方式：autoindent, cindent, indentexpr

set smartindent
set autoindent

set hlsearch

" 快捷键
let mapleader = ';'
nnoremap <Leader>a viw<esc>bi"<esc>ea"<esc>
nmap <Leader>f ^i# <Esc>
nmap <Leader>j ^2x <Esc>
map <Leader>m o<ESC>:call setline(".", "if __name__ == '__main__':")<ESC> 
map <Leader>b o<ESC>:call setline(".", "import pdb; pdb.set_trace()")<ESC> 
nmap <Leader>e :call Cmd()<ESC>
nmap <Leader>h :call append(0, ["#!/usr/bin/python3", "#-*- coding:utf-8 -*-"])<ESC>
nmap <Leader>w :w <Esc>
nmap <Leader>z :qa! <CR>
nmap <Leader>x :wqa! <CR>
nmap <Leader>T o<ESC>:call setline(".", "# TODO ^?^")<ESC>
nmap <Leader>t :call Test()<ESC>
nmap <Leader>d :Gvdiffsplit! <ESC>
nmap <F5> :call Cmd()<ESC>
nmap <F6> :!time python3 -m pdb %<ESC>
nmap <F10> :call OpenTestFile()<ESC>
nmap <cr> j
function! OpenTestFile()
    if ! isdirectory('tests')
        exec "silent !mkdir tests"
    endif
    exec "vsp tests/test_%"
endfunction

" 缩进
set foldmethod=indent
set foldlevel=99

" 函数跳转
set tags=tags
" set autochdir
" set laststatus=2
" set incsearch

" 自动换行
" set textwidth=100

syntax on
colorscheme desert

" let g:solarized_termcolors=256

" 定义函数，做条件映射
function! Cmd()
    if expand('%:e') == 'py'
        exec "!time python3 %"
    elseif expand('%:e') == 'rkt'
        exec "!time racket %"
    elseif expand('%:e') == 'lua'
        exec "!time lua %"
    else
        echo expand('%:e')
    endif
endfunction

function! Test()
    if split(getcwd(), '/')[-1] == 'tests'
        exec "!time cd ..;pytest -v tests/%;cd -"
    else
        exec "!time pytest -v %"
    endif
endfunction

function! RelativeCmd(cmd)
    if eval('&' . a:cmd) == 1 
        let tmp = "set " . "no" . a:cmd
    else
        let tmp = "set " . a:cmd
    endif
    echom ':' . tmp
    exec tmp
endfunction

function! DirOrClose()
    if getline(1) == "../"
        let tmp = "q!"
    else
        let tmp = "Vex"
    endif
    echom ":" . tmp
    exec tmp
endfunction

nmap <M-P> :call RelativeCmd("paste")<CR>
imap <M-P> <ESC>:set paste<CR>i
nmap @r :call RelativeCmd("relativenumber")<CR>
nmap <C-N> :call RelativeCmd("number")<CR>
nmap <C-L> :call RelativeCmd("cursorline")<CR>
"nmap <C-J> :call RelativeCmd("cursorcolumn")<CR>
nmap <C-K> :call DirOrClose()<CR>
nmap <S-F> :Rg<CR>
nmap <C-P> :Files<CR>
nmap <C-M> :NERDTreeFind<CR>
nmap <C-B> :NERDTree<CR>

hi Search term=standout ctermfg=0 ctermbg=3


if ! has("gui_running")
    set t_Co=256
endif

" 设置窗口的行和列
" set lines=35 columns=118

" 设置目录树
let g:netrw_liststyle = 4
let g:netrw_alto = 1
let g:netrw_browse_split=3
let g:netrw_altv = 1
let g:netrw_winsize = 15
let g:netrw_banner = 0
" svn-blame - Show SVN blame annotation for the current file.
" Maintainer:   Paul Nechifor <paul@nechifor.net>
" Version:      0.1
"
" This was originally copied from here:
" https://svn.apache.org/repos/asf/subversion/trunk/contrib/client-side/vim/vim-blame.vimrc

if exists("g:loaded_svnblame") || &cp || v:version < 700
  finish
endif
let g:loaded_svnblame = 1

function! s:svnBlame()
  let line = line(".")
  setlocal nowrap

  " Create a new window at the left-hand side.
  aboveleft 18vnew

  " Blame, ignoring white space changes.
  %!svn blame -x-w "#"
  setlocal nomodified readonly buftype=nofile nowrap winwidth=1
  setlocal nonumber
  if has('&relativenumber') | setlocal norelativenumber | endif

  " Return to original line.
  exec "normal " . line . "G"

  " Synchronize scrolling, and return to original window.
  setlocal scrollbind
  wincmd p
  setlocal scrollbind
  syncbind
endfunction
command Blame call s:svnBlame()

"ommi completion
set ofu=syntaxcomplete#Complete
imap <C-A> <C-X><C-O>
" 状态栏
set laststatus=2      " 总是显示状态栏
" highlight StatusLine cterm=bold ctermfg=blue ctermbg=black
" 获取当前路径，将$HOME转化为~
" function! CurDir()
"         let curdir = substitute(getcwd(), $HOME, "~", "g")
"         return curdir
" endfunction
" set statusline=[%n]\ %f%m%r%h\ \|\ \ pwd:\ %{CurDir()}\ \|%=\ %l,%c\ %p%%\ 



function AddAuthor()
        let n=1
        while n < 5
                let line = getline(n)
                if line =~'^\s#\#\s#\S#Last\s#modified\s#:\s#\S#.#$'
                        call UpdateTitle()
                        return
                endif
                let n = n + 1
        endwhile
        call AddTitle()
endfunction

function UpdateTitle()
        normal m'
        execute '/# Last modified\s#:/s@:.#$@\=strftime(": %Y-%m-%d %H:%M")@'
        normal "
        normal mk
        execute '/# Filename\s#:/s@:.#$@\=": ".expand("%:t")@'
        execute "noh"
        normal 'k
        echohl WarningMsg | echo "Successful in updating the copy right." | echohl None
endfunction

function AddTitle()
        call append(1,"##########################################################")
        call append(2,"# Author        : luyangong")
        call append(3,"# Email         : luyangong@moojing.com")
        call append(4,"# Last modified : ".strftime("%Y-%m-%d %H:%M"))
        call append(5,"# Filename      : ".expand("%:t"))
        call append(6,"# Description   : ")
        call append(7,"# #######################################################")
        echohl WarningMsg | echo "Successful in adding the copyright." | echohl None
endfunction

" python from powerline.vim import setup as powerline_setup
" python powerline_setup()
" python del powerline_setup

set rtp+=~/.vim/vundle.git/
call vundle#rc()

" Auto generate tags file on file write of *.c and *.h files
" autocmd BufWritePost *.py silent! !ctags . &

call plug#begin()
    Plug 'preservim/nerdtree', {'on': 'NERDTreeToggle'}
    Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
    Plug 'junegunn/fzf.vim'
    Plug 'gabrielelana/vim-markdown'
    Plug '~/lyg/learn/open_terminal_plugin'
    Plug 'tpope/vim-fugitive'
    Plug 'MattesGroeger/vim-bookmarks'
    Plug 'ludovicchabant/vim-gutentags'
    Plug 'puremourning/vimspector'
call plug#end()
" Bookmarks per working directory
let g:bookmark_save_per_working_dir = 1
let g:bookmark_auto_save = 1
let g:vimspector_enable_mappings = 'HUMAN'
let g:vimspector_base_dir='/home/luyangong/.vim/plugged/vimspector'
```
