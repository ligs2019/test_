#! /usr/bin/python
# -*- coding:utf-8 -*-
import socket
while True:
    #创建套接字
    sock=socket.socket()
    #建立连接
    sock.connect(('192.168.2.231',80))
    #发送请求

    msg=input(">>")
    #发送
    sock.send(msg.encode('utf-8'))
    #接收
    reg=sock.recv(1024)
    print(reg.decode('utf-8'))
    #断开连接
    sock.close()