import utils
import sys
from moviepy.editor import *


class clip:
    """
    Simple clip class to get stuff organized
    """

    def __init__(self, title, url, author, index, path):
        self.title = title
        self.url = url
        self.author = author
        self.index = index
        self.path = path


def get_clips(subreddit, maxPosts):
    posts = utils.get_posts(subreddit, maxPosts)
    clips = []

    # loop through the link posts and downloads from gfycat or imgur
    for index, post in enumerate(posts):

        print
        print "retrieving video #{0:0>3}".format(index + 1)
        if 'gfycat' in post.url:
            path = utils.gfycat_mp4(post.url, str(subreddit), index)
        elif 'imgur' in post.url:
            path = utils.imgur_mp4(post.url, str(subreddit), index)

        currentClip = clip(post.title, post.url, post.author, index + 1, path)
        clips.append(currentClip)

        if index + 1 >= maxPosts:
            print "All {} clips have been downloaded!\n".format(maxPosts)
            break
        print

    return clips


def edit_clips(clips, subreddit, maxPosts):
    paths = []
    for clip in clips:
        currClip = VideoFileClip(clip.path)
        currClip = vfx.resize(currClip, width=1280, height=720)
        paths.append(currClip)

    finalClip = concatenate_videoclips(paths)
    finalClip.write_videofile('Exports/{}_top{}.mp4'.format(subreddit, maxPosts), fps=24)


def main():
    subreddit = raw_input("Subreddit: ")
    maxPosts = 5
    print
    clips = get_clips(subreddit, maxPosts)
    edit_clips(clips, subreddit, maxPosts)

if __name__ == '__main__':
    main()
