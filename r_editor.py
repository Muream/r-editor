import praw
import urllib
import wget
import urllib2


USERAGENT = "(r)editor v1.0 by /u/Muream"
MAXPOSTS = 5

r = praw.Reddit(user_agent = USERAGENT)

def run_bot(subreddit):
    subreddit = r.get_subreddit(subreddit)
    posts = subreddit.get_top_from_all(limit=MAXPOSTS)
    i=1
    for post in posts:
        print "post {0:0>3}: ".format(i) + str(post.title)
        print "     url: {} ".format(str(post.url))
        print "  author: /u/{} ".format(str(post.author))
        print

        url = post.url
        fileName = url.split('/')[-1]
        urllib.urlretrieve (url, fileName)


        i += 1

# Main method
def main():
    subreddit = raw_input("Subreddit: ")
    print
    run_bot(subreddit)

if __name__ == '__main__':
    main()

