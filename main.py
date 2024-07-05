# import necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    # URL of the website
    url = "http://127.0.0.1:7860/"

    # Path to the ChromeDriver executable
    chromedriver_path = r"C:\Users\hanay\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe"
    
    # Number of times to repeat clicking the queue button
    repeat_times = int(input("Enter the number of times to click the queue button: "))

    # Default prompts and user inputs
    prompt1 = "instagram image style, realistic, cinematic, advertisement food picture, centered, 8k uhd, high quality , background dark marble stone table, seductive, open appetit, <lora:Seductive_Dishes_Anatomy:0.8>"
    user_input1 = input("Enter user input for first textarea: ")
    prompt2 = "unrealistic, easynegative, duplicate bred, bad proportion, bad perspective. dish not in center, multiple dishes, deformed food, recepie, soup,"
    user_input2 = input("Enter user input for second textarea: ")

    # Set up the WebDriver with the specified service
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service)

    try:
        # Open the URL
        driver.get(url)
        time.sleep(5)  # Adjust wait time as needed

        # Locate and fill the first textarea
        textarea1 = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/gradio-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[2]/label/textarea"))
        )
        textarea1.clear()
        textarea1.send_keys(prompt1 + ", " + user_input1)

        # Locate and fill the second textarea
        textarea2 = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/gradio-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/label/textarea"))
        )
        textarea2.clear()
        textarea2.send_keys(prompt2 + " " + user_input2)

        # Click the queue button specified number of times
        for _ in range(repeat_times):
            queue_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/gradio-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/button"))
            )
            queue_button.click()
            time.sleep(0.5)  # Wait 0.5 seconds before clicking again

        # Long wait time to keep the WebDriver open
        wait_time_seconds = 3600  # 1 hour
        print(f"Waiting for {wait_time_seconds} seconds before exiting...")
        time.sleep(wait_time_seconds)

    except Exception as e:
        print(f"An error occurred: {e}")

    # Optionally, you can keep the driver open by not calling driver.quit()

if __name__ == "__main__":
    main()
