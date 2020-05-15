import pytest
from fixture.application import Application


# pytest.fixture - декоратор, указывающий, что ф-ция ниже является фикстурой
@pytest.fixture(scope="session")
def app(request):
    fixture = Application()  # Initialization. Создание фикстуры
    request.addfinalizer(fixture.destroy)  # Указали то, как фикстура должна быть разрушена
    return fixture
