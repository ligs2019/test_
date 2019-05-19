#! /usr/bin/python
# -*- coding:utf-8 -*-
a=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
while True:
    b=int(input('请输入一个十进制数:'))
    if b<0:
        break
    f=''
    while True:
        c=b%16
        b=b//16
        f=f+a[c]
        if b==0:
            break
    if b<0:
        break
    print(f[::-1])