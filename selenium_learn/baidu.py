#-*-coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
#driver = webdriver.Chrome()

first_url="http://baidu.com"
print("now access %s" %(first_url))
driver.get(first_url)
print(driver.title)
driver.find_element_by_id("kw").send_keys("综艺")
driver.find_element_by_id("su").click()
above = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(above).perform()

second_url="http://news.baidu.com"
print("now access %s" %(second_url))
driver.get(second_url)
driver.refresh()

print("back to last_page")
driver.back()
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").submit()

print("forward to next_page")
driver.forward()

driver.quit()
