

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
