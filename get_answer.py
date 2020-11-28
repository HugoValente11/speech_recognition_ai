import time
from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys


class Fetcher:
    def __init__(self, url):
        self.driver = webdriver.Edge()
        self.driver.wait = WebDriverWait(self.driver, 5)
        self.url = url

    def lookup(self):
        self.driver.get(self.url)
        try:
            ip = self.driver.wait.until(EC.presence_of_element_located(
                (By.CLASS_NAME, "gsfi")
            ))
        except:
            print("Failed fetcher.")

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        with open("soup.html", "w+", encoding="utf-8") as f:
            f.write(str(soup))
            f.close()
        self.driver.quit()

        answer = soup.find_all(class_="_sPg")

        if not answer:
            answer = soup.find_all(class_="_XWk")

        if not answer:
            answer = soup.find_all(class_="hgKElc")

        if not answer:
            answer = ["I don't know what you asked."]

        return answer[0]
