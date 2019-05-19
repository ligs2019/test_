#! /usr/bin/python
# -*- coding:utf-8 -*-
import requests
import unittest
def bingli():
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

    bl = response.json()
    return bl

