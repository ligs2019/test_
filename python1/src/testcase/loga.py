#!/user/bin/python
#--*--coding:utf-8--*--
import os
import logging
import datetime
#创建一个日志名字
logss=os.path.join(r'E:\Users\PycharmProjects\python1\src\logs',str(datetime.datetime.now().date())+'.out')
print(logss)
#创建日志输出的格式
formatter=logging.Formatter(fmt='%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',datefmt='%d-%m-%Y:%H:%M:%S')
print(formatter)
#日志输出到控制台
con_handler=logging.StreamHandler()
#加载日志格式
con_handler.setFormatter(formatter)
#将日志输出到文本
fil_handler=logging.FileHandler(logss,encoding='utf-8')
#定义一个函数
def get_logger(name):
    # 获取脚本的名字传入日志中
    logger=logging.getLogger(name)
    # 加入一个手柄
    logger.addHandler(con_handler)
    logger.addHandler(fil_handler)
    #设置日志等级
    logger.setLevel(logging.INFO)
    return logger
go=get_logger('loga.py')
#info代表第四个等级
go.info('hahaha')
