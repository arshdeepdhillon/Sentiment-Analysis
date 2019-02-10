# from textblob import TextBlob #for processing textual data  

# Feedback1 = " The food at pika was awsome"
# Feedback2 = " The food at pika was super good"
# Feedback3 = "i hate apples"

# blob1 = TextBlob(Feedback1)
# blob2 = TextBlob(Feedback2)
# blob3 = TextBlob(Feedback3)

# print(blob1.sentiment)
# print(blob2.sentiment)
# print(blob3.sentiment)


from bs4 import BeautifulSoup

import requests

url = requests.get("http://redditmetrics.com/top")

soup = BeautifulSoup(url.text, 'html.parser')

with open('sb.txt','w') as f:
    for subriddit in soup.find_all('a'):
        try:
            if "r" in subriddit.string:
                f.write(subriddit.string[3:] + "\n")
        except:
            TypeError