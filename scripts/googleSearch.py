from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options


def search_google(search_text):
	print("Googling... " + search_text)
	try:
		# Start Chrome browser
		chrome_options = Options()
		chrome_options.add_experimental_option("detach", True)
		browser = driver = webdriver.Chrome("C:\\bin\\chromedriver.exe", options = chrome_options)
		# Go to Google search page
		browser.get('https://www.google.com')
		# Find search field and search text
		search = browser.find_element_by_name('q')
		search.send_keys(search_text)
		search.submit()
	except TimeoutException:
		print(TimeoutException)
	except:
		print("Unknown error. Try again later")


def main(search_text):
	search_google(search_text)


if __name__ == '__main__':
	main("python")
	