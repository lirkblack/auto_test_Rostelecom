from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RecoveryPassPage(BasePage):
    LOCATOR_SECTION_TITLE = (By.XPATH, "//h1[contains(text(),'Восстановление пароля')]")

    def check_section_title_pass(self):
        return self.find_element(self.LOCATOR_SECTION_TITLE).text
