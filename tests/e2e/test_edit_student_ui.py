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

    # Find first editable name cell and edit it
    name_cells = driver.find_elements(By.CLASS_NAME, "name")
    if name_cells:
        name_cells[0].click()
        name_cells[0].clear()
        name_cells[0].send_keys("Updated Name")

    save_buttons = driver.find_elements(By.CLASS_NAME, "save-btn")
    if save_buttons:
        save_buttons[0].click()

    time.sleep(2)
    print("✅ Student edited successfully.")

finally:
    driver.quit()
