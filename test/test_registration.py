import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import random
import HtmlTestRunner
import time

driver = webdriver.Chrome()


class TestRegistration(unittest.TestCase):
    rlogin = "test_0.1.5"
    remail = "test@ssss.ru"
    rpassword = "Asdf1234%"
    rrepeat = "Asdf1234%"
    parent = "test_0.1"
    login = rlogin
    password = rpassword
    location_to_avatar = "F:/Cactus_Vision/AT_Golden/User_photos/test_6.jpg"
    doc_address = "F:/Cactus_Vision/AT_Golden/User_photos/London.jpg"
    name = "Patrick"
    last_name = "Bryant"
    city = "Los Angeles"
    address = "2086  East Avenue"
    number_doc = random.randint(1, 1000)

    def setUp(self):
        driver.get("https://4dev.at-profit.com/signup")
        self.registration()
        self.find_invitor()
        self.logout()

    def registration(self):
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[1]').send_keys(self.rlogin)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[2]').send_keys(self.remail)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[3]').send_keys(self.rpassword)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[4]').send_keys(self.rrepeat)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/button').click()

    def find_invitor(self):
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/main/div[1]/div/div/div[2]/div[3]/input').send_keys(self.parent)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/main/div[1]/div/div/div[2]/div[3]/ul/li[1]').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/main/div[1]/div/div/div[2]/a').click()

    def logout(self):
        driver.implicitly_wait(2)
        driver.find_element_by_class_name('pointer').click()

    def test_login(self):
        driver.get("https://4dev.at-profit.com/signin")
        self.sign_in()
        self.upload_avatar()
        self.fill_name()
        self.fill_last_name()
        self.choose_city()
        self.fill_address()
        self.choose_country()
        self.choose_page_language()
        self.fill_birth_date()
        self.upload_documents()

    def sign_in(self):
        driver.maximize_window()
        driver.implicitly_wait(2)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[1]').send_keys(self.login)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/input[2]').send_keys(self.password)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div/form/button').click()

    def upload_avatar(self):
        driver.find_element_by_xpath("//div[@id='app']/div/div/div/div[2]/div/ul/li/ul/a/li").click()
        avatar = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[1]/div/div[1]/label/input')
        avatar.send_keys(self.location_to_avatar)

    def fill_name(self):
        driver.find_element_by_xpath("//input[@type='']").clear()
        driver.find_element_by_xpath("//input[@type='']").send_keys(self.name)

    def fill_last_name(self):
        driver.find_element_by_xpath("(//input[@type=''])[2]").clear()
        driver.find_element_by_xpath("(//input[@type=''])[2]").send_keys(self.last_name)

    def choose_city(self):
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/input').clear()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/input').send_keys(self.city)

    def fill_address(self):
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/input').clear()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/input').send_keys(self.address)

    def choose_country(self):
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div/ul/li[236]').click()

    def choose_page_language(self):
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div[3]/div').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/div[3]/div/div/ul/li[2]').click()

    def fill_birth_date(self):
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div/div[1]').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div/div[1]/div/ul/li[15]').click()
        # month
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div/div[2]').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div/div[2]/div/ul/li[13]').click()
        # year
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div/div[3]').click()
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div/div[3]/div/ul/li[37]').click()

    def upload_documents(self):
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/ul/li[1]/ul/a[2]').click()
        driver.find_element_by_class_name('number-document').send_keys(self.number_doc)
        # passport
        doc1 = driver.find_element_by_id("passport")
        doc1.send_keys(self.location_to_avatar)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div[3]/div[6]/div[2]/a').click()
        # address
        doc2 = driver.find_element_by_id('registration')
        actions = ActionChains(driver)
        actions.move_to_element(doc2).perform()
        doc2.send_keys(self.doc_address)
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div[4]/div[5]/div[2]/a').click()
        time.sleep(1)
        p_status = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div[3]/div[5]/span').text
        a_status = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div[4]/div[4]/span').text
        self.assertEqual(p_status, "Check in progress", "Scan of the passport didn't upload")
        self.assertEqual(a_status, "Check in progress", "Scan of the address didn't upload")

    def tearDown(self):
        self.logout()
        driver.close()


if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output = 'F:/Cactus_Vision/AT_Golden/Auto_tests/Reports'))
