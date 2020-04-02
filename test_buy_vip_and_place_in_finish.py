import pytest
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()  # Initialization. Создание фикстуры
    request.addfinalizer(fixture.destroy)  # Указали то, как фикстура должна быть разрушена
    return fixture


def test_standard_and_start(app):
    app.login()
    app.buy_vip()
    app.place_in_finish()
    app.logout()



