from selenium.webdriver.common.by import By


class LoginPage:

    email_xpath = "//input[@data-qa='login-email']"

    password_xpath = "//input[@placeholder='Password']"

    login_button_xpath = "//button[@data-qa='login-button']"

    logout_xpath = "//a[contains(text(),'Logout')]"

    def __init__(self, driver):

        self.driver = driver

    def enter_email(self, email):

        self.driver.find_element(By.XPATH, self.email_xpath).clear()

        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

    def enter_password(self, password):

        self.driver.find_element(By.XPATH, self.password_xpath).clear()

        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def click_login(self):

        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def login_successful(self):

        try:

            return self.driver.find_element(
                By.XPATH,
                self.logout_xpath
            ).is_displayed()

        except:

            return False