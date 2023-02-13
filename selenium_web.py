from re import search
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Infow():
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


    def get_info(self,query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        search = WebDriverWait(self.driver, 5).until(
EC.presence_of_element_located((By.XPATH, '//*[@id="searchInput"]')))
        
        search.click()
        search.send_keys(query)
        enter = WebDriverWait(self.driver, 5).until(
EC.presence_of_element_located((By.XPATH, '//*[@id="search-form"]/fieldset/button')))
        enter.click()
