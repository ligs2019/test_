#!/user/bin/python
#--*--coding:utf-8--*--
from time import sleep
import unittest
from appium import webdriver
class diesheng(unittest.TestCase):
    d = {
        "device": "android",
        "platformName": "Android",
        "platformVersion": "7.1.1",
        "deviceName": "851QFDSJ2254U",
        "appPackage": "com.qk.butterfly",
        "appActivity": ".main.LauncherActivity",
        "noReset": "True"
    }
    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=cls.d)

    def login(self, name, password):
        sleep(2)
        self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
        sleep(2)
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(name)
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').clear()
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(name)
        sleep(2)
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(password)
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').clear()
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(password)
        sleep(2)
        print('准备登陆')
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
        sleep(2)

    def test_1(self):
        self.login('15903893872', 'lgs0624')
        sleep(2)
        print('开始断言')
        text = self.dr.find_element_by_id('com.qk.butterfly:id/tv_tag1').text
        self.assertEqual(text, '热门')

    def exit(self):
        # find_element_by_class_name()  定位一个class属性的元素，要求该元素唯一
        # find_elements_by_class_name()  定位多个class属性的元素，元素是多个
        aa = self.dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
        print(aa)
        aa[3].click()
        self.dr.find_element_by_id('com.qk.butterfly:id/v_me_setting').click()
        sleep(0.5)
        self.dr.find_element_by_id('com.qk.butterfly:id/v_me_grade').click()
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_ok').click()

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()


if __name__ == '__main__':
    unittest.main()