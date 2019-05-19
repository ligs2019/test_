#!/user/bin/python
#--*--coding:utf-8--*--
from time import sleep
import unittest
from appium import webdriver
class zheda(object):
    d = {
        "device": "android",
        "platformName": "Android",
        "platformVersion": "7.1.1",
        "deviceName": "851QFDSJ2254U",
        "appPackage": "net.crigh.cgapp_schedule",
        "appActivity": ".activity.login.LoginActivity",
        "noReset": "True"
    }

    dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=d)

    def login(self, name, password):
        # sleep(2)
        # self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
        # sleep(2)
        self.dr.find_element_by_id('net.crigh.cgapp_schedule:id/editLoginUserName').send_keys(name)
        # self.dr.find_element_by_id('net.crigh.cgapp_schedule:id/editLoginUserName').clear()
        # self.dr.find_element_by_id('net.crigh.cgapp_schedule:id/editLoginUserName').send_keys(name)
        sleep(2)
        self.dr.find_element_by_id('net.crigh.cgapp_schedule:id/editLoginUserPas').send_keys(password)
        self.dr.find_element_by_id('net.crigh.cgapp_schedule:id/editLoginUserPas').clear()
        self.dr.find_element_by_id('net.crigh.cgapp_schedule:id/editLoginUserPas').send_keys(password)
        sleep(2)
        print('准备登陆')
        self.dr.find_element_by_id('net.crigh.cgapp_schedule:id/btnLogin').click()
        sleep(2)
    def exit(self):
        aa=self.dr.find_elements_by_class_name('android.widget.LinearLayout')

        # aa[2].click()
        # self.dr.find_element_by_id('net.crigh.cgapp_schedule:id/btn_exit_app').click()

zheda().exit()
