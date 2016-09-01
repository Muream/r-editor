import requests
from bs4 import BeautifulSoup
import urllib
import os


def check_dir(subreddit):
    directory = os.path.join(os.path.dirname(__file__), 'Downloads/{}'.format(subreddit))
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


def gfycat_mp4(url, subreddit, index):
    print "Downloading from gfycat..."
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    directory = check_dir(subreddit)

    # finds all the .mp4 files in the page
    for source in soup.find_all('source', {"id": "mp4Source"}):
        fileUrl = source['src']

        fileName = subreddit + '_{0:0>3}'.format(index + 1) + '.' + fileUrl.split('.')[-1]
        urllib.urlretrieve(fileUrl, directory + '/' + fileName)

    return directory


def imgur_mp4(url, subreddit, index):
    # find <source src="//i.imgur.com/G6j4BBF.mp4" type="video/mp4">
    print "Downloading from imgur..."
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    directory = check_dir(subreddit)

    for source in soup.find_all('source', {"type": "video/mp4"}):
        fileUrl = "https:{}".format(source['src'])
        print fileUrl
        fileName = subreddit + '_{0:0>3}'.format(index + 1) + '.' + fileUrl.split('.')[-1]
        urllib.urlretrieve(fileUrl, directory + '/' + fileName)

    return directory

if __name__ == '__main__':
    imgur_mp4('http://i.imgur.com/G6j4BBF.gifv', 'overwatch', 1)
