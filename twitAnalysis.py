from textblob import TextBlob

Feedback1 = " The food at pika was awsome"
Feedback2 = " The food at pika was super good"
Feedback3 = "i hate apples"

blob1 = TextBlob(Feedback1)
blob2 = TextBlob(Feedback2)
blob3 = TextBlob(Feedback3)

print(blob1.sentiment)
print(blob2.sentiment)
print(blob3.sentiment)