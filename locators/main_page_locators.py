from selenium.webdriver.common.by import By


class MainPageLocators:
    BUT_ENTER_ACC = (By.XPATH, "//button[text()='Войти в аккаунт']")
    BUT_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    LINK_CONSTRUCT = (By.XPATH, "//a[p[text()='Конструктор']]")
    LINK_ORDER_FEED = (By.XPATH, "//a[p[text()='Лента Заказов']]")
    BUN_KRATOR = (By.XPATH, "//a[p[text()='Краторная булка N-200i']]")
    COUNTER_BUN = (
        By.XPATH,
        "//p[text()='Краторная булка N-200i']"
        "/ancestor::a//p[contains(@class, 'counter_counter__num')]"
    )

    ANY_NON_BUN_CARD = (
        By.XPATH,
        "//section[.//h2[text()='Соусы'] or .//h2[text()='Начинки']]"
        "//a[contains(@class,'BurgerIngredient_ingredient__')]"
    )
    POS_TOP_BASKET = (By.XPATH, "//div[contains(@class, 'constructor-element_pos_top')]")
    MODAL_WINDOW = (By.XPATH, "//section[contains(@class,'Modal_modal')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")
    OVERLAY = (By.XPATH, "//div[contains(@class,'Modal_modal_overlay')]/parent::div")
    INGREDIENT_MODAL = (By.XPATH, "//section[contains(@class,'Modal_modal__')]")
    ORDER_SUCCESS_TEXT = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal')]//p[contains(.,'Ваш заказ начали готовить')]"
    )
    ORDER_NUMBER = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal')]//h2[contains(@class,'digits-large')]"
    )
