import random
from selenium.webdriver.common.action_chains import ActionChains


class PersonalInformationHelper:

    location_to_avatar = "F:/Cactus_Vision/AT_Golden/User_photos/test_6.jpg"
    doc_address = "F:/Cactus_Vision/AT_Golden/User_photos/London.jpg"
    number_doc = random.randint(1, 1000)

    def __init__(self, app):
        self.app = app

    def upload_avatar(self):
        self.app.driver.implicitly_wait(10)
        self.app.driver.find_element_by_xpath("//div[@id='app']/div/div/div/div[2]/div/ul/li/ul/a/li").click()
        avatar = self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[1]/div/div[1]/label/input')
        avatar.send_keys(self.location_to_avatar)

    def fill_name(self, name):
        self.app.driver.find_element_by_xpath("//input[@type='']").clear()
        self.app.driver.find_element_by_xpath("//input[@type='']").send_keys(name)

    def fill_last_name(self, last_name):
        self.app.driver.find_element_by_xpath("(//input[@type=''])[2]").clear()
        self.app.driver.find_element_by_xpath("(//input[@type=''])[2]").send_keys(last_name)

    def choose_city(self, city):
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/input').clear()
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/input').send_keys(city)

    def fill_address(self, address):
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/input').clear()
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/input').send_keys(address)

    def choose_country(self):
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div').click()
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div/ul/li[236]').click()

    def choose_page_language(self):
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div[3]/div').click()
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div[3]/div/div/ul/li[2]').click()

    def fill_birth_date(self):
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div/div[1]').click()
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div/div[1]/div/ul/li[15]').click()
        # month
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div/div[2]').click()
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div/div[2]/div/ul/li[13]').click()
        # year
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div/div[3]').click()
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div/div[3]/div/ul/li[37]').click()

    def upload_documents(self):
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/ul/li[1]/ul/a[2]').click()
        self.app.driver.find_element_by_class_name('number-document').send_keys(self.number_doc)
        # passport
        doc1 = self.app.driver.find_element_by_id("passport")
        doc1.send_keys(self.location_to_avatar)
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div[3]/div[6]/div[2]/a').click()
        # address
        doc2 = self.app.driver.find_element_by_id('registration')
        actions = ActionChains(self.app.driver)
        actions.move_to_element(doc2).perform()
        doc2.send_keys(self.doc_address)
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div[4]/div[5]/div[2]/a').click()
