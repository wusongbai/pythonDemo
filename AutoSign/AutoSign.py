import time
from selenium import webdriver
import unittest

from selenium.webdriver import ActionChains


class LoginCase(unittest.TestCase):
    def setUp(self):
        print('before test')
        self.dr = webdriver.Chrome()
        # self.dr.get('http://localhost/wordpress/wp-admin/edit.php')

    def test_go(self):
        self.dr.get('http://localhost/wordpress/wp-login.php')
        username = password = 'admin'
        self.login(username, password)

        self.dr.get('http://localhost/wordpress/wp-admin/edit.php')
        actions = ActionChains(self.dr)
        list1 = self.by_css('#the-list tr')
        trash = self.by_css('.trash')
        actions.move_to_element(list1).click(trash).perform()
        time.sleep(4)
        # list1.find_element_by_css_selector('.submitdelete').click()



    def login(self, username, password):
        self.by_id('user_login').send_keys(username)
        self.by_id('user_pass').send_keys(password)
        self.by_id('wp-submit').click()

    def by_id(self, the_id):
        return self.dr.find_element_by_id(the_id)

    def by_name(self, the_name):
        return self.dr.find_element_by_name(the_name)

    def by_css(self, css):
        return self.dr.find_element_by_css_selector(css)

    def tearDown(self):
        print('after every test')
        self.dr.quit()