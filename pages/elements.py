from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AuthElement(BasePage):
    LOCATOR_USERNAME = (By.ID, "username")
    LOCATOR_PASSWORD = (By.ID, "password")
    LOCATOR_BUTTON_ENTER = (By.ID, "kc-login")
    LOCATOR_BUTTON_REGISTER = (By.ID, "kc-register")
    LOCATOR_BUTTON_FORGOT_PASS = (By.XPATH, "//a[@id='forgot_password']")

    def input_username(self):
        return self.find_element(self.LOCATOR_USERNAME)

    def input_password(self):
        return self.find_element(self.LOCATOR_PASSWORD)

    def click_button_to_enter(self):
        return self.find_element(self.LOCATOR_BUTTON_ENTER).click()

    def button_register(self):
        return self.find_element(self.LOCATOR_BUTTON_REGISTER)

    def button_forgot_pass(self):
        return self.find_element(self.LOCATOR_BUTTON_FORGOT_PASS)


class AuthTab(BasePage):
    LOCATOR_TAB_PHONE = (By.ID, "t-btn-tab-phone")
    LOCATOR_TAB_EMAIL = (By.ID, "t-btn-tab-mail")
    LOCATOR_TAB_LOGIN = (By.ID, "t-btn-tab-login")
    LOCATOR_TAB_LS = (By.ID, "t-btn-tab-ls")

    def click_tab_phone(self):
        return self.find_element(self.LOCATOR_TAB_PHONE).click()

    def click_tab_email(self):
        return self.find_element(self.LOCATOR_TAB_EMAIL).click()

    def click_tab_login(self):
        return self.find_element(self.LOCATOR_TAB_LOGIN).click()

    def click_tab_ls(self):
        return self.find_element(self.LOCATOR_TAB_LS).click()


class ErrorMessage(BasePage):
    LOCATOR_MESSAGE_USERNAME = (By.XPATH, "//span[contains(text(),'Введите номер телефона')]")
    LOCATOR_MESSAGE_LOGIN_AND_PASS = (By.XPATH, "//span[@id='form-error-message']")

    def error_message_username(self):
        return self.find_element(self.LOCATOR_MESSAGE_USERNAME).text

    def error_message_login_end_pass(self):
        return self.find_element(self.LOCATOR_MESSAGE_LOGIN_AND_PASS).text


class AuthTabActive(BasePage):
    LOCATOR_TAB_PHONE_ACTIVE = (By.XPATH, "//div[@id='t-btn-tab-phone'][@class='rt-tab rt-tab--small rt-tab--active']")
    LOCATOR_TAB_EMAIL_ACTIVE = (By.XPATH, "//div[@id='t-btn-tab-mail'][@class='rt-tab rt-tab--small rt-tab--active']")
    LOCATOR_TAB_LOGIN_ACTIVE = (By.XPATH, "//div[@id='t-btn-tab-login'][@class='rt-tab rt-tab--small rt-tab--active']")
    LOCATOR_TAB_LS_ACTIVE = (By.XPATH, "//div[@id='t-btn-tab-ls'][@class='rt-tab rt-tab--small rt-tab--active']")

    def check_tab_phone(self):
        return self.find_element(self.LOCATOR_TAB_PHONE_ACTIVE).text

    def check_tab_email(self):
        return self.find_element(self.LOCATOR_TAB_EMAIL_ACTIVE).text

    def check_tab_login(self):
        return self.find_element(self.LOCATOR_TAB_LOGIN_ACTIVE).text

    def check_tab_ls(self):
        return self.find_element(self.LOCATOR_TAB_LS_ACTIVE).text