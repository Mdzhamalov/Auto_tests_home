

def test_create_new_user(app):  # В качастве параметра принимает фикстуру app
    app.page.open_sign_up()
    app.session.signup_to_bonus(rlogin="test_2", remail="test@ssss.ru", rpassword="Asdf1234%", rrepeat="Asdf1234%")
    app.find_invitor(parent="test_0")
    app.wallet.add_money(value="9000000")
    app.session.logout()
    app.page.open_deposit()
    app.session.login_to_backend(admin_login="Adminadmin", admin_password="5GxS4PA76vBdL4cE")
    app.wallet.move_request_to_process()
    app.wallet.approve_request()
    app.session.logout_from_backend()
