import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from data.urls import URL


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    """
    Логинимся перед тестом.
    Логин/пароль берём из переменных окружения:
    STELLAR_EMAIL и STELLAR_PASSWORD
    """
    email = os.getenv("STELLAR_EMAIL")
    password = os.getenv("STELLAR_PASSWORD")
    if not email or not password:
        raise RuntimeError(
            "Не заданы STELLAR_EMAIL / STELLAR_PASSWORD. "
            "Добавь в переменные окружения (Run Configuration -> Environment variables)."
        )

    driver.get(URL.MAIN_PAGE)

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Войти в аккаунт')]"))
    ).click()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@type='text' or @type='email']"))
    ).send_keys(email)

    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)

    driver.find_element(By.XPATH, "//button[contains(.,'Войти')]").click()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='Конструктор']"))
    )
