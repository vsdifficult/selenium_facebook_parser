from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome('путь_к_chromedriver', options=options)


driver.get('ссылка_на_пост')


wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.UFIPagerRow')))


comments = driver.find_elements(By.CSS_SELECTOR, 'div.UFICommentContentBlock')


for comment in comments:
    print(comment.text)

driver.quit()
