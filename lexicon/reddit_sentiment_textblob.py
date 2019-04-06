import sys
sys.path.insert(0, '../extract_data')
import extract_reddit_comments as RDT
import timeit
from textblob import TextBlob


class TxtBlob:

    def __init__(self):

        # file's name that will be genereated in the comments_parsed_path folder
        self.comments_parsed_file_name = "output.txt"

        # all comments from each file that resides in json_formatted_path folder is
        # extracted and aggregated into one file under comments_parsed_path folder
        self.comments_parsed_path = "comments_extracted/" + self.comments_parsed_file_name


    def getRedditData(self):
        rd = RDT.Extract()
        rd.getComments()


    def TextblobAnalysis(self):
        # this will put it in your current dir
        self.getRedditData()

        # since textblob doesn't explicitly give a positive, neutral and negative value
        # I have set a compoundScore var that is similar ad vader's
        # compoundScore (which is set to 0.05).
        compoundScore = 0.05

        ####################### check for positive text ########################
        nPosCorrect = 0
        nPosCount = 0
        #with open(self.comments_parsed_path, "r") as f:
        with open("positive.txt", "r") as f:
            startPos = timeit.default_timer()
            for line in f:
                analysis = TextBlob(line)
                nPosCount += 1
                if analysis.sentiment.polarity >= compoundScore:
                    if analysis.sentiment.polarity > 0:
                        nPosCorrect += 1
            stopPos = timeit.default_timer()

        ####################### check for negative text #########################
        nNegCorrect = 0
        nNegCount = 0
        #with open(self.comments_parsed_path, "r") as f:
        with open("negative.txt", "r") as f:
            startNeg = timeit.default_timer()
            for line in f:
                analysis = TextBlob(line)
                nNegCount += 1
                if analysis.sentiment.polarity <= -compoundScore:
                    if analysis.sentiment.polarity <= 0:
                        nNegCorrect += 1
            stopNeg = timeit.default_timer()

        print("\nFinished in {:0.4f} sec".format(stopPos-startPos + stopNeg-startNeg))
        print("Positive " + self.percentage(nPosCorrect,nPosCount))
        print("Negative " + self.percentage(nNegCorrect,nNegCount))
        return((stopPos-startPos) + (stopNeg-startNeg))

    def percentage(self,nCorrect, nCounted):
        return ("Accuracy is {:0.4f}% via {} samples".format(nCorrect/nCounted*100.0, nCounted))




# run the analysis couple of time to get the average time
totalTime = 0.0
nRuns = 1
for i in range(nRuns):
    print("\nRun #{:}".format(i+1))
    totalTime += TxtBlob().TextblobAnalysis()

print("\nFinished with ave. time {:0.4f} sec".format(totalTime/nRuns))