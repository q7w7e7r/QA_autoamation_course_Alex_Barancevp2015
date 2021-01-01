from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Test_add_group():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
      self.driver.quit()

    def test_add_group(self):
        self.driver.get("http://localhost/addressbook/")
        # self.driver.set_window_size(1536, 824)
        self.driver.find_element(By.NAME, "user").click()
        self.driver.find_element(By.NAME, "user").send_keys("admin")
        self.driver.find_element(By.NAME, "pass").send_keys("secret")
        self.driver.find_element(By.NAME, "pass").send_keys(Keys.ENTER)
        self.driver.find_element(By.LINK_TEXT, "groups").click()
        self.driver.find_element(By.NAME, "new").click()
        self.driver.find_element(By.NAME, "group_name").click()
        self.driver.find_element(By.NAME, "group_name").send_keys("1qaz")
        self.driver.find_element(By.NAME, "group_header").click()
        self.driver.find_element(By.CSS_SELECTOR, "form:nth-child(2)").click()
        self.driver.find_element(By.NAME, "group_header").send_keys("2wsx")
        self.driver.find_element(By.NAME, "group_footer").click()
        self.driver.find_element(By.NAME, "group_footer").send_keys("3edc")
        self.driver.find_element(By.NAME, "submit").click()
        self.driver.find_element(By.LINK_TEXT, "group page").click()
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
