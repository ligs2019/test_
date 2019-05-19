#! /usr/bin/python
# -*- coding:utf-8 -*-
from python1.HTMLTestRunner import HTMLTestRunner
import unittest
# from jiekou.用例.test_denglu import denglu
def Baogao(name):
    suit = unittest.TestSuite()
    for i in name:
        print(i)
        dis = unittest.defaultTestLoader.discover(r'e:\Users\PycharmProjects\python1\jiekou\用例',
                                                  pattern='test_{}.py'.format(i.strip()))
        for j in dis:
            suit.addTest(j)
    # suit.addTest(Denglu('test_2'))
    #     第二种方式
    # 将qwe类中所有以test开头的函数都添加进去
    #     suit.addTest(unittest.makeSuite(ceshi))
    #  打开一个空文件
    f = open(r'E:\Users\PycharmProjects\python1\jiekou\report\abcde.html','wb')
    # 定义测试报告的信息
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='脉感测试报告', tester='李国帅', description='结果如下')
    runner.run(suit)
    f.close()

