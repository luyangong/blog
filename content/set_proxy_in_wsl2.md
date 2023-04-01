Title: 在windows wsl2 中使用代理
Date: 2023-04-01 11:40
Category: article



## 创建proxy.sh



```shell
touch ~/proxy.sh
```



```shell
# The content of proxy.sh

export hostip=$(ip route | grep default | awk '{print $3}')
export hostport=10810
alias proxy='
    export HTTPS_PROXY="socks5://${hostip}:${hostport}";
    export HTTP_PROXY="socks5://${hostip}:${hostport}";
    export ALL_PROXY="socks5://${hostip}:${hostport}";
    echo -e "Acquire::http::Proxy \"http://${hostip}:${hostport}\";" | sudo tee -a /etc/apt/apt.conf.d/proxy.conf > /dev/null;
    echo -e "Acquire::https::Proxy \"http://${hostip}:${hostport}\";" | sudo tee -a /etc/apt/apt.conf.d/proxy.conf > /dev/null;
    echo "Proxy has been set to ${HTTP_PROXY}"
'
alias unproxy='
    unset HTTPS_PROXY;
    unset HTTP_PROXY;
    unset ALL_PROXY;
    sudo sed -i -e '/Acquire::http::Proxy/d' /etc/apt/apt.conf.d/proxy.conf;
    sudo sed -i -e '/Acquire::https::Proxy/d' /etc/apt/apt.conf.d/proxy.conf;
    echo "Proxy has been unset"
'
```



## 使用proxy.sh

```shell
echo "source ~/proxy.sh" >> ~/.zshrc
source ~/.zshrc
proxy # Proxy has been set to ...
unproxy # Proxy has been unset
```



参照： [WSL2内使用windows的v2ray代理配置方式](https://zhuanlan.zhihu.com/p/414627975)
