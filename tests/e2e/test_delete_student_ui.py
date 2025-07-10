from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:5000")
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("Admin@Password12")
    driver.find_element(By.TAG_NAME, "form").submit()
    time.sleep(2)

    # Find delete buttons and click one
    delete_buttons = driver.find_elements(By.XPATH, "//a[contains(@href, '/delete_student/')]")
    if delete_buttons:
        delete_buttons[0].click()
        print("✅ Student deleted successfully.")
    else:
        print("⚠️ No student to delete.")

finally:
    driver.quit()
