# Comparative Sentiment Analysis of Lexicon and Machine Learning

## Installation 
```javascript
pip install textblob
pip install vaderSentiment
python -m pip install [package]
```

 



### Reddit Sample Data
```json
{"author_flair_css_class":null,"created_utc":1141171505,"score":4,"ups":4,"subreddit":"reddit.com","link_id":"t3_2cms","stickied":false,"subreddit_id":"t5_6","controversiality":0,"body":"THIS IS TEST 1: comment 1","retrieved_on":1473821737,"distinguished":null,"gilded":0,"id":"c2id4","edited":false,"parent_id":"t1_c2g7c","author":"enjahova","author_flair_text":null}
{"gilded":0,"retrieved_on":1473821737,"distinguished":null,"author_flair_text":null,"author":"arakyd","id":"c2ie5","parent_id":"t1_c2ic7","edited":false,"subreddit":"reddit.com","created_utc":1141171952,"author_flair_css_class":null,"score":6,"ups":6,"body":"THIS IS TEST 1: comment 2","controversiality":0,"stickied":false,"link_id":"t3_2aru","subreddit_id":"t5_6"}
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

### Additional Information
* [Comparative analysis using supervised and unsupervised learning](https://bit.ly/2I5WBOP)
* [Vader](https://github.com/cjhutto/vaderSentiment)
* [TextBlob](https://textblob.readthedocs.io/en/dev/index.html#)
* [Reddit Data](http://files.pushshift.io/reddit/comments/)
