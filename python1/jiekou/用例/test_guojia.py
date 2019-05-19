#! /usr/bin/python
# -*- coding:utf-8 -*-
import unittest
from jiekou.config.Guojia import guojia
class GUOjia(unittest.TestCase):
    def test_guojia1(self):
        gj = guojia()
        self.assertEqual(gj['code'], 0)
if __name__== '__main__':
    unittest.main()