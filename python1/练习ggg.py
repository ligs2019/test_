#! /usr/bin/python
# -*- coding:utf-8 -*-
import requests
import unittest
import xlrd
import HTMLTestRunner
f = xlrd.open_workbook('aaa.xls')
sheet = f.sheets()[0]
row_1 = sheet.nrows
class Denglu(unittest.TestCase):
    def test_dizi(self,username,password):
        url = "http://120.132.8.33:9000/api/Account/LoginByPhone"
        payload = '{\r\n    \"phone\":\"%s\",\r\n    \"password\":\"%s\",\r\n    \"zone\":\"86\",\r\n    \"loginType\":0,\r\n    \"isAuto\":0,\r\n    \"deviceId\":\"ec:89:14:54:93:007\"\r\n}' %(username,password)
        headers = {
                'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
                'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
                'Language': "zh_CN",
                'APIVersion': "3.0",
                'Content-Type': "application/json",
                'cache-control': "no-cache",
                'Postman-Token': "c3e8a8e4-d355-49b2-93b8-b4f814eb148a"
                }

        response = requests.request("POST", url, data=payload, headers=headers)

        zhuye=response.json()
        # print(zhuye)
        return zhuye
    # def setUp(self): #  初始化测试环境
    #     print('开始登录')
    # def tearDown(self): #清理测试环境
    #     print('结束登录')
    def test_1(self):    #有效
        bbb=self.test_dizi(int(sheet.cell(1, 0).value),int(sheet.cell(1, 1).value))
        print('查询成功,学校如下')
        print(bbb)
        self.assertEqual(bbb['code'],0)
        # print('查询成功,学校如下')
    def test_2(self):  #无效
        for i in range(2,row_1):
            ccc=self.test_dizi(int(sheet.cell(i, 0).value),int(sheet.cell(i, 1).value))
            print(ccc)
            self.assertNotEqual(ccc['code'],0)
            # print('输入格式有误')
if  __name__=='__main__':
    suit = unittest.TestSuite()
    # 将测试用例添加道测试套件中
    #     第一种方式
    suit.addTest(Denglu('test_1'))
    suit.addTest(Denglu('test_2'))
    #     第二种方式
    # 将qwe类中所有以test开头的函数都添加进去
    #     suit.addTest(unittest.makeSuite(ceshi))
    #  打开一个空文件
    f = open('abc.html', 'wb')
    # 定义测试报告的信息
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='接口测试报告', tester='李国帅', description='结果如下')
    runner.run(suit)
    f.close()


