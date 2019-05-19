#! /usr/bin/python
# -*- coding:utf-8 -*-
# class yunsuan():
#     def yinshu(self,a):
#         r=0
#         for i in range(1,a+1):
#             b=0
#             for j in range(2,i+1):
#                 d=i/j
#                 if i%j==0:
#                     b=b+d
#             if i==b:
#                 print(i)
#     def zhishu(self,a):
#         b=0
#         for i in range(2,a+1):
#             for j in range(2,i+1):
#                 if i %j==0:
#                     break
#             if i==j:
#                 print(i)
#                 b=b+i
#         print(b)
#     def jiecheng(self,a):
#         b=1
#         c=0
#         for i in range(1,a+1):
#             b=b*i
#             c=c+b
#         print(b)
#         print(c)
#     def xiangjia(self,a):
#         b=0
#         for i in range(a+1):
#             b=i+b
#         print(b)
# class paixu():
#     def maopo(self,a):
#         a=[]
#         b=input('请输入数字:')
#         c=b.split(',')
#         for i in c:
#             a.append(int(i))
#         for x in range(1,len(a)):
#            for y in range(0,len(a)-1):
#                if a[y] > a[y+1]:
#                    a[y],a[y+1]=a[y+1],a[y]
#         print(a)
#     def xuanze(self,a):
#         a=[]
#         b=input('请输入数据:')
#         c=b.split(',')
#         for i in c:
#             a.append(int(i))
#         for x in range(0,len(a)):
#             for y in range(x+1,len(a)):
#                 if a[x] > a[y] :
#                     a[x],a[y]=a[y],a[x]
#         print(a)
# class jinzhi():
#     def shiliu(self,a):
#         a=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
#         while True:
#             b=int(input('请输入一个十进制数:'))
#             if b<0:
#                 break
#             f=''
#             while True:
#                 c=b%16
#                 b=b//16
#                 f+=a[c]
#                 if b==0:
#                     break
#             if b<0:
#                 break
#             print(f[::-1])
#     def ba(self,a):
#         a = ['0', '1', '2', '3', '4', '5', '6', '7']
#         while True:
#             b = int(input('请输入一个十进制数:'))
#             if b < 0:
#                 break
#             f = ''
#             while True:
#                 c = b % 8
#                 b = b // 8
#                 f += a[c]
#                 if b == 0:
#                     break
#             if b < 0:
#                 break
#             print(f[::-1])
#     def er(self,a):
#         a = ['0', '1', '2']
#         while True:
#             b = int(input('请输入一个十进制数:'))
#             if b < 0:
#                 break
#             f = ''
#             while True:
#                 c = b % 2
#                 b = b // 2
#                 f += a[c]
#                 if b == 0:
#                     break
#             if b < 0:
#                 break
#             print(f[::-1])
#爬取糗事多页段子并追加到Excel中
# import xlwt
# import xlrd
# from xlutils.copy import copy
# import requests
# import re
# for k in range(1,5):
#     a = 'http://www.qiushibaike.com/text/page/{}/.'.format(k)
#     # 发送请求
#     oo = {'User-Agent': 'Mozilla/5.0(WindowsNT10.0;WOW64;rv:66.0)Gecko/20100101Firefox/66.0'}
#     b = requests.get(a, headers=oo)
#     # 接收响应
#     c = b.content.decode('utf-8')
#     z = re.compile('<h2>(.*?)</h2>', re.S)
#     v = z.findall(c)
#     d = re.compile('<div class="content">(.*?)</span>', re.S)
#     e = d.findall(c)
#     ff = []
#     for i in e:
#         i = i.replace('<span>', '')
#         i = i.strip()
#         i = i.replace('<br/>', '')
#         ff.append(i)
#     try:
#         fff = xlrd.open_workbook('h.xls')
#         sheet1=fff.sheets()[0]
#         num=sheet1.nrows
#         print(num)
#         new_f=copy(fff)
#         sheet=new_f.get_sheet(0)
#         for i,j in enumerate(ff):
#             sheet.write(num+i,0,v[i]+':')
#             sheet.write(num+i,1,j)
#         new_f.save('h.xls')
#     except:
#         f = xlwt.Workbook()
#         sheet = f.add_sheet('qiushi')
#         l = 0
#         for y in v:
#             sheet.write(l, 0, y + ':')
#             l = l + 1
#         p = 0
#         for j in ff:
#             sheet.write(p, 1, j)
#             p = p + 1
#         f.save('h.xls')
#爬取GIF图片
# import requests
# import re
# class tupian(object):
#     def fasongqingqiu(self,page):
#         url='http://699pic.com/gif-0-1-0-0-0-0-popular-all-0-all-all-all-all.html?sem=1&sem_kid=84191&sem_type=1'
#         head={'User-Agent':'Mozilla/5.0(WindowsNT10.0;WOW64;rv:66.0)Gecko/20100101Firefox/66.0'}
#         res=requests.get(url,headers=head)
#         html=res.content.decode('utf-8')
#         return html
#     def guolv(self,abc):
#         lianjie=[]
#         # ming=[]
#         patt=re.compile(r'<div class="thumb">(.*?)</a>',re.S)
#         items=patt.findall(abc)
#         # print(len(items))
#         for i in items:
#             new=re.compile(r'src="(.*?)"')
#             aaa=new.findall(i)
#             lianjie.append(aaa[0])
#         # kk=re.compile(r'<img width="100" alt="(.*?)" src="',re.S)
#         # name=kk.findall(abc)
#         # for j in name:
#         #     ming.append(j)
#         return lianjie
#     def save(self,shuju):
#         #需要请求图片的链接
#         global aa
#         for a,i in enumerate(shuju):
#             res=requests.get('https:'+i)
#             #注：接收响应的结果只能用content，因为图片是二进制
#             qq = res.content
#             with open('{}.jpg'.format(aa),'ab') as f:
#                 f.write(qq)
#             aa=aa+1
# tu=tupian()
# aa = 0
# for  ll in range(6):
#     ab=tu.fasongqingqiu(1)
#     tu.guolv(ab)
#     shu=tu.guolv(ab)
#     tu.save(shu)
#爬取豆瓣
# import xlwt
# import xlrd
# from xlutils.copy import copy
# import requests
# import re
# class douban():
#     def qingqiu(self,page):
#         url=url='https://movie.douban.com/top250?start={}&filter='.format(page)
#         head = {'User-Agent': 'Mozilla/5.0(WindowsNT10.0;WOW64;rv:66.0)Gecko/20100101Firefox/66.0'}
#         res = requests.get(url, headers=head)
#         html = res.content.decode('utf-8')
#         return html
#     def guolv(self,abc):
#         ming=[]
#         dao=[]
#         ping=[]
#         lv1=re.compile(r'<img width="100" alt="(.*?)" src="',re.S)
#         name1=lv1.findall(abc)
#         lv2=re.compile(r'导演: (.*?)&nbsp;&nbsp;&nbsp;',re.S)
#         name2=lv2.findall(abc)
#         # lv3=re.compile(r'<p class="">(.*?)</p>',re.S)
#         # name3=lv3.findall(abc)
#         # for i in name3:
#         #     lv31=re.compile(r'<br>(.*?)</p>',re.S)
#         #     name31=lv31.findall(i)
#         #     ming.append(name31[0])
#         # for j in name31:
#         #     j=j.replace('&nbsp;/&nbsp;','')
#         #     j=j.replace()
#         #     ming.append(j)
#         lv5=re.compile(r'<span property="v:best" content="10.0"></span>(.*?) </div>',re.S)
#         name5=lv5.findall(abc)
#         for k in name5:
#             lv51=re.compile(r'<span>(.*?)评价',re.S)
#             ddd=lv51.findall(k)
#             ping.append(ddd[0])
#         lv4=re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
#         name4=lv4.findall(abc)
#         # print(name1,name2,name4,ping)
#         return list(zip(name1,name2,name4,ping))
#     # def save(self,pm):
#     #     try:
#     #         fff = xlrd.open_workbook('h.xls')
#     #         sheet1=fff.sheets()[0]
#     #         num=sheet1.nrows
#     #         print(num)
#     #         new_f=copy(fff)
#     #         sheet=new_f.get_sheet(0)
#     #         for q, w, e, r in pm:
#     #             sheet.write(num, 0, q)
#     #             sheet.write(num, 1, w)
#     #             sheet.write(num, 2, e)
#     #             sheet.write(num, 3, r)
#     #             num=num+1
#     #         new_f.save('h.xls')
#     #     except:
#     #         f = xlwt.Workbook()
#     #         sheet = f.add_sheet('qiushi')
#     #         sheet.write(0,0,'片名')
#     #         sheet.write(0,1,'导演')
#     #         sheet.write(0,2,'评分')
#     #         sheet.write(0,3,'评价人数')
#     #         l = 1
#     #         for q,w,e,r in pm:
#     #             sheet.write(l,0,q)
#     #             sheet.write(l, 1, w)
#     #             sheet.write(l, 2, e)
#     #             sheet.write(l, 3, r)
#     #             l=l+1
#     #         f.save('h.xls')
# p=douban()
# for j in range(0,125,25):
#     shu=p.qingqiu(j)
#     a=p.guolv(shu)
#      # p.save(a)
# import xlwt
# import xlrd
# from xlutils.copy import copy
# import requests
# import re
# import pymysql
# class boss():
#     def qingqiu(self,page):
#         url=url='https://www.zhipin.com/c101280100/?query=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&page={}&ka=page-{}'.format(page,page)
#         head = {'User-Agent': 'Mozilla/5.0(WindowsNT10.0;WOW64;rv:66.0)Gecko/20100101Firefox/66.0'}
#         res = requests.get(url, headers=head)
#         html = res.content.decode('utf-8')
#         return html
#     def guolv(self,abc):
#         gongsi0=[]
#         dizhi0=[]
#         jingyan0=[]
#         xueli0=[]
#         shangshi0=[]
#         lv1=re.compile(r'<div class="job-title">(.*?)</div>',re.S)
#         zhiwei=lv1.findall(abc)
#         lv2=re.compile(r'<span class="red">(.*?)</span>',re.S)
#         xinzi=lv2.findall(abc)
#         lv3=re.compile(r'<div class="company-text">(.*?)</h3>',re.S)
#         g=lv3.findall(abc)
#         for i in g:
#             lv31=re.compile(r'blank">(.*?)</a>',re.S)
#             gongsi=lv31.findall(i)
#             gongsi0.append(gongsi[0])
#         # lv6=re.compile(r'<div class="company-text">(.*?)</p>',re.S)
#         # shangshi1=lv6.findall(abc)
#         # for p in shangshi1:
#         #     lv32 = re.compile(r'<em class="vline"></em>(.*?<em class="vline">)', re.S)
#         #     shangshi = lv32.findall(p)
#
#         lv4=re.compile(r' <div class="info-detail"></div>(.*?)/p>',re.S)
#         dizhi=lv4.findall(abc)
#
#         for j in dizhi:
#             lv41=re.compile(r'<p>(.*?)<em class="vline">',re.S)
#             dizhi1=lv41.findall(j)
#             dizhi0.append(dizhi1[0])
#             lv42=re.compile(r'</em>(.*?)<em',re.S)
#             jingyan=lv42.findall(j)
#             jingyan0.append(jingyan[0])
#             lv43=re.compile(r'(大专|本科|学历不限|硕士|中专/中技|高中)',re.S)
#             xueli=lv43.findall(j)
#             xueli0.append(xueli[0])
#         return list(zip(zhiwei,xinzi,dizhi0,jingyan0,xueli0,gongsi0))
#     def save(self,a):
#         try:
#             fff = xlrd.open_workbook('boss.xls')
#             sheet1=fff.sheets()[0]
#             num=sheet1.nrows
#             print(num)
#             new_f=copy(fff)
#             sheet=new_f.get_sheet(0)
#             for q, w, e, r,t,y in a:
#                 sheet.write(num, 0, q)
#                 sheet.write(num, 1, w)
#                 sheet.write(num, 2, e)
#                 sheet.write(num, 3, r)
#                 sheet.write(num, 4, t)
#                 sheet.write(num, 5, y)
#                 # sheet.write(num,6,u)
#                 num=num+1
#             new_f.save('boss.xls')
#         except:
#             f = xlwt.Workbook()
#             sheet = f.add_sheet('xinxi')
#             sheet.write(0,0,'职位')
#             sheet.write(0,1,'薪资')
#             sheet.write(0,2,'公司地址')
#             sheet.write(0,3,'经验要求')
#             sheet.write(0,4,'学历')
#             sheet.write(0,5,'公司名称')
#             # sheet.write(0,6,'是否上市')
#             l = 1
#             for q,w,e,r,t,y in a:
#                 sheet.write(l,0,q)
#                 sheet.write(l, 1, w)
#                 sheet.write(l, 2, e)
#                 sheet.write(l, 3, r)
#                 sheet.write(l, 4, t)
#                 sheet.write(l, 5, y)
#                 # sheet.write(1,6,u)
#                 l=l+1
#             f.save('boss.xls')
#     def shujuku(self,ka):
#         conn=pymysql.connect(host='192.168.1.104',port=3306,user='root',passwd='123456')
#         mycursor=conn.cursor()
#         mycursor.execute('use li_text')
#         for q,w,e,r,t,y in ka:
#             mycursor.execute('insert into  bossw values(%s,%s,%s,%s,%s,%s)',(q,w,e,r,t,y))
#             conn.commit()
#
#
#
# bb=boss()
# for o in range(1,6):
#     dd=bb.qingqiu(o)
#     a=bb.guolv(dd)
#     bb.shujuku(a)
    # bb.save(a)
# import requests
# import re
# import json
# url='https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=13&city=410200&geoobj=114.289449%7C34.775662%7C114.441578%7C34.820781&keywords=%E6%B4%97%E6%B5%B4%E4%B8%AD%E5%BF%83'
# res=requests.get(url)
# qwe=res.text
# asd=json.loads(qwe)
# for i in range(1,20):
#     print(asd['data']['poi_list'][i]['address'])
# import pymysql
# # # 连接数据库
# conn=pymysql.connect(host='192.168.2.115',port=3306,user='root',passwd='123456')

# #创建游标:conn.cursor
# mycusor=conn.cursor()
# #执行SQL语句:execute
# mycusor.execute('show databases')
# #fetchall 获取上一个SQL语句的执行结果
# abc=mycusor.fetchall()
# # print(abc)
# mycusor.execute('use li_text;')
# mycusor.execute('show tables;')
# a=mycusor.fetchall()
# print(a)
# mycusor.execute('show tables')
# a=mycusor.fetchall()
# print(a)

# d=mycusor.fetchmany(4)
# print(d)


# #创建数据库
# mycusor.execute('create database li_text;')

# import pymysql
# # 连接数据库
# conn=pymysql.connect(host='192.168.2.115',port=3306,user='root',passwd='123456')
# mysqla=conn.cursor()
# while True:
#     a=input('>>')
#     if a=='exit':
#         print('byby')
#         break
#     try:
#         mysqla.execute('{}'.format(a))
#         conn.commit()
#         b=mysqla.fetchall()
#         print(b)
#     except:
#         while True:
#             print('sql语句有错请重新输入')
#             break
# import os
# b=os.popen('ipconfig')
# # print(b.read())
#
# # os.chdir(r'D:')
# f=os.listdir('.')
# for i in f:
#     if i.endswith('.py'):
#         print(i)
#爬取智联并导入到数据库
# import pymysql
# import requests
# import re
# import json
# # import xlwt
# # import xlrd
# # from xlutils.copy import copy
# # 将爬取的内容添加到数据库
# # import pymysql
# # # 连接数据库
# conn=pymysql.connect(host='192.168.2.115',port=3306,user='root',passwd='123456')
# class zhilian():
#     def qingqiu(self,page=90):
#         url=url='https://fe-api.zhaopin.com/c/i/sou?start=90&pageSize=90&cityId=763&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&=0&_v=0.96098276&x-zp-page-request-id=3b9e4dc1506b4f5182c7167a623b9ef2-1553946367768-63410'
#         head = {'User-Agent': 'Mozilla/5.0(WindowsNT10.0;WOW64;rv:66.0)Gecko/20100101Firefox/66.0'}
#         res = requests.get(url, headers=head)
#         html = res.content.decode('utf-8')
#         html1=json.loads(html)
#         return html1
#     def guolv(self,abc):
#         zhiwei=[]
#         dizhi=[]
#         xinzi=[]
#         jingyan=[]
#         xueli=[]
#         updatetime=[]
#
#         for i in range(90):
#             zhiwei.append(abc['data']['results'][int(i)]['jobName'])
#             dizhi.append(abc['data']['results'][int(i)]['city']['display'])
#             xinzi.append(abc['data']['results'][int(i)]['salary'])
#             jingyan.append(abc['data']['results'][int(i)]['workingExp']['name'])
#             xueli.append((abc['data']['results'][int(i)]['eduLevel']['name']))
#             updatetime.append(abc['data']['results'][int(i)]['endDate'])
#         # print(zhiwei,dizhi,xinzi,jingyan,xueli,updatetime)
#
#         return list(zip(zhiwei,dizhi,xinzi,jingyan,xueli,updatetime))
#
# b=zhilian()
# hh=b.qingqiu()
# shuju=b.guolv(hh)
#
# mycusor=conn.cursor()
# mycusor.execute('use li_text')
# for q,w,e,r,t,y in shuju:
#     # print(q,w,e,r,t,y)
#     mycusor.execute('insert into zhilian values(%s,%s,%s,%s,%s,%s)',(q,w,e,r,t,y))
#     conn.commit()

# import pymysql

# import xlwt
# import xlrd
# from xlutils.copy import copy
# 将爬取的内容添加到数据库
# import pymysql
# # # 连接数据库
# conn=pymysql.connect(host='192.168.2.115',port=3306,user='root',passwd='123456')
#
# mycusor=conn.cursor()
# import requests
# # #创建游标:conn.cursor
# import re
# class boss():
#     def qingqiu(self,page=1):
#         url=url='https://www.zhipin.com/c101280100/?query=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&page={1}&ka=page-{1}'
#         head = {'User-Agent': 'Mozilla/5.0(WindowsNT10.0;WOW64;rv:66.0)Gecko/20100101Firefox/66.0'}
#         res = requests.get(url, headers=head)
#         html = res.content.decode('utf-8')
#         return html
#     def guolv(self,abc):
#         gongsi0=[]
#         dizhi0=[]
#         jingyan0=[]
#         xueli0=[]
#         shangshi0=[]
#         lv1=re.compile(r'<div class="job-title">(.*?)</div>',re.S)
#         zhiwei=lv1.findall(abc)
#         lv2=re.compile(r'<span class="red">(.*?)</span>',re.S)
#         xinzi=lv2.findall(abc)
#         lv3=re.compile(r'<div class="company-text">(.*?)</h3>',re.S)
#         g=lv3.findall(abc)
#         for i in g:
#             lv31=re.compile(r'blank">(.*?)</a>',re.S)
#             gongsi=lv31.findall(i)
#             gongsi0.append(gongsi[0])
#         # lv6=re.compile(r'<div class="company-text">(.*?)</p>',re.S)
#         # shangshi1=lv6.findall(abc)
#         # for p in shangshi1:
#         #     lv32 = re.compile(r'<em class="vline"></em>(.*?<em class="vline">)', re.S)
#         #     shangshi = lv32.findall(p)
#
#         lv4=re.compile(r' <div class="info-detail"></div>(.*?)/p>',re.S)
#         dizhi=lv4.findall(abc)
#
#         for j in dizhi:
#             lv41=re.compile(r'<p>(.*?)<em class="vline">',re.S)
#             dizhi1=lv41.findall(j)
#             dizhi0.append(dizhi1[0])
#             lv42=re.compile(r'</em>(.*?)<em',re.S)
#             jingyan=lv42.findall(j)
#             jingyan0.append(jingyan[0])
#             lv43=re.compile(r'(大专|本科|学历不限|硕士|中专/中技|高中)',re.S)
#             xueli=lv43.findall(j)
#             xueli0.append(xueli[0])
#         return list(zip(zhiwei,xinzi,dizhi0,jingyan0,xueli0,gongsi0))
# b=boss()
# f=b.qingqiu()
# tt=b.guolv(f)
# # print(tt)
#
# mycusor=conn.cursor()
# mycusor.execute('use li_text')
# for q,w,e,r,t,y in tt:
#     mycusor.execute('insert into boss values("{}","{}","{}","{}","{}","{}")'.format(q,w,e,r,t,y))
#     conn.commit()

# import paramiko
# ssh123=paramiko.SSHClient()
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh123.connect(hostname='192.168.2.115',port=22,username='root',password='123456')
# a,b,c=ssh123.exec_command('ls -al')
# print(b.read().decode())
# ssh123.connect(hostname='192.168.2.115',port=22,username='root',password='123456')
# while True:
#         q=input('请输入命令:')
#         a,b,c=ssh123.exec_command('{}'.format(q))
#         print(a)
#         print(b)
#         print(c)
#         if q=='exit':
#             break
#
# import paramiko
# #建立通道
# ssh123=paramiko.Transport(('192.168.2.115',22))
# #连接主机
# qwe=ssh123.connect(username='root',password='123456')
# #创建一个sftp客户端
# sftp=paramiko.SFTPClient.from_transport(ssh123)
# #从Linux下载文件到Windows
# sftp.get('/opt/ggg','fff')
# import smtplib#封装了smtp协议
# import email.mime.multipart#处理邮件中的组成部分
# import email.mime.text#处理文件中的正文
# #设置发件人
# fr='15903893872@163.com'
# #设置收件人
# res='969598484@qq.com'
# #设置服务器
# server='smtp.163.com'
# #设置密码
# password='lgs418710'
# #设置一个空邮件
# mes=email.mime.multipart.MIMEMultipart()
# #添加发件人
# mes['from']=fr
# #添加收件人
# mes['to']=res
# #添加主题
# mes['Subject']='日报'
# #设置正文
# text="哈哈哈哈哈 \n  你好啊"
# #处理及添加正文
# txt=email.mime.text.MIMEText(text)
# mes.attach(txt)
# # 添加附件
# att2 = email.mime.text.MIMEText(open('a.txt', 'rb').read(), 'base64', 'utf-8')
# att2["Content-Type"] = 'application/octet-stream'
# att2["Content-Disposition"] = 'attachment; filename="a.txt"'
# ## 头部字段
# mes.attach(att2)
# #定义服务器
# smtp123=smtplib.SMTP_SSL(server,465)
# #登陆服务器
# smtp123.login(fr,password)
# #发送邮件
# smtp123.sendmail(fr,res,mes.as_string())
# #断开连接
# smtp123.close()
# #server  端
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










































