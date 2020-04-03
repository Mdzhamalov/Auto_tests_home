

def test_create_new_user(app):  # В качастве параметра принимает фикстуру app
    app.page.open_sign_up()
    app.signup_to_bonus()
    app.find_invitor()
    app.add_money()
    app.session.logout()
    app.page.open_deposit()
    app.session.login_to_backend()
    app.move_request_to_process()
    app.approve_request()
