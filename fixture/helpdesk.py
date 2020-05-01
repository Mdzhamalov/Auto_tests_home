import time


class HelpDesk:

    def __init__(self, app):
        self.app = app

    def new_account_ticket(self):
        self.app.driver.implicitly_wait(3)
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[1]/ul/li[2]/a/div/span').click()
        self.app.driver.implicitly_wait(3)
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/form/div[1]/div[2]/label[3]/span[2]').click()

    def new_customer_ticket(self):
        self.app.driver.implicitly_wait(3)
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[1]/ul/li[2]/a/div/span').click()
        self.app.driver.implicitly_wait(3)
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/form/div[1]/div[2]/label[2]/span[2]').click()

    def new_technical_ticket(self):
        self.app.driver.implicitly_wait(3)
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[1]/ul/li[2]/a/div/span').click()
        self.app.driver.implicitly_wait(3)
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/form/div[1]/div[2]/label[1]/span[2]').click()

    def create_ticket(self, topic, message):
        self.app.driver.find_element_by_css_selector("[placeholder = 'Введите тему сообщения']").send_keys(topic)
        self.app.driver.find_element_by_css_selector("[placeholder = 'Текст сообщения']").send_keys(message)
        self.app.driver.find_element_by_class_name('send-message-icon').click()

    def choose_ticket_to_archive(self):
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[1]').click()
        self.app.driver.implicitly_wait(2)
        self.app.driver.find_element_by_css_selector('a.button-component.support-button').click()

    def rate_ticket(self, sometext):
        self.app.driver.implicitly_wait(2)
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/span[4]').click()
        self.app.driver.find_element_by_css_selector('[placeholder = "Текст сообщения"]').send_keys(sometext)
        self.app.driver.find_element_by_css_selector('a.button-component.review_button').click()
        time.sleep(2)

    def get_tickets_list(self):
        self.app.driver.implicitly_wait(5)
        tickets = []
        for element in self.app.driver.find_element_by_css_selector("div.td-component support-td col-number circle"):
            text = element.text
            tickets.append(text)
        return tickets