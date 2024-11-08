from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# Initialize the WebDriver with the options
driver = webdriver.Chrome(options=options)

try:
    # Open Google and search for "bowiestate.edu"
    driver.get("https://www.google.com")
    
    # Search for "bowiestate.edu"
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("bowiestate.edu")
    search_box.send_keys(Keys.RETURN)
    
    # Wait until results are loaded and click on the first result
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "h3"))
    ).click()
    
    # Wait until the Bowie State University page loads and click on MyBSU link
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "MyBSU"))
    ).click()
    
    # Click on the Blackboard link on the MyBSU page
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Blackboard"))
    ).click()
    
    # Keep the browser open for 10 seconds
    time.sleep(10)
    
finally:
    # Close the browser after 10 seconds
    driver.quit()
