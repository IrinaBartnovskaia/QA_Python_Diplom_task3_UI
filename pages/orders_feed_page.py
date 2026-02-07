import allure

from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrdersFeedPage(BasePage):

    @allure.step("Ожидание открытия страницы 'Лента заказов'")
    def wait_page_loaded(self):
        self.find_element(OrderFeedLocators.ORDERS_LIST)

    @allure.step("Получаем значение счетчика 'Выполнено за всё время'")
    def get_total_orders_count(self):
        return int(self.find_element(OrderFeedLocators.TOTAL_ORDERS).text)

    @allure.step("Получаем значение счетчика 'Выполнено за сегодня'")
    def get_today_orders_count(self):
        return int(self.find_element(OrderFeedLocators.TODAY_ORDERS).text)
