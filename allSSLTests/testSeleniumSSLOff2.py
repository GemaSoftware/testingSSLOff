from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get('https://127.0.0.1:5000/')

