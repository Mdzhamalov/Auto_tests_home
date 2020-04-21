

def test_add_credit_card(app):
    app.page.open_credit_card_generator()
    app.wallet.generate_valid_card_number()
    app.page.open_balance()
    app.session.login(user_login="test_0.30", password="Asdf1234%")
    app.wallet.attach_card()
    app.wallet.input_number_and_name(card_holder="JULIA MCKINNEY")
    app.session.logout()


def test_add_credit_card_2(app):
    app.page.open_credit_card_generator()
    app.wallet.generate_valid_card_number()
    app.page.open_balance()
    app.session.login(user_login="test_0.31", password="Asdf1234%")
    app.wallet.attach_card()
    app.wallet.input_number_and_name(card_holder="ROBERT MCKINNEY")
    app.session.logout()