

def test_money_transfer(app):
    app.page.open_balance()
    app.session.login(user_login="test_0", password="Asdf1234%")
    app.wallet.click_transfer()
    app.wallet.transfer_money_to_user(value="9", receiver="test_0.1.1")
    app.page.open_confirmation_key_in_new_tab()
    app.session.login_to_backend(admin_login="Adminadmin", admin_password="5GxS4PA76vBdL4cE")
    app.wallet.find_key_and_confirm_operation()
