import allure


@allure.feature("Авторизация")
class TestSignin:
    @allure.title("Авторизация: переход на главную страницу и отображение кнопки 'Выход'")
    def test_user_can_signin_redirects_to_main_and_shows_logout(
        self,
        signin_page,
        main_page,
        registered_user
    ):
        signin_page.open_page()
        assert signin_page.is_auth_form_visible()

        signin_page.login(login_value=registered_user.username, password=registered_user.password)

        assert main_page.is_opened()