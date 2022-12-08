from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_capabilities = DesiredCapabilities.FIREFOX.copy()
desired_capabilities['acceptInsecureCerts'] = True

driver = webdriver.Firefox(capabilities=desired_capabilities)
driver.get('https://url')
print(driver.title)
driver.close()