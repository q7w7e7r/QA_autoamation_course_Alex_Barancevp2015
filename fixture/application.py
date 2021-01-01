from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Fixture
class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.vars = {}

    def destroy(self):
        self.wd.quit()

    def logout(self):
        wd = self.wd
        self.wd.find_element(By.LINK_TEXT, "Logout").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        self.wd.find_element(By.NAME, "user").click()
        self.wd.find_element(By.NAME, "user").send_keys(username)
        self.wd.find_element(By.NAME, "pass").send_keys(password)
        self.wd.find_element(By.NAME, "pass").send_keys(Keys.ENTER)

    def open_group_page(self):
        wd = self.wd
        self.wd.find_element(By.LINK_TEXT, "groups").click()

    def return_to_group_page(self):
        wd = self.wd
        self.wd.find_element(By.LINK_TEXT, "group page").click()

    def create_group(self, group):
        wd = self.wd
        self.open_group_page()
        # init group creation
        self.wd.find_element(By.NAME, "new").click()
        # fill group form
        self.wd.find_element(By.NAME, "group_name").click()
        self.wd.find_element(By.NAME, "group_name").send_keys(group.name)
        self.wd.find_element(By.NAME, "group_header").click()
        self.wd.find_element(By.CSS_SELECTOR, "form:nth-child(2)").click()
        self.wd.find_element(By.NAME, "group_header").send_keys(group.header)
        self.wd.find_element(By.NAME, "group_footer").click()
        self.wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        self.wd.find_element(By.NAME, "submit").click()
        self.return_to_group_page()

    def open_home_page(self):
        wd = self.wd
        self.wd.get("http://localhost/addressbook/")
