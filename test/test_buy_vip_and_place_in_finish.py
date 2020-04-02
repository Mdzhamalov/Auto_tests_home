import pytest
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()  # Initialization. Создание фикстуры
    request.addfinalizer(fixture.destroy)  # Указали то, как фикстура должна быть разрушена
    return fixture


def test_vip_and_finish(app):
    app.page.open_contracts()
    app.session.login()
    app.contract.buy_vip()
    app.table.place_in_finish()
    app.session.logout()



