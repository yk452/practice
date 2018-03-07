#-*-coding:utf-8-*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Firefox()
driver.set_page_load_timeout(30)
driver.implicitly_wait(10)
driver.get("http://www.12306.cn")

#selenium无法控制浏览器标签页，故此路暂时不通
'''
url1=driver.current_url
print(url1)
gp=driver.find_element_by_link_text("购票")
print(gp)
time.sleep(3)
driver.find_element_by_link_text("购票").send_keys(Keys.ENTER)
ActionChains(driver).key_down(Keys.CONTROL).send_keys("T").key_up(Keys.CONTROL).perform()
src = driver.find_element_by_id("fromStationText")
print(src)
'''

des_url=driver.find_element_by_link_text("购票").get_attribute("href")
print(des_url)
driver.get(des_url)

src=driver.find_element_by_id("fromStationText")
src.clear()
src.send_keys("北京")
ActionChains(driver).click(driver.find_element_by_id("citem_2")).perform()

des=driver.find_element_by_id("toStationText")
ActionChains(driver).click(des).perform()
ActionChains(driver).click(driver.find_element_by_id("nav_list4")).perform()
des_child=driver.find_element_by_css_selector("#ul_list4>ul>li[title='南京']")
ActionChains(driver).click(des_child).perform()

btn_check=driver.find_element_by_id("a_search_ticket")
btn_check.send_keys(Keys.ENTER)

#selenium切换窗口的操作
'''
front_window=driver.current_window_handle
print(front_window)
all_handles=driver.window_handles
print(all_handles)
for handle in all_handles:
    if handle != front_window:
        driver.switch_to.window(handle)
        print(driver.current_window_handle)
        src = driver.find_element_by_id("fromStationText")
        src.send_keys(Keys.ENTER)
        print("123")
    else:
        print("bingo")
'''


