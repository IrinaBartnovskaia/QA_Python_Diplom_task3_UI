from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDERS_LIST = (By.XPATH, "//ul[contains(@class,'OrderFeed_list')]")

    TOTAL_ORDERS = (
        By.XPATH,
        "//p[text()='Выполнено за все время:']/following-sibling::p"
    )

    TODAY_ORDERS = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p"
    )

    IN_PROGRESS_ORDERS = (
        By.XPATH,
        "//ul[contains(@class,'OrderFeed_orderListReady')]"
    )
