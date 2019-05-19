#! /usr/bin/python
# -*- coding:utf-8 -*-
import pymysql
import xlwt
conn=pymysql.connect(host='192.168.2.115',port=3306,user='root',passwd='123456')
mycursor=conn.cursor()
mycursor.execute('use li_text;')
mycursor.execute('select * from boss;')
nnn=mycursor.fetchall()
print(nnn)
f=xlwt.Workbook()
sheet=f.add_sheet('jkjk')
sheet.write(0,0,'职位')
sheet.write(0,1,'薪资')
sheet.write(0,2,'地址')
sheet.write(0,3,'jingyan')
sheet.write(0,4,'学历')
sheet.write(0,5,'name')
i=1
for q,w,e,r,t,y in nnn:
   sheet.write(i,0,'{}'.format(q))
   sheet.write(i,1,'{}'.format(w))
   sheet.write(i,2,'{}'.format(e))
   sheet.write(i,3,'{}'.format(r))
   sheet.write(i,4,'{}'.format(t))
   sheet.write(i,5,'{}'.format(y))
   i+=1
f.save('hh.xls')