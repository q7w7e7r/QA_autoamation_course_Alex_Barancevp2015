import pytest
from fixture.application import *

fixture = None


@pytest.fixture  # (scope="session")
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()  # создание фикстуры

    else:
        if not fixture.is_valid():
            fixture = Application()  # создание фикстуры
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)  # teardown фикстуры
    return fixture
