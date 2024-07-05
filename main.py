# main.py

# import necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import config 

def main():
    try:
        # Number of times to repeat clicking the queue button
        repeat_times = int(input("Enter the number of times to click the queue button: "))

        # User inputs
        user_input1 = input("Enter user input for first textarea: ")
        user_input2 = input("Enter user input for second textarea: ")

        # Set up the WebDriver with the specified service
        service = Service(config.chromedriver_path)
        driver = webdriver.Chrome(service=service)

        # Open the URL
        driver.get(config.url)
        time.sleep(5)  

        # Locate and fill the first textarea
        textarea1 = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/gradio-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[2]/label/textarea"))
        )
        textarea1.clear()
        textarea1.send_keys(config.prompt1 + ", " + user_input1)

        # Locate and fill the second textarea
        textarea2 = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/gradio-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/label/textarea"))
        )
        textarea2.clear()
        textarea2.send_keys(config.prompt2 + " " + user_input2)

        # Click the queue button specified number of times
        for _ in range(repeat_times):
            queue_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/gradio-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/button"))
            )
            queue_button.click()
            time.sleep(0.5)  

        # Long wait time to keep the WebDriver open
        wait_time_seconds = 3600  # 1 hour
        print(f"Waiting for {wait_time_seconds} seconds before exiting...")
        time.sleep(wait_time_seconds)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
