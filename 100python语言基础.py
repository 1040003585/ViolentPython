import socket
import os
import sys

def retBanner(ip,port):
	try:
		socket.setdefaulttimeout(2)	#set socket default timeout 2s
		s=socket.socket()
		s.connect((ip,port))
		banner=s.recv(1024)		#receive 1024B data
		return banner
	except:
		return				#None

def checkVulns(banner,filename):
	f=open(filename,'r')			#open the file with read 
	for line in f.readlines():
		if line.strip('\n') in banner:	#filter the char of '\n'
			print "[+] Server is vulnerable: "+ \
				banner.strip('\n')
## 2.define the main fun
def main():
	if len(sys.argv)==2:				#sys model
		filename=sys.argv[1]			#first argv
		if not os.path.isfile(filename):	#os model
			print '[-] '+filename+' does not exist!'
			exit(0)
		if not os.access(filename,os.R_OK):
			print '[-] '+filename+" access denied!"
			exit(0)
	else:					#sys.argv[0] is py file name
		print '[-] Usage: '+str(sys.argv[0])+' <vuln filename>'
		exit(0)

	portList=[21,22,25,80,110,443,5000,9955]
	for x in range(100,122):			#
		ip='192.168.1.'+str(x)			#type interfer,
		for port in portList:
			#banner=retBanner(ip,port)	#
			banner=retBanner("localhost",port)
			if banner:			# isn't None
				print '[+] '+ip+":"+banner
				checkVulns(banner,filename)
## 1.start the main fun
if __name__=='__main__':	
	main()

