

class ContractHelper:

    def __init__(self, app):
        self.app = app

    def buy_vip(self):
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div[4]/div[2]/button').click()
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[2]/a').click()
