import allure

from pages.base_page import BasePage
from locators.signup_page_locators import SignupPageLocators
from utils.config import Config
from utils.test_data import UserData


class SignupPage(BasePage):
    def __init__(self, driver, cfg: Config):
        super().__init__(driver=driver, cfg=cfg)

    def is_signup_form_visible(self) -> bool:
        with allure.step("Проверить, что отображается форма регистрации"):
            return (
                self.is_visible(SignupPageLocators.EMAIL_INPUT)
                and self.is_visible(SignupPageLocators.PASSWORD_INPUT)
                and self.is_visible(SignupPageLocators.SUBMIT_BUTTON)
            )

    def fill_form(self, user: UserData) -> None:
        with allure.step("Заполнить форму регистрации"):
            self.type(SignupPageLocators.FIRST_NAME_INPUT, user.first_name)
            self.type(SignupPageLocators.LAST_NAME_INPUT, user.last_name)
            self.type(SignupPageLocators.USERNAME_INPUT, user.username)
            self.type(SignupPageLocators.EMAIL_INPUT, user.email)
            self.type(SignupPageLocators.PASSWORD_INPUT, user.password)

    def submit(self) -> None:
        with allure.step("Нажать 'Создать аккаунт' (после активации кнопки)"):
            self.wait_until_enabled(SignupPageLocators.SUBMIT_BUTTON)

            try:
                self.click(SignupPageLocators.SUBMIT_BUTTON)
            except Exception:
                self.js_click(SignupPageLocators.SUBMIT_BUTTON)