from sklearn import svm
import zipfile
from sklearn.preprocessing import MultiLabelBinarizer
# Using code from sklearn to help imeplement our SVM approach
#https://medium.com/nlpython/sentiment-analysis-analysis-part-2-support-vector-machines-31f78baeee09

#First part unpacks the zip file and then breaks it down.
with zipfile.ZipFile("reviews.zip", 'r') as zip_ref:
    zip_ref.extractall(".")

with open("reviews.txt") as f:
    reviews = f.read().split("\n")
with open("labels.txt") as f:
    labels = f.read().split("\n")
labels = labels[:-1]

reviews_tokens = [review.split() for review in reviews]

#now it coverts inputs to binary vectors
from sklearn.preprocessing import MultiLabelBinarizer
onehot_enc = MultiLabelBinarizer()
onehot_enc.fit(reviews_tokens)

#next splits into training and test.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(reviews_tokens, labels, test_size=0.25, random_state=None)

#trains
from sklearn.svm import LinearSVC
lsvm = LinearSVC()
lsvm.fit(onehot_enc.transform(X_train), y_train)

#check training score
score = lsvm.score(onehot_enc.transform(X_test), y_test)
print(score)
