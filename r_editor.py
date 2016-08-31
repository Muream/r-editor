import praw
import downloadUtils
import sys


USERAGENT = "(r)editor v1.0 by /u/Muream"
limitPosts = 100

r = praw.Reddit(user_agent=USERAGENT)


def run_bot(subreddit, maxPosts):
    subreddit = r.get_subreddit(subreddit)
    posts = subreddit.get_top_from_all(limit=limitPosts)
    linkPosts = []

    # Flush the text posts
    for post in posts:
        if not post.is_self:
            linkPosts.append(post)

    # loop through the link posts
    for index, post in enumerate(linkPosts):
        print type(post.title)
        print "post {0:0>3}: ".format(index + 1) + str(post.title)
        print "     url: {} ".format(str(post.url))
        print "  author: /u/{} ".format(str(post.author))

        # if link is a gfycat link : Download the mp4
        # if 'gfycat' in post.url:
        #     downloadUtils.gfycat_mp4(post.url, str(subreddit), index)

        if index + 1 > maxPosts:
            break
        print


def main():
    subreddit = raw_input("Subreddit: ")
    print
    run_bot(subreddit, 100)

if __name__ == '__main__':
    main()
