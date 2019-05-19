#! /usr/bin/python
# -*- coding:utf-8 -*-
import requests
import unittest
from jiekou.data.zhizhi import Zhi
from jiekou.config.请求 import qingqiu
from jiekou.config.请求 import token66
class Xinxi(unittest.TestCase):
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
if __name__== '__main__':
    shu=Zhi()
    # print(shu)
    for i in range(3):
        aa=Xinxi().xinxi(shu[i][0])
        print(aa)