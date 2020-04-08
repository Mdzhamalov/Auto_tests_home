

def test_a_preliminary(app):
    app.page.open_contracts()
    app.session.login(user_login="test_1.19", password="Asdf1234%")
    app.contract.buy_preliminary()
    app.session.logout()


def test_b_standard(app):
    app.page.open_contracts()
    app.session.login(user_login="test_1.19", password="Asdf1234%")
    app.contract.buy_standard()
    app.session.logout()


def test_c_premium(app):
    app.page.open_contracts()
    app.session.login(user_login="test_1.19", password="Asdf1234%")
    app.contract.buy_preumium()
    app.session.logout()


def test_d_vip(app):
    app.page.open_contracts()
    app.session.login(user_login="test_1.19", password="Asdf1234%")
    app.contract.buy_premium()
    app.session.logout()