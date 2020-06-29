

def test_money_transfer(app):
    app.page.open_balance()
    app.session.login(user_login="test_0", password="Asdf1234%")
    balance_before = app.driver.find_element_by_css_selector("p.value.hover").text
    app.wallet.click_transfer()
    app.wallet.transfer_money_to_user(value="10", receiver="test_0.1.1")
    app.page.open_confirmation_key_in_new_tab()
    app.session.login_to_backend(admin_login="Adminadmin", admin_password="5GxS4PA76vBdL4cE")
    app.wallet.find_key_and_confirm_operation()
    balance_after = app.driver.find_element_by_css_selector("p.value.hover").text
    print(balance_before, balance_after)
    assert int(balance_before) - 10 == int(balance_after)

