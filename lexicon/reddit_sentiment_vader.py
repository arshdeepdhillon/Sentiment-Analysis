import sys
sys.path.insert(0, '../extract_data')
import extract_reddit_comments as RDT

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import timeit



def getRedditData():
    rd = RDT.Extract()
    rd.getComments()

def VaderAnalysis():
    getRedditData()
    analyzer = SentimentIntensityAnalyzer()
    threshold = 0.09 # accuracy is good when threshold is close to 0.09
    nPosCorrect = 0
    nPosCount = 0

    # with open("comments_extracted/output.txt", "r") as f:
    with open("positive.txt", "r") as f:
        startP = timeit.default_timer()
        for line in f:

            vs = analyzer.polarity_scores(line)
            if not vs['neg'] > threshold:
                if vs['pos'] - vs['neg'] > 0:
                    nPosCorrect += 1
                nPosCount += 1
        stopP = timeit.default_timer()

    nNegCorrect = 0
    nNegCount = 0

    # with open("comments_extracted/output.txt", "r") as f:
    with open("negative.txt", "r") as f:
        startN = timeit.default_timer()
        for line in f:
            vs = analyzer.polarity_scores(line)
            if not vs['pos'] > threshold:
                if vs['pos'] - vs['neg'] <= 0:
                    nNegCorrect += 1
                nNegCount += 1
        stopN = timeit.default_timer()


    print("\nFinished in {:0.4f} sec".format(stopP-startP + stopP-startP))
    print("Positive " + percentage(nNegCorrect,nNegCount))
    print("Negative " + percentage(nPosCorrect,nPosCount))

    # plotting data
    import matplotlib.pyplot as plt

    # declare variables
    labels = 'Positive', 'Neutral'
    sizes = [nPosCorrect, nNegCorrect]
    colors = ['green', 'red']

    # using matplotlib to plot the data
    plt.pie(sizes, labels = labels, colors = colors, shadow = True, startangle = 90)
    strg = str("Sentiment of {} positives and {} negatives").format(nPosCount,nPosCount)
    plt.title(strg)
    plt.show()



def percentage(nCorrect, nCounted):
    return ("Accuracy is {:0.4f}% via {} samples".format(nCorrect/nCounted*100.0, nCounted))

VaderAnalysis()

















"""
# from nltk import tokenize
threshold = 0.5
nPosCorrect = 0
nPosCount = 0
with open("positive.txt", "r") as f:
    for line in f:
        vs = analyzer.polarity_scores(line)
        if vs['compound'] >= threshold or vs['compound'] <= -threshold:
            if vs['compound'] > 0:
                nPosCorrect += 1
            nPosCount += 1


        # breaking paragraph into sentences
        # paragraphSentiments = 0.0
        # sentence_list = tokenize.sent_tokenize(line)
        # for sentence in sentence_list:
        #     vs = analyzer.polarity_scores(sentence)
        #     print("{:-<69} {}".format(sentence, str(vs["compound"])))
        #     paragraphSentiments += vs["compound"]
        # print("\t\tAVERAGE SENTIMENT FOR PARAGRAPH: \t" + str(round(paragraphSentiments / len(sentence_list), 4)))

nNegCorrect = 0
nNegCount = 0
with open("negative.txt", "r") as f:
    for line in f:
        vs = analyzer.polarity_scores(line)
        if vs['compound'] >= threshold or vs['compound'] <= -threshold:
            if vs['compound'] <= 0:
                nNegCorrect += 1
            nNegCount += 1

print("Positive accuracy = {}% via {} samples".format(nPosCorrect/nPosCount*100.0, nPosCount))
print("Negative accuracy = {}% via {} samples".format(nNegCorrect/nNegCount*100.0, nNegCount))
"""





"""
nPosCorrect = 0
nPosCount = 0
with open("positive.txt", "r") as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)
        if analysis.sentiment.subjectivity > 0.9:
            if analysis.sentiment.polarity > 0:
                nPosCorrect += 1
            nPosCount += 1



nNegCorrect = 0
nNegCount = 0
with open("negative.txt", "r") as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)

        if analysis.sentiment.subjectivity > 0.9:
            if analysis.sentiment.polarity <= 0:
                nNegCorrect += 1
            nNegCount += 1

print("Positive accuracy = {}% via {} samples".format(nPosCorrect/nPosCount*100.0, nPosCount))
print("Negative accuracy = {}% via {} samples".format(nNegCorrect/nNegCount*100.0, nNegCount))
"""




"""
def getRedditData():
    rd = RDT.Extract()
    rd.getComments()

getRedditData()
analysis1 = TextBlob("Wow how nice of you to bring my phone")
print(analysis1.polarity)
print(analysis1.sentiment)

analysis2 = TextBlob("If you had to guess what do think about the future of antartica")
print(analysis2.polarity)
print(analysis2.sentiment)
"""































"""
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
"""










"""
import datetime
sTimeStamp = datetime.datetime(2010, 12, 1, 0, 0).timestamp()
eTimeStamp = datetime.datetime(2018, 12, 1, 0, 0).timestamp()

analyze sentiment
with open("C:\\Users\\arshdeep.dhillon1\\Desktop\\cpsc571\\Practice Code\\Sentiment-Analysis\\sb.txt","r") as f:

    for line in f:
        subreddit = reddit.subreddit(line.strip())
        # prep for sentiment analysis
        subSentiment, nComments = 0,0

        # for submission in subSubmissions:
        for submission in subreddit.stream.submissions():
            # if its not a sticky submission (pinned at thr top) then grab the rest
            if not submission.stickied:
                submission.comments.replace_more(limit=2)

                # prep for sentiment analysis
                for comment in submission.comments.list():

                    print(comment.body)

                    blob = TextBlob(comment.body)

                    # this will return a tuple that contains (polarity, subjectivity)
                    # subjectivity score: [0.0, 1.0], 0.0 => very objective and 1.0 => very subjective
                    # polarity score:     [-1.0, 1.0]
                    commentSentiment = blob.sentiment.polarity

                    # this will be used on each relative subreddit by taking the total number of comments
                    subSentiment += commentSentiment
                    nComments += 1
        print("/r/" + str(subreddit.display_name))
        try:
            print("Ratio: " + str(math.floor(subSentiment/nComments * 100)) + "\n")
        except:
            print("Unable to calculate sentiment of each subreddit")
"""
