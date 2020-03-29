import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


class WalletReplenishment(unittest.TestCase):

    user_login = "test_0.1.5"
    password = "Asdf1234%"
    value = "9000000"
    admin_login = "Adminadmin"
    admin_password = "5GxS4PA76vBdL4cE"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://4dev.at-profit.com/signin")
        self.driver.maximize_window()

    def test_replenishment(self):
        self.login()
        self.create_request_EUR()
        self.logout()
        self.login_to_backend()
        self.move_request_to_process()
        self.approve_request()
        self.driver.implicitly_wait(5)
        self.request_status = self.driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[1]/td[2]').text
        self.assertEqual(self.request_status, "запрос выполнен", "Request didn't approved")

    def login(self):
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[1]').send_keys(self.user_login)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[2]').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/button').click()

    def create_request_EUR(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/ul/li[1]/ul/a[3]').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[3]/div/div[1]/a').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[3]/div/div[2]/ul/li[2]/div/label').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[3]/div/div[2]/div[2]/button[2]').click()
        self.driver.find_element_by_css_selector('[placeholder = "0"]').send_keys(self.value)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[3]/div/div[2]/div[3]/button[2]').click()
        time.sleep(1)
        self.driver.implicitly_wait(4)
        status = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[3]/div/div[2]/div[1]/div/a').text
        self.assertEqual(status, "Скачать", "Request didn't created")

    def logout(self):
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_class_name('pointer').click()

    def login_to_backend(self):
        self.driver.get("https://4dev.backend.at-profit.com/admin/bank/depositinvoice/")
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_name("username").send_keys(self.admin_login)
        self.driver.find_element_by_name("password").send_keys(self.admin_password)
        self.driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()

    def move_request_to_process(self):
        self.driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[1]/th/a').click()
        self.select = Select(self.driver.find_element_by_id("id_status"))
        self.select.select_by_value('in_progress')
        self.driver.find_element_by_name('_continue').click()

    def approve_request(self):
        self.driver.implicitly_wait(5)
        self.select_approve = Select(self.driver.find_element_by_id('id_status'))
        self.select_approve.select_by_value('complete')
        self.driver.find_element_by_name('_save').click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()