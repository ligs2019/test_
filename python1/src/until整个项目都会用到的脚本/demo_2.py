from appium import webdriver
from time import sleep
import unittest
#
d = {
        "device": "android",
        "platformName": "Android",
        "platformVersion": "7.1.1",
        "deviceName": "851QFDSJ2254U",
        "appPackage": "com.qk.butterfly",
        "appActivity": ".main.LauncherActivity",
        "noReset": "True"
    }
dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=d)
sleep(10)
a = dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
print(a)
#所有操作在登录状态
#可点击操作   返回列表
a[3].click()
#模拟手机屏幕滑动
#1.获取当前屏幕分辨率
# size = dr.get_window_size()
# #2.建立坐标
# x1 = size['width'] * 0.5  # x坐标 50
# y1 = size['height'] * 0.25  # 起始y坐标 50
# y2 = size['height'] * 0.75  # 150
# for i in range(2):
#     dr.swipe(x1, y2, x1, y1)
dr.find_element_by_id('com.qk.butterfly:id/v_me_setting').click()
sleep(0.5)
dr.find_element_by_id('com.qk.butterfly:id/v_me_grade').click()
dr.find_element_by_id('com.qk.butterfly:id/tv_ok').click()

# 关闭app
dr.quit()
