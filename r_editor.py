import praw


user_agent = "(r)editor v1.0 by /u/Muream"
r = praw.Reddit(user_agent = user_agent)

def run_bot(subreddit):
    subreddit = r.get_subreddit(subreddit)
    posts = subreddit.get_top(limit=25)
    i=1
    for post in posts:
        print "post {}: ".format(i) + str(post)
        i += 1

# Main method
def main():
    subreddit = raw_input("Subreddit: ")
    run_bot(subreddit)

if __name__ == '__main__':
    main()
