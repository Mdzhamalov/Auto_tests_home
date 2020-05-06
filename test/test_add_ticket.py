from random import randrange


def test_add_account_ticket(app):
    app.page.open_tickets_page()
    app.session.login(user_login="test_0", password="Asdf1234%")
    old_tickets = app.driver.find_elements_by_css_selector("div.tr-component.support-tr")
    app.helpdesk.new_account_ticket()
    app.helpdesk.create_ticket(topic="Issue with wallet 7", message="Can't return my money")
    app.page.open_tickets_page()
    new_tickets = app.driver.find_elements_by_css_selector("div.tr-component.support-tr")
    assert len(old_tickets) + 1 == len(new_tickets)
    app.session.logout()


def test_add_customer_ticket_with_file(app):
    app.page.open_tickets_page()
    app.session.login(user_login="test_0", password="Asdf1234%")
    old_tickets = app.driver.find_elements_by_css_selector("div.tr-component.support-tr")
    app.helpdesk.new_customer_ticket()
    app.helpdesk.attach_file(location_to_file="F:/Cactus_Vision/AT_Golden/User_photos/test_6.jpg")
    app.helpdesk.create_ticket(topic="Issue with parent 3", message="Can't define my parent in bonus program")
    app.page.open_tickets_page()
    new_tickets = app.driver.find_elements_by_css_selector("div.tr-component.support-tr")
    assert len(old_tickets) + 1 == len(new_tickets)
    app.session.logout()


def test_add_technical_ticket(app):
    app.page.open_tickets_page()
    app.session.login(user_login="test_0.1.1", password="Asdf1234%")
    old_tickets = app.driver.find_elements_by_css_selector("div.tr-component.support-tr")
    app.helpdesk.new_technical_ticket()
    app.helpdesk.create_ticket(topic="Problems with training", message="The link isn't correct in step 1")
    app.page.open_tickets_page()
    new_tickets = app.driver.find_elements_by_css_selector("div.tr-component.support-tr")
    assert len(old_tickets) + 1 == len(new_tickets)
    print("Old tickets: " + str(len(old_tickets)), "and new tickets: " + str(len(new_tickets)))
    app.session.logout()


def test_ticket_to_archive_by_index(app):
    app.page.open_tickets_page()
    app.session.login(user_login="test_0", password="Asdf1234%")
    old_tickets = app.driver.find_elements_by_css_selector("div.tr-component.support-tr")
    index = randrange(len(old_tickets))
    app.helpdesk.choose_ticket_to_archive_by_index(index)
    app.helpdesk.rate_ticket(sometext="Some test message")
    new_tickets = app.driver.find_elements_by_css_selector("div.tr-component.support-tr")
    assert len(old_tickets) - 1 == len(new_tickets)
    app.session.logout()

# Negative


def test_add_ticket_with_empty_message(app):
    app.page.open_tickets_page()
    app.session.login(user_login="test_0", password="Asdf1234%")
    old_tickets = app.driver.find_elements_by_css_selector("div.tr-component.support-tr")
    app.helpdesk.new_account_ticket()
    app.helpdesk.create_ticket(topic="Problems with replenishment 9", message="")
    app.page.open_tickets_page()
    new_tickets = app.driver.find_elements_by_css_selector("div.tr-component.support-tr")
    assert len(old_tickets) + 1 == len(new_tickets)
    app.session.logout()


def test_add_ticket_with_empty_topic(app):
    app.page.open_tickets_page()
    app.session.login(user_login="test_0.1", password="Asdf1234%")
    old_tickets = app.driver.find_elements_by_css_selector("div.tr-component.support-tr")
    app.helpdesk.new_account_ticket()
    app.helpdesk.create_ticket(topic="", message="Empty topic")
    app.page.open_tickets_page()
    new_tickets = app.driver.find_elements_by_css_selector("div.tr-component.support-tr")
    assert len(old_tickets) + 1 == len(new_tickets)
    app.session.logout()
