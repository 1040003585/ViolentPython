#coding:UTF-8

import optparse
import socket
from socket import *

def ConnScan(tgtHost,tgtPort):
	try:
		connSkt=socket(AF_INET,SOCK_STREAM)
		connSkt.connect((tgtHost,tgtPort))
		connSkt.send('ViolentPython\r\n')
		results=connSkt.recv(1000)
		print "[+]%d/tcp open"%tgtPort
		print "[+] "+str(results)
		connSkt.close()
	except:
		print "[-]%d/tcp close" %tgtPort

def PortScanner(tgtHost,tgtPorts):
	print '[+]tgtHost:'+tgtHost
	try:
		tgtIP=gethostbyname(tgtHost)	#from socket import *
	except:
		print "[-]1Cannot resolve '%s': Unknown host" %tgtHost
		return
	'''
	try:
		tgtName=gethostbyaddr(tgtIP)	#from socket import *
		print "[+]Can resolve " + tgtName[0]
	except:
		print "[-]2Cannot resolve " + tgtIP
		return
	'''
	for tgtPort in tgtPorts:
		print '[+]Port:'+tgtPort
		ConnScan(tgtHost,int(tgtPort))

def main():
	parser=optparse.OptionParser("Usage %prog -H <target host> -p <target port>");
	parser.add_option('-H',dest='tgthost',type='string',help='specity target host');
	parser.add_option('-p',dest='tgtport',type='string',help='specity target port[s] separeted b comma');
	(options,args)=parser.parse_args() #错误提示：Usage: Usage 201portscanner.py -H <target host> -p <target port>
	tgtHost=options.tgthost
	tgtPorts=str(options.tgtport).split(',')
	if(tgtHost==None)|(tgtPorts[0]==None):
		print '[-]You must specify a target host and port[s]'
		exit(0)
	PortScanner(tgtHost,tgtPorts)	
		
if __name__=="__main__":
	main()

 #python 201portscanner.py -H 202.192.224.137 -p 80,139,445,135

