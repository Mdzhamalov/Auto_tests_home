

def test_new_user_with_docs(app):
    app.page.open_sign_up()
    app.session.signup_to_bonus(rlogin="test_1.22", remail="test@ssss.ru", rpassword="Asdf1234%", rrepeat="Asdf1234%")
    app.find_invitor(parent="test_1")
    app.session.logout()
    app.page.open_sign_in()
    app.session.login(user_login="test_1.22", password="Asdf1234%")
    app.personal_info.upload_avatar()
    app.personal_info.fill_name(name="Patrick")
    app.personal_info.fill_last_name(last_name="Bryant")
    app.personal_info.choose_city(city="Los Angeles")
    app.personal_info.fill_address(address="2086  East Avenue")
    app.personal_info.choose_country()
    app.personal_info.choose_page_language()
    app.personal_info.fill_birth_date()
    app.personal_info.upload_documents()
    app.session.logout()
