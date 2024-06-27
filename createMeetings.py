from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup WebDriver (assuming Chrome)
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the URL
driver.get("https://turtled-admin-dashboard.netlify.app")

# Wait for page to load
time.sleep(2)  # Adjust as necessary

try:
    # Commands from JSON script
    driver.execute_script("window.scrollTo(0, 0);")
    driver.execute_script("window.scrollTo(0, 180);")

    element = driver.find_element(By.NAME, "email")
    element.click()
    element.clear()
    element.send_keys("john@admin.com")

    element = driver.find_element(By.NAME, "password")
    element.click()
    element.clear()
    element.send_keys("Test@1234")

    driver.find_element(By.CSS_SELECTOR, ".justify-center").click()

    # Wait For Next Page
    next_page_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Calendar"))
    )

    driver.find_element(By.LINK_TEXT, "Calendar").click()

    # Click on element
    driver.find_element(By.CSS_SELECTOR, ".border > .hidden .flex").click()
    
    # Start Date
    element = driver.find_element(By.NAME, "start_date")
    element.click()
    element.clear()
    element.send_keys("2024-07-01")


    # <<<<<<<<<<<<<<<<<<       START - TIME       >>>>>>>>>>>>>>>>>>>>>>


    # Start Time Hour
    element = driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .flex > div:nth-child(1) > .w-12")
    element.click()
    element.clear()
    element.send_keys("10")

    # Start Time Minute
    element = driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .flex > div:nth-child(2) > .w-12")
    element.click()
    element.clear()
    element.send_keys("0")

    # Start Time AM/PM
    dropdown = Select(driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > .flex > .min-w-20"))
    dropdown.select_by_visible_text("PM")

    
    # <<<<<<<<<<<<<<<<<<       END - TIME       >>>>>>>>>>>>>>>>>>>>>>


    # End Time Hour
    element = driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .flex > div:nth-child(1) > .w-12")
    element.click()
    element.clear()
    element.send_keys("11")

    # End Time Minute
    element = driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .flex > div:nth-child(2) > .w-12")
    element.click()
    element.clear()
    element.send_keys("0")

    # End Time AM/PM
    dropdown = Select(driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .flex > .min-w-20"))
    dropdown.select_by_visible_text("PM")



    # Select School
    driver.find_element(By.CSS_SELECTOR, ".w-full:nth-child(3) > .w-full > .relative > .w-full").click()
    driver.find_element(By.CSS_SELECTOR, ".px-4:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".w-full:nth-child(3) > .w-full > .relative > .w-full > div").click()
    driver.find_element(By.CSS_SELECTOR, ".hover\3A bg-blue-600:nth-child(2)").click()

    
    # Repeat similar steps for other interactions...
    
    # Click buttons, select options, type values, etc.
    
finally:
    # Close the browser
    driver.quit()