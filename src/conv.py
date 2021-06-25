"Takes channel link and returns RSS link"

#import requests

def convert_link(link):
    "Takes a youtube channel link as an argument and returns the RSS link for that channel"
    #try:
    #    #Gets HTML of youtube channel, then finds RSS link
    #    page = requests.get(link).text
    #    print("Here")
    #    identifier = "<link rel=\"alternate\" type=\"application/rss+xml\" title=\"RSS\" href=\""
    #    page = page[page.find(identifier):][67:143]
    #
    #    #Checks if link has been found
    #    if page[:8] == "https://":
    #        return page
    #    return "Failed, possibly incorrect link?"
    #
    #except:
    #    return "Failed, not a URL"

    youtube = "youtube.com/channel/"
    if(link.find(youtube) == -1):
        return "Not a correct youtube URL. Must contain " + youtube
    else:
        link = link.split(youtube)[-1]
        return "https://www.youtube.com/feeds/videos.xml?channel_id=" + link

def mass_convert(links, length):
    "Convert and print multiple links"
    for i in range(length):
        print(convert_link(links[i]))
