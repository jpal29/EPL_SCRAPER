from selenium import webdriver


def create_driver():
    options = webdriver.ChromeOptions()
    options.binary_location = '/usr/local/bin/chromedriver'
    options.add_argument('window-size=800x841')
    options.add_argument('headless')
    driver = webdriver.Chrome(options.binary_location)
    return driver