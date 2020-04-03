import pytest
from fixture.application import Application


@pytest.fixture(scope = "session")  # Запуск тестов в одном окне браузера
def app(request):
    fixture = Application()  # Initialization. Создание фикстуры
    request.addfinalizer(fixture.destroy)  # Указали то, как фикстура должна быть разрушена
    return fixture
