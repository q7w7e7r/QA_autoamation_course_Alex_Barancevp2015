from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper
from fixture.group import GroupHelper


# Fixture
class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.vars = {}
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def destroy(self):
        self.wd.quit()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
