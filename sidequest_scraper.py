import csv
import requests
from bs4 import BeautifulSoup

# def scrape_page(soup, )

# Define grabbing the apps page
base_url = "https://sidequestvr.com/category/all"

# Define valid Header
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
}

# retrieving the target web page
page = requests.get(base_url, headers=headers)

# Parse webpage with BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')

# List to store all apps
apps = []

