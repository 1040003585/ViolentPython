# -*- coding: utf-8 -*- 
import telnetlib
'''Telnet远程登录：Windows客户端连接Linux服务器(复制所有脚本到
python>>> ...)'''
# 配置选项
Host = '127.0.0.1' # Telnet服务器IP
username = 'wu_being'   # 登录用户名
password = 'wu.com'  # 登录密码
finish = ':~$ '      # 命令提示符（标识着上一条命令已执行完毕）
# 连接Telnet服务器
tn = telnetlib.Telnet(Host)
# 输入登录用户名
tn.read_until('login:')
tn.write(username + '\n')
# 输入登录密码
tn.read_until('Password:').decode('utf-8')
tn.write(password + '\n')
# 登录完毕后，执行ls命令
tn.read_until(finish).decode('utf-8')
tn.write('ls\n')
# ls命令执行完毕后，终止Telnet连接（或输入exit退出）
tn.read_until(finish).decode('utf-8')
tn.close() # tn.write('exit\n')





"""
wu_being@ubuntukylin64:~/GitHub/ViolentPython/Chapter-2用Python进行渗透测试/wu2
.用Python构建一个Telnet僵尸网络$ python
Python 2.7.12 (default, Nov 19 2016, 06:48:10) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import telnetlib
>>> '''Telnet远程登录：Windows客户端连接Linux服务器(复制所有脚本到python>>> ...)'''
'Telnet\xe8\xbf\x9c\xe7\xa8\x8b\xe7\x99\xbb\xe5\xbd\x95\xef\xbc\x9aWindows\xe5\xae\xa2\xe6\x88\xb7\xe7\xab\xaf\xe8\xbf\x9e\xe6\x8e\xa5Linux\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8(\xe5\xa4\x8d\xe5\x88\xb6\xe6\x89\x80\xe6\x9c\x89\xe8\x84\x9a\xe6\x9c\xac\xe5\x88\xb0python>>> ...)'
>>> # 配置选项
... Host = '127.0.0.1' # Telnet服务器IP
>>> username = 'wu_being'   # 登录用户名
>>> password = 'wu.com'  # 登录密码
>>> finish = ':~$ '      # 命令提示符（标识着上一条命令已执行完毕）
>>> # 连接Telnet服务器
... tn = telnetlib.Telnet(Host)
>>> # 输入登录用户名
... tn.read_until('login:')
'Ubuntu 16.04 LTS\r\nubuntukylin64 login:'
>>> tn.write(username + '\n')
>>> # 输入登录密码
... tn.read_until('Password:')
' wu_being\r\nPassword:'
>>> tn.write(password + '\n')
>>> # 登录完毕后，执行ls命令
... tn.read_until(finish)
' \r\nLast login: Thu Feb  9 16:38:38 CST 2017 from localhost on pts/21\r\nWelcome to Ubuntu 16.04 LTS (GNU/Linux 4.4.0-57-generic x86_64)\r\n\r\n * Documentation:  https://help.ubuntu.com/\r\n\r\n315 \xe4\xb8\xaa\xe5\x8f\xaf\xe5\x8d\x87\xe7\xba\xa7\xe8\xbd\xaf\xe4\xbb\xb6\xe5\x8c\x85\xe3\x80\x82\r\n6 \xe4\xb8\xaa\xe5\xae\x89\xe5\x85\xa8\xe6\x9b\xb4\xe6\x96\xb0\xe3\x80\x82\r\n\r\nwu_being@ubuntukylin64:~$ '
>>> tn.write('ls\n')
>>> tn.read_until(finish)
'ls\r\nAlibaba                 GitHub           rmq_bk_gc.log    web2py           \xe5\x9b\xbe\xe7\x89\x87\r\nalibaba-rocketmq-3.2.6  jdk1.7.0         rmq_srv_gc.log   zookeeper-3.4.5  \xe6\x96\x87\xe6\xa1\xa3\r\napache-maven-3.3.9      jstorm-2.1.1     store            zookeeper.out    \xe4\xb8\x8b\xe8\xbd\xbd\r\napache-tomcat-7.0.70    logs             tair             \xe5\x85\xac\xe5\x85\xb1\xe7\x9a\x84           \xe9\x9f\xb3\xe4\xb9\x90\r\ndata                    nohup.out        tb-common-utils  \xe6\xa8\xa1\xe6\x9d\xbf             \xe6\xa1\x8c\xe9\x9d\xa2\r\ndeja-dup                PreliminaryDemo  trunk            \xe8\xa7\x86\xe9\xa2\x91\r\nwu_being@ubuntukylin64:~$ '
>>> 
"""
