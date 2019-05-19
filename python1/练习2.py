#! /usr/bin/python
# -*- coding:utf-8 -*-
import requests
import unittest
import xlrd
class stday(unittest.TestCase):
    def shuju1(self):
        shuju=[]
        f = xlrd.open_workbook('aaa.xls')
        sheet = f.sheets()[0]
        for i in range(sheet.nrow):
            shuju.append(sheet.row_values(i))
        return shuju
    def denglu(self,name,passwd):
        url = "http://120.132.8.33:9000/api/Account/LoginByPhone"
        payload = "{\r\n    \"phone\":\"%s\",\r\n    \"password\":\"%s\",\r\n    \"zone\":\"86\",\r\n    \"loginType\":0,\r\n    \"isAuto\":0,\r\n    \"deviceId\":\"ec:89:14:54:93:007\"\r\n}"%(name,passwd)
        headers = {
            'Content-Type': "application/json",
            'PhoneInfo': "{'platform': 'iOS','systemVersion': '12.0','phoneModel': 'iPhone X'}",
            'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
            'Language': "zh_CN",
            'APIVersion': "3.0",
            'User-Agent': "PostmanRuntime/7.11.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "be21f0c1-037f-45e7-87dc-79690bb42158,d6bf673e-9525-4f0e-96d7-6666409b7e89",
            'Host': "120.132.8.33:9000",
            'accept-encoding': "gzip, deflate",
            'content-length': "150",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        response = requests.request("POST", url, data=payload, headers=headers)
        res=response.json()
        return res
    # def setUp(self):
    #     print('a')
    # def tearDown(self):
    #     print('s')
    def test_1(self):
        qq=self.denglu(self.shuju1[0][0],self.shuju1[0][1])
        self.assertAlmostEqual(qq['msg'],'OK')
        # def test_2(self):
        #     for i in range(num):
        #         print(i)
        #         b = sheet.row_values(i)
        #         ww=self.denglu(int(b[0]),int(b[1]))
        #         self.assertAlmostEqual(ww['code'],0)
        # def test_3(self):
        #     ee=self.denglu(int(b[0]),int(b[1]))
        #     print(ee)
        #     self.assertAlmostEqual(ee['code'],0)

if __name__=='__main__':
    unittest.main()



