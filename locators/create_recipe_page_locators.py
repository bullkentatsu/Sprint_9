from selenium.webdriver.common.by import By


class CreateRecipePageLocators:
    CREATE_RECIPE_LINK = (By.CSS_SELECTOR, "a[href='/recipes/create']")

    TITLE_INPUT = (
        By.XPATH,
        "//label[.//div[normalize-space()='Название рецепта']]//input",
    )

    TAG_BREAKFAST = (
        By.XPATH,
        "//*[normalize-space()='Завтрак']/ancestor::*[self::label or self::div][1]//button",
    )
    TAG_LUNCH = (
        By.XPATH,
        "//*[normalize-space()='Обед']/ancestor::*[self::label or self::div][1]//button",
    )
    TAG_DINNER = (
        By.XPATH,
        "//*[normalize-space()='Ужин']/ancestor::*[self::label or self::div][1]//button",
    )

    INGREDIENT_NAME_INPUT = (
        By.XPATH,
        "//label[.//div[normalize-space()='Ингредиенты']]//input",
    )

    INGREDIENT_AMOUNT_INPUT = (
        By.XPATH,
        "//label[.//div[normalize-space()='Ингредиенты']]//input/following::input[1]",
    )

    ADD_INGREDIENT_LINK = (By.XPATH, "//*[normalize-space()='Добавить ингредиент']")

    COOKING_TIME_INPUT = (
        By.XPATH,
        "//label[.//div[normalize-space()='Время приготовления']]//input",
    )

    DESCRIPTION_TEXTAREA = (
        By.XPATH,
        "//label[.//div[normalize-space()='Описание рецепта']]//textarea",
    )

    FILE_INPUT = (By.CSS_SELECTOR, "input[type='file']")
    SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space()='Создать рецепт']")

    CREATED_RECIPE_TITLE_H1 = (By.XPATH, "//h1[normalize-space()!='']")