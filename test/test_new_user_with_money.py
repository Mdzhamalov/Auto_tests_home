

def test_create_new_user(app):  # В качастве параметра принимает фикстуру app
    app.page.open_sign_up()
    app.session.signup_to_bonus(rlogin="test_1.28", remail="test@ssss.ru", rpassword="Asdf1234%", rrepeat="Asdf1234%")
    app.find_invitor(parent="test_1")
    app.add_money(value="9000000")
    app.session.logout()
    app.page.open_deposit()
    app.session.login_to_backend(admin_login="Adminadmin", admin_password="5GxS4PA76vBdL4cE")
    app.move_request_to_process()
    app.approve_request()
    app.session.logout_from_backend()


def test_create_new_user_2(app):
    app.page.open_sign_up()
    app.session.signup_to_bonus(rlogin="test_1.29", remail="test@ssss.ru", rpassword="Asdf1234%", rrepeat="Asdf1234%")
    app.find_invitor(parent="test_1")
    app.add_money(value="5000000")
    app.session.logout()
    app.page.open_deposit()
    app.session.login_to_backend(admin_login="Adminadmin", admin_password="5GxS4PA76vBdL4cE")
    app.move_request_to_process()
    app.approve_request()
    app.session.logout_from_backend()
