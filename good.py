import re
import urllib
from bs4 import BeautifulSoup

# The URL that should be opened
url = input("Please enter a URL\n")

# The term to search for in the link text
search = input("Please enter a search term\n")


def search():
    html = urllib.request.urlopen(url)
    data = BeautifulSoup(html, features="lxml")
    links = data.findAll('a')

    for link in [
            link for link in links if re.search(search_term, link.text, re.I)
    ]:
        print(f'Link Text: {link["href"]}')
        print(f"Link Destination: {link.text}\n")


search()
