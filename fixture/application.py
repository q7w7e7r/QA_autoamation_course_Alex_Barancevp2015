from selenium import webdriver
from selenium.webdriver.common.by import By
from  fixture.session import SessionHelper


# Fixture
class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.vars = {}
        self.session = SessionHelper(self)

    def destroy(self):
        self.wd.quit()

    def open_group_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def return_to_group_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

    def create_group(self, group):
        wd = self.wd
        self.open_group_page()
        # init group creation
        wd.find_element(By.NAME, "new").click()
        # fill group form
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.CSS_SELECTOR, "form:nth-child(2)").click()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_group_page()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
