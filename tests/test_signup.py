import allure

from utils.test_data import generate_user


@allure.feature("Создание аккаунта")
class TestSignup:
    @allure.title("Регистрация: переход на авторизацию и отображение формы входа")
    def test_user_can_signup_redirects_to_signin_and_shows_form(self, signin_page, signup_page):
        user = generate_user()

        signin_page.open_page()
        signin_page.click_create_account()

        assert signup_page.is_signup_form_visible()

        signup_page.fill_form(user)
        signup_page.submit()

        signin_page.wait_url_contains("/signin")
        assert signin_page.is_auth_form_visible()