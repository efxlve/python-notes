from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

driver = webdriver.Chrome()
driver.maximize_window()

'''
driver.get("https://www.google.com/")
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.NAME, "q")))

input_element_by_name = driver.find_element(By.NAME, "q")
# input_element_by_class_name = driver.find_element(By.CLASS_NAME, "gLFyf")
# input_element_by_xpath = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')

# print(input_element_by_name)
# print(input_element_by_class_name)
# print(input_element_by_xpath)

input_element_by_name.send_keys("Selenium")
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.NAME, "btnK")))

search_button = driver.find_element(By.NAME, "btnK")
WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.NAME, "btnK")))
search_button.click()

time.sleep(5)
'''

driver.get("https://atilsamancioglu.com")
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div/header/div[1]/div[3]/nav/div/ul/li[3]/a")))

blog_page = driver.find_element(By.XPATH,"/html/body/div/header/div[1]/div[3]/nav/div/ul/li[3]/a")
blog_page.click()
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"button")))

read_button = driver.find_element(By.CLASS_NAME,"button")
read_button.click()
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div/div[1]/div[2]/aside[4]")))

article_list = driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/aside[4]")
print(f" atilsamancioglu.com has {len(article_list.text.splitlines())} blog posts")

