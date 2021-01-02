import pytest
from fixture.application import Application

fixture = None

@pytest.fixture  # (scope="session")
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()  # создание фикстуры
        fixture.session.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Application()  # создание фикстуры
            fixture.session.login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)  # teardown фикстуры
    return fixture
