import praw
import downloadUtils
import sys


USERAGENT = "(r)editor v1.0 by /u/Muream"
limitPosts = 100

r = praw.Reddit(user_agent=USERAGENT)


class clip(praw.objects.Submission):
    """
    The clip class, inherited from the Submission class of Praw (not sure if it's the right one)
    """
    def __init__(self, path):
        self.path = path

    def download_video(self):



def run_bot(subreddit, maxPosts):
    subreddit = r.get_subreddit(subreddit)
    posts = subreddit.get_top_from_all(limit=limitPosts)
    linkPosts = []
    clips = []
    # Flush the text posts
    for post in posts:
        if not post.is_self:
            linkPosts.append(post)

    # loop through the link posts
    for index, post in enumerate(linkPosts):

        # FIXME: Some titles seem to have encoding problems
        # print type(post.title)
        # name = "post {0:0>3}: ".format(index + 1) + str(post.title)
        print "     url: {} ".format(str(post.url))
        print "  author: /u/{} ".format(str(post.author))

        # if link is a gfycat link : Download the mp4
        if 'gfycat' in post.url:
            print "gfycat link"
            directory = downloadUtils.gfycat_mp4(post.url, str(subreddit), index)
        elif 'imgur' in post.url:
            print "imgur link"
            directory = downloadUtils.imgur_mp4(post.url, str(subreddit), index)

        if index + 1 > maxPosts:
            break
        print

        return clips


def main():
    subreddit = raw_input("Subreddit: ")
    print
    run_bot(subreddit, 5)

if __name__ == '__main__':
    main()
