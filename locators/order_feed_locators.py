from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDERS_LIST = (By.XPATH, "//ul[contains(@class,'OrderFeed_list')]")

    COUNTER_TOTAL = (
        By.XPATH,
        "//p[contains(.,'Выполнено за') and contains(.,'все')]/following-sibling::p"
    )

    COUNTER_TODAY = (
        By.XPATH,
        "//p[contains(.,'Выполнено за сегодня')]/following-sibling::p"
    )

    IN_WORK_LIST = (By.XPATH, "//p[contains(.,'В работе')]/following-sibling::ul")
    IN_WORK_NUMBERS = (By.XPATH, "//p[contains(.,'В работе')]/following-sibling::ul//li")
