#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# from sklearn import svm
# import zipfile
# import timeit
# from sklearn.preprocessing import MultiLabelBinarizer
# # Using code from sklearn to help imeplement our SVM approach
# #https://medium.com/nlpython/sentiment-analysis-analysis-part-2-support-vector-machines-31f78baeee09
#
# import csv
#
#
# #First part unpacks the zip file and then breaks it down.
# # with zipfile.ZipFile("reviews.zip", 'r') as zip_ref:
# #     zip_ref.extractall(".")
# #
# # with open("reviews.txt") as f:
# #     reviews = f.read().split("\n")
# # with open("labels.txt") as f:
# #     labels = f.read().split("\n")
# # labels = labels[:-1]
#
# # reviews_tokens = [review.split() for review in reviews]
#
# #new way of processings the CSV file. Should work but the file is too large so it fails later on
# # lines = 0
# reviews = []
# labels = []
# # with open("imdb_master.csv", 'r') as f:
# #     reader = csv.reader(f)
# #     for row in reader:
# #         if lines == 0:
# #             lines = lines + 1
# #         else:
# #             reviews.append(row[2])
# #             labels.append(row[3])
# #             lines = lines + 1
# #
# # print("Lines processed ", lines)
# #
# # f.close()
#
# print("Reading positive.txt...", end = '')
# #Now trying with Chandlers data
# with open("positive.txt") as f:
#     reviews = f.read().split("\n")
# for review in reviews:
#     labels.append("positive")
# f.close();
# labels = labels[:-1]
# reviews = reviews[:-1]
# print("Done.")
#
#
# print("Reading negative.txt...", end = '')
# with open("negative.txt") as f:
#     reviews2 = f.read().split("\n")
# for review2 in reviews2:
#     reviews.append(review2)
#     labels.append("negative")
# f.close()
# print("Done.")
#
# print("Reading RC_2006-03.txt...", end = '')
# with open("RC_2006-03.txt") as f:
# 	reviews3 = f.read().split("\n")
# for review3 in reviews3:
# 	reviews.append(review3)
# 	labels.append("positive")
#
# labels = labels[:-1]
# reviews = reviews[:-1]
# print("Done.")
#
# # reviews = reviews.append(reviews2)
# # print(len(reviews))
# print(len(labels))
# reviews_tokens = [review.split() for review in reviews]
#
# #now it coverts inputs to binary vectors
# from sklearn.preprocessing import MultiLabelBinarizer
# onehot_enc = MultiLabelBinarizer()
# onehot_enc.fit(reviews_tokens)
#
# #next splits into training and test.
# from sklearn.model_selection import train_test_split
# #this was my attempt to make the data set smaller.
# # reviews_tokens = reviews_tokens[7500:-87500]
# # labels = labels[7500:-87500]
# #This is where it fails based on all the data being negative or too large i believe.
# X_train, X_test, y_train, y_test = train_test_split(reviews_tokens, labels, test_size=0.58, random_state=None, shuffle = False)
#
# #trains
# from sklearn.svm import LinearSVC
#
########################################################################################

# We can use a grid search to find the best parameters for this model. Lets try
#Define a list of parameters for the models
#params = {'C': [0.001, 0.01, 0.1, 1, 10, 100],
 #              'gamma': [0.001, 0.01, 0.1, 1, 10, 100]}
# params = {'C': [1, 10, 100],'gamma': [1, 10, 100]}
#
#
# #We can build Grid Search model using the above parameters.
# #cv=5 means cross validation with 5 folds
# print("Finding the best parameters...", end = '')
# lsvm = GridSearchCV(SVC(random_state=0,dual = False), params, cv=2, n_jobs=1)
# print("Done.")
#
# print("Training the model the best parameters...", end = '')
# lsvm.fit(onehot_enc.transform(X_train), y_train)
# print("Done.")
# print("Best parameters set found on development set:")
# print()
# print(lsvm.best_params_)
#print("train score - " + str(lsvm.score(onehot_enc.transform(X_train), y_train)))
#print("test score - " + str(lsvm.score(onehot_enc.transform(X_train), y_test)))

########################################################################################
#
#
#
#
#
#
#
# # print("Training the model...", end = '')
# # startTrain = timeit.default_timer()
# # lsvm = LinearSVC(dual = False)
# # lsvm.fit(onehot_enc.transform(X_train), y_train)
# # endTrain = timeit.default_timer()
# # print("Done.")
#
#
# #check training score
# print("Checking the training score...", end = '')
# startTest = timeit.default_timer()
# score = lsvm.score(onehot_enc.transform(X_test), y_test)
# endTest = timeit.default_timer()
# print("Done.")
#
# print("Training Time: ", end="")
# print(endTrain - startTrain)
# print("Time on test: ", end="")
# print(endTest - startTest)
# print(score)
#
#
# ####################  Evaluate the Classifier  ####################
# print("\n\n####################  Evaluate the Classifier  ####################\n")
# from sklearn.metrics import classification_report
# predicted = lsvm.predict(onehot_enc.transform(X_test))
# report = classification_report(y_test, predicted)
# print(report)
#
# # if you want only the f-score, then uncomment the following 2 lines.
# """
# from sklearn.metrics import f1_score
# print("F-score is ", '{0:.3g}'.format(f1_score(y_test, predicted, average='weighted')))
# """
# print("\n####################            Done           ####################\n\n")






import pandas as pd
# train Data
trainData = pd.read_csv("https://raw.githubusercontent.com/Vasistareddy/sentiment_analysis/master/data/train.csv")
# test Data
testData = pd.read_csv("https://raw.githubusercontent.com/Vasistareddy/sentiment_analysis/master/data/test.csv")


# test Data
testData = pd.read_csv("https://raw.githubusercontent.com/Vasistareddy/sentiment_analysis/master/data/test.csv")


print(trainData.sample(frac=1).head(5))


from sklearn.feature_extraction.text import TfidfVectorizer

# Create feature vectors
vectorizer = TfidfVectorizer(min_df = 5,
                             max_df = 0.8,
                             sublinear_tf = True,
                             use_idf = True)
train_vectors = vectorizer.fit_transform(trainData['Content'])
test_vectors = vectorizer.transform(testData['Content'])



import time
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
# Perform classification with SVM, kernel=linear
# params = {'C': [1, 10, 100],'gamma': [1, 10, 100]}
params = {'C': [0.001, 0.01, 0.1, 1, 10, 100],'gamma': [0.001, 0.01, 0.1, 1, 10, 100]}

#We can build Grid Search model using the above parameters.
#cv=5 means cross validation with 5 folds
print("Finding the best parameters...", end = '')
lsvm = GridSearchCV(svm.SVC(random_state=0, kernel='linear'), params, cv=2, n_jobs=1)
print("Done.")

# classifier_linear = svm.SVC(kernel='linear')
classifier_linear = lsvm
t0 = time.time()
classifier_linear.fit(train_vectors, trainData['Label'])
t1 = time.time()
prediction_linear = classifier_linear.predict(test_vectors)
t2 = time.time()
time_linear_train = t1-t0
time_linear_predict = t2-t1

# results
print()
print(classifier_linear.best_params_)
print()
print("Training time: %fs; Prediction time: %fs" % (time_linear_train, time_linear_predict))
report = classification_report(testData['Label'], prediction_linear, output_dict=True)
print('positive: ', report['pos'])
print('negative: ', report['neg'])
