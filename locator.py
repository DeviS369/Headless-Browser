from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Open the Saucedemo website
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    # Display cookies before login
    print("Cookies before login:")
    cookies_before_login = driver.get_cookies()
    for cookie in cookies_before_login:
        print(cookie)

    # Login credentials
    username = "standard_user"
    password = "secret_sauce"

    # Perform login
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()
    time.sleep(3)

    # Display cookies after login
    print("\nCookies after login:")
    cookies_after_login = driver.get_cookies()
    for cookie in cookies_after_login:
        print(cookie)

    # Perform logout
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()
    time.sleep(2)
    logout_link = driver.find_element(By.ID, "logout_sidebar_link")
    logout_link.click()
    time.sleep(2)

    print("\nSuccessfully logged out.")

finally:
    # Close the browser
    driver.quit()
