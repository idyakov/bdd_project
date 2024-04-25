class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.find_element(*locator).send_keys(text)


class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.default_pw = 'Password'


class HomePage(Page):
    def verify_home_page_url(self):
        print('Verification')

    def verify_user_name(self, name):
        print('name:', name)


