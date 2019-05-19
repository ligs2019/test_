#! /usr/bin/python
# -*- coding:utf-8 -*-
import unittest
from jiekou.config.xinxixi import Xinxi
from jiekou.data.zhizhi import Zhi
class ceshi(unittest.TestCase):
    def test_right(self):
        qq = Xinxi().xinxi((Zhi()[0][0]))
        print(qq)
        self.assertEqual(qq['code'], 0)
#
#
    def test_ture(self):
        hh = Zhi()
        for i in range(1, len(hh) - 1):
            ww = Xinxi().xinxi(Zhi()[i][0])
            self.assertNotEqual(ww['code'], 0)
if __name__== '__main__':
    unittest.main()
# print(Xinxi().xinxi((Zhi()[0][0])))