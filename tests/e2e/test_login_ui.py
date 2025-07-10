# tests/test_login_ui.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login(driver):
    driver.get("http://localhost:5000")
    driver.find_element(By.NAME, "username").send_keys("asif")
    driver.find_element(By.NAME, "password").send_keys("Wild@Asif12")
    driver.find_element(By.TAG_NAME, "form").submit()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Add Student']"))
    )

    assert "Dashboard" in driver.page_source
