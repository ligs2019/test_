#导入函数

from python1.src.func.func_1 import foo
from python1.src.func.func_1 import qq
from python1.src.func.func_1 import wb,pd
from appium import webdriver
import time
import unittest
from python1.src.until整个项目都会用到的脚本.xixi import REPORT_DIR
from python1.src.HTMLTestRunner  import HTMLTestRunner
from python1.src.testcase.loga import get_logger
g=get_logger(name='test_ceshi.py')
class TEXT(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        d = {
            "device": "android",
            "platformName": "Android",
            "platformVersion": "7.1.1",
            "deviceName": "851QFDSJ2254U",
            "appPackage": "com.qk.butterfly",
            "appActivity": ".main.LauncherActivity",
            "noReset": "True"
        }
        cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=d)
        time.sleep(5)
        g.info('app建立')
    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()
        g.info('app结束')
    def test_wx(self):
        # 验证微信的用例
        g.info('执行微信用例')
        text = foo(self.dr)
        # 断言
        # self.assertEqual(wx(self.dr),'微信')
        self.assertEqual(text,'微信')


    def test_wb(self):
        g.info('执行微博')
        text = wb(self.dr)
        self.assertEqual(text,'微博')

    def test_pd(self):
        g.info('执行密码')
        text = pd(self.dr)
        self.assertEqual(text,'密码')

    def test_qq(self):
        g.info('执行qq')
        text = qq(self.dr)
        self.assertEqual(text,'QQ')

if __name__ == '__main__':
        suit = unittest.TestSuite()
        suit.addTest(TEXT('test_wx'))
        suit.addTest(TEXT('test_wb'))
        suit.addTest(TEXT('test_pd'))
        suit.addTest(TEXT('test_qq'))
        # lujing=REPORT_DIR+'aaa.html'
        f = open('aaa.html', 'wb')
        runner = HTMLTestRunner(stream=f, title='接口测试报告', tester='李国帅', description='结果如下')
        # verbosity 默认是0，2使控制台输出信息更加详细
        runner.run(suit)
        # f.close()
