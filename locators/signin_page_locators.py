from selenium.webdriver.common.by import By


class SigninPageLocators:
    TITLE = (By.XPATH, "//h1[normalize-space()='Войти на сайт']")

    FORM = (By.XPATH, "//form")

    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")

    SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")
    SIGNIN_LINK = (By.CSS_SELECTOR, "a[href='/signin']")
    CREATE_ACCOUNT_LINK = (By.CSS_SELECTOR, "a[href='/signup']")

    LOGOUT_LINK = (By.XPATH, "//a[normalize-space()='Выход']")