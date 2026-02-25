import allure
import pytest

from utils.config import Config
from utils.test_data import generate_user, UserData
from utils.webdriver_factory import WebDriverFactory

from pages.signin_page import SigninPage
from pages.signup_page import SignupPage
from pages.main_page import MainPage
from pages.create_recipe_page import CreateRecipePage


@pytest.fixture(scope="session")
def cfg() -> Config:
    return Config()


@pytest.fixture
def driver(cfg: Config):
    driver = WebDriverFactory.get_driver(cfg)
    yield driver
    driver.quit()


@pytest.fixture
def signin_page(driver, cfg: Config) -> SigninPage:
    return SigninPage(driver, cfg)


@pytest.fixture
def signup_page(driver, cfg: Config) -> SignupPage:
    return SignupPage(driver, cfg)


@pytest.fixture
def main_page(driver, cfg: Config) -> MainPage:
    return MainPage(driver, cfg)


@pytest.fixture
def create_recipe_page(driver, cfg: Config) -> CreateRecipePage:
    return CreateRecipePage(driver, cfg)


@pytest.fixture
def registered_user(signin_page: SigninPage, signup_page: SignupPage) -> UserData:
    user = generate_user()

    signin_page.open_page()
    signin_page.click_create_account()

    assert signup_page.is_signup_form_visible()

    signup_page.fill_form(user)
    signup_page.submit()

    signin_page.wait_url_contains("/signin")
    assert signin_page.is_auth_form_visible()

    return user


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        drv = item.funcargs.get("driver")
        if drv:
            try:
                allure.attach(
                    drv.get_screenshot_as_png(),
                    name="failure_screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception:
                pass