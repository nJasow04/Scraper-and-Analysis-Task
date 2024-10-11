from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# Replace with the path to your WebDriver
# driver_path = '/chromedriver-mac-arm64/chromedriver'
driver_path = '/Users/jasonwan/Code/YuanTian Lab/Start Scraper Lab/chromedriver-mac-arm64/chromedriver'

service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Open the target webpage
driver.get('https://sidequestvr.com/category/all')


scrollable_div = driver.find_element(By.CSS_SELECTOR, '.content')

# Get initial height of the page
# last_height = driver.execute_script("return document.body.scrollHeight")
last_height = driver.execute_script("return arguments[0].scrollHeight;", scrollable_div)


# Infinite scroll to load all the cards
SCROLL_PAUSE_TIME = 5  # Adjust this if the page is slower to load content

count = 0
max_count = 10

# # Scroll down to the bottom to load all sidequest apps
# while count < max_count:
#     # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", scrollable_div)

#     # Wait for new content to load
#     time.sleep(SCROLL_PAUSE_TIME)
    
#     # Calculate new scroll height and compare with the last height
#     # new_height = driver.execute_script("return document.body.scrollHeight")
#     new_height = driver.execute_script("return arguments[0].scrollHeight;", scrollable_div)
    
#     if new_height == last_height:
#         break  # If heights are the same, the content has stopped loading
#     last_height = new_height
#     count += 1

# # Now, find all the cards and extract href links
# cards = driver.find_elements(By.CSS_SELECTOR, '.virtual-scroller__card-wrapper a')
# links = [card.get_attribute('href') for card in cards]

# # Print or store the extracted links
# for link in links:
#     print(link)

# Initialize a set to store unique links
links = set()

while count < max_count:
    # Scroll to the bottom of the scrollable element
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", scrollable_div)

    # Wait for new content to load
    time.sleep(SCROLL_PAUSE_TIME)
    
    # Find all the cards currently in the DOM and extract href links
    cards = driver.find_elements(By.CSS_SELECTOR, '.virtual-scroller__card-wrapper a')
    for card in cards:
        link = card.get_attribute('href')
        if link:
            links.add(link)  # Add the link to the set to avoid duplicates

    # Calculate new scroll height and compare with the last height
    new_height = driver.execute_script("return arguments[0].scrollHeight;", scrollable_div)
    
    if new_height == last_height:
        break  # If heights are the same, the content has stopped loading
    
    last_height = new_height
    count += 1

# Convert the set to a list if needed
links = list(links)

for link in links:
    print(link)

# Close the driver after scraping
driver.quit()