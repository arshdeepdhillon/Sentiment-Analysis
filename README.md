# Sentiment-Analysis

## Installation 
```python
pip install textblob
```
```python
pip install praw
```



### [Reddit Sample Data](http://files.pushshift.io/reddit/comments/)
```json
{"author_flair_css_class":null, ... ,"body":"This is a reddit comment!!"},
{"author_flair_css_class":null, ... ,"body":"Another reddit comment"}
```

### Formatted Data 
```json
{
   "formattedFile1.txt":{
      "comments":[
         {"body":"THIS IS TEST 1: comment 1"},
         {"body":"THIS IS TEST 1: comment 2"}
      ]
   },
   "formattedFile2.txt":{
      "comments":[
         {"body":"THIS IS TEST 2: comment 1"},
         {"body":"THIS IS TEST 2: comment 2"}
      ]
   },
   "formattedFile3.txt":{
      "comments":[
         {"body":"THIS IS TEST 3: comment 1"},
         {"body":"THIS IS TEST 3: comment 2"}
      ]
   }
}
```