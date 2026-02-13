import allure

from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrdersFeedPage(BasePage):

    @allure.step("Ожидание открытия страницы 'Лента заказов'")
    def wait_page_loaded(self):
        self.wait_for_element_visible(OrderFeedLocators.ORDERS_LIST, timeout=20)

    @allure.step("Получить значение выбранного счётчика")
    def get_value_any_counter(self, counter_locator):
        text = self.get_text_of_element(counter_locator, timeout=20)
        return int(text)

    @allure.step("Подождать, что блок 'В работе' появился")
    def wait_for_orders_in_progress(self):
        self.wait_for_element_visible(OrderFeedLocators.IN_WORK_LIST, timeout=20)

    @allure.step("Получить ВСЕ номера заказов из блока 'В работе'")
    def get_numbers_orders_in_progress(self):
        self.wait_for_orders_in_progress()
        items = self.driver.find_elements(*OrderFeedLocators.IN_WORK_NUMBERS)
        numbers = []
        for i in items:
            t = i.text.strip()
            if t.isdigit():
                numbers.append(int(t))  # int сам уберёт ведущие нули
        return numbers
