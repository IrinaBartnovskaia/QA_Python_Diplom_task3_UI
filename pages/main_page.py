import allure
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Ожидание загрузки главной страницы")
    def main_page_loading_wait(self):
        self.wait_for_element_visible(MainPageLocators.LINK_CONSTRUCT, timeout=20)
        try:
            self.wait_for_element_hide(MainPageLocators.OVERLAY, timeout=10)
        except Exception:
            pass

    @allure.step("Клик по ссылке 'Конструктор'")
    def click_by_link_constructor(self):
        self.click_on_element(MainPageLocators.LINK_CONSTRUCT, timeout=20)

    @allure.step("Клик по ссылке 'Лента заказов'")
    def click_by_link_orders_feed(self):
        self.click_on_element(MainPageLocators.LINK_ORDER_FEED, timeout=20)

    @allure.step("Создать заказ (добавить ингредиенты и нажать 'Оформить заказ')")
    def create_order(self):
        self.drag_ingredient_bun_to_basket()
        self.drag_any_non_bun_to_basket()
        self.click_order_button()

    @allure.step("Клик по ингредиенту (Краторная булка)")
    def click_on_ingredient(self):
        self.click_on_element(MainPageLocators.BUN_KRATOR, timeout=20)

    @allure.step("Проверить, что модальное окно открыто")
    def is_modal_visible(self):
        return self.is_element_visible(MainPageLocators.MODAL_WINDOW, timeout=20)

    @allure.step("Закрыть модальное окно ингредиента")
    def close_ingredient_modal(self):
        # закрываем безопасно (оверлей иногда перехватывает)
        self.safe_click(
            MainPageLocators.MODAL_CLOSE_BUTTON,
            overlay_locator=MainPageLocators.OVERLAY,
            timeout=20
        )

    @allure.step("Подождать, что модальное окно закрылось")
    def is_modal_closed(self):
        return self.wait_for_element_hide(MainPageLocators.MODAL_WINDOW, timeout=20)

    @allure.step("Получить значение счётчика у булки")
    def get_ingredient_counter(self):
        elems = self.driver.find_elements(*MainPageLocators.COUNTER_BUN)
        if not elems:
            return 0
        text = elems[0].text.strip()
        return int(text) if text.isdigit() else 0

    @allure.step("Перетащить булку в корзину")
    def drag_ingredient_bun_to_basket(self):
        source = self.wait_for_element_visible(MainPageLocators.BUN_KRATOR, timeout=20)
        target = self.wait_for_element_visible(MainPageLocators.POS_TOP_BASKET, timeout=20)

        try:
            ActionChains(self.driver).drag_and_drop(source, target).perform()
        except Exception:
            ActionChains(self.driver) \
                .click_and_hold(source) \
                .move_to_element(target) \
                .pause(0.2) \
                .release() \
                .perform()

    @allure.step("Перетащить любой НЕ-булочный ингредиент в корзину")
    def drag_any_non_bun_to_basket(self):
        source = self.wait_for_element_visible(MainPageLocators.ANY_NON_BUN_CARD, timeout=20)
        target = self.wait_for_element_visible(MainPageLocators.POS_TOP_BASKET, timeout=20)

        try:
            ActionChains(self.driver).drag_and_drop(source, target).perform()
        except Exception:
            ActionChains(self.driver) \
                .click_and_hold(source) \
                .move_to_element(target) \
                .pause(0.2) \
                .release() \
                .perform()

    @allure.step("Нажать кнопку 'Оформить заказ'")
    def click_order_button(self):
        self.click_on_element(MainPageLocators.BUT_ORDER, timeout=20)

    @allure.step("Проверить, что модалка успешного заказа появилась")
    def is_order_success_modal_visible(self):
        self.wait_for_element_visible(MainPageLocators.ORDER_SUCCESS_TEXT, timeout=30)
        return True

    @allure.step("Дождаться, что номер заказа подставился (НЕ '9999')")
    def wait_for_animation_end(self):
        def real_order_number_loaded(d):
            text = d.find_element(*MainPageLocators.ORDER_NUMBER).text.strip()
            return text.isdigit() and text != "9999"

        WebDriverWait(self.driver, 40).until(real_order_number_loaded)

    @allure.step("Получить номер заказа из модального окна")
    def get_number_of_order(self):
        # на всякий случай ещё раз убеждаемся, что это не '9999'
        self.wait_for_animation_end()
        return self.get_text_of_element(MainPageLocators.ORDER_NUMBER, timeout=20).strip()

    @allure.step("Закрыть модалку успешного заказа")
    def click_close_button_success_modal(self):
        self.safe_click(
            MainPageLocators.MODAL_CLOSE_BUTTON,
            overlay_locator=MainPageLocators.OVERLAY,
            timeout=20
        )

    @allure.step("Дождаться, что модалка успешного заказа скрылась")
    def wait_for_order_success_modal_hidden(self):
        self.wait_for_element_hide(MainPageLocators.ORDER_SUCCESS_TEXT, timeout=20)
