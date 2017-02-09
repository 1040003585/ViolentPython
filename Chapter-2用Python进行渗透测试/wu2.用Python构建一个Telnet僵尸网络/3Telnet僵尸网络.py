#!/usr/bin/python
# -*- coding: utf-8 -*-
import telnetlib

class Client:
    #PROMPT = ['# ', '>>> ', '> ','\$ ']
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            tn = telnetlib.Telnet(self.host)
            tn.read_until('login:')
            tn.write(self.user + '\n')
            tn.read_until('Password:')
            tn.write(self.password + '\n')
            tn.read_until('$')
            return tn
        except Exception, e:
            print e
            print '[-] Error Connecting'

    def send_command(self, cmd):
        self.session.write(cmd+'\n')
        self.session.read_until('$')


def botnetCommand(command):
    for client in botNet:
        client.send_command(command)
        print '[*] Output from ' + client.host

def addClient(host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

botNet = []
#addClient('127.0.0.1', 'root', 'wu.com')
addClient('127.0.0.1', 'wu_being', 'wu.com')
addClient('127.0.0.2', 'wu_being', 'wu.com')
addClient('localhost', 'wu_being', 'wu.com')
#addClient('121.42.199.205', 'root', 'since2016')

botnetCommand('uname -v')
botnetCommand('ls')
botnetCommand('ping www.baidu.com -c 4')
#botnetCommand('cat /etc/issue')

