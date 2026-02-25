import allure

from pages.base_page import BasePage
from utils.config import Config
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver, cfg: Config):
        super().__init__(driver=driver, cfg=cfg)

    def is_logout_visible(self) -> bool:
        with allure.step("Проверить, что отображается кнопка/ссылка 'Выход'"):
            return self.is_visible(MainPageLocators.LOGOUT_LINK)

    def is_opened(self) -> bool:
        with allure.step("Проверить, что открыта главная страница /recipes"):
            return ("/recipes" in self.current_url()) and self.is_logout_visible()

    def go_to_create_recipe(self) -> None:
        with allure.step("Перейти на страницу 'Создать рецепт'"):
            self.click(MainPageLocators.CREATE_RECIPE_LINK)