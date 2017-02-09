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

def main():
    ipFile = open('4switcher_ip8.txt', 'r')
    for ip in ipFile.readlines():
        ip = ip.strip('\n')
        addClient(ip, 'switch', 'hd&3467')
        botnetCommand('help\n')

if __name__ == '__main__':
	main()

