#! /usr/bin/python
# -*- coding:utf-8 -
import requests
import HTMLTestRunner
import unittest
import xlrd
class Xinxi(unittest.TestCase):
    def Zhi(self):
        f=xlrd.open_workbook('zhi.xlsx')
        sheet=f.sheets()[0]
        qwe=[]
        num=sheet.nrows
        for i in range(0,num):
            qwe.append(sheet.row_values(i))
        return qwe
    def xinxi(self,token):
        url = "http://120.132.8.33:9000/api/Account/GetUserInfo"

        querystring = {"accountGuid":"0c9a2e9b-ba05-4921-b801-1337abb33038","targetUserGui\nd\n":"0c9a2e9b-ba05-4921-b801-1337abb33038","targetUserGui%0Ad%0A":"0c9a2e9b-ba05-4921-b801-1337abb33038"}

        payload = ""
        headers = {
            'Content-Type': "application/json",
            'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
            'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
            'Language': "zh_CN",
            'APIVersion': "3.0",
            'AccessToken': "{}".format(token),
            'TimeZone': "GMT+4",
            'User-Agent': "PostmanRuntime/7.11.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "067249db-ccba-4810-b296-77f647cc7543,dca6807e-faab-4095-9997-22dadcd56170",
            'Host': "120.132.8.33:9000",
            'accept-encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        res=response.json()
        return res
    def test_right(self):
        qq=self.xinxi(self.Zhi()[0][0])
        self.assertEqual(qq['code'],0)
    def test_ture(self):
        hh=self.Zhi()
        for i in range(1,len(hh)-1):
            ww=self.xinxi(self.Zhi()[i][0])
            self.assertNotEqual(ww['code'],0)
if __name__== '__main__':
    unittest.main()
    # suit = unittest.TestSuite()
    # # 将测试用例添加道测试套件中
    # #     第一种方式
    # suit.addTest(Xinxi('test_right'))
    # suit.addTest(Xinxi('test_ture'))
    # #     第二种方式
    # # 将qwe类中所有以test开头的函数都添加进去
    # #     suit.addTest(unittest.makeSuite(ceshi))
    # #  打开一个空文件
    # f = open('abcDDD.html', 'wb')
    # # 定义测试报告的信息
    # runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='接口测试报告', tester='李国帅', description='结果如下')
    # runner.run(suit)
    # f.close()





