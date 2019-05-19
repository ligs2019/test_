#! /usr/bin/python
# -*- coding:utf-8 -*-
import socket
while True:
    #创建套接字
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #不要建立连接,但需要
    host=('127.0.0.1',800)
    #发送请求

    msg=input(">>")
    #发送
    s.sendto(msg.encode('utf-8'),host)
    #接收
    reg=s.recv(1024)
    print(reg.decode('utf-8'))
    #断开连接
    s.close()