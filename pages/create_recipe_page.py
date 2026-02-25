import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from utils.config import Config
from utils.test_data import RecipeData
from locators.create_recipe_page_locators import CreateRecipePageLocators


class CreateRecipePage(BasePage):
    def __init__(self, driver, cfg: Config):
        super().__init__(driver=driver, cfg=cfg)

    def is_opened(self) -> bool:
        with allure.step("Проверить, что открыта страница создания рецепта"):
            return "/recipes/create" in self.current_url() and self.is_visible(CreateRecipePageLocators.TITLE_INPUT)

    def _click_tag(self, locator, tag_name: str) -> None:
        with allure.step(f"Выбрать тег '{tag_name}'"):
            try:
                self.click(locator)
            except Exception:
                self.js_click(locator)

    def select_breakfast_tag(self) -> None:
        self._click_tag(CreateRecipePageLocators.TAG_BREAKFAST, "Завтрак")

    def set_title(self, title: str) -> None:
        self.type(CreateRecipePageLocators.TITLE_INPUT, title)

    def set_cooking_time(self, cooking_time: str) -> None:
        self.type(CreateRecipePageLocators.COOKING_TIME_INPUT, cooking_time)

    def add_ingredient_from_autocomplete(self, ingredient_prefix: str) -> None:
        with allure.step(f"Выбрать ингредиент из подсказок: {ingredient_prefix}"):
            self.type(CreateRecipePageLocators.INGREDIENT_NAME_INPUT, ingredient_prefix)
            prefix = ingredient_prefix.strip().lower()

            def _options(driver):
                candidates = driver.find_elements(By.XPATH, "//div[normalize-space()!='']")
                matched = []
                for el in candidates:
                    try:
                        if not el.is_displayed():
                            continue
                        txt = (el.text or "").strip()
                        if txt and txt.lower().startswith(prefix):
                            matched.append(el)
                    except Exception:
                        continue
                return matched if matched else False

            options = WebDriverWait(self.driver, self.cfg.wait_timeout).until(_options)

            try:
                options[0].click()
            except Exception:
                self.driver.execute_script("arguments[0].click();", options[0])

            self.wait_visible(CreateRecipePageLocators.INGREDIENT_AMOUNT_INPUT)

    def set_ingredient_amount(self, amount: str) -> None:
        with allure.step(f"Указать количество ингредиента: {amount}"):
            self.type(CreateRecipePageLocators.INGREDIENT_AMOUNT_INPUT, amount)

    def click_add_ingredient(self) -> None:
        with allure.step("Нажать 'Добавить ингредиент' (если доступно)"):
            try:
                self.scroll_into_view(CreateRecipePageLocators.ADD_INGREDIENT_LINK)
                self.click(CreateRecipePageLocators.ADD_INGREDIENT_LINK)
            except Exception:
                try:
                    self.js_click(CreateRecipePageLocators.ADD_INGREDIENT_LINK)
                except Exception:
                    pass

    def set_description(self, text: str) -> None:
        self.type(CreateRecipePageLocators.DESCRIPTION_TEXTAREA, text)

    def upload_image(self, filename: str) -> None:
        with allure.step("Загрузить фото"):
            self.scroll_into_view(CreateRecipePageLocators.FILE_INPUT)
            self.upload_file_from_assets(CreateRecipePageLocators.FILE_INPUT, filename)

            file_input = self.wait_present(CreateRecipePageLocators.FILE_INPUT)
            value = file_input.get_attribute("value") or ""
            assert value.strip() != ""

    def submit(self) -> None:
        with allure.step("Нажать 'Создать рецепт' и дождаться редиректа"):
            self.wait_until_enabled(CreateRecipePageLocators.SUBMIT_BUTTON)

            try:
                self.click(CreateRecipePageLocators.SUBMIT_BUTTON)
            except Exception:
                self.js_click(CreateRecipePageLocators.SUBMIT_BUTTON)

            def _redirected(driver):
                url = driver.current_url
                return ("/recipes/" in url) and ("/recipes/create" not in url)

            WebDriverWait(self.driver, self.cfg.wait_timeout).until(_redirected)

    def get_created_recipe_title(self) -> str:
        with allure.step("Получить название созданного рецепта из H1 на странице рецепта"):
            h1 = self.wait_visible((By.XPATH, "//h1[normalize-space()!='']"))
            return h1.text.strip()

    def is_recipe_created(self) -> bool:
        with allure.step("Проверить, что рецепт создан (мы не на /recipes/create и есть H1)"):
            try:
                url = self.current_url()
                if "/recipes/create" in url:
                    return False
                self.wait_visible((By.XPATH, "//h1[normalize-space()!='']"))
                return True
            except Exception:
                return False

    def create_recipe(self, data: RecipeData) -> None:
        with allure.step("Заполнить форму создания рецепта"):
            self.set_title(data.title)
            self.select_breakfast_tag()
            self.add_ingredient_from_autocomplete(data.ingredient)
            self.set_ingredient_amount(data.amount)
            self.click_add_ingredient()
            self.set_cooking_time(data.cooking_time)
            self.set_description("Описание для автотеста")
            self.upload_image(data.image_filename)