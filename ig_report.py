import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Get user inputs
username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")
target_accounts = input("Enter the usernames to report, separated by commas: ").split(',')

# Set up Firefox options for headless mode
options = Options()
options.headless = True  # Ensures it runs without a GUI, suitable for Termux

# Initialize WebDriver with Firefox
driver = webdriver.Firefox(options=options)  # Assumes geckodriver is installed and in PATH

try:
    driver.get("https://www.instagram.com/")

    # Wait for the login page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

    # Enter credentials and log in
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Wait for login to complete
    WebDriverWait(driver, 10).until(EC.url_contains("instagram.com"))

    for account in target_accounts:
        account = account.strip()
        driver.get(f"https://www.instagram.com/{account}/")

        # Wait for the profile page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@role='button' and contains(@aria-label, 'More')]")))

        # Click on the options (three dots) button
        options_button = driver.find_element(By.XPATH, "//div[@role='button' and contains(@aria-label, 'More')]")
        options_button.click()

        # Click on the Report option
        report_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Report') or contains(@aria-label, 'Report')]")))
        report_button.click()

        # Select a report reason (e.g., "It's spam")
        reason_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'It’s spam')]")))
        reason_button.click()

        # Confirm the report
        confirm_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Report') or contains(@aria-label, 'Report')]")))
        confirm_button.click()

        print(f"Processed report for {account}")

finally:
    driver.quit()
    print("Script completed.")