import requests
from bs4 import BeautifulSoup
import urllib
import os


def gfycat_mp4(url, subreddit, index):
    print "Downloading..."
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    directory = os.path.join(os.path.dirname(__file__), 'Downloads/{}'.format(subreddit))
    if not os.path.exists(directory):
        os.makedirs(directory)

    # finds all the .mp4 files in the page
    for source in soup.find_all('source', {"id": "mp4Source"}):
        fileUrl = source['src']

        fileName = subreddit + '_{0:0>3}'.format(index + 1) + '.' + fileUrl.split('.')[-1]
        urllib.urlretrieve(fileUrl, directory + '/' + fileName)


if __name__ == '__main__':
    gfycat_download('https://gfycat.com/FarawayLinedDouglasfirbarkbeetle', 'overwatch')
