from selenium import webdriver
from selenium.common.exceptions import TimeoutException

def search_google(search_text):
	# Start Chrome browser
	browser = driver = webdriver.Chrome("C:\\bin\\chromedriver.exe")
	# Go to Google search page
	browser.get('https://www.google.com')
	# Find search field and search text
	search = browser.find_element_by_name('q')
	search.send_keys(search_text)
	search.submit()

def main(search_text):
	search_google(search_text)


if __name__ == '__main__':
	main("search text")