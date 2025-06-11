from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_youtube_search():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com")

    time.sleep(2)  # wait for page to load

    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys("QA Automation Kayalvizhi")
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)

    # Check that search results are displayed
    results = driver.find_elements(By.ID, "video-title")
    assert len(results) > 0, "No video results found!"

    print(f"{len(results)} video results found for search.")

    driver.quit()
