from fixture.application import Application
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()  # Initialization. Создание фикстуры
    request.addfinalizer(fixture.destroy)  # Указали то, как фикстура должна быть разрушена
    return fixture


def test_create_new_user(app):  # В качастве параметра принимает фикстуру app
    app.signup_to_bonus()
    app.find_invitor()
    app.add_money()
    app.session.logout()
    app.open_deposit_page()
    app.session.login_to_backend()
    app.move_request_to_process()
    app.approve_request()
