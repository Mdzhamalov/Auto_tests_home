import time


class SessionHelper:
    admin_login = "Adminadmin"
    admin_password = "5GxS4PA76vBdL4cE"
    user_login = "test_1.8"
    password = "Asdf1234%"

    def __init__(self, app):
        self.app = app

    def login(self):
        self.app.driver.implicitly_wait(15)
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[1]').send_keys(self.user_login)
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[2]').send_keys(self.password)
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/button').click()

    def login_to_backend(self):
        self.app.driver.implicitly_wait(5)
        self.app.driver.find_element_by_name("username").send_keys(self.admin_login)
        self.app.driver.find_element_by_name("password").send_keys(self.admin_password)
        self.app.driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()

    def logout(self):
        time.sleep(3)
        self.app.driver.implicitly_wait(2)
        self.app.driver.find_element_by_class_name('pointer').click()
