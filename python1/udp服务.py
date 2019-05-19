#! /usr/bin/python
# -*- coding:utf-8 -*-
import socket
#创建一个有接受能力和发送能力的东西
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定ip和端口号
s.bind(('127.0.0.1',800))
while True:
    #接收建立连接，第一个值是客户端的请求数据的信息，第二个值是客户端的IP地址和端口号
    client,addr=s.recvfrom(1024)
    print(client.decode('utf-8'))
    #发送响应
    msg='hello'
    s.sendto(msg.encode('utf-8'),addr)#s是套接字，addr是客户端的IP地址和端口号
