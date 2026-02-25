import allure
from utils.test_data import DEFAULT_RECIPE


class TestCreateRecipe:
    @allure.title("Создание рецепта: отображается карточка и корректное название")
    def test_user_can_create_recipe_and_see_card_and_title(
        self,
        signin_page,
        main_page,
        create_recipe_page,
        registered_user
    ):
        signin_page.open_page()
        signin_page.login(login_value=registered_user.username, password=registered_user.password)

        assert main_page.is_opened()

        main_page.go_to_create_recipe()
        assert create_recipe_page.is_opened()

        create_recipe_page.create_recipe(DEFAULT_RECIPE)
        create_recipe_page.submit()

        assert create_recipe_page.is_recipe_created()

        actual_title = create_recipe_page.get_created_recipe_title()
        assert actual_title == DEFAULT_RECIPE.title