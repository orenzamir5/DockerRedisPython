# Imports
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

# Set selenium chrome driver
chromedriver_path = '/Users/orenz/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=chromedriver_path)

# Go to site
driver.get('http://192.168.99.100:5000')

# Print body
element = driver.find_element_by_tag_name('body')
print(element.text)

driver.close()