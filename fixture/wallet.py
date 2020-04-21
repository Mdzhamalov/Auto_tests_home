from selenium.webdriver.support.ui import Select
import time


class WalletHelper:

    def __init__(self, app):
        self.app = app

    def add_money(self, value):
        self.app.driver.implicitly_wait(10)
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/ul/li[1]/ul/a[3]').click()
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[3]/div/div[1]/a').click()
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[3]/div/div[2]/ul/li[2]/div/label').click()
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[3]/div/div[2]/div[2]/button[2]').click()
        self.app.driver.find_element_by_css_selector('[placeholder = "0"]').send_keys(value)
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[3]/div/div[2]/div[3]/button[2]').click()

    def move_request_to_process(self):
        self.app.driver.implicitly_wait(10)
        self.app.driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[1]/th/a').click()
        self.select = Select(self.app.driver.find_element_by_id("id_status"))
        self.select.select_by_value('in_progress')
        self.app.driver.find_element_by_name('_continue').click()

    def approve_request(self):
        self.app.driver.implicitly_wait(10)
        self.select_approve = Select(self.app.driver.find_element_by_id('id_status'))
        self.select_approve.select_by_value('complete')
        self.app.driver.find_element_by_name('_save').click()

    def generate_valid_card_number(self):
        self.app.driver.implicitly_wait(10)
        self.app.driver.find_element_by_id("master").click()
        self.app.driver.find_element_by_id("preloader").click()
        time.sleep(3)
        self.card_number = self.app.driver.find_element_by_xpath('//*[@id="jp-card"]/div[1]/div[7]/div[2]').text

    def attach_card(self):
        self.app.driver.implicitly_wait(10)
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[2]/div/div[1]/a').click()
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[2]/div/div[2]/div[3]/button[2]').click()

    def input_number_and_name(self, card_holder):
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[2]/div/div[2]/div[2]/div[1]/input').send_keys(self.card_number)
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[2]/div/div[2]/div[2]/div[2]/input').send_keys(card_holder)
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[2]/div/div[2]/div[2]/div[3]/div[1]/div/div[1]/div/div').click()
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[2]/div/div[2]/div[2]/div[3]/div[1]/div/div[1]/div/ul/li[3]').click()
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[2]/div/div[2]/div[2]/div[3]/div[1]/div/div[2]/div/div').click()
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[2]/div/div[2]/div[2]/div[3]/div[1]/div/div[2]/div/ul/li[4]').click()
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div/div').click()
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div/div/ul/li[2]').click()
        time.sleep(1)
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[2]/div/div[2]/div[3]/button[2]').click()
