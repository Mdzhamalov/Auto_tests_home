import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def signup_to_bonus(self, rlogin, remail, rpassword, rrepeat):
        self.app.driver.implicitly_wait(10)
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[1]').send_keys(rlogin)
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[2]').send_keys(remail)
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[3]').send_keys(rpassword)
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[4]').send_keys(rrepeat)
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/button').click()

    def login(self, user_login, password):
        self.app.driver.implicitly_wait(15)
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[1]').send_keys(user_login)
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[2]').send_keys(password)
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/button').click()

    def logout(self):
        time.sleep(1)
        self.app.driver.implicitly_wait(2)
        self.app.driver.find_element_by_class_name('pointer').click()

    def login_to_backend(self, admin_login, admin_password):
        self.app.driver.implicitly_wait(5)
        self.app.driver.find_element_by_name("username").send_keys(admin_login)
        self.app.driver.find_element_by_name("password").send_keys(admin_password)
        self.app.driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input').click()

    def logout_from_backend(self):
        time.sleep(1)
        self.app.driver.find_element_by_class_name("sidebar-dependent").click()
        self.app.driver.find_element_by_link_text("Выйти").click()
        time.sleep(1)
