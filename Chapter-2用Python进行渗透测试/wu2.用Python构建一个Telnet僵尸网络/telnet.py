# -*- coding: utf-8 -*- 
import telnetlib
'''Telnet远程登录：Windows客户端连接Linux服务器(复制所有脚本到python>>> ...)'''
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
tn.read_until('Password:')
tn.write(password + '\n')
# 登录完毕后，执行ls命令
tn.read_until(finish)
tn.write('ls\n')
# ls命令执行完毕后，终止Telnet连接（或输入exit退出）
tn.read_until(finish)
tn.close() # tn.write('exit\n')

