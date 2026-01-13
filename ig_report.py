import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuration
instagram_username = "your_instagram_username"  # Replace with your Instagram username
instagram_password = "your_instagram_password"  # Replace with your Instagram password
target_account = "target_instagram_account"  # Replace with the username of the account to report
num_reports = 100  # Number of times to report the account

# Set up the webdriver (make sure you have ChromeDriver installed and in your PATH)
driver = webdriver.Chrome()  # Use webdriver.Chrome() for Chrome, or adjust as needed

try:
    # Step 1: Go to Instagram login page
    driver.get("https://www.instagram.com/accounts/login/")
    
    # Step 2: Wait for the page to load and enter credentials
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    username_field.send_keys(instagram_username)
    password_field.send_keys(instagram_password)
    password_field.send_keys(Keys.RETURN)
    
    # Step 3: Wait for login to complete
    WebDriverWait(driver, 10).until(EC.url_contains("instagram.com"))
    
    for _ in range(num_reports):
        # Step 4: Navigate to the target account
        driver.get(f"https://www.instagram.com/{target_account}/")
        
        # Step 5: Wait for the page to load and find the report option
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'x1i10hfl') and contains(text(), 'More')]")))  # This might need adjustment based on Instagram's current HTML
        more_options_button = driver.find_element(By.XPATH, "//div[contains(@class, 'x1i10hfl') and contains(text(), 'More')]")
        more_options_button.click()
        
        # Step 6: Click on 'Report' (this is approximate; Instagram's UI changes frequently)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Report')]")))
        report_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Report')]")
        report_button.click()
        
        # Step 7: Select a report reason (e.g., 'It's spam')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), \"It's spam\")]")))
        spam_reason = driver.find_element(By.XPATH, "//div[contains(text(), \"It's spam\")]")
        spam_reason.click()
        
        # Step 8: Confirm the report
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Submit')]")))
        submit_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Submit')]")
        submit_button.click()
        
        # Step 9: Wait a bit to avoid rate limiting or detection
        time.sleep(5)  # Sleep for 5 seconds between reports
        
        print(f"Report {_ + 1} completed.")  # Optional logging; remove if you want silence

finally:
    # Step 10: Clean up
    driver.quit()