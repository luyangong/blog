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
nmap <Leader>m o<ESC>:call setline(".", "if __name__ == \"__main__\":")<ESC>
nmap <Leader>e :call append(0, "#-*- coding:utf-8 -*-")<ESC>
nmap <Leader>s :call append(0, "#!/usr/bin/python")<ESC>
nmap <Leader>h :call append(0, ["#!/usr/bin/python", "#-*- coding:utf-8 -*-"])<ESC>
nmap <Leader>q :q <Esc>
nmap <Leader>z :qa! <CR>
nmap <Leader>x :wqa! <CR>

" 缩进
set foldmethod=indent
set foldlevel=99

" 函数跳转
set tags=~/tags
set autochdir
" set laststatus=2
" set incsearch

" 自动换行
set textwidth=100

" syntax enable
" set background=dark
" colorscheme solarized

" let g:solarized_termcolors=256

" 定义函数，做条件映射
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
nmap <C-P> :call RelativeCmd("paste")<CR>
imap <C-P> <ESC>:set paste<CR>i
nmap @r :call RelativeCmd("relativenumber")<CR>
nmap <C-N> :call RelativeCmd("number")<CR>
nmap <C-L> :call RelativeCmd("cursorline")<CR>
nmap <C-J> :call RelativeCmd("cursorcolumn")<CR>
nmap <C-K> :call DirOrClose()<CR>
nmap <C-V> :vsplit<CR>
nmap <C-Z> :q <CR>
nmap <C-X> :wq <CR>

hi Search term=standout ctermfg=0 ctermbg=3


if ! has("gui_running")
    set t_Co=256
endif

if &diff
  " colorscheme evening
  highlight DiffAdd    cterm=bold ctermfg=10 ctermbg=17 gui=none guifg=bg guibg=Red
  highlight DiffDelete cterm=bold ctermfg=10 ctermbg=17 gui=none guifg=bg guibg=Red
  highlight DiffChange cterm=bold ctermfg=10 ctermbg=17 gui=none guifg=bg guibg=Red
  highlight DiffText   cterm=bold ctermfg=10 ctermbg=88 gui=none guifg=bg guibg=Red
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
```