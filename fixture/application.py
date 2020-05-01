from selenium import webdriver
import time

from fixture.session import SessionHelper
from fixture.contract import ContractHelper
from fixture.table import TableHelper
from fixture.page import PageHelper
from fixture.personal_info import PersonalInformationHelper
from fixture.wallet import WalletHelper
from fixture.store import StoreHelper
from fixture.helpdesk import HelpDesk


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()  # Инициализация драйвера
        self.driver.maximize_window()
        # Инициализация помошников
        self.session = SessionHelper(self)
        self.contract = ContractHelper(self)
        self.table = TableHelper(self)
        self.page = PageHelper(self)
        self.personal_info = PersonalInformationHelper(self)
        self.wallet = WalletHelper(self)
        self.store = StoreHelper(self)
        self.helpdesk = HelpDesk(self)

    def find_invitor(self, parent):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/main/div[1]/div/div/div[2]/div[3]/input').send_keys(parent)
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/main/div[1]/div/div/div[2]/div[3]/ul/li[1]').click()
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div/div[2]/div[2]/main/div[1]/div/div/div[2]/a').click()

    def destroy(self):
        self.driver.quit()
