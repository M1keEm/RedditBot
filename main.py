#!/usr/bin/python
import os
import re
import praw

# Create the Reddit instance
reddit = praw.Reddit('bot1')

# and login
# reddit.login(REDDIT_USERNAME, REDDIT_PASS)

# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

# Get the top 5 values from our subreddit
subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=5):
    # print(submission.title)

    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:

        # Do a case insensitive search
        if re.search("i love python", submission.title, re.IGNORECASE):
            # Reply to the post
            submission.reply("Manual bot test")
            print("Bot replying to : ", submission.title)
            print("Bot replying to url: ", submission.url)
            print("Bot replying to id: ", submission.id)
            print("Bot replying to author: ", submission.author)
            print("Bot replying to author id: ", submission.author.id)
            print("Bot replying to author name: ", submission.author.name)
            print("Bot replying to author fullname: ", submission.author.fullname)
            print("Text:", submission.selftext)
            print("Score:", submission.score)
            # Store the current id into our list
            posts_replied_to.append(submission.id)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
