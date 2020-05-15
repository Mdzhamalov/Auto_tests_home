from random import randrange


def test_add_credit_card(app):
    app.page.open_credit_card_generator()
    app.wallet.generate_valid_card_number()
    app.page.open_balance()
    app.session.login(user_login="test_0", password="Asdf1234%")
    app.wallet.linked_cards()
    app.wallet.attach_card()
    app.wallet.input_number_and_name(card_holder="JULIA MCKINNEY")
    app.session.logout()


def test_del_credit_card(app):
    app.page.open_balance()
    app.session.login(user_login="test_0", password="Asdf1234%")
    app.wallet.linked_cards()
    old_list = app.driver.find_elements_by_css_selector("span.delete.ml-auto")
    index = randrange(len(old_list))
    app.wallet.choose_random_card_to_del(index)
    new_list = app.driver.find_elements_by_css_selector("span.delete.ml-auto")
    assert len(old_list) - 1 == len(new_list)
    app.session.logout()

