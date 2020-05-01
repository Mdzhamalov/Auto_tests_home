

def test_buy_1g_for_bonus(app):
    app.page.open_sign_in()
    app.session.login(user_login="test_0", password="Asdf1234%")
    app.store.go_to_catalog()
    app.store.add_1g_to_basket()
    app.store.navigate_to_basket()
    app.store.choose_contract()
    app.store.pay_for_bonus()
    app.session.logout()
