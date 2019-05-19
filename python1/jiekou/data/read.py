#! /usr/bin/python
# -*- coding:utf-8 -*-
import xlrd
class hahaha():
    def haha(self):
        f = xlrd.open_workbook(r'E:\Users\PycharmProjects\python1\jiekou\data\aaa.xls')
        sheet = f.sheets()[0]
        num = sheet.nrows
        shu=[]
        for i in range(0,num):
            shu.append(sheet.row_values(i))
        return shu

