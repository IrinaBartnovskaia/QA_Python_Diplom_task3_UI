import allure
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Подождать видимость элемента")
    def wait_for_element_visible(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Подождать пока элемент станет кликабельным")
    def wait_for_element_clickable(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Подождать, что элемент исчезнет")
    def wait_for_element_hide(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    # алиас (в твоих файлах местами используется это имя)
    def wait_for_element_invisible(self, locator, timeout=10):
        return self.wait_for_element_hide(locator, timeout)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=20):
        element = self.wait_for_element_clickable(locator, timeout)
        element.click()

    @allure.step("Кликнуть на элемент (с повтором, если перехватывает оверлей)")
    def safe_click(self, locator, overlay_locator=None, timeout=20):

        try:
            self.click_on_element(locator, timeout=timeout)
            return
        except ElementClickInterceptedException:
            if overlay_locator is not None:
                try:
                    self.wait_for_element_hide(overlay_locator, timeout=10)
                except Exception:
                    pass


        try:
            self.click_on_element(locator, timeout=timeout)
            return
        except (ElementClickInterceptedException, StaleElementReferenceException):
            # принудительный клик
            element = self.wait_for_element_visible(locator, timeout=timeout)
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получить текст элемента")
    def get_text_of_element(self, locator, timeout=20):
        return self.wait_for_element_visible(locator, timeout).text

    @allure.step("Проверить, что элемент отображается")
    def is_element_visible(self, locator, timeout=20):
        return self.wait_for_element_visible(locator, timeout).is_displayed()

    @allure.step("Скролл к элементу")
    def scroll_to_element(self, locator, timeout=20):
        element = self.wait_for_element_visible(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        return element

    @allure.step("Перетащить элемент в корзину")
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    @allure.step("Подождать, что текст элемента изменится")
    def wait_for_text_changed(self, locator, old_text: str, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(*locator).text.strip() != str(old_text).strip()
        )
