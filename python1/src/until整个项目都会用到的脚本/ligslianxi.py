#!/user/bin/python
#--*--coding:utf-8--*--
from time import sleep
import unittest
from appium import webdriver
from python1.HTMLTestRunner import HTMLTestRunner
class zheda(unittest.TestCase):
    d = {
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "deviceName": "emulator-5554",
        "appPackage": "net.crigh.cgapp_schedule",
        "appActivity":".ui.activity.LoginActivity"
    }

    dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=d)

    def login(self, name, password):
        # sleep(2)
        # self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
        # sleep(2)
        self.dr.find_element_by_id('net.crigh.cgapp_schedule:id/et_username').send_keys(name)
        sleep(3)
        # self.dr.find_element_by_id('net.crigh.cgapp_schedule:id/editLoginUserName').clear()
        # sleep(3)
        # self.dr.find_element_by_id('net.crigh.cgapp_schedule:id/editLoginUserName').send_keys(name)
        sleep(5)
        self.dr.find_element_by_id('net.crigh.cgapp_schedule:id/et_password').send_keys(password)
        sleep(3)
        self.dr.find_element_by_id('net.crigh.cgapp_schedule:id/et_password').clear()
        sleep(3)
        self.dr.find_element_by_id('net.crigh.cgapp_schedule:id/et_password').send_keys(password)
        sleep(2)
        print('准备登陆')
        self.dr.find_element_by_id('net.crigh.cgapp_schedule:id/btn_login').click()
        sleep(10)
        text = self.dr.find_element_by_id('net.crigh.cgapp_schedule:id/largeLabel').text
        print(text)

    def exit(self):

        self.dr.find_element_by_id('net.crigh.cgapp_schedule:id/viewUserInfo').click()
        sleep(10)
        self.dr.find_element_by_id('net.crigh.cgapp_schedule:id/btn_exit').click()
        sleep(8)
        self.dr.find_element_by_id('net.crigh.cgapp_schedule:id/md_buttonDefaultPositive').click()
        print('成功退出')
    def test_1(self):
        self.login('1138100002','123456')
        sleep(5)
        text=self.dr.find_element_by_id('net.crigh.cgapp_schedule:id/largeLabel').text
        sleep(5)
        self.assertEqual(text,'首页')
    def test_2(self):
        # self.login('1138100002', '123456')
        # sleep(8)
        self.dr.find_element_by_id('net.crigh.cgapp_schedule:id/action_myself').click()
        sleep(10)
        textt = self.dr.find_element_by_id('net.crigh.cgapp_schedule:id/mineIntegral').find_element_by_class_name(
            'android.widget.TextView').text
        print(textt)
        self.assertEqual(textt,'我的积分')
        sleep(10)

    def close_app(self):
        self.dr.quit()
if __name__== '__main__':
    suit=unittest.TestSuite()
    suit.addTest(zheda('test_1'))
    suit.addTest(zheda('test_2'))
    f=open('zhedajiaoshi.html','wb')
    runner=HTMLTestRunner(stream=f,title='浙大教室测试报告',tester='李国帅',description='结果如下')
    runner.run(suit)



    # zheda().login('1138100002','123456')
    # zheda().exit()
# zheda().exit()
# zheda().close_app()