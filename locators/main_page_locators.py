from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_TAB = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_TAB = (By.XPATH, "//p[contains(text(),'Лента')]")
