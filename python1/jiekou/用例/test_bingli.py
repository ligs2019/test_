#! /usr/bin/python
# -*- coding:utf-8 -*-
import unittest
from jiekou.config.Bingli import bingli
class BINGli(unittest.TestCase):
    def test_bingli1(self):
        bl = bingli()
        self.assertEqual(bl['code'], 0)
    def test_bingli2(self):
        bl = bingli()
        self.assertEqual(bl['msg'], 'OK')
if __name__== '__main__':
    unittest.main()