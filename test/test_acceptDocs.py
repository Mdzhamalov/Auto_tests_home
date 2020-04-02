import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

class AcceptDocs(unittest.TestCase):

    admin_login = "Adminadmin"
    admin_password = "5GxS4PA76vBdL4cE"
    user_login = "test_0.110"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://4dev.backend.at-profit.com/admin/account/userdocument/")
        self.driver.maximize_window()
        self.login()

    def login(self):
        self.driver.find_element_by_name("username").send_keys(self.admin_login)
        self.driver.find_element_by_name("password").send_keys(self.admin_password)
        self.driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()

    def test_acceptDocs(self):
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('searchbar').send_keys(self.user_login)
        self.driver.find_element_by_css_selector("[value = 'Найти']").click()
        self.accept_address()
        self.accept_passport()

    def accept_address(self):
        self.driver.find_element_by_link_text(self.user_login).click()
        self.select = Select(self.driver.find_element_by_id('id_status'))
        self.select.select_by_value("ok")
        self.driver.find_element_by_name('_save').click()
        self.driver.implicitly_wait(2)
        add_status = self.driver.find_element_by_class_name('field-status').text
        if add_status == "принято":
            print("Address has been successfully accepted")
        else:
            print("Address didn't accepted")
        self.assertEqual(add_status, "принято", "Address didn't accepted")

    def accept_passport(self):
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[2]/td[5]/a[1]').click()
        self.driver.find_element_by_id('searchbar').send_keys(self.user_login)
        self.driver.find_element_by_css_selector("[value = 'Найти']").click()
        pass_status = self.driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[2]/td[4]').text
        if pass_status == "принято":
            print("Passport has been successfully accepted")
        else:
            print("Passport didn't accepted")
        self.assertEqual(pass_status, "принято", "Passport didn't accepted")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()