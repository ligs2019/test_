#! /usr/bin/python
# -*- coding:utf-8 -*-
import HTMLTestRunner
from jiekou.用例.test_xinxi import ceshi
import unittest
if __name__== '__main__':
    suit = unittest.TestSuite()
    # 将测试用例添加道测试套件中
    #     第一种方式
    suit.addTest(ceshi('test_right'))
    suit.addTest(ceshi('test_ture'))
    #     第二种方式
    # 将qwe类中所有以test开头的函数都添加进去
    #     suit.addTest(unittest.makeSuite(ceshi))
    #  打开一个空文件
    f = open('abcDDD.html', 'wb')
    # 定义测试报告的信息
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='接口测试报告', tester='李国帅', description='结果如下')
    runner.run(suit)
    f.close()