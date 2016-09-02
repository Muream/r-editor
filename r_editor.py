import praw
import utils
import sys


# class clip(praw.objects.Submission):
#     """
#     The clip class, inherited from the Submission class of Praw
#     (not sure if it's the right one)
#     """
#     def __init__(self, path):
#         self.path = path


def run_bot(subreddit, maxPosts):
    posts = utils.get_posts(subreddit, maxPosts)
    clips = []

    # loop through the link posts
    for index, post in enumerate(posts):

        # FIXME: Some titles seem to have encoding problems
        # print type(post.title)
        # name = "post {0:0>3}: ".format(index + 1) + str(post.title)

        print index + 1
        print "url: {} ".format(str(post.url))
        print "author: /u/{} ".format(str(post.author))

        # if link is a gfycat link : Download the mp4
        # if 'gfycat' in post.url:
        #     print "gfycat link"
        #     directory = downloadUtils.gfycat_mp4(post.url, str(subreddit), index)
        # elif 'imgur' in post.url:
        #     print "imgur link"
        #     directory = downloadUtils.imgur_mp4(post.url, str(subreddit), index)

        if index + 1 >= maxPosts:
            print "break"
            break
        print

    return clips


def main():
    subreddit = raw_input("Subreddit: ")
    print
    run_bot(subreddit, 5)

if __name__ == '__main__':
    main()
