from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AccountPage(BasePage):
    LOCATOR_ACCOUNT_BUTTON_EXIT = (By.ID, "logout-btn")

    def check_button_exit(self):
        return self.find_element(self.LOCATOR_ACCOUNT_BUTTON_EXIT).text
