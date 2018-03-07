#-*-coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
driver.get("https://mail.163.com")

driver.switch_to.frame("x-URS-iframe")
email=driver.find_element_by_name("email")
email.clear()
email.send_keys("fengxin")
password=driver.find_element_by_name("password")
password.clear()
password.send_keys("34345345435")
driver.find_element_by_id("dologin").send_keys(Keys.ENTER)