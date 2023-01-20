from selenium import webdriver
import sys

options = webdriver.FirefoxOptions()
options.add_argument('--headless')

driver = webdriver.Firefox(options=options)

url = sys.argv[1]

driver.get(url)
try:
    robots_txt = driver.find_element_by_xpath("//*[@id='robots_txt']")
    print(robots_txt.text)
except Exception as e:
    print("robots.txt not found.")
driver.quit()
