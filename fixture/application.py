from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


class Application:
    rlogin = "test_0.100"
    remail = "test@ssss.ru"
    rpassword = "Asdf1234%"
    rrepeat = "Asdf1234%"
    parent = "test_0"
    value = "9000000"
    admin_login = "Adminadmin"
    admin_password = "5GxS4PA76vBdL4cE"
    user_login = "test_0.8"
    password = "Asdf1234%"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def signup_to_bonus(self):
        self.driver.get("https://4dev.at-profit.com/signup")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[1]').send_keys(self.rlogin)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[2]').send_keys(self.remail)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[3]').send_keys(self.rpassword)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[4]').send_keys(self.rrepeat)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/button').click()

    def find_invitor(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/main/div[1]/div/div/div[2]/div[3]/input').send_keys(self.parent)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/main/div[1]/div/div/div[2]/div[3]/ul/li[1]').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/main/div[1]/div/div/div[2]/a').click()

    def add_money(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/ul/li[1]/ul/a[3]').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[3]/div/div[1]/a').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[3]/div/div[2]/ul/li[2]/div/label').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[3]/div/div[2]/div[2]/button[2]').click()
        self.driver.find_element_by_css_selector('[placeholder = "0"]').send_keys(self.value)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/ul/div[3]/div/div[2]/div[3]/button[2]').click()

    def logout(self):
        time.sleep(3)
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

    def destroy(self):
        self.driver.quit()

    def login(self):
        self.driver.get("https://4dev.at-profit.com/profile/contracts")
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[1]').send_keys(self.user_login)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[2]').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/button').click()

    def buy_vip(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div[4]/div[2]/button').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[2]/a').click()

    def place_in_finish(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/ul/li[2]/ul/a[2]').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/ul[1]/li[1]/div/div/div[1]/button').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div[2]/a').click()

