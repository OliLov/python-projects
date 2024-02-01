"""Web scraper."""
import requests
from bs4 import BeautifulSoup

# Define URL.
URL = "https://medium.com/@oliver.lovstrom"

# Send a GET request to the URL.
response = requests.get(URL, timeout=120)

# Parse the HTML content of the page using BeautifulSoup.
soup = BeautifulSoup(response.text, "html.parser")

# Extract and print the title of the page.
title = soup.find("title").text
print(title)
