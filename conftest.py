import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()  # создание фикстуры
    request.addfinalizer(fixture.destroy)  # teardown фикстуры
    return fixture
