import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
    else:
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )

    driver.maximize_window()
    yield driver
    driver.quit()


@allure.suite("Основная функциональность")
class TestMainPage:

    @allure.title("Переход между вкладками Конструктор / Лента заказов")
    def test_navigation_tabs(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_for_page_to_load()

        main_page.click_on_feed_button()
        main_page.click_on_constructor_button()

    @allure.title("Открытие и закрытие модального окна ингредиента")
    def test_ingredient_modal_open_close(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_for_page_to_load()

        main_page.click_on_ingredient()
        assert main_page.is_modal_visible()

        main_page.close_ingredient_modal()

    @allure.title("Счетчик ингредиента увеличивается при добавлении в заказ")
    def test_ingredient_counter_increases_after_adding(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_for_page_to_load()

        before = main_page.get_ingredient_counter()

        main_page.drag_ingredient_bun_to_basket()

        # Ждём, что счетчик изменится
        main_page.wait_for_text_changed(
            MainPageLocators.INGREDIENT_COUNTER,
            str(before),
            timeout=10
        )

        after = main_page.get_ingredient_counter()
        assert after > before
