#! /usr/bin/python
# -*- coding:utf-8 -*-
import unittest
from jiekou.config.请求 import qingqiu
from jiekou.data.read import hahaha
import unittest
from jiekou.config.xinxixi import Xinxi
from jiekou.data.zhizhi import Zhi
from jiekou.config.请求 import qingqiu
class denglu(unittest.TestCase):
    def test_denglu1(self):  # 有效
        ccc= hahaha().haha()
        bbb=qingqiu().denglu(int(ccc[0][0]),int(ccc[0][1]))
        print(bbb)
        self.assertEqual(bbb['code'], 0)
    def test_denglu2(self):
        ddd=hahaha().haha()
        for i in range(1,len(ddd)-1):
            eee = qingqiu().denglu(int(ddd[i][0]), int(ddd[i][1]))
            self.assertNotEqual(eee['code'],0)
    def test_xinxi1(self):
        qq = Xinxi().xinxi((Zhi()[0][0]))
        print(qq)
        self.assertEqual(qq['code'], 0)
    def test_xinxi2(self):
        hh = Zhi()
        for i in range(1, len(hh) - 1):
            ww = Xinxi().xinxi(Zhi()[i][0])
            self.assertNotEqual(ww['code'], 0)
    def test_guojia1(self):
        gj=qingqiu().guojia()
        self.assertEqual(gj['code'],0)
    def test_bingli1(self):
        bl=qingqiu().bingli()
        self.assertEqual(bl['code'],0)




if __name__== '__main__':
    unittest.main()