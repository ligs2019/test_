#! /usr/bin/python
# -*- coding:utf-8 -*-
from jiekou.report.baogao import Baogao
with open('b.txt','r') as f:
    bb=f.readlines()
if 'all' in bb:
    Baogao('*')
else:
    Baogao(bb)