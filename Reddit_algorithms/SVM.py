from sklearn import svm
import zipfile
import timeit
from sklearn.preprocessing import MultiLabelBinarizer
# Using code from sklearn to help imeplement our SVM approach
#https://medium.com/nlpython/sentiment-analysis-analysis-part-2-support-vector-machines-31f78baeee09

import csv


#First part unpacks the zip file and then breaks it down.
# with zipfile.ZipFile("reviews.zip", 'r') as zip_ref:
#     zip_ref.extractall(".")
#
# with open("reviews.txt") as f:
#     reviews = f.read().split("\n")
# with open("labels.txt") as f:
#     labels = f.read().split("\n")
# labels = labels[:-1]

# reviews_tokens = [review.split() for review in reviews]

#new way of processings the CSV file. Should work but the file is too large so it fails later on
# lines = 0
reviews = []
labels = []
# with open("imdb_master.csv", 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         if lines == 0:
#             lines = lines + 1
#         else:
#             reviews.append(row[2])
#             labels.append(row[3])
#             lines = lines + 1
#
# print("Lines processed ", lines)
#
# f.close()


#Now trying with Chandlers data
with open("positive.txt") as f:
    reviews = f.read().split("\n")
for review in reviews:
    labels.append("positive")
f.close();
labels = labels[:-1]
reviews = reviews[:-1]

with open("negative.txt") as f:
    reviews2 = f.read().split("\n")
for review2 in reviews2:
    reviews.append(review2)
    labels.append("negative")
f.close()

with open("RC_2006-03.txt") as f:
	reviews3 = f.read().split("\n")
for review3 in reviews3:
	reviews.append(review3)
	labels.append("positive")

labels = labels[:-1]
reviews = reviews[:-1]


# reviews = reviews.append(reviews2)
# print(len(reviews))
print(len(labels))
reviews_tokens = [review.split() for review in reviews]

#now it coverts inputs to binary vectors
from sklearn.preprocessing import MultiLabelBinarizer
onehot_enc = MultiLabelBinarizer()
onehot_enc.fit(reviews_tokens)

#next splits into training and test.
from sklearn.model_selection import train_test_split
#this was my attempt to make the data set smaller.
# reviews_tokens = reviews_tokens[7500:-87500]
# labels = labels[7500:-87500]
#This is where it fails based on all the data being negative or too large i believe.
X_train, X_test, y_train, y_test = train_test_split(reviews_tokens, labels, test_size=0.58, random_state=None, shuffle = False)

#trains
from sklearn.svm import LinearSVC
startTrain = timeit.default_timer()
lsvm = LinearSVC(dual = False)
lsvm.fit(onehot_enc.transform(X_train), y_train)
endTrain = timeit.default_timer()

#check training score
startTest = timeit.default_timer()
score = lsvm.score(onehot_enc.transform(X_test), y_test)
endTest = timeit.default_timer()

print("Training Time: ", end="")
print(endTrain - startTrain)
print("Time on test: ", end="")
print(endTest - startTest)
print(score)


####################  Evaluate the Classifier  ####################
print("\n\n####################  Evaluate the Classifier  ####################\n")
from sklearn.metrics import classification_report
predicted = lsvm.predict(onehot_enc.transform(X_test))
report = classification_report(y_test, predicted)
print(report)

# if you want only the f-score, then uncomment the following 2 lines.
"""
from sklearn.metrics import f1_score
print("F-score is ", '{0:.3g}'.format(f1_score(y_test, predicted, average='weighted')))
"""
print("\n####################            Done           ####################\n\n")
