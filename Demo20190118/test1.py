from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 这三行，可以去掉浏览器的提示信息“chrome正受到自动测试软件的控制”
options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=options)

driver.get('https://www.baidu.com')


def by_id(dr, the_id):
    return dr.find_element_by_id(the_id)

by_id(driver, 'kw').send_keys('wusongbai')
by_id(driver, 'kw').send_keys(Keys.CONTROL, 'a')
by_id(driver, 'kw').send_keys(Keys.CONTROL, 'c')
by_id(driver, 'kw').send_keys(Keys.CONTROL, 'v')
by_id(driver, 'kw').send_keys(Keys.CONTROL, 'v')
time.sleep(10)
by_id(driver, 'su').send_keys(Keys.ENTER)
time.sleep(10)

