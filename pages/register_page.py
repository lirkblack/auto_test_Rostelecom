from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegisterPage(BasePage):
    LOCATOR_SECTION_TITLE = (By.XPATH, "//h1[contains(text(),'Регистрация')]")

    def check_section_title(self):
        return self.find_element(self.LOCATOR_SECTION_TITLE).text