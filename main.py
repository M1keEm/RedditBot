import praw

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("learnpython")

# to verify whether the instance is authorized instance or not
print(reddit.read_only)

subreddit = reddit.subreddit('GRE')

# display the subreddit name
print(subreddit.display_name)

# display the subreddit title
print(subreddit.title)

# display the subreddit description
print(subreddit.description)
