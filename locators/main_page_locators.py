from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[normalize-space()='Конструктор']/ancestor::a[1]")
    FEED_BUTTON = (By.XPATH, "//a[contains(@href,'/feed') and .//p[contains(.,'Лента')]]")
    FLUORESCENT_BUN = (By.XPATH, "//p[contains(.,'Флюоресцентная булка')]/ancestor::a[1]")
    INGREDIENT_COUNTER = (
        By.XPATH,
        "//p[contains(.,'Флюоресцентная булка')]/ancestor::a[1]"
        "//p[contains(@class,'counter_counter__num')]"
    )
    BASKET_LIST = (By.XPATH, "//section[contains(@class,'BurgerConstructor_basket')]")
    MODAL_WINDOW = (By.XPATH, "//section[contains(@class,'Modal_modal')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")
    OVERLAY = (By.XPATH, "//div[contains(@class,'Modal_modal_overlay')]")
