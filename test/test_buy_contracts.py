

def test_a_buy_preliminary_contract(app):
    app.page.open_contracts()
    app.session.login()
    app.contract.buy_preliminary()
    app.session.logout()


def test_b_buy_standard_contract(app):
    app.page.open_contracts()
    app.session.login()
    app.contract.buy_standard()
    app.session.logout()


def test_c_buy_premium_contract(app):
    app.page.open_contracts()
    app.session.login()
    app.contract.buy_premium()
    app.session.logout()


def test_d_buy_vip_contract(app):
    app.page.open_contracts()
    app.session.login()
    app.contract.buy_premium()
    app.session.logout()