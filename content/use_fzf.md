Title:  在zsh中配置fzf
Date: 2023-03-31 23:18
Category:  article

## fzf简介

fzf是一个命令行模糊查询的工具。主要使用go语言实现。它提供一个友好的命令行模糊查询的界面，按照它的格式要求传参后，可以很好实现先搜索再操作，即"search and action"模式。这样就可以大大降低记忆负担，只需输入关键词即可完成各种操作。

## 安装fzf

```zsh
# mac
brew install fzf

# ubuntu
apt install fzf
```

参考：[github fzf](https://github.com/junegunn/fzf[GitHub - junegunn/fzf: A command-line fuzzy finder](https://github.com/junegunn/fzf))

## 安装并配置fzf-tab-completion

```shell
curl https://raw.githubusercontent.com/lincheney/fzf-tab-completion/master/zsh/fzf-zsh-completion.sh > ~/fzf-zsh-completion.sh

echo "source ~/fzf-zsh-completion.sh" >> ~/.zshrc
echo "bindkey '^]' fzf_completion" >> ~/.zshrc # 使用ctrl + ]触发fzf补全
```

参考：[github fzf-tab-completion](https://github.com/lincheney/fzf-tab-completion)

## 安装并配置fzf-history-search

```shell
curl https://raw.githubusercontent.com/joshskidmore/zsh-fzf-history-search/master/zsh-fzf-history-search.zsh > ~/zsh-fzf-history-search.zsh

echo "source ~/zsh-fzf-history-search.zsh" >> ~/.zshrc

# 以下只是设置fzf样式，可选
export FZF_DEFAULT_OPTS='--height 60% --reverse --color border:46 --prompt="➤ "'
export FZF_COMPLETION_OPTS=$FZF_DEFAULT_OPTS
```

参考：[github fzf-history-search](https://github.com//joshskidmore/zsh-fzf-history-search)

## 重置zsh

```zsh
source ~/.zshrc
```

这样，ctrl-r搜索history，或者在输入命令并按ctrl-]时，都将触发fzf搜索。
