from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[normalize-space()='Конструктор']/ancestor::a[1]")
    FEED_BUTTON = (By.XPATH, "//a[contains(@href,'/feed') and .//p[contains(.,'Лента')]]")

    FLUORESCENT_BUN = (By.XPATH, "//p[contains(.,'Флюоресцентная булка')]/ancestor::a[1]")

    BASKET_LIST = (By.XPATH, "//section[contains(@class,'BurgerConstructor_basket')]")

    MODAL_WINDOW = (By.XPATH, "//section[contains(@class,'Modal_modal')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")

    OVERLAY = (By.XPATH, "//div[contains(@class,'Modal_modal_overlay')]")
    OVERLAY_CLICK = (By.XPATH, "//div[contains(@class,'Modal_modal_overlay__x2ZCr')]")

    ORDER_BUTTON = (By.XPATH, "//button[contains(.,'Оформить заказ')]")

    ORDER_NUMBER = (By.XPATH, "//section[contains(@class,'Modal_modal')]//h2")

    ORDER_NUMBER_VALUE = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal')]//p[normalize-space() and not(contains(.,'идентификатор')) and string-length(normalize-space())>=5 and translate(normalize-space(), '0123456789', '')='']"
    )

    ANY_NON_BUN_CARD = (
        By.XPATH,
        "(//a[.//p and not(.//p[contains(translate(., 'БУЛКА', 'булка'),'булка')])])[1]"
    )
