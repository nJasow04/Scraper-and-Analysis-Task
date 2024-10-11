import csv
import requests
from bs4 import BeautifulSoup

def scrape_page(soup, posts):
    post_elements = soup.find_all('article', class_= "custom-blog-article-tile")
    
    for post_element in post_elements:
        post = {}
        post['title'] = post_element.find('h3').text.strip()
        post['date'] = post_element.find('time').text.strip()
        post['url'] = post_element.find('h3').find('a')['href']
        post['preview'] = post_element.find('p').text.strip()
        posts.append(post)

# Define grabbing the apps page
base_url = "https://communityforums.atmeta.com/t5/Announcements/bg-p/AnnouncementsBlog"

# Define valid Header
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
}

# retrieving the target web page
page = requests.get(base_url, headers=headers)

print("Page Retrieved")

# Parse webpage with BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')

# List to store all apps
posts = []

scrape_page(soup, posts)

print("Contents Scraped")

next_li_element = soup.find('li', class_='lia-paging-page-next').find('a')['href']

print("Next Page Found: ", next_li_element)

count = 2

# while next_li_element is not None:
#     next_page = requests.get(next_li_element, headers=headers, allow_redirects=False)
#     next_soup = BeautifulSoup(next_page.text, 'html.parser')
#     scrape_page(next_soup, posts)
    
#     next_li_element = next_soup.find('li', class_='lia-paging-page-next').find('a')['href']
    
#     print("count: ", count, "Next Page Found: ", next_li_element)
#     count += 1

while count < 9:
    next_page = requests.get(next_li_element, headers=headers, allow_redirects=False)
    next_soup = BeautifulSoup(next_page.text, 'html.parser')
    scrape_page(next_soup, posts)
    
    next_li_element = "https://communityforums.atmeta.com/t5/Announcements/bg-p/AnnouncementsBlog/page/" + str(count + 1)
    
    print("count: ", count, "Next Page Found: ", next_li_element)
    count += 1
    
   
print("All Pages Scraped")
    
# Write the data to a CSV file
forums_csv = open('meta-forums.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(forums_csv)
writer.writerow(['Title', 'Date', 'URL', 'Preview'])

# Writing data for each row
for post in posts:
    writer.writerow([post['title'], post['date'], post['url'], post['preview']])
                    

# Terminate operation
forums_csv.close()
