from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import re
import functools #for reduce_concat function
import datetime #for csv file title

now = datetime.datetime.now() #for csv file title

#For csv file names (testing)
def reduce_concat(x, sep=""):
	return functools.reduce(lambda x, y: str(x) + sep + str(y), x)
	
def paste(*lists, sep=" ", collapse=None):
	result = map(lambda x: reduce_concat(x, sep=sep), zip(*lists))
	if collapse is not None:
		return reduce_concat(result, sep=collapse)
	return list(result)
	
def writeevents(events, writer, driver):
	for i in range(1, len(events)):
		#dictionary to store event data
		event_dict = {}
		
		#set event data equal to html elements
		link = events[i].find_element_by_xpath('./div/a')
		sale_url = link.get_attribute('href')
		month = events[i].find_element_by_xpath('./div/a/div[1]/div/div[1]').text
		day = events[i].find_element_by_xpath('./div/a/div[1]/div/div[2]').text
		weekday = events[i].find_element_by_xpath('./div/a/div[1]/div/div[3]').text
		performer = events[i].find_element_by_xpath('./div/a/div[2]/div[1]').text
		venue = events[i].find_element_by_xpath('./div/a/div[2]/div[2]/span[1]').text
		city = events[i].find_element_by_xpath('./div/a/div[2]/div[2]/span[2]').text
		time.sleep(0.5)
		
		#navigate to a new page for time and price
		driver.get(sale_url)
		new_page_wait = wait_event.until(EC.presence_of_all_elements_located((By.XPATH,
							'//body')))
		hour = driver.find_element_by_xpath('//section[@id="event-info-section"]/div[2]/div[2]/span[1]').text
		price = driver.find_element_by_xpath('//section[@id="event-ticket-options"]/div/div[2]/div').text
		time.sleep(2)
		driver.back()
		
		#write variables to dictionary
		event_dict['sale_url'] = sale_url
		event_dict['month'] = month
		event_dict['day'] = day
		event_dict['weekday'] = weekday
		event_dict['performer'] = performer
		event_dict['venue'] = venue
		event_dict['city'] = city
		event_dict['time'] = hour
		event_dict['price'] = price
		
		#ensure accurate data collection
		print(i)
		i
		print(event_dict)
		event_dict
		
		#write event to CSV
		writer.writerow(event_dict.values())
		
		calm = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//html"))) #if elements aren't available it will return a timeout error and alert user that script must be altered
		time.sleep(3)
		lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
		match=False

		while(match==False):
			lastCount = lenOfPage
			time.sleep(random.uniform(2, 3.5))
			lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
			if lastCount==lenOfPage:
				match=True

		scroll = driver.find_element_by_xpath('//html')
		time.sleep(2)
		scroll.send_keys(Keys.HOME)
		time.sleep(2)
		
		scrollerArg = paste(["window.scrollTo(0, "], [newPos], [");"], sep = '')
		scrollerArg = ''.join(scrollerArg)
		scroller = driver.execute_script(scrollerArg)
		events = wait_event.until(EC.presence_of_all_elements_located((By.XPATH,
					'//div[@class="results-table results-table--events"]')))

#Initiate Chrome Driver and ignore certificate errors
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.axs.com/browse/music")
#actionChains = webdriver.ActionChains(driver)

#give the website time to load
time.sleep(5)
driver.maximize_window()

#Wait for JavaScript to appear before entering location
enterloc = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//body")))
time.sleep(5)

#Navigate to input for location and enter city name
enterloc = driver.find_element_by_xpath('//div[@class="nav-item-container"]/ul/li/a[@class="nav-location location-search-trigger"]')
enterloc.click()
time.sleep(1.5)
typeloc = driver.find_element_by_xpath('//div/input[@class="location-search__form-input"]')

#Type the string more slowly to avoid detection
keysender = "New York City, NY"
keysender.split()
for i in keysender:
	typeloc.send_keys(i)
	time.sleep(0.1)
	typeloc.send_keys(Keys.END)
	time.sleep(0.1)
time.sleep(2)
typeloc.send_keys(Keys.ENTER)
time.sleep(3)
							
#scroll to end of page so that all elements are visible
calm = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//html"))) #if elements aren't available it will return a timeout error and alert user that script must be altered
time.sleep(3)
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False

while(match==False):
	lastCount = lenOfPage
	time.sleep(random.uniform(2.0, 3.5))
	lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
	if lastCount==lenOfPage:
		match=True

scroll = driver.find_element_by_xpath('//html')
time.sleep(2)
scroll.send_keys(Keys.HOME)
time.sleep(2)

#Open CSV Writer
filename = paste(['axs_events_'], [now.year], ['-'], [now.month], ['-'], [now.day],['.csv'], sep='')
filename = ''.join(filename)
csv_file = open(filename, 'w', newline = '')
writer = csv.writer(csv_file)

#collect html tags, this will need to go inside of the nested loop function
wait_event = WebDriverWait(driver, 10)
events = wait_event.until(EC.presence_of_all_elements_located((By.XPATH,
							'//div[@class="results-table results-table--events"]')))

newPos = 0
while (newPos <= lenOfPage):
	print('Number of events:', len(events))
	print('position pre-loop:', newPos) #for testing
	writeevents(events, writer, driver)
	offprep = paste(["var offprep = window.screen.height * "], [(len(events))/8], [";return offprep"], sep='') #7 fit on a page, giving myself room for error
	offprep = ''.join(offprep)
	offset = driver.execute_script(offprep)
	newPos = newPos + offset
	scrollerArg = paste(["window.scrollTo(0, "], [newPos], [");"], sep = '')
	scrollerArg = ''.join(scrollerArg)
	scroller = driver.execute_script(scrollerArg)
	events = wait_event.until(EC.presence_of_all_elements_located((By.XPATH,
				'//div[@class="results-table results-table--events"]')))
	print('Number of events:', len(events)) #testing
	print('current position:', newPos) #testing
print('Complete.')
csv_file.close()
driver.close()


#mutate required in pandas to create a full date column (month, day, year)
#clean up start time and price in pandas
#mutate required in pandas to split performers and clean up performer names