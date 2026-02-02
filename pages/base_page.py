import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открываем страницу: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Ждём видимость элемента: {locator}")
    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Кликаем по элементу: {locator}")
    def click(self, locator):
        self.wait_visible(locator).click()

    @allure.step("Получаем текст элемента: {locator}")
    def get_text(self, locator):
        return self.wait_visible(locator).text
