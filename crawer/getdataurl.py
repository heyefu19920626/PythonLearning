import requests
from selenium import webdriver
import time

response = requests.get("http://localhost:8080/export/listAndImgExport.jsp")

print(response.text)



driver = webdriver.Chrome("/home/heyefu/python/PythonLearning/crawer/chromedriver")
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("http://localhost:8080/export/listAndImgExport.jsp")
time.sleep(3)
img = driver.find_element_by_id("imgUrl")
print(img.text)

