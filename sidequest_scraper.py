from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

import csv

# Path to driver
driver_path = '/Users/jasonwan/Code/YuanTian Lab/Start Scraper Lab/chromedriver-mac-arm64/chromedriver'

# Setting up webdriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Open the target webpage
driver.get('https://sidequestvr.com/category/all')


scrollable_div = driver.find_element(By.CSS_SELECTOR, '.content')


# Initialize variables
SCROLL_PAUSE_TIME = 3  # Reduced pause time to minimize content unloading
scroll_step = 1000      # Pixels to scroll each time
max_count = 1000       # Max number of scroll increments
links = set()          # Use a set to store unique links
count = 0              # Scroll iteration counter

# Get initial scroll height
last_scroll_height = driver.execute_script("return arguments[0].scrollHeight;", scrollable_div)
current_scroll_position = 0

# **Collect links before scrolling**
cards = driver.find_elements(By.CSS_SELECTOR, '.virtual-scroller__card-wrapper a')
for card in cards:
    link = card.get_attribute('href')
    if link:
        links.add(link)

# Start scrolling in increments
while count < max_count:
    # Scroll down by 'scroll_step' pixels
    current_scroll_position += scroll_step
    driver.execute_script("arguments[0].scrollTop = arguments[1];", scrollable_div, current_scroll_position)

    # Wait for new content to load
    time.sleep(SCROLL_PAUSE_TIME)

    # Collect links at current scroll position
    cards = driver.find_elements(By.CSS_SELECTOR, '.virtual-scroller__card-wrapper a')
    for card in cards:
        link = card.get_attribute('href')
        if link:
            links.add(link)
            
    if len(links) >= 150:
        break

    # Check if we've reached the bottom
    new_scroll_height = driver.execute_script("return arguments[0].scrollHeight;", scrollable_div)
    if current_scroll_position >= new_scroll_height:
        break  # Exit loop if we've scrolled past the total height

    # Update last scroll height
    last_scroll_height = new_scroll_height
    count += 1

# Convert the set to a list and print the links
links = list(links)
for link in links:
    print(link)
    
print(len(links))


# Set up CSV File
csv_file = open('sidequest_reviews_final.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Game Title', 'Game Link', 'Review Text', 'Review Rating'])




for link in links:
    driver.get(link)
    time.sleep(4)

    # Scroll to the reviews section if necessary
    driver.execute_script("window.scrollBy(0, 500);")  # Adjust as needed

    # Extract the game title
    try:
        game_title_element = driver.find_element(By.CSS_SELECTOR, 'mat-card-title.mat-card-title:not(.post-body)')
        game_title = game_title_element.text.strip()
    except Exception as e:
        print(f"Failed to get game title for {link}: {e}")
        continue

    # Wait for the reviews to load
    # time.sleep(2)

    try:
        reviews = driver.find_elements(By.CSS_SELECTOR, 'mat-card-title.post-body')
        ratings = driver.find_elements(By.CSS_SELECTOR, 'div.star-container.flex.align-center')
    except Exception as e:
        print(f"Failed to get reviews for {link}: {e}")
        reviews = []
        ratings = []
    
    
    # Handle the case where there are no reviews or ratings
    if not reviews or not ratings:
        # Write a single entry with "N/A" for both review and rating
        csv_writer.writerow([game_title, link, "N/A", "N/A"])
        print(f"No reviews found for {game_title}. Added N/A entry.")
    else:
        for review_elem, rating_elem in zip(reviews, ratings):
            review_text = review_elem.text.strip()
            rating_text = rating_elem.text.strip()
            
            # Clean up rating text to extract the numeric value
            rating_value = ''.join(filter(str.isdigit, rating_text))
            
            # Write the data to the CSV file
            csv_writer.writerow([game_title, link, review_text, rating_value])
            print(f"Saved review for {game_title}")

# Close resources
csv_file.close()
driver.quit()