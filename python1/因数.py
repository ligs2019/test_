#! /usr/bin/python
# -*- coding:utf-8 -*-
def yinshu(a):
    c=0
    for i in range(1,a+1):
        b = 0
        for j in range(1,i):
            if i%j==0:
                b=b+j
        if b==i:
            print(i)
            c=c+i
    print(c)
yinshu(1000)