

class TableHelper:

    def __init__(self, app):
        self.app = app

    def place_in_finish(self):
        # Открыть страницу Маркетинг
        self.app.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[1]/ul/li[2]/ul/a[2]').click()
        self.app.driver.implicitly_wait(5)
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div/ul[1]/li[1]/div/div/div[1]/button').click()
        self.app.driver.implicitly_wait(5)
        self.app.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div[2]/a').click()
