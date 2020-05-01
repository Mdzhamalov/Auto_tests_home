

class PageHelper:

    def __init__(self, app):
        self.app = app

    def open_sign_up(self):
        self.app.driver.get("https://4dev.at-profit.com/signup")

    def open_sign_in(self):
        self.app.driver.get("https://4dev.at-profit.com/signin")

    def open_deposit(self):
        self.app.driver.get("https://4dev.backend.at-profit.com/admin/bank/depositinvoice/")

    def open_contracts(self):
        self.app.driver.get("https://4dev.at-profit.com/profile/contracts")

    def open_credit_card_generator(self):
        self.app.driver.get("https://www.prepostseo.com/tool/ru/credit-card-generator")

    def open_balance(self):
        self.app.driver.get("https://4dev.at-profit.com/profile/balance")

    def open_tickets_page(self):
        self.app.driver.get("https://4dev.at-profit.com/profile/support-history")
