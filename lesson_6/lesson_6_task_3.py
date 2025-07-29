from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
firefox_options = webdriver.FirefoxOptions()

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

# зайти на сайт
# https://bonigarcia.dev/selenium-webdriver-java/loading-images.html
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

# Ожидание, пока текст элемента с ID 'text' не станет равен "Done!"
waiter = WebDriverWait(driver, 20)
waiter.until(
    lambda driver: driver.find_element(By.ID, 'text').text == "Done!"
)
# поиск третьей картинки с ID=award
pict_award = driver.find_element(By.ID, 'award')

# печать атрибута src третьей картинки
src_value = pict_award.get_attribute('src')
print(src_value)

# закрытие браузера
driver.quit()
