from selenium import webdriver
from getElement import *
br = webdriver.Chrome()
br.get('https://www.baidu.com/')

by_id(br,'kw').clear()
by_id(br,'kw').send_keys('uzi')
br.find_element_by_id('su').click()

