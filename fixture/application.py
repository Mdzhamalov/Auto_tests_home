from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from fixture.session import SessionHelper
from fixture.contract import ContractHelper
from fixture.table import TableHelper
from fixture.page import PageHelper


class Application:
    rlogin = "test_0.104"
    remail = "test@ssss.ru"
    rpassword = "Asdf1234%"
    rrepeat = "Asdf1234%"
    parent = "test_0"
    value = "9000000"

    def __init__(self):
        self.driver = webdriver.Chrome()  # Инициализация драйвера
        self.driver.maximize_window()
        self.session = SessionHelper(self)  # Инициализация помошников
        self.contract = ContractHelper(self)
        self.table = TableHelper(self)
        self.page = PageHelper(self)

    def signup_to_bonus(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[1]').send_keys(self.rlogin)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[2]').send_keys(self.remail)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[3]').send_keys(self.rpassword)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[4]').send_keys(self.rrepeat)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/button').click()

    def find_invitor(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/main/div[1]/div/div/div[2]/div[3]/input').send_keys(self.parent)
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/main/div[1]/div/div/div[2]/div[3]/ul/li[1]').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/main/div[1]/div/div/div[2]/a').click()

    def add_money(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/ul/li[1]/ul/a[3]').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[3]/div/div[1]/a').click()
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[3]/div/div[2]/ul/li[2]/div/label').click()
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[3]/div/div[2]/div[2]/button[2]').click()
        self.driver.find_element_by_css_selector('[placeholder = "0"]').send_keys(self.value)
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[3]/div/div[2]/div[3]/button[2]').click()

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

    def destroy(self):
        self.driver.quit()


