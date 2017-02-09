#﻿使用Python实现Telnet远程登录
发表于2012/9/4 21:29:29  21131人阅读
分类： python

#一、Windows下开启Telnet服务
（详见：与Win7防火墙无缝结合 Telnet功能测试）
1、Windows 2000/XP/2003/Vista：默认已安装但禁止了Telnet服务
（1）开启Telnet：运行services.msc打开服务管理，找到Telnet服务项设置其启动类型为“自动”或者“手动”（更安全，只在需要的时候才启用），然后启动该服务即可。
2、Windos 7：默认未安装Telnet服务
（1）安装Telnet：依次点击“开始”→“控制面板”→“程序”，“在程序和功能”找到并点击“打开或关闭Windows 功能”进入Windows 功能设置对话框。找到并勾选“Telnet客户端”和“Telnet服务器”，最后“确定”稍等片刻即可完成安装。
（2）开启Telnet：方法同1中的（1）
#二、Linux下开启Telnet服务
（详见：Ubuntu 10.10 下配置Telnet服务器）
（1）安装telnetd（即telnet-server）：sudo apt-get install telnetd
（2）安装xinetd（telnet-server的运行需要由xinetd来管理）：sudo apt-get install xinetd
（3）配置telnet文件：vi /etc/xinetd.d/telnet
（4）开启xinetd：service xinetd start
#三、使用Python实现Telnet远程登录
　　Python中专门提供了telnetlib库，用来完成基于telnet协议的通信功能。
　　利用telnetlib实现远程登录功能的代码如下：

```python
# -*- coding: utf-8 -*- 
import telnetlib
'''Telnet远程登录：Windows客户端连接Linux服务器'''
# 配置选项
Host = '192.168.1.2' # Telnet服务器IP
username = 'admin'   # 登录用户名
password = '123456'  # 登录密码
finish = ':~$ '      # 命令提示符（标识着上一条命令已执行完毕）
# 连接Telnet服务器
tn = telnetlib.Telnet(Host)
# 输入登录用户名
tn.read_until('login: ')
tn.write(username + '\n')
# 输入登录密码
tn.read_until('Password: ')
tn.write(password + '\n')
# 登录完毕后，执行ls命令
tn.read_until(finish)
tn.write('ls\n')
# ls命令执行完毕后，终止Telnet连接（或输入exit退出）
tn.read_until(finish)
tn.close() # tn.write('exit\n')
```

转载出处：http://www.cnblogs.com/russellluo/archive/2012/02/11/2346501.html


