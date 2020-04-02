

class PageHelper:

    def __init__(self, app):
        self.app = app

    def open_sign_up(self):
        self.app.driver.get("https://4dev.at-profit.com/signup")

    def open_deposit(self):
        self.app.driver.get("https://4dev.backend.at-profit.com/admin/bank/depositinvoice/")

    def open_contracts(self):
        self.app.driver.get("https://4dev.at-profit.com/profile/contracts")
