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
driver.get("https://example.app")

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


    # Loading is complete
    elementLoc = (By.CSS_SELECTOR, "svg > g > g > g > path")

    loader = WebDriverWait(driver, 10).until(
        EC.invisibility_of_element(elementLoc)
    )

    # Click on element
    driver.find_element(By.CSS_SELECTOR, ".border > .hidden .flex").click()
    
    # Start Date
    element = driver.find_element(By.NAME, "start_date")
    element.click()
    element.clear()
    element.send_keys("07-03-2024")


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


    # <<<<<<<<<<<<<<<<<<       SELECT - OPTIONS       >>>>>>>>>>>>>>>>>>>>>>


    # Select School
    driver.find_element(By.CSS_SELECTOR, ".w-full:nth-child(3) > .w-full > .relative > .w-full").click()
    driver.find_element(By.CSS_SELECTOR, ".px-4:nth-child(2)").click()



    # Select Group 
    driver.find_element(By.CSS_SELECTOR, ".w-full:nth-child(4) .relative > .w-full").click()
    target_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".px-4:nth-child(4)"))
    )
    target_element.click()



    # Select Teacher 
    driver.find_element(By.CSS_SELECTOR, ".w-full:nth-child(5) .relative > .w-full").click()
    driver.find_element(By.CSS_SELECTOR, ".px-4:nth-child(6)").click()


    # <<<<<<<<<<<<<<<<<<       TITLE       >>>>>>>>>>>>>>>>>>>>>>


    # Add Title
    element = driver.find_element(By.NAME, "title")
    element.click()
    element.clear()
    element.send_keys("Game Design Class")


    # <<<<<<<<<<<<<<<<<<       CREATE - MEETING       >>>>>>>>>>>>>>>>>>>>>>


    # Click Create
    driver.find_element(By.CSS_SELECTOR, ".flex-1 > .bg-primary > .flex").click()


    # <<<<<<<<<<<<<<<<<<       MEETING - CREATION - SUCCESFUL       >>>>>>>>>>>>>>>>>>>>>>


    # Assuming driver is your WebDriver instance
    command = "wait for text"
    target = (By.CSS_SELECTOR, ".go3958317564")
    value = "Class has been created successfully!"

    # Wait for the specific text to be present in the element
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(target, value)
    )
    
finally:
    # Close the browser
    driver.quit()