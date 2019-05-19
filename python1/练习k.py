#! /usr/bin/python
# -*- coding:utf-8 -*-
from appium import webdriver
from time import sleep
import unittest


class DS(unittest.TestCase):

    # 测试脚本与appium服务器进行连接的参数数据
    d =  {
  "device": "android",
  "platformName": "Android",
  "platformVersion": "7.1.1",
  "deviceName": "851QFDSJ2254U",
  "appPackage": "com.qk.butterfly",
  "appActivity": ".main.LauncherActivity",
  "noReset": "True"
}
    @classmethod#加这个就是代表下面的setup是一个类
    # 建立连接的函数
    def  setUpClass(cls):#cls表示类的实例
        cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=cls.d)
    # 跳转至手机号/密
    # 码登录页面的函数
    # def tiao_zhuan(self):
    #     # 点击密码图标
    #     self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
    #     sleep(2)

    # 账号密码输入函数
    def login(self, phone, password):
        self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
        # 向账号输入框内输入手机号
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(phone)
        # 向密码输入框内输入密码
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(password)
        # 点击登录按钮
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
        # 查看登录之后的效果
        sleep(5)
    def test_1(self):
        self.login('15903893872','lgs0624')
        text = self.dr.find_element_by_id('com.qk.butterfly:id/tv_tag1').text
        self.assertEqual(text, '热门')
    def exit(self):
        # find_element_by_class_name()  定位一个class属性的元素，要求该元素唯一
        # find_elements_by_class_name()  定位多个class属性的元素，元素是多个
       aa= self.dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
       print(aa)
    # 关闭app的函数
    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()
if __name__ == '__main__':
    # unittest.main()
    DS().exit()


