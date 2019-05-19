#! /usr/bin/python
# -*- coding:utf-8 -*-
import xlrd
def Zhi():
    f = xlrd.open_workbook('zhi.xlsx')
    sheet = f.sheets()[0]
    qwe = []
    num = sheet.nrows
    for i in range(0, num):
        qwe.append(sheet.row_values(i))
    return qwe
Zhi()