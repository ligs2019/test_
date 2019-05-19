#! /usr/bin/python
# -*- coding:utf-8 -*-
import  xlwt
f=xlwt.Workbook(encoding='utf-8')
sheet=f.add_sheet('score')
a=open('a.txt','r',encoding='utf-8')
j=0
while True:
    b=a.readline()
    c=b.split(',')
    if b=='':
        break
    for i in range(len(c)):
        sheet.write(j,i,c[i])
    j=j+1
    f.save('aaa.xls')