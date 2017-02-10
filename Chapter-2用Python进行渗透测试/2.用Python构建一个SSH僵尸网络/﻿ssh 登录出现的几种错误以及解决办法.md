# ﻿ssh 登录出现的几种错误以及解决办法
60773阅读　1评论2010-03-28　wwwzyf
分类：LINUX
首先、确保server端的ssh服务是开的（`service shhd start`）
然后在client端输入： `ssh usrname@serverip` （远程登录）
`scp filename usrname@serverip：/URL` (远程传输)
常出现的问题：
# 问题一 ssh登录的时候链接端口失败
## 提示（1）：
```
 # ssh 192.168.***.**
 ssh: connect to host 192.168.***.** port 22: No route to host
```
这由于server端没有开机或是网络不通（这个原因很多，最简单的是网线没有插。还有就是可能会是网卡down了等）如果是网卡down了ifup相应的网卡再试试
## 提示（2）：
```
 # ssh zhou@192.168.***.**
 ssh: connect to host 192.168.***.** port 22: Connection refused
```
这是由于对方server的ssh服务没有开。这个server端开启服务即可。 
## 如何开启ssh服务呢？
首先确保要登录的主机安装了openssh-client（ubuntu有默认安装，如果没有则`sudo apt-get install openssh-client`），如果要使本机开放SSH服务就需要安装 `openssh-server`: `sudo apt-get install openssh-server`
   然后确认sshserver是否启动了：
   `ps -e |grep ssh`
如果看到sshd那说明ssh-server已经启动了。
如果没有则可以这样启动：`sudo /etc/init.d/ssh start`
ssh-server配置文件位于`/ etc/ssh/sshd_config`，在这里可以定义SSH的服务端口，默认端口是22，你可以自己定义成其他端口号，如222。
然后重启SSH服务：
`sudo /etc/init.d/ssh stop`or`service ssh stop`
`sudo /etc/init.d/ssh start`or`service ssh start`
然后使用以下方式登陆SSH：
ssh zhou@192.168.***.** zhou为192.168.***.**机器上的用户，需要输入密码。
断开连接：exit
# 问题二、ssh到server上的时候密码是对的但是报如下信息：
```
 # ssh 192.168.***.**
 root@192.168.***.**'s password:
 Permission denied, please try again.
```
这个是由于如果不输入用户名的时候默认的是root用户，但是安全期间ssh服务默认没有开root用户的ssh权限
解决方法：
要修改root的ssh权限，即修改 `/etc/ssh/sshd_config`文件中
PermitRootLogin no 改为 PermitRootLogin yes
# 问题三 登录是出现如下提示：
```
ssh root@192.168.***.**
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED! @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that the RSA host key has just been changed.
The fingerprint for the RSA key sent by the remote host is
76:fb:b3:70:14:48:19:d6:29:f9:ba:42:46:be:fb:77.
Please contact your system administrator.
Add correct host key in /home/fante/.ssh/known_hosts to get rid of this
message.
Offending key in /home/fante/.ssh/known_hosts:68
RSA host key for 192.168.***.** has changed and you have requested strict checking.
Host key verification failed.
```
server端密码或是其他发生改变的时候。
解决方法一般就需要删除~/.ssh/known_hosts的东西，然后再登录即可。


上一篇：ubuntu 9.10 源
下一篇：vim ctags cscope的配合使用阅读源码
文章评论
2010-12-14caojiangfeng
