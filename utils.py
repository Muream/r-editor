import requests
from bs4 import BeautifulSoup
import urllib
import os
import math
import praw

USERAGENT = "(r)editor v1.0 by /u/Muream"
r = praw.Reddit(user_agent=USERAGENT)


def check_dir(subreddit):
    """
    creates a directory to download the videos from the subreddit
    """
    directory = os.path.join(os.path.dirname(__file__), 'Downloads/{}'.format(subreddit))
    directory = directory.replace('\\', '/')
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


def round_up(x):
    return int(math.ceil(x / 100.0)) * 100


def get_posts(subreddit, maxPosts):
    retrievePosts = round_up(maxPosts)
    subreddit = r.get_subreddit(subreddit)
    print "Retrieving posts..."
    posts = subreddit.get_top_from_all(limit=retrievePosts)
    linkPosts = []

    # Flush the text posts
    for post in posts:
        if not post.is_self:
            linkPosts.append(post)

    if len(linkPosts) < maxPosts:
        print
        print len(linkPosts), maxPosts
        retrievePosts += 100
        print "Didn't get enough posts, retrieving more..."
        print
        posts = subreddit.get_top_from_all(limit=retrievePosts)

    return linkPosts


def download_link(fileUrl, subreddit, index):
    directory = check_dir(subreddit)
    fileName = subreddit + '_{0:0>3}'.format(index + 1) + '.' + fileUrl.split('.')[-1]
    path = directory + '/' + fileName
    urllib.urlretrieve(fileUrl, directory + '/' + fileName)
    return path

def get_gfycat_mp4(url, subreddit, index):
    """
    get the link of the mp4 from gfycat
    """
    print "Downloading file {0:0>3} from gfycat...".format(index + 1)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # finds all the .mp4 files in the page
    sources = soup.find_all('source', {"id": "mp4Source"})
    if len(sources) == 1:
        fileUrl = sources[0]['src']
    elif len(sources) == 0:
        return None
    else:
        print "Got more Urls than expected, downloading the first one"
        fileUrl = sources[0]['src']

    return fileUrl


def get_imgur_mp4(url, subreddit, index):
    """
    get the link of the mp4 from imgur
    """
    print "Downloading file {0:0>3} from imgur...".format(index + 1)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # finds all the .mp4 files in the page
    sources = soup.find_all('source', {"type": "video/mp4"})
    if len(sources) == 1:
        fileUrl = sources[0]['src']
    elif len(sources) == 0:
        return None
    else:
        print "Got more Urls than expected, downloading the first one"
        fileUrl = sources[0]['src']

    return fileUrl
