#! /usr/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver

from time import sleep
# #定义要打开的浏览器
# dr=webdriver.Firefox()
# #请求网页
# dr.get('https://www.douban.com/')
# sleep(3)
# #frame（网页框架），切换到框架，通过id或name去切换
# #或者先定为到框架。再付给一个变量，下面填写id或name的地方填变量
# #dr.switch_to.frame('login_frame')
# #
# dr.find_element_by_id('switcher_plogin').click()
# sleep(3)
# dr.find_element_by_id('u').send_keys('969598484@')
# sleep(3)
# dr.find_element_by_id('p').send_keys('lgs418710...')
# sleep(3)
#
# dr.find_element_by_id('login_button').click()
# sleep(10)
# #退出框架,是退出到最初页面
# #dr.switch_to_default.content()
# #退出到上一层框架(多层框架时候)
# dr.switch_to.parent_frame()


# dr.switch_to.default_content()
# dr.find_element_by_id('composebtn').click()
# sleep(2)
# dr.find_element_by_xpath('/html/body').send_keys('6666666')
# dr.find_element_by_id('subject').send_keys('hahaha')

# dr.find_element_by_id('login_button').click()
# # dr.get('https://www.jd.com')
# sleep(3)
# #回到上一次打开的网页
# dr.back()
# sleep(3)
# #前进
# dr.forward()
#关闭浏览器
# dr.quit()
#获取网页标题,一般用作断言，判断请求到的网页标题是否符合预期结果
# print(dr.title)
# #获取请求的网址
# print(dr.current_url)
# #设置浏览器窗口大小
# dr.set_window_size(400,400)
# #设置浏览器窗口的位置
# dr.set_window_position(400,400)
# #最大化浏览器
# dr.maximize_window()
# sleep(3)
# #最小化
# dr.minimize_window()
#1.id定位
# dr.find_element_by_id('kw').send_keys('哈哈')
# dr.find_element_by_id('su').click()
# #2.class定位，为了区分python中的class，这里叫class_name，单个定位时候，要保证class值是唯一的
# dr.find_elements_by_class_name('manv')[0].click()
#3.name定位,name不一定有
#4. dr.find_element_by_name('wd').send_keys('hahaha')
#link_text文本定位，保证文本的唯一性
#5. dr.find_element_by_link_text('hao123').click()
#模糊文本定位partial link text，保证唯一性
# dr.find_element_by_partial_link_text('hao').click()
#6.tag_name定位   通过标签页名称定位
# dr.find_element_by_tag_name()
#7.路径定位xpath （路径标记语言）一个/叫绝对路径，两个//是相对路径
# dr.find_element_by_xpath('//*[@id="kw"]').click()
#8.css  定位  复制css路径，选择器都行
# dr.find_element_by_css_selector('#kw').click()
#动作   1.send_keys 输入
     # 2.click 点击
     # 3.clear   清除
     # 4.text   文本（就是获取这位置的文本
#9.定位一组对象（定位多个数据）elements,就是有多个数据
# dr.find_elements_by_id('su')
#10.层级定位，就是先定位一个顶层元素大的方向，再定位这个元素下面的元素，多用于复杂的定位场景下，父元素必须是单一的
#   例如下面例子中id的值必须是唯一的
# aa=dr.find_element_by_id('searchHotelLevelSelect').find_elements_by_tag_name('option')
# for i in aa:
#    print(i.text)
#qq空间页面点击退出会弹出框，叫alter
#定位退出按钮
# dr.switch_to.default_content()
# dr.find_element_by_class_name('ui-icon icon-logout').click()
#
#切换到alter上去，自动点击确定,将控制器切换到弹出框
#
# dr.find_element_by_xpath('/html/body/input').click()
# sleep(2)
# # 将控制器切换到弹出框
# ww=dr.switch_to_alert()
# # 获取弹出框上的文本
# print(ww.text)
# #点击确定
# # ww.accept()
# #输入数据
# ww.send_keys('join')
# ww.accept()
#点击取消
# ww.dismiss()
dr=webdriver.Firefox()
# #请求网页
dr.get('https://www.douban.com/')#1号窗口
dr.find_element_by_xpath('/html/body/div[1]/div[1]/ul/li[1]/a').click()
sleep(3)
#获取当前窗口的标识(句柄)
print(dr.current_window_handle)
sleep(3)
#获取所有窗口的标识
ww=dr.window_handles
#切换窗口
dr.switch_to.window(ww[-1])
print(dr.title)
#浏览器本身是无法决定什么情况下打开哪个窗口的
#按照窗口打开的顺序gei窗口标号（唯一标识窗口的字符串）


