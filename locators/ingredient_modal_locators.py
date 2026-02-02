from selenium.webdriver.common.by import By


class IngredientModalLocators:
    INGREDIENT_CARD = (By.XPATH, "//div[contains(@class,'BurgerIngredient_ingredient')]")

    MODAL_WINDOW = (By.XPATH, "//section[contains(@class,'Modal_modal')]")

    CLOSE_BUTTON = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal')]//button"
    )
