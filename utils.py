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


def get_posts(subreddit, sorting, time, maxPosts):
    retrievePosts = round_up(maxPosts)
    subreddit = r.get_subreddit(subreddit)
    print "Retrieving posts..."
    print
    if sorting == "Hot":
        print "Hot !"
        posts = subreddit.get_hot(limit=retrievePosts)
    elif sorting == "New":
        print "New !"
        posts = subreddit.get_new(limit=retrievePosts)
    elif sorting == "Rising":
        print "Rising !"
        posts = subreddit.get_rising(limit=retrievePosts)
    elif sorting == "Top":
        print "Top !"
        if time == "Hour":
            print "Hour !"
            posts = subreddit.get_top_from_hour(limit=retrievePosts)
        elif time == "Day":
            print "Day !"
            posts = subreddit.get_top_from_day(limit=retrievePosts)
        elif time == "Week":
            print "Week !"
            posts = subreddit.get_top_from_week(limit=retrievePosts)
        elif time == "Month":
            print "Month !"
            posts = subreddit.get_top_from_month(limit=retrievePosts)
        elif time == "All Time":
            print "All Time !"
            posts = subreddit.get_top_from_all(limit=retrievePosts)

    linkPosts = []

    # Flush the text posts and non downloadable links
    print "flushing unusable posts..."
    print "this might take some time..."
    for post in posts:
        if not post.is_self:
            if 'gfycat' in post.url:
                url = get_gfycat_mp4(post.url, str(subreddit))
            elif 'imgur' in post.url:
                url = get_imgur_mp4(post.url, str(subreddit))
            else:
                url = None
                print "Link not supported... skipping."
            if url is not None:
                linkPosts.append(post)
            else:
                print "post flushed"

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


def get_gfycat_mp4(url, subreddit):
    """
    get the link of the mp4 from gfycat
    """
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


def get_imgur_mp4(url, subreddit):
    """
    get the link of the mp4 from imgur
    """
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
