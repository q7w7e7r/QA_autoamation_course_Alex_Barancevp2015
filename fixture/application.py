from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper
from fixture.group import GroupHelper


# Fixture
class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        # Неявное ожидание указывает WebDriver опрашивать DOM в течение определенного периода времени при попытке найти
        # любой элемент (или элементы), который не доступен сразу. Значение по умолчанию-0 (ноль).
        # После установки неявное ожидание устанавливается на весь срок службы объекта WebDriver.
        self.wd.implicitly_wait(5)
        self.vars = {}
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
