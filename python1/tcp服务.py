#! /usr/bin/python
# -*- coding:utf-8 -*-
# import socket
# #创建一个有接受能力和发送能力的东西
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #绑定ip和端口号
# s.bind(('192.168.2.147',30000))
# #监听,数3指的是最大等待个数
# s.listen(3)
# #
# while True:
#     #接收建立连接，第一个值得到的建立连接的信息，第二个值是客户端的IP地址和端口号
#     client,addr=s.accept()
#     #接收客户端发送的请求,最大接收1024个字节
#     msg=client.recv(1024)
#     print(msg.decode('utf-8'))
#     #发送响应
#
#     reg=input(">>")
#     client.send(reg.encode('utf-8'))
