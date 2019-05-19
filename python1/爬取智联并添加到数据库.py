#! /usr/bin/python
# -*- coding:utf-8 -*-
import pymysql
import requests
import re
import xlwt
import xlrd
from xlutils.copy import copy
import json
conn=pymysql.connect(host='192.168.2.115',port=3306,user='root',passwd='123456')
class zhilian():
    def qingqiu(self,page=90):
        url=url='https://fe-api.zhaopin.com/c/i/sou?start=90&pageSize=90&cityId=763&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&=0&_v=0.96098276&x-zp-page-request-id=3b9e4dc1506b4f5182c7167a623b9ef2-1553946367768-63410'
        head = {'User-Agent': 'Mozilla/5.0(WindowsNT10.0;WOW64;rv:66.0)Gecko/20100101Firefox/66.0'}
        res = requests.get(url, headers=head)
        html = res.content.decode('utf-8')
        html1=json.loads(html)
        return html1
    def guolv(self,abc):
        zhiwei=[]
        dizhi=[]
        xinzi=[]
        jingyan=[]
        xueli=[]
        updatetime=[]

        for i in range(90):
            zhiwei.append(abc['data']['results'][int(i)]['jobName'])
            dizhi.append(abc['data']['results'][int(i)]['city']['display'])
            xinzi.append(abc['data']['results'][int(i)]['salary'])
            jingyan.append(abc['data']['results'][int(i)]['workingExp']['name'])
            xueli.append((abc['data']['results'][int(i)]['eduLevel']['name']))
            updatetime.append(abc['data']['results'][int(i)]['endDate'])
        # print(zhiwei,dizhi,xinzi,jingyan,xueli,updatetime)

        return list(zip(zhiwei,dizhi,xinzi,jingyan,xueli,updatetime))
    def shujuku(self,ka):
        mycusor = conn.cursor()
        mycusor.execute('use li_text')
        for q, w, e, r, t, y in ka:
            # print(q,w,e,r,t,y)
            mycusor.execute('insert into zhilian values(%s,%s,%s,%s,%s,%s)', (q, w, e, r, t, y))
            conn.commit()
    # def save(self,kaka):
    #     try:
    #             fff = xlrd.open_workbook('zhilian.xls')
    #             sheet1=fff.sheets()[0]
    #             num=sheet1.nrows
    #             print(num)
    #             new_f=copy(fff)
    #             sheet=new_f.get_sheet(0)
    #             for q, w, e, r in kaka:
    #                 sheet.write(num, 0, q)
    #                 sheet.write(num, 1, w)
    #                 sheet.write(num, 2, e)
    #                 sheet.write(num, 3, r)
    #                 num=num+1
    #             new_f.save('zhilian.xls')
    #         except:
    #             f = xlwt.Workbook()
    #             sheet = f.add_sheet('xinxi')
    #             sheet.write(0,0,'片名')
    #             sheet.write(0,1,'导演')
    #             sheet.write(0,2,'评分')
    #             sheet.write(0,3,'评价人数')
    #             l = 1
    #             for q,w,e,r in kaka:
    #                 sheet.write(l,0,q)
    #                 sheet.write(l, 1, w)
    #                 sheet.write(l, 2, e)
    #                 sheet.write(l, 3, r)
    #                 l=l+1
    #             f.save('zhilian.xls')


    # shu=p.qingqiu(j)
    # a=p.guolv(shu)
    #  # p.save(a)
# for j in range(0,125,25):
b=zhilian()
hh=b.qingqiu()
shuju=b.guolv(hh)
b.shujuku(shuju)

#
