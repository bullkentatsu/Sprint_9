from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGOUT_LINK = (By.XPATH, "//a[normalize-space()='Выход']")
    CREATE_RECIPE_LINK = (By.CSS_SELECTOR, "a[href='/recipes/create']")