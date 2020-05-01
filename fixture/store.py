import time


class StoreHelper:

    def __init__(self, app):
        self.app = app

    def go_to_catalog(self):
        time.sleep(1)
        self.app.driver.find_element_by_xpath('//*[@id="app"]/header/div/div/div/div[1]/nav/ul/li[3]').click()

    def navigate_to_basket(self):
        self.app.driver.find_element_by_xpath('//*[@id="app"]/header/div/div/div/div[2]/div[1]/div/span[1]').click()

    def add_1g_to_basket(self):
        self.app.driver.implicitly_wait(5)
        one_g = self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[4]/div/div/div/div/div/h3/span')
        self.app.driver.execute_script("arguments[0].scrollIntoView();", one_g)
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[4]/div/div/div/button').click()

    def add_5g_to_basket(self):
        self.app.driver.implicitly_wait(5)
        five_g = self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div[2]/div/div/div/h3/span')
        self.app.driver.execute_script("arguments[0].scrollIntoView();", five_g)
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/div/div[3]/div/button').click()

    def add_10g_to_basket(self):
        self.app.driver.implicitly_wait(5)
        ten_g = self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div[3]/div/div/div/h3/span')
        self.app.driver.execute_script("arguments[0].scrollIntoView();", ten_g)
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div[3]/div/button').click()

    def add_20g_to_basket(self):
        self.app.driver.implicitly_wait(5)
        twenty_g = self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/div/div/h3/span')
        self.app.driver.execute_script("arguments[0].scrollIntoView();", twenty_g)
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/button').click()

    def add_oz_to_basket(self):
        self.app.driver.implicitly_wait(5)
        oz = self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/h3/span')
        self.app.driver.execute_script("arguments[0].scrollIntoView();", oz)
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/button').click()

    def add_50g_to_basket(self):
        self.app.driver.implicitly_wait(5)
        fifty_g = self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/div/div/h3/span')
        self.app.driver.execute_script("arguments[0].scrollIntoView();", fifty_g)
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/button').click()

    def add_100g_to_basket(self):
        self.app.driver.implicitly_wait(5)
        oneh_g = self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/div/div/div/div/div/h3/span')
        self.app.driver.execute_script("arguments[0].scrollIntoView();", oneh_g)
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/div/div/div/button').click()

    def return_to_basket(self):
        time.sleep(1)
        self.app.driver.implicitly_wait(5)
        self.app.driver.find_element_by_xpath('//*[@id="app"]/header/div/div/div/div[2]/div[1]/div/div').click()

    def choose_contract(self):
        self.app.driver.find_element_by_class_name("select").click()
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/div/div[3]/div/div/ul/li[1]').click()

    def pay_for_bonus(self):
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[2]/button').click()

    def pay_for_euro(self):
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[4]/span[2]').click()
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[2]/button').click()




