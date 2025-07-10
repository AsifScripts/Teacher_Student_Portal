from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch Chrome browser with basic options
driver = webdriver.Chrome()

try:
    print("🔄 Opening login page...")
    driver.get("http://localhost:5000")
    print("🌐 Page loaded.")

    # Fill in login credentials
    print("🔐 Entering credentials...")
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("Admin@Password12")

    print("📤 Submitting login form...")
    driver.find_element(By.TAG_NAME, "form").submit()
    print("📨 Login form submitted.")

    # Wait for dashboard to load
    print("⏳ Waiting for dashboard to load...")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Add Student']"))
    )
    print("✅ Logged in. Dashboard is ready.")

    # Click the "Add Student" button
    driver.find_element(By.XPATH, "//button[text()='Add Student']").click()

    # Wait for modal form
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "name"))
    )
    print("📝 Filling Add Student form...")

    # Fill the form
    driver.find_element(By.NAME, "name").send_keys("Test User")
    Select(driver.find_element(By.NAME, "subject")).select_by_visible_text("Math")
    driver.find_element(By.NAME, "marks").send_keys("89")

    # Submit the form
    driver.find_element(By.XPATH, "//button[text()='Save']").click()
    print("📤 Submitted student form. Waiting for update...")

    # Wait for the dashboard to reload/update
    time.sleep(2)

    # Debug info
    print("🔍 Current URL:", driver.current_url)
    print("🔍 Page snapshot:\n", driver.page_source[:800])

    # Assert the student is visible in the table
    if "Test User" in driver.page_source:
        print("✅ Student added successfully.")
    else:
        raise AssertionError("Student not found in page source")

except AssertionError as ae:
    print(f"❌ Assertion failed: {ae}")
    print("🔍 Page source (partial):")
    print(driver.page_source[:800])

except Exception as e:
    print(f"❌ Unexpected error: {e}")

finally:
    driver.quit()
    print("🧹 Browser closed.")
