from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from group import Group


class Test_add_group():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_add_group(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_group_page()
        self.create_group(Group(name="1qaz", header="2wsx", footer="3edc"))
        self.return_to_group_page()
        self.logout()

    def test_empty_group(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_group_page()
        self.create_group(Group(name="", header="", footer=""))
        self.return_to_group_page()
        self.logout()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def open_group_page(self):
        self.driver.find_element(By.LINK_TEXT, "groups").click()

    def login(self, username, password):
            self.driver.find_element(By.NAME, "user").click()
            self.driver.find_element(By.NAME, "user").send_keys(username)
            self.driver.find_element(By.NAME, "pass").send_keys(password)
            self.driver.find_element(By.NAME, "pass").send_keys(Keys.ENTER)

    def return_to_group_page(self):
        self.driver.find_element(By.LINK_TEXT, "group page").click()

    def create_group(self, group):
        # init group creation
        self.driver.find_element(By.NAME, "new").click()
        # fill group form
        self.driver.find_element(By.NAME, "group_name").click()
        self.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.driver.find_element(By.NAME, "group_header").click()
        self.driver.find_element(By.CSS_SELECTOR, "form:nth-child(2)").click()
        self.driver.find_element(By.NAME, "group_header").send_keys(group.header)
        self.driver.find_element(By.NAME, "group_footer").click()
        self.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        self.driver.find_element(By.NAME, "submit").click()

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

