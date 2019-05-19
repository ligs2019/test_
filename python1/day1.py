#! /usr/bin/python
#  -*- coding:utf-8 -*-
#判断成绩
# a=input("请输入成绩：")
# a=int(a)
# if  90<a and a<=100:
#     print('优秀')
# elif  60<=a<=90:
#     print('及格')
# elif      0<a<60:
#     print('不及格')
# else:
#    b= input('请重新输入：')
#    b=int(b)
# if 90 < b<= 100:
#     print('优秀')
# elif 60 <= b <= 90:
#     print('及格')
# elif 0 < b < 60:
#     print('不及格')
#同时整除2和3；整除2；整除3
# a=int(input('请输入数字:'))
# if a%2==0:
#     if a%3==0:
#         print('hello world')
#     elif a%2==0:
#      print('hello')
# elif a%3==0:
#     print('world')
# else:
#     print(666)
#以a或A开头以c结尾；以a开头；以c结尾
# a=input('请输入数据:')
# b=a[0]
# c=a[-1]
# if b=='a' and c=='c' or b=='A' and c=='c':
#      print(110)
# elif b=='a':
#     print(120)
# elif c=='c':
#     print(130)
# else:
#     print(250)
# for i in range(10):
#     if i==7:
#        continue
#     else:
#         print(i)
# else:
#     print('hha')
# b=0
# c=0
# for i in range(1,100):
#     if i%2 !=0 :
#         b=i+b
#     else:
#         c=i+c
# print(b-c)

# a=0
#猜数字
# import  random
# a = random.randrange(1,10)
# print(a)
# for i in range(100):
#     b=int(input('请输入数字:'))
#     if b > a :
#         print('大''还有{}次机会'.format(3-i))
#     elif b< a :
#         print('小''还有{}次机会'.format(3-i))
#     elif b == a :
#         print('正确')
#         break
# 99乘法表
# for a in range(1,10):
#     for b in range(1,a+1):
#         print('{}*{}={}'.format(b,a,a*b),end='\t')
#     print()
#将大于55的加入到一个列表，小与等于的的加入到另一个列表
# a=[99,44,66,77,33,22,11,88,55]
# b = list()
# c = list()
# for i in a:
#     if i > 55:
#         b.append(i)
#     else:
#         c.append(i)
# # print(b,c)
#质数之和
# def zhishu(a):
#     b=0
#     for i in range(2,a+1):
#         for j in range(2,i+1):
#             if i%j==0:
#                 break
#         if i==j:
#             print(i)
#             b=b+i
#     print(b)
# 水仙花数
# for a in range(1,10):
#     for b in range(0,10):
#         for c in range(0,10):
#             d=a*100+b*10+c
#             e=a**3+b**3+c**3
#             if d==e:
#                 print(d)
#因数
# def yinshu(a):
#     c=0
#     for i in range(1,a+1):
#         b = 0
#         for j in range(1,i):
#             if i%j==0:
#                 b=b+j
#         if b==i:
#             print(i)
#             c=c+i
#     print(c)
#阶乘之和
# def jiecheng(a):
#     b,c=1,0
#     for i in range(1,a+1):
#         b=b*i
#         c=c+b
#     print(c)
#判断三角形钝角锐角直角
# a=int(input('>>'))
# b=int(input('>>'))
# c=int(input('>>'))
# if c>a and c>b and a+b>c and a+c>b and b+c>a:
#         if a**2+b**2==c**2:
#             print('直角')
#         if a**2+b**2>c**2:
#             print('锐角')
#         if a**2+b**2<c**2:
#             print('钝角')
# elif a+b>c and a+c>b and b+c>a:
#     print('C不是最大值')
# else:
#     print('不是三角形')
#输入一组数，大于平均数打印出来
# c=[]
# while True:
#       a=input('请输入数字:')
#       b=a.split(',')
#       for i in b:
#           c.append(int(i))
#           avg=sum(c)/len(c)
#       print(avg)
#           # print(c)
#       for j in c:
#          if j>avg:
#            print(j)
#从键盘上输入若干个学生的成绩，统计出平均成绩并输出低于平均分的学生成绩，用输入负数结束输入
# while True:
#     a=[]
#     b=input('请输入数字:')
#     if '-' in b:
#         break
#     c=b.split(',')
#     for i in c:
#      a.append(int(i))
#     d=sum(a)/len(a)
#     print(d)
#     for j in a:
#      if j < d:
#       print(j)
#去重,并排序
# a=input('请输入数据:')
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
# c=[]
# for i in b:
#     c.append(int(i))
# for x in range(1,len(c)):
#     for y in range(0,len(c)-1):
#         if c[y]>c[y+1]:
#             c[y],c[y+1]=c[y+1],c[y]
# print(c)
# 冒泡排序
# a=[]
# b=input('请输入数字:')
# c=b.split(',')
# for i in c:
#     a.append(int(i))
# for x in range(0,len(a)):
#    for y in range(0,len(a)-1):
#        if a[y] > a[y+1]:
#            a[y],a[y+1]=a[y+1],a[y]
# print(a)
#选择排序法
# a=[]
# b=input('请输入数据:')
# c=b.split(',')
# for i in c:
#     a.append(int(i))
# for x in range(0,len(a)):
#     for y in range(x+1,len(a)):
#         if a[x] > a[y] :
#             a[x],a[y]=a[y],a[x]
# print(a)
#冒泡函数
# def maopo(a):
#     global maopo
#     a=[]
#     b=input('请输入数字:')
#     c=b.split(',')
#     for i in c:
#         a.append(int(i))
#     for x in range(1,len(a)):
#        for y in range(0,len(a)-1):
#            if a[y] > a[y+1]:
#                a[y],a[y+1]=a[y+1],a[y]
#     print(a)
# return赋值例子
# def xiangjia(a):
#     x=0
#     for i in range(1,a+1):
#         x=i+x
#     print(x)
#     return x
# xiangjia(10)
# print(xiangjia(10))
# b=[]
# for i in range(1,int(input('>'))+1):
#     c=xiangjia(i)
#     b.append(c)
# print(b)
#打印列表中第一大和第二大的值
# a=[]
# b=input('请输入数字:')
# c=b.split(',')
# for i in c:
#     a.append(int(i))
# for x in range(1,len(a)):
#    for y in range(0,len(a)-1):
#        if a[y] > a[y+1]:
#            a[y],a[y+1]=a[y+1],a[y]
# print('最大值为{},第二大值为{}'.format(a[-1],a[-2]))
# a=[]
# b=input('请输入数字:')
# c=b.split(',')
# for i in c:
#     a.append(int(i))
#回文字符串
# s = input('请输入一组字符串,以逗号隔开：')
# b = s.split(',')
# b.reverse()
# a = b.copy()
# a = ','.join(a)
# print(a)
# if a == s:
#     print('您输入的字符串是回文')
# else:
#     print('您输入的字符串不是回文')
#十进制转十六进制
# a=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
# while True:
#     b=int(input('请输入一个十进制数:'))
#     if b<0:
#         break
#     f=''
#     while True:
#         c=b%16
#         b=b//16
#         f+=a[c]
#         if b==0:
#             break
#     if b<0:
#         break
#     print(f[::-1])
#打印最大值二大值升级版
# a = [1,4,3,2,4,5,5,7,6,7,5,7,6]
# c = []
# for i in a:
#     if i not in c:
#         c.append(i)
# for j in range(len(c)):
#     for x in range(len(c)-1):
#         if c[x] > c[x+1]:
#             c[x], c[x + 1] = c[x + 1], c[x]
# print(a.count(max(c)), '个', max(c))
# print(a.count(c[-2]), '个', c[-2])
#统计文件行数
# with open(r'C:\Users\哈哈哈\Desktop\ll.txt','r',encoding='utf-8') as  a:
#     b=a.readlines()
#     d=0
#     for i in b:
#         if i.startswith('#') or i=='\n':
#             d=d+1
#     print(len(b)-d)
#     print(d)
#不用int将字符串变成整数
# a=input('请输入数据:')
# a=a[::-1]
# b=0
# for i in range(len(a)):
#     for j in range(10):
#         if str(j)==a[i]:
#             b=b+j*10**i
# print(type(a))
# print(type(b))
#打印最大二大的
# a=[1,3,2,6,5,8,7,9,9,40,40]
# b=a.copy()
# b=list(set(b))
# b.sort()
# for i in a:
#     if i ==b[-1] or i==b[-2]:
#         print(i)
#买鸡
# for x in range(1,100):
#     for y in range(1,100):
#         for z in range(1,100):
#             if 2*x+1*y+0.5*z==100 and x+y+z==100:
#                 print(x,y,z)
#一个函数，传两个参数a,b，a是数组，b是一个数字，找出a数组中两数只和等于b，打印出来这两个数
# def xx(a,b):
#     for i in range(len(a)):
#         for j in range(i+1,len(a)):
#             if a[i]+a[j]==b:
#                 print(a[i],a[j],b)
# xx((1,2,3,4),5)
#一个有顺序的列表，随机加入一个数，加入的数在正确的位置
# a=[1,3,4,5,6,7,8,9]
# b=int(input('请输入数字:'))
# a.append(b)
# a.sort()
# print(a)
#任意4个数字，组成不相同的三位数
# a=input('请输入数字:')
# b=a.split(',')
# c=[]
# d=[]
# for i in b:
#     c.append(int(i))
# for x in c:
#     for y in c:
#         for z in c:
#             if x != y and x != z and y != z:
#                 e=x*100+y*10+z*1
#                 d.append(int(e))
# print(len(d))
#购物车
# splb=[
#     {"name":"电脑","price":2000},
#     {"name":"鼠标","price":100},
#     {"name":"游艇","price":5000},
#     {"name":"美女","price":6000},
#     {"name":"空无","price":0}
# ]
# a=int(input('请输入银行卡金额:'))
# b=[]
# c=[]
# while True:
#     print('商品列表')
#     for i,j in enumerate(splb):
#         print(i,j)
#     d=int(input('请选择商品:'))
#     if d>4 or d<0:
#         print('没有该商品')
#         break
#     else:
#         s=splb[d]
#         b.append(s)
#         print('购物车:')
#         print(b)
#         c.append(splb[d]['price'])
#         u=sum(c)
#         print('价格{}'.format(u))
#     e=int(input('请输入选择:1.结算2.删除商品3.充值4.退出5.继续添加:'))
#     if e==1:
#         if a>u or a==u:
#             print('购买成功')
#             a=a-u
#             c.clear()
#             b.clear()
#             print('余额为{}'.format(a))
#         if a<u:
#             print('购买当前商品余额不足，请充值,或退出')
#             h=u-a
#             print('需充值{}元'.format(h))
#             i=int(input('请选择:1.充值2.退出3.删除商品'))
#             if i==1:
#                 g = input('请输入充值金额:')
#                 a = int(a) + int(g)
#                 print('当前余额{}元'.format(a))
#             if i==2:
#                continue
#             if i==3:
#                 for i, j in enumerate(splb):
#                     print(i, j)
#                 print(b)
#                 h = int(input('请输要删除的商品号:'))
#                 c.remove(splb[h]['price'])
#                 b.remove(splb[h])
#                 print(c)
#                 print(b)
#     if e==2:
#          for i, j in enumerate(splb):
#             print(i, j)
#          print(b)
#          h=int(input('请输要删除的商品号:'))
#          c.remove(splb[h]['price'])
#          b.remove(splb[h])
#          print(c)
#          print(b)
#     if e==3:
#         g = input('请输入充值金额:')
#         a = int(a) + int(g)
#         print('当前余额{}元'.format(a))
#     if e==4:
#         print('再见')
#         break
#将列表中的元素向左挪一位
# a=[1,2,3,4,5,6]
# for i in range(1,len(a)):
#     a[i-1],a[i]=a[i],a[i-1]
# print(a)
#将列表中最大的放在最后一位，最小的放在第一位
# a=(input('请输入数据:'))
# b=a.split(',')
# c=[]
# for i in b:
#     c.append(int(i))
# c.sort()
# c[0],c[-1]=c[-1],c[0]
# print(c)
#

#
# class 小爱():
#     def __init__(self,b):
#         self.name=b
#     def 打电话(self):
#         print('打电话给{}'.format(self.name))
#     def 发短信(self):
#         print('发短信给{}'.format(self.name))
#     def 放音乐(self,a):
#         print('放音乐给{}'.format(a))
# 小爱('dd').打电话()
# a=[str(i) for i in range(10)]+[chr(i) for i in range(65,71)]
# print(a)
# e = int(input('请输入十进制数:'))
# f=''
# while True:
#     c=e%16
#     e=e//16
#     f = f+a[c]
#     if e==0:
#         break
# f=f[::-1]
# print(f)
#将文件中内容导入到Excel中
# import  xlwt
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('score')
# a=open('a.txt','r',encoding='utf-8')
# j=0
# while True:
#     b=a.readline()
#     c=b.split(',')
#     if c=='':
#         break
#     for i in range(len(c)):
#         sheet.write(j,i,c[i])
#     j=j+1
#     f.save('a.xls')

#将Excel中内容导入到文件中
# import  xlrd
# f=xlrd.open_workbook('a.xls')
# sheet=f.sheets()[0]
# c=sheet.nrows
# x=open('c.txt','w',encoding='utf-8')
# for i in range(c):
#     j=sheet.row_values(i)
#     for m,k in enumerate(j):
#         print(m,k)
#         if m==len(j)-1:
#             x.write(k)
#         else:
#             x.write(k+',')
# f.save('d.xls')
#将Excel表中的99乘法表导入到文件中
# import xlrd
# f=xlrd.open_workbook('a.xls')
# sheet=f.sheets()[0]
# num= sheet.nrows
# with open('b.txt','w',encoding='utf-8') as ff:
#     for i in range(num):
#         i =sheet.row_values(i)
#         for j,k in enumerate(i):
#             if j==len(i)-1:
#                 ff.write('\n')
#             else:
#                 ff.write(k+' ')
# 将文件中的99乘法表导入到Excel表中
# import xlwt
# f=xlwt.Workbook()
# sheet=f.add_sheet('hhh')
# with open('a.txt','r',encoding='utf-8') as a:
#     j=0
#     while True:
#         b=a.readline()
#         c=b.split(' ')
#         if b == '':
#             break
#         print(c)
#         for i in range(len(c)):
#             sheet.write(j,i,c[i])
#         j=j+1
#     f.save('a.xls')
#在文件中写入99乘法表
# with open('a.txt','w',encoding='utf-8') as a:
#     for i in range(1,10):
#         for j in range(1,i+1):
#             a.write('{}*{}={} '.format(i,j,i*j))
#         a.write('\n')
#将99乘法表写入到Excel中
# import xlwt
# f=xlwt.Workbook()
# sheet=f.add_sheet('99')
# for i in range(1,10):
#     for j in range(1,i+1):
#         sheet.write(i-1,j-1,'{}*{}={}\n'.format(i,j,i*j))
# f.save('b.xls')
#打印文件中带有关键字的行
# with open('c.txt','r',encoding='utf-8') as a:
#     while True:
#         b=a.readline()
#         if 'abc' in b:
#             print(b)
#         if b=='':
#             break
#Excel追加例子
# from  xlutils.copy import copy
# import xlrd
# f=xlrd.open_workbook('b.xls')
# new_f=copy(f)
# sheet=new_f.get_sheet(0)
# sheet.write(0,0,'hahaha')
# new_f.save('b.xls')
#判断是否为闰年，并打印过去几天，是周几
# import time
# a=input("请输入日期:")
# b=a.split(',')
# c=[]
# for i in b:
#     c.append(int(i))
# if c[0]%400==0 or c[0]%4==0:
#     print('闰年')
# else:
#     print('非闰年')
# d=time.strptime('{},{},{}'.format(c[0],c[1],c[2]),'%Y,%m,%d')
# print('本年已经过去{}天,周{}'.format(d[-2],d[-3]+1))
#输出日期比输入日期提前一天
# import time
# a=input("请输入日期,以','隔开:")
# b=a.split(',')
# c=[]
# for i in b:
#     c.append(int(i))
# d=time.strptime('{},{},{}'.format(c[0],c[1],c[2]),'%Y,%m,%d')
# f=time.mktime(d)
# h=int(f)-86400
# g=time.localtime(h)
# print('前一天的日期:{}-{}-{}'.format(g[0],g[1],g[2]))
#爬虫，爬取糗事百科
# import requests
# import re
# for k in range(1,6):
#     a='http://www.qiushibaike.com/text/page/{}/.'.format(k)
#     #发送请求
#     oo={'User-Agent':'Mozilla/5.0(WindowsNT10.0;WOW64;rv:66.0)Gecko/20100101Firefox/66.0'}
#     b=requests.get(a,headers=oo)
#     #接收响应
#     c=b.content.decode('utf-8')
#     z=re.compile('<h2>(.*?)</h2>',re.S)
#     v=z.findall(c)
#     d=re.compile('<div class="content">(.*?)</span>',re.S)
#     e=d.findall(c)
#     ff=[]
#     for i in e:
#         i=i.replace('<span>','')
#         i=i.strip()
#         i=i.replace('<br/>','')
#         ff.append(i)
#     with open('h.txt','a',encoding='utf-8') as j:
#                 for i in ff:
#                     s=ff.index(i)
#                     j.write(v[s])
#                     j.write(i)
# import xlwt
# f=xlwt.Workbook()
# sheet=f.add_sheet('qiushi')
# with open('h.txt','r',encoding='utf-8') as a:
#     m=0
#     while True:
#         b = a.readline()
#         c = b.split(' ')
#         if b == '':
#             break
#         print(c)
#         for i in range(len(c)):
#             sheet.write(m, i, c[i])
#         m = m + 1
#     f.save('h.xls')
#爬取糗事多页段子并写入Excel中
# import requests
# import re
# ff=[]
# dd=[]
# for k in range(1,3):
#     a='http://www.qiushibaike.com/text/page/{}/.'.format(k)
#     #发送请求
#     oo={'User-Agent':'Mozilla/5.0(WindowsNT10.0;WOW64;rv:66.0)Gecko/20100101Firefox/66.0'}
#     b=requests.get(a,headers=oo)
#     #接收响应
#     c=b.content.decode('utf-8')
#     z=re.compile('<h2>(.*?)</h2>',re.S)
#     v=z.findall(c)
#     d=re.compile('<div class="content">(.*?)</span>',re.S)
#     e=d.findall(c)
#     for j in v:
#         dd.append(j)
#     for i in e:
#         i=i.replace('<span>','')
#         i=i.strip()
#         i=i.replace('<br/>','')
#         ff.append(i)
# import xlwt
# f=xlwt.Workbook()
# sheet=f.add_sheet('qiushi')
# for x in range(len(dd)):
#     sheet.write(x,0,dd[x]+':')
#     sheet.write(x,1,ff[x])
# f.save('h.xls')
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

# import requests
# import re
# for k in range(1,2):
#     a='http://www.qiushibaike.com/text/page/{}/.'.format(k)
#     #发送请求
#     oo={'User-Agent':'Mozilla/5.0(WindowsNT10.0;WOW64;rv:66.0)Gecko/20100101Firefox/66.0'}
#     b=requests.get(a,headers=oo)
#     #接收响应
#     c=b.content.decode('utf-8')
#     z=re.compile('<h2>(.*?)</h2>',re.S)
#     v=z.findall(c)
#     d=re.compile('<div class="content">(.*?)</span>',re.S)
#     e=d.findall(c)
#     ff=[]
#     for i in e:
#         i=i.replace('<span>','')
#         i=i.strip()
#         i=i.replace('<br/>','')
#         ff.append(i)
# #爬虫爬取豆瓣图片
# import requests
# import re
# class tupian(object):
#     def fasongqingqiu(self,page):
#         url='https://movie.douban.com/top250?start={}&filter='.format(page)
#         head={'User-Agent':'Mozilla/5.0(WindowsNT10.0;WOW64;rv:66.0)Gecko/20100101Firefox/66.0'}
#         res=requests.get(url,headers=head)
#         html=res.content.decode('utf-8')
#         return html
#     def guolv(self,abc):
#         lianjie=[]
#         ming=[]
#         patt=re.compile(r'<img width="100" (.*?)</a>',re.S)
#         items=patt.findall(abc)
#         # print(len(items))
#         for i in items:
#             new=re.compile(r'src="(.*?)"')
#             aaa=new.findall(i)
#             lianjie.append(aaa[0])
#         kk=re.compile(r'<img width="100" alt="(.*?)" src="',re.S)
#         name=kk.findall(abc)
#         for j in name:
#             ming.append(j)
#         return lianjie,ming
#     def save(self,shuju,mingzi):
#         #需要请求图片的链接
#         for a,i in enumerate(shuju):
#             res=requests.get(i)
#             #注：接收响应的结果只能用content，因为图片是二进制
#             qq = res.content
#             z=mingzi[a]
#             with open('{}.jpg'.format(z),'ab') as f:
#                 f.write(qq)

# tu=tupian()
# for  ll in range(0,125,25):
#     ab=tu.fasongqingqiu(ll)
#     tu.guolv(ab)
#     shu,m=tu.guolv(ab)
#     tu.save(shu,m)
#爬取糗事图片
# import requests
# import re
# class tupian(object):
#     def fasongqingqiu(self,page):
#         url='https://www.qiushibaike.com/imgrank/page/{}/'.format(page)
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



