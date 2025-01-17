import sys
sys.path.insert(0, '../extract_data')
import extract_reddit_comments as RDT

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import timeit

class Vader:

    def __init__(self):

        # file's name that will be genereated in the comments_parsed_path folder
        self.comments_parsed_file_name = "output.txt"

        # all comments from each file that resides in json_formatted_path folder is
        # extracted and aggregated into one file under comments_parsed_path folder
        self.comments_parsed_path = "comments_extracted/" + self.comments_parsed_file_name

        # used to plot a chart
        self.nPosCorrect = 0
        self.nPosCount = 0
        self.nNegCorrect = 0
        self.nNegCount = 0


    def getRedditData(self):
        rd = RDT.Extract()
        rd.getComments()

    def VaderAnalysis(self):
        self.getRedditData()
        analyzer = SentimentIntensityAnalyzer()
        compoundScore = 0.05 # accuracy is good when threshold is close to 0.09


        # check for positive text
        #with open(self.comments_parsed_path, "r") as f:
        with open("positive_movie_reviews.txt", "r") as f:
            startP = timeit.default_timer()
            for line in f:
                analysis = analyzer.polarity_scores(line)
                self.nPosCount += 1
                if analysis['compound'] >= compoundScore:

                    if analysis['compound'] > 0:
                        self.nPosCorrect += 1
            stopP = timeit.default_timer()

        # check for neutral text
        #with open(self.comments_parsed_path, "r") as f:
        with open("negative_movie_reviews.txt", "r") as f:
            startN = timeit.default_timer()
            for line in f:
                analysis = analyzer.polarity_scores(line)
                self.nNegCount += 1
                if analysis['compound'] <= -compoundScore:

                    if analysis['compound'] <= 0:
                        self.nNegCorrect += 1
            stopN = timeit.default_timer()


        print("\nFinished in {:0.4f} sec".format(stopP-startP + stopN-startN))
        print("Positive " + self.percentage(self.nNegCorrect,self.nNegCount))
        print("Negative " + self.percentage(self.nPosCorrect,self.nPosCount))
        return(stopP-startP + stopN-startN)
        # uncomment the below line to view the result using pie chart
        # self.plotData()


    def percentage(self,nCorrect, nCounted):
        return ("Accuracy is {:0.4f}% via {} samples".format(nCorrect/nCounted*100.0, nCounted))

    def plotData(self):
        # plotting data
        import matplotlib.pyplot as plt

        # declare variables
        labels = 'Positive', 'Neutral'
        sizes = [self.nPosCorrect, self.nNegCorrect]
        colors = ['green', 'red']

        # using matplotlib to plot the data
        plt.pie(sizes, labels = labels, colors = colors, shadow = True, startangle = 90)
        strg = str("Sentiment of {} positives and {} negatives").format(self.nPosCount,self.nNegCount)
        plt.title(strg)
        plt.show()



# run the analysis couple of time to get the average time
totalTime = 0.0
nRuns = 1
for i in range(nRuns):
    print("\nRun #{:}".format(i+1))
    totalTime += Vader().VaderAnalysis()

print("\nFinished with ave. time {:0.4f} sec".format(totalTime/nRuns))
