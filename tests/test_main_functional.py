import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pages.main_page import MainPage
from data.urls import Urls


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        drv = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    else:
        drv = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    drv.maximize_window()
    yield drv
    drv.quit()


@allure.suite("Основная функциональность")
class TestMainPage:

    @allure.title("Переход по вкладкам Конструктор / Лента заказов")
    def test_navigation_tabs(self, driver):
        main_page = MainPage(driver)
        main_page.open(Urls.MAIN_PAGE)

        main_page.click_order_feed_tab()
        main_page.click_constructor_tab()

    @allure.title("Открытие и закрытие модального окна ингредиента")
    def test_ingredient_modal_open_close(self, driver):
        main_page = MainPage(driver)
        main_page.open(Urls.MAIN_PAGE)

        main_page.click_first_ingredient()
        main_page.is_ingredient_modal_opened()
        main_page.close_ingredient_modal()
