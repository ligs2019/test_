#! /usr/bin/python
# -*- coding:utf-8 -*-
import unittest
import requests
def guojia():
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
    guo = response.json()
    return guo