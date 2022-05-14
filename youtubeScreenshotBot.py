from selenium import webdriver
import time
driver=webdriver.Chrome()
url="https://www.youtube.com/"
driver.get(url)
time.sleep(3)
driver.maximize_window()
driver.save_screenshot("youtube.com-homepage.png")
url="https://www.youtube.com/watch?v=AzYIJdsSDms"
driver.get(url)
print(driver.title)
if "Evgeny" in driver.title:
    driver.save_screenshot("youtube.com-Evgeny.png")
time.sleep(3)
driver.back()
time.sleep(3)
driver.close()
