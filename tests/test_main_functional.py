import allure

from data.urls import URL
from pages.main_page import MainPage
from pages.orders_feed_page import OrdersFeedPage
from locators.main_page_locators import MainPageLocators
from locators.order_feed_locators import OrderFeedLocators


@allure.suite("Основная функциональность")
class TestMainPage:

    @allure.title("Переход во вкладку «Лента заказов»")
    def test_open_orders_feed_tab(self, driver):
        main_page = MainPage(driver)
        feed_page = OrdersFeedPage(driver)

        main_page.open_page(URL.MAIN_PAGE)
        main_page.main_page_loading_wait()

        main_page.click_by_link_orders_feed()

        # assert: лента реально открылась (ждём список заказов)
        feed_page.wait_page_loaded()
        assert True

    @allure.title("Переход во вкладку «Конструктор»")
    def test_open_constructor_tab(self, driver):
        main_page = MainPage(driver)

        main_page.open_page(URL.MAIN_PAGE)
        main_page.main_page_loading_wait()

        # уходим в ленту и возвращаемся в конструктор
        main_page.click_by_link_orders_feed()
        main_page.click_by_link_constructor()

        # assert: конструктор открыт (ждём кнопку/вкладку Конструктор)
        main_page.wait_for_element_visible(MainPageLocators.LINK_CONSTRUCT, timeout=10)
        assert True

    @allure.title("Открытие и закрытие модального окна ингредиента")
    def test_ingredient_modal_open_close(self, driver):
        main_page = MainPage(driver)

        main_page.open_page(URL.MAIN_PAGE)
        main_page.main_page_loading_wait()

        # открываем модалку
        main_page.click_on_ingredient()

        # assert: модалка открылась
        assert main_page.is_modal_visible()

        # закрываем
        main_page.close_ingredient_modal()

        # assert: модалка исчезла
        main_page.wait_for_element_invisible(MainPageLocators.INGREDIENT_MODAL, timeout=10)
        assert True

    @allure.title("Счетчик ингредиента увеличивается при добавлении в заказ")
    def test_ingredient_counter_increases_after_adding(self, driver):
        main_page = MainPage(driver)

        main_page.open_page(URL.MAIN_PAGE)
        main_page.main_page_loading_wait()

        before = main_page.get_ingredient_counter()

        main_page.drag_ingredient_bun_to_basket()

        # ждём, что счетчик поменялся
        main_page.wait_for_text_changed(
            MainPageLocators.COUNTER_BUN,
            str(before),
            timeout=10
        )

        after = main_page.get_ingredient_counter()
        assert after > before
