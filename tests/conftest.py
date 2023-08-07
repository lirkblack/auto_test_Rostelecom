import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



from pages.elements import AuthElement, AuthTab, ErrorMessage, AuthTabActive
from pages.account_page import AccountPage
from pages.register_page import RegisterPage
from pages.recovery_pass_page import RecoveryPassPage


@pytest.fixture(scope='session')
def browser():
    options = Options()
    options.binary_location = '.chromedriver.exe'
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def auth_elements(browser):
    auth_elements = AuthElement(browser)
    return auth_elements


@pytest.fixture(scope="session")
def auth_tab(browser):
    auth_tab = AuthTab(browser)
    return auth_tab


@pytest.fixture(scope="session")
def button_exit(browser):
    button_exit = AccountPage(browser)
    return button_exit


@pytest.fixture(scope="session")
def error_message(browser):
    error_message = ErrorMessage(browser)
    return error_message


@pytest.fixture(scope="session")
def register_page(browser):
    section_title = RegisterPage(browser)
    return section_title


@pytest.fixture(scope="session")
def recovery_pass_page(browser):
    section_title_pass = RecoveryPassPage(browser)
    return section_title_pass


@pytest.fixture(scope="session")
def auth_tab_active(browser):
    auth_tab_active = AuthTabActive(browser)
    return auth_tab_active