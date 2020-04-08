

def test_preliminary(app):
    app.page.open_contracts()
    app.session.login(user_login="test_1.26", password="Asdf1234%")
    app.contract.buy_preliminary()
    app.table.place_in_preliminary()
    app.session.logout()


def test_standard_and_start(app):
    app.page.open_contracts()
    app.session.login(user_login="test_1.27", password="Asdf1234%")
    app.contract.buy_standard()
    app.table.place_in_start()
    app.session.logout()


def test_premium_and_gold(app):
    app.page.open_contracts()
    app.session.login(user_login="test_1.28", password="Asdf1234%")
    app.contract.buy_premium()
    app.table.place_in_gold()
    app.session.logout()


def test_vip_and_finish(app):
    app.page.open_contracts()
    app.session.login(password="test_1.29", user_login="Asdf1234%")
    app.contract.buy_vip()
    app.table.place_in_finish()
    app.session.logout()
