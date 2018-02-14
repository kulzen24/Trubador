trash code

try:
	#enterloc = WebDriverWait(driver, 10).until(
	#	EC.presence_of_element_located((By.XPATH, "//li/a[@class='nav-location location-search-trigger']"))
	#)
	#enterloc = driver.find_element_by_xpath("//li/a[@class='nav-location location-search-trigger']")
	enterloc = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.XPATH, "//body"))
	)
	for i in range(1,8):
		enterloc.send_keys(Keys.TAB)
	enterloc.send_keys("Los Angeles, CA")
	enterloc.send_keys(Keys.RETURN)
except:
	
	#submitloc = WebDriverWait(driver, 10).until(
	#	EC.presence_of_element_located((By.XPATH, "//li/a[@class='nav-search global-search-trigger']"))
	#)
	#submitloc = driver.find_element_by_xpath("//li/a[@class='nav-search global-search-trigger']")
	#submitloc.click()
	enterloc = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.XPATH, "//body"))
	)
	for i in range(1,8):
		enterloc.send_keys(Keys.TAB)
	enterloc.send_keys("Los Angeles, CA")
	enterloc.send_keys(Keys.RETURN)
finally:
	driver.quit()
	
# Windows users need to open the file using 'wb'
# csv_file = open('reviews.csv', 'wb')
#csv_file = open('axs_shows.csv', 'w', newline = '')
#writer = csv.writer(csv_file)
# Page index used to keep track of where we are.
#index = 1
# Initialize two variables refer to the next button on the current page and previous page.
#prev_button = None
#current_button = None
#while True:
#	try:
		# We first need to make sure the button on the previous page is not available anymore.
#		if prev_button is not None:
#			WebDriverWait(driver, 10).until(EC.staleness_of(prev_button))
#
#		print("Scraping Page number " + str(index))
#		index = index + 1
		# Find all the reviews on the page
#		wait_review = WebDriverWait(driver, 10)
#		reviews = wait_review.until(EC.presence_of_all_elements_located((By.XPATH,
#									'//li[@class="bv-content-item bv-content-top-review bv-content-review"]')))
#		for review in reviews:
			# Initialize an empty dictionary for each review
#			review_dict = {}
			# Use relative xpath to locate the title, content, username, date.
			# Once you locate the element, you can use 'element.text' to return its string.
			# To get the attribute instead of the text of each element, use 'element.get_attribute()'
#			title = review.find_element_by_xpath('.//h4[@class="bv-content-title"]').text
			# There might be multiple paragraphs, so you use find elements instead of find element.
#			content = review.find_elements_by_xpath('.//div[@class="bv-content-summary-body-text"]/p')
#			content = ''.join(map(lambda x: x.text, content))
#			username = review.find_element_by_xpath('.//h3[@class="bv-author"]').text
#			date = review.find_element_by_xpath('.//meta[@itemprop="datePublished"]').get_attribute('content')
#			rating = review.find_element_by_xpath('.//span[@class="bv-rating-stars-container"]/span').text
#			rating = re.search('\d+', rating).group()

#			review_dict['title'] = title
#			review_dict['content'] = content
#			review_dict['username'] = username
#			review_dict['date'] = date
#			review_dict['rating'] = rating
#			writer.writerow(review_dict.values())

		# Locate the next button on the page.
#		wait_button = WebDriverWait(driver, 10)
#		current_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,
#									'//li[@class="bv-content-pagination-buttons-item bv-content-pagination-buttons-item-next"]')))
#		prev_button = current_button
#		current_button.click()
#except Exception as e:
#print(e)
#		csv_file.close()
#driver.close()
#break

#calm = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//body"))

//*[@id="page-relative-block"]/div/div[2]/div/div/div[2]/div/div[2]/div/a

[contains(@href,"com"]

enterloc = WebDriverWait(driver, 20).until(
		EC.presence_of_element_located((By.XPATH, "//div[@class='nav-item-container']/ul/li[@class=nav-location location-search-trigger]"))
	)
	
#testing ability to scroll page
#scroll = browser.find_element_by_css_selector('body')
#calm = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//html")))

#submitloc = driver.find_element_by_xpath('//button[@class="new-modal__search-btn"]').click()
#submitloc
#enterloc.send_keys(Keys.RETURN)

#driver.implicitly_wait(10)


#was testing below but don't think it's necessary. Selenium should just be able to snatch all of the data by XPATH now in a single for loop
#height = driver.execute_script("document.body.scrollHeight")
#print(height)

#scroll.send_keys(Keys.HOME) #before loop to reposition to top of page
#loop while i < height
#end of each loop execution sets i = to current position

#test code to ensure that page can be scrolled
#scroll.send_keys(Keys.END)
#time.sleep(10)
#scroll.send_keys(Keys.HOME)