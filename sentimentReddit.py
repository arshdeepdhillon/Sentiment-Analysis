import praw
from textblob import TextBlob
import math


# obtain authentication


# setup API call to reddit
reddit = praw.Reddit(client_id='qNTP2_GctGNpOw', client_secret="dmFBzbXT5LkH9ym_Q7oTDQCf9CI", password='cpsc571',  
                        user_agent='Doing Sentiment magic from some scary subs', username='sentimeplz')


subreddit = reddit.subreddit('python')
hotPython = subreddit.hot(limit=2)

for submission in hotPython:
    if not submission.stickied:
        print('Title ===> ' + submission.title)
        comments = submission.comments
        for comment in comments:
            # print(20*'-')
            print(comment.body)




















# import datetime
# sTimeStamp = datetime.datetime(2010, 12, 1, 0, 0).timestamp()
# eTimeStamp = datetime.datetime(2018, 12, 1, 0, 0).timestamp()

# analyze sentiment
# with open("C:\\Users\\arshdeep.dhillon1\\Desktop\\cpsc571\\Practice Code\\Sentiment-Analysis\\sb.txt","r") as f:

#     for line in f:
#         subreddit = reddit.subreddit(line.strip())
#         # prep for sentiment analysis
#         subSentiment, nComments = 0,0

#         # for submission in subSubmissions:
#         for submission in subreddit.stream.submissions():
#             # if its not a sticky submission (pinned at thr top) then grab the rest 
#             if not submission.stickied:
#                 submission.comments.replace_more(limit=2)

#                 # prep for sentiment analysis
#                 for comment in submission.comments.list():

#                     print(comment.body)

#                     blob = TextBlob(comment.body)
                    
#                     # this will return a tuple that contains (polarity, subjectivity)
#                     # subjectivity score: [0.0, 1.0], 0.0 => very objective and 1.0 => very subjective
#                     # polarity score:     [-1.0, 1.0]
#                     commentSentiment = blob.sentiment.polarity

#                     # this will be used on each relative subreddit by taking the total number of comments
#                     subSentiment += commentSentiment
#                     nComments += 1 
#         print("/r/" + str(subreddit.display_name))
#         try:
#             print("Ratio: " + str(math.floor(subSentiment/nComments * 100)) + "\n")
#         except:
#             print("Unable to calculate sentiment of each subreddit")