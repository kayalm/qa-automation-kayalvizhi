import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_api_ui_combo():
    # Step 1 – API call (fake placeholder)
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200
    assert "title" in response.json()[0]

    # Step 2 – UI open Google and search
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    search = driver.find_element(By.NAME, "q")
    search.send_keys("API Testing Python Kayalvizhi")
    search.submit()

    time.sleep(2)
    assert "API" in driver.title
    driver.quit()
