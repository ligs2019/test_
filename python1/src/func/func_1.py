#!/user/bin/python
#--*--coding:utf-8--*--
import yaml
import appium
with open(r'E:\Users\PycharmProjects\python1\src\func\item.yaml','r',encoding='utf-8') as fb:
    # a=yaml.load(fb) 使用yaml模块的load方法将yaml文件中的数据转换成python字典的形式
    item_data=yaml.load(fb,Loader=yaml.FullLoader) #字典
    # print(item_data)
    # print(item_data['three']['wx_id'])

def foo(driver):
    text=driver.find_element_by_id(item_data['three']['wx_id']).find_element_by_class_name('android.widget.TextView').text
    return text
def qq(driver):
    text02=driver.find_element_by_id(item_data['three']['qq_id']).find_element_by_class_name('android.widget.TextView').text
    return text02
def wb(driver):
    text03=driver.find_element_by_id(item_data['three']['wb_id']).find_element_by_class_name('android.widget.TextView').text
    return text03
def pd(driver):
    text04=driver.find_element_by_id(item_data['three']['pd_id']).find_element_by_class_name('android.widget.TextView').text
    return text04

