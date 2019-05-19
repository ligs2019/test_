#! /usr/bin/python
# -*- coding:utf-8 -*-
import unittest
class qwe(unittest.TestCase):
    def test_1(self):
        a=4+5
        self.assertEqual(a,9)
    def test_2(self):
        b=6-5
        self.assertEqual(b,1)
# 统一执行测试
if __name__=='__main__':
    unittest.main()
