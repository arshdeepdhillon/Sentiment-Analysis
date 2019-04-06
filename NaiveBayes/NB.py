#Upack the zip file
# import zipfile
# with zipfile.ZipFile("reviews.zip", 'r') as zip_ref:
#     zip_ref.extractall(".")
#
#     #Get the label and reviews ready for processing
#     with open("reviews.txt") as f:
#         reviews = f.read().split("\n")
#         with open("labels.txt") as f:
#             labels = f.read().split("\n")
#             labels = labels[:-1]

labels = []
reviews = []
#Now trying with Chandlers data
with open("imdb_positive.txt") as f:
    reviews = f.read().split("\n")
for review in reviews:
    labels.append("positive")
f.close();
labels = labels[:-1]
reviews = reviews[:-1]

with open("imdb_negative.txt") as f:
    reviews2 = f.read().split("\n")
for review2 in reviews2:
    reviews.append(review2)
    labels.append("negative")
f.close()
labels = labels[:-1]
reviews = reviews[:-1]

reviews_tokens = [review.split() for review in reviews]

#Process data
from sklearn.preprocessing import MultiLabelBinarizer
onehot_enc = MultiLabelBinarizer()
onehot_enc.fit(reviews_tokens)

#Split data for training and testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(reviews_tokens, labels, test_size=0.25, random_state=None)

#Get ML algorithm to train
from sklearn.naive_bayes import BernoulliNB

bnbc = BernoulliNB(binarize=None)
bnbc.fit(onehot_enc.transform(X_train), y_train)

#Get score
score = bnbc.score(onehot_enc.transform(X_test), y_test)
print(score)
