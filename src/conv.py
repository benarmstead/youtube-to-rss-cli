"Converts the link and prints it"

import requests

def convert(link):
    "Converts the channel URL to the RSS URL by scraping the channel URL and extracting the RSS URL"
    
    try:
        page = requests.get(link).text
        identifier = "<link rel=\"alternate\" type=\"application/rss+xml\" title=\"RSS\" href=\""
        return page[page.find(identifier):][67:143]

    except:
        return "Not a URL"


def mass_convert(links, length):
    "Convert and print multiple links"

    for i in range(length):
        print(convert(links[i]))
