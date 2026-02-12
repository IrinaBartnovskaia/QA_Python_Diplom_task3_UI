import allure
import re

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Дождаться загрузки главной страницы")
    def main_page_loading_wait(self):
        self.wait_for_element_visible(MainPageLocators.CONSTRUCTOR_BUTTON, timeout=20)
        self.wait_for_element_hide(MainPageLocators.OVERLAY, timeout=20)

    @allure.step("Кликнуть на Конструктор")
    def click_by_link_constructor(self):
        self.scroll_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на Лента заказов")
    def click_by_link_orders_feed(self):
        self.scroll_to_element(MainPageLocators.FEED_BUTTON)
        self.click_on_element(MainPageLocators.FEED_BUTTON)

    @allure.step("Создать заказ: булка + любой ингредиент")
    def create_order(self):
        target = self.wait_for_element_visible(MainPageLocators.BASKET_LIST, timeout=20)

        bun = self.scroll_to_element(MainPageLocators.FLUORESCENT_BUN)
        self.drag_and_drop_element(bun, target)

        other = self.scroll_to_element(MainPageLocators.ANY_NON_BUN_CARD)
        self.drag_and_drop_element(other, target)

        self.click_on_element(MainPageLocators.ORDER_BUTTON, timeout=20)

    @allure.step("Проверить, что модалка успешного заказа появилась")
    def is_order_success_modal_visible(self):
        return self.wait_for_element_visible(MainPageLocators.MODAL_WINDOW, timeout=20)

    @allure.step("Дождаться окончания анимации (ждём реальный номер заказа, не 9999)")
    def wait_for_animation_end(self):
        # ждём, что в модалке появился настоящий номер (цифры и не '9999')
        def _real_number_present(_):
            num = self.get_number_of_order(safe=True)
            return num is not None and num != "9999" and len(num) >= 5

        WebDriverWait(self.driver, 20).until(_real_number_present)

    @allure.step("Получить номер заказа")
    def get_number_of_order(self, safe=False):
        """
        safe=True -> вернёт None если не получилось взять номер прямо сейчас
        """
        try:
            # Сначала пробуем правильное поле с реальными цифрами
            text = self.get_text_of_element(MainPageLocators.ORDER_NUMBER_VALUE, timeout=3).strip()
        except Exception:
            # Фолбэк: иногда номер в h2, но там может быть 9999
            try:
                text = self.get_text_of_element(MainPageLocators.ORDER_NUMBER, timeout=3).strip()
            except Exception:
                return None if safe else ""

        # вытаскиваем только цифры
        digits = re.sub(r"\D", "", text)
        if safe and not digits:
            return None
        return digits

    @allure.step("Закрыть модалку успешного заказа (оверлей/ESC/JS)")
    def click_close_button_success_modal(self):
        # 1) клик по оверлею (точный класс)
        try:
            overlay = self.wait_for_element_visible(MainPageLocators.OVERLAY_CLICK, timeout=5)
            overlay.click()
            return
        except Exception:
            pass

        # 2) общий оверлей
        try:
            overlay = self.wait_for_element_visible(MainPageLocators.OVERLAY, timeout=5)
            overlay.click()
            return
        except Exception:
            pass

        # 3) ESC
        try:
            self.driver.switch_to.active_element.send_keys(Keys.ESCAPE)
            return
        except Exception:
            pass

        # 4) обычный клик по крестику
        try:
            self.click_on_element(MainPageLocators.MODAL_CLOSE_BUTTON, timeout=5)
            return
        except ElementClickInterceptedException:
            # 5) JS-клик по крестику
            btn = self.wait_for_element_visible(MainPageLocators.MODAL_CLOSE_BUTTON, timeout=5)
            self.driver.execute_script("arguments[0].click();", btn)

    @allure.step("Подождать, что модалка скрылась")
    def wait_for_order_success_modal_hidden(self):
        self.wait_for_element_hide(MainPageLocators.MODAL_WINDOW, timeout=20)
