import unittest
from selenium import webdriver
import time


class AddCreditCard(unittest.TestCase):

    user_login = "test_0.2"
    password = "Asdf1234%"
    card_holder = "JULIA MCKINNEY"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_add_card(self):
        self.generate_valid_card_number()
        self.login()
        self.attach_card()
        self.input_number_and_name()
        self.status = self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[2]/div/div[2]/div[3]/button[2]').text
        self.assertEqual(self.status, "Add card", "You didn't attach your credit card")
        self.logout()

    def generate_valid_card_number(self):
        self.driver.get("https://www.prepostseo.com/tool/ru/credit-card-generator")
        self.driver.find_element_by_id("master").click()
        self.driver.find_element_by_id("preloader").click()
        time.sleep(3)
        self.card_number = self.driver.find_element_by_xpath('//*[@id="jp-card"]/div[1]/div[7]/div[2]').text

    def login(self):
        self.driver.get("https://4dev.at-profit.com/profile/balance")
        self.driver.implicitly_wait(40)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[1]').send_keys(self.user_login)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[2]').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/button').click()

    def attach_card(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[2]/div/div[1]/a').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[2]/div/div[2]/div[3]/button[2]').click()

    def input_number_and_name(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[2]/div/div[2]/div[2]/div[1]/input').send_keys(self.card_number)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[2]/div/div[2]/div[2]/div[2]/input').send_keys(self.card_holder)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[2]/div/div[2]/div[2]/div[3]/div[1]/div/div[1]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[2]/div/div[2]/div[2]/div[3]/div[1]/div/div[1]/div/ul/li[3]').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[2]/div/div[2]/div[2]/div[3]/div[1]/div/div[2]/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[2]/div/div[2]/div[2]/div[3]/div[1]/div/div[2]/div/ul/li[4]').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div/div').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div/div/ul/li[2]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[2]/div/div[2]/div[3]/button[2]').click()

    def logout(self):
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_class_name('pointer').click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()