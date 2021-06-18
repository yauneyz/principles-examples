import re
import urllib
from bs4 import BeautifulSoup

# The URL that should be opened
url = input("Please enter a URL\n")

# The term to search for in the link text
search_term = input("Please enter a search term\n")

# Add one more line to nicely separate out the future output
print("\n")


def search():
    # Get the HTML data and create the soup
    html = urllib.request.urlopen(url)
    data = BeautifulSoup(html, features="lxml")

    # Get all the links on the page
    links = data.findAll('a')

    # Filter the links
    links = filter(lambda x: re.search(search_term, x.text), links)

    # Turn the filtered links into a string
    answer = map(
        lambda x: f"Link Text: {x.text}\nLink Destination: {x['href']}\n",
        links)

    # Print the string
    print("Results:\n" + "\n".join(answer))


search()
