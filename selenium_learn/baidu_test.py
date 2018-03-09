#-*-coding:utf-8-*-
import unittest
from selenium import webdriver
import  HTMLTestRunner

class TestBaiDu(unittest.TestCase):

    #unittest定义测试固件类，这样保证在整个测试中，setUp与tearDown只执行一次
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.driver.get("http://www.baidu.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_b1(self):
        self.assertEqual(self.driver.title,"百度一下，你就知道")

    def test_b2(self):
        self.assertEqual(self.driver.current_url,"https://www.baidu.com/")

    def test_b3(self):
        self.assertTrue(self.driver.find_element_by_id("kw").is_enabled())

if __name__ =="__main__":
    #unittest.main(verbosity=2)
    suite=unittest.TestLoader().loadTestsFromTestCase(TestBaiDu)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=open('testReport.html','wb'),
        title='测试报告',
        description="测试报告详细信息"
    )
    runner.run(suite)


