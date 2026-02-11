import allure

from data.urls import URL
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open_page(URL.MAIN_PAGE)

    @allure.step("Дождаться загрузки главной страницы")
    def wait_for_page_to_load(self):
        # 1) дождались, что появились табы/хедер
        self.wait_for_element_visible(MainPageLocators.CONSTRUCTOR_BUTTON, timeout=20)
        # 2) если вдруг висит оверлей — подождали исчезновение
        self.wait_for_element_hide(MainPageLocators.OVERLAY, timeout=20)

    @allure.step("Проверить, что главная открыта")
    def is_main_page_opened(self):
        return self.get_current_url() == URL.MAIN_PAGE

    @allure.step("Кликнуть на Конструктор")
    def click_on_constructor_button(self):
        self.scroll_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на Лента заказов")
    def click_on_feed_button(self):
        self.scroll_to_element(MainPageLocators.FEED_BUTTON)
        self.click_on_element(MainPageLocators.FEED_BUTTON)

    @allure.step("Кликнуть по ингредиенту (флюоресцентная булка)")
    def click_on_ingredient(self):
        self.scroll_to_element(MainPageLocators.FLUORESCENT_BUN)
        self.click_on_element(MainPageLocators.FLUORESCENT_BUN)

    @allure.step("Закрыть модальное окно ингредиента")
    def close_ingredient_modal(self):
        self.click_on_element(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Проверить, что модальное окно открыто")
    def is_modal_visible(self):
        return self.is_element_visible(MainPageLocators.MODAL_WINDOW)

    @allure.step("Подождать, что модальное окно закрылось")
    def is_modal_closed(self):
        return self.wait_for_element_hide(MainPageLocators.MODAL_WINDOW, timeout=20)

    @allure.step("Получить значение счётчика ингредиента")
    def get_ingredient_counter(self):
        text = self.get_text_of_element(MainPageLocators.INGREDIENT_COUNTER, timeout=20)
        return int(text)

    @allure.step("Перетащить булку в корзину")
    def drag_ingredient_bun_to_basket(self):
        source = self.scroll_to_element(MainPageLocators.FLUORESCENT_BUN)
        target = self.wait_for_element_visible(MainPageLocators.BASKET_LIST)
        self.drag_and_drop_element(source, target)
