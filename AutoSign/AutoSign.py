import time
from selenium import webdriver
import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class LoginCase(unittest.TestCase):
    def setUp(self):
        print('before test')
        self.dr = webdriver.Chrome()
        # self.dr.get('http://localhost/wordpress/wp-admin/edit.php')

    def test_go(self):
        self.dr.get('https://test.everonet.com/everonet/#/login')
        username = 'whoosha'
        password = 'wKUO09nGodD75YBI'
        self.login(username, password)

        # self.dr.get('http://localhost/wordpress/wp-admin/edit.php')
        # actions = ActionChains(self.dr)
        # list1 = self.by_css('#the-list tr')
        # trash = self.by_css('.trash')
        # actions.move_to_element(list1).click(trash).perform()
        # time.sleep(4)
        # list1.find_element_by_css_selector('.submitdelete').click()
        time.sleep(4)

        self.dr.get('https://test.everonet.com/everonet/#/trade/list')
        self.by_id('orderNO').send_keys('20190218101634493')
        self.by_xpath('//*[@id="content"]/div/trade-list/div/div/div[1]/form/div[16]/div[2]/button').click()
        time.sleep(4)


    def login(self, username, password):
        self.by_id('username').send_keys(username)
        self.by_id('password').send_keys(password)
        # self.by_id('wp-submit').click()
        self.by_id('password').send_keys(Keys.ENTER)

    def by_id(self, the_id):
        return self.dr.find_element_by_id(the_id)

    def by_name(self, the_name):
        return self.dr.find_element_by_name(the_name)

    def by_css(self, css):
        return self.dr.find_element_by_css_selector(css)
    def by_xpath(self, xpath):
        return self.dr.find_element_by_xpath(xpath)

    def tearDown(self):
        print('after every test')
        self.dr.quit()

if __name__ == "__main__":
    unittest.main()