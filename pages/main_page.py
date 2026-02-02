import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.ingredient_modal_locators import IngredientModalLocators


class MainPage(BasePage):

    @allure.step("Клик по вкладке 'Конструктор'")
    def click_constructor_tab(self):
        self.click(MainPageLocators.CONSTRUCTOR_TAB)

    @allure.step("Клик по вкладке 'Лента заказов'")
    def click_order_feed_tab(self):
        self.click(MainPageLocators.ORDER_FEED_TAB)

    @allure.step("Клик по первому ингредиенту")
    def click_first_ingredient(self):
        self.click(IngredientModalLocators.INGREDIENT_CARD)

    @allure.step("Проверяем, что модальное окно ингредиента открыто")
    def is_ingredient_modal_opened(self):
        self.wait_visible(IngredientModalLocators.MODAL_WINDOW)

    @allure.step("Закрываем модальное окно ингредиента")
    def close_ingredient_modal(self):
        self.click(IngredientModalLocators.CLOSE_BUTTON)
