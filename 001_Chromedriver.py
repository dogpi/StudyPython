from selenium import webdriver
import time

option = webdriver.ChromeOptions()
# option.add_argument('disable-infobars')
# option.add_argument("headless")

driver = webdriver.Chrome(options = option)
driver.get("http://www.baidu.com")
time.sleep(5)
driver.get("http://www.zhihu.com")
time.sleep(5)
driver.get("http://www.taobao.com")
time.sleep(5)
driver.close()