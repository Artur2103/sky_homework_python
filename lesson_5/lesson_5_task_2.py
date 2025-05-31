from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

#зайти на сайт http://uitestingplayground.com/dynamicid
driver.get("http://uitestingplayground.com/dynamicid")
sleep(2)

# поиск и клик по кнопке с тэгом button, классом btn-primary
blue_button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary')
blue_button.click()
sleep(3)

# закрытие браузера
driver.quit()
