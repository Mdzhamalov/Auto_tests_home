
def test_add_account_ticket(app):
    app.page.open_tickets_page()
    app.session.login(user_login="test_0", password="Asdf1234%")
    #  old_tickets = app.helpdesk.get_tickets_list()
    app.helpdesk.new_account_ticket()
    app.helpdesk.create_ticket(topic="Issue with wallet 6", message="Can't return my money")
    #  new_tickets = app.helpdesk.get_tickets_list()
    #  assert len(old_tickets) + 1 == len(new_tickets)
    app.session.logout()


def test_add_customer_ticket(app):
    app.page.open_tickets_page()
    app.session.login(user_login="test_0.1", password="Asdf1234%")
    app.helpdesk.new_customer_ticket()
    app.helpdesk.create_ticket(topic="Issue with parent", message="Can't define my parent in bonus program")
    app.session.logout()


def test_add_technical_ticket(app):
    app.page.open_tickets_page()
    app.session.login(user_login="test_0.1.1", password="Asdf1234%")
    app.helpdesk.new_technical_ticket()
    app.helpdesk.create_ticket(topic="Problems with training", message="The link isn't correct in step 1")
    app.session.logout()


def test_ticket_to_archive(app):
    app.page.open_tickets_page()
    app.session.login(user_login="test_0", password="Asdf1234%")
    app.helpdesk.choose_ticket_to_archive()
    app.helpdesk.rate_ticket(sometext="Some test message")
    app.session.logout()
