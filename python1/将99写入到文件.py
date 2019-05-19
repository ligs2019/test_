#! /usr/bin/python
# -*- coding:utf-8 -*-
with open('aa.txt','w')as ff:
    for i in range(1,10):
        for j in range(1,i+1):
            ff.write('{}*{}={} '.format(i,j,i*j))
        ff.write('\n')
