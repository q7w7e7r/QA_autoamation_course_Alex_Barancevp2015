import pytest
import json
from fixture.application import *
import os.path

fixture = None
target = None

@pytest.fixture  # (scope="session")
def app(request):
    global fixture
    global target
    browser = request.config.getoption('--browser')
    if target is None:
        config_file =  os.path.join(os.path.dirname(os.path.abspath(__file__)),request.config.getoption('--target'))
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or fixture.is_valid():
        fixture = Application(browser=browser,base_url=target['baseUrl'])  # создание фикстуры
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)  # teardown фикстуры
    return fixture

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome' )
    parser.addoption('--target', action='store', default='target.json')