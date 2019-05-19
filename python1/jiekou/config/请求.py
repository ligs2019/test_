#! /usr/bin/python
# -*- coding:utf-8 -*-
import requests
from jiekou.data.read import hahaha
from jiekou.data.zhizhi import Zhi
class qingqiu():
    def denglu(self,username,password):
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
        return zhuye
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
    def guojia(self):
        url = "http://120.132.8.33:9000/api/Others/GetCountryList"
        payload = ""
        headers = {
            'Content-Type': "application/json",
            'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
            'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
            'Language': "zh_CN",
            'APIVersion': "3.0",
            'User-Agent': "PostmanRuntime/7.11.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "74b45bd6-131d-416f-8116-b7320915771b,4c09a5b2-9f1a-4758-99d9-15e93557b003",
            'Host': "120.132.8.33:9000",
            'accept-encoding': "gzip, deflate",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }

        response = requests.request("GET", url, data=payload, headers=headers)
        guo=response.json()
        return guo
    def bingli(self):
        url = "http://120.132.8.33:9000/api/Account/GetAllDiseaseInfo"

        payload = ""
        headers = {
            'Content-Type': "application/json",
            'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
            'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
            'Language': "zh_CN",
            'APIVersion': "3.0",
            'cache-control': "no-cache",
            'Postman-Token': "c4bf5d6b-7487-4025-9dde-3961589c5ba3"
        }

        response = requests.request("GET", url, data=payload, headers=headers)

        bl=response.json()
        return bl

class token66():
    def token666(self):
        url = "http://120.132.8.33:9000/api/Account/LoginByPhone"
        payload = '{\r\n    \"phone\":\"15993835273\",\r\n    \"password\":\"111111\",\r\n    \"zone\":\"86\",\r\n    \"loginType\":0,\r\n    \"isAuto\":0,\r\n    \"deviceId\":\"ec:89:14:54:93:007\"\r\n}'
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
        dataa = response.json()
        token666 = dataa['data']['accessToken']
        return dataa['data']['accessToken']

# if __name__== '__main__':
#     shu = hahaha().haha()
#     print(shu)
#     for i in range(len(shu)):
#         aa=qingqiu().denglu(int(shu[i][0]),int(shu[i][1]))
#
#     ss=qingqiu().guojia()
#     print(ss)
#     ff=qingqiu().bingli()
#     print(ff)
#     gg=qingqiu().xinxi(Zhi()[0][0])
#     print(gg)
print(token66().token666())
