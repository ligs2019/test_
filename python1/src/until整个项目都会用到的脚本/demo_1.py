#!/user/bin/python
#--*--coding:utf-8--*--
from appium import webdriver
from time import sleep


class DS(object):

    # 测试脚本与appium服务器进行连接的参数数据
    d = {
  "device": "android",
  "platformName": "Android",
  "platformVersion": "7.1.1",
  "deviceName": "851QFDSJ2254U",
  "appPackage": "com.qk.butterfly",
  "appActivity": ".main.LauncherActivity",
  "noReset": "True"
}

    # 建立连接的函数
    def __init__(self):

        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.d)
        sleep(10.0)

    # 检查那四个文字的函数/方法
    def check_text(self):

        # 获取微信文字
        # text = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
        test = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name(
          'android.widget.TextView').text
        test1 = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name(
          'android.widget.TextView').text
        test2 = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name(
          'android.widget.TextView').text
        test3 = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').find_element_by_class_name(
          'android.widget.TextView').text
        print(test,test1,test2,test3)
        return test,test1,test2,test3

    # 关闭app的函数
    def close_app(self):
        self.dr.quit()


if __name__ == '__main__':
    go = DS()  # 创建一个DS类的实例，赋值给变量go
    # 调用DS类的方法
    go.check_text()
    go.close_app()
