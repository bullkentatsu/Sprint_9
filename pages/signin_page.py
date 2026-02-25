import allure
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage
from locators.signin_page_locators import SigninPageLocators
from utils.config import Config


class SigninPage(BasePage):
    def __init__(self, driver, cfg: Config):
        super().__init__(driver=driver, cfg=cfg)

    def open_page(self) -> None:
        with allure.step("Открыть страницу авторизации"):
            super().open(self.cfg.base_url + "/signin")

    def is_auth_form_visible(self) -> bool:
        with allure.step("Проверить, что отображается форма авторизации"):
            return self.is_visible(SigninPageLocators.TITLE) and self.is_visible(SigninPageLocators.FORM)

    def click_create_account(self) -> None:
        with allure.step("Нажать 'Создать аккаунт'"):
            self.click(SigninPageLocators.CREATE_ACCOUNT_LINK)

    def login(self, login_value: str, password: str) -> None:
        with allure.step("Авторизоваться"):
            self.type(SigninPageLocators.EMAIL_INPUT, login_value)
            self.type(SigninPageLocators.PASSWORD_INPUT, password)

            self.wait_until_enabled(SigninPageLocators.SUBMIT_BUTTON)

            try:
                self.click(SigninPageLocators.SUBMIT_BUTTON)
            except Exception:
                self.js_click(SigninPageLocators.SUBMIT_BUTTON)

            self.accept_alert_if_present()

            try:
                self.wait_url_contains("/recipes")
            except TimeoutException:
                self.accept_alert_if_present()
                raise