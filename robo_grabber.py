from selenium import webdriver
import sys

options = webdriver.FirefoxOptions()
options.add_argument('--headless')

driver = webdriver.Firefox(options=options)

url = sys.argv[1]

driver.get(url)
print(driver.find_element_by_xpath("//*[@id='robots_txt']").text)
driver.quit()
