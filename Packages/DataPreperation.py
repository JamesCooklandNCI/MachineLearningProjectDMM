import re
from nltk.stem import snowball
import pandas as pd
import numpy as np
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS
from textblob import TextBlob as txt
from Data import config
from nltk.stem.snowball import SnowballStemmer


class CleanData(object):
    def __init__(self):
        print("Data cleansing initialised.")


    def getTag(self, text):
        # Get word tags for each item in the text.
        # This is used to increase the lemmitizers accuracy.
        try:
            tag = wn.synsets(text)[0].pos()
            return tag
        except:
            return ""


    def remEmoji(self, text):
        # Defind and remove Emoji symbols as they wont used for 
        # sentiment detetion.
        regrex_pattern = re.compile(pattern = "["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags = re.UNICODE)
        return regrex_pattern.sub(r'',text)


    def RemoveEmoticonsFor(self, df):
        # Remove Emoticons
        remEmoji = lambda x: " ".join(self.remEmoji(x) for x in str(x).split())
        df["newReview"] = df["newReview"].apply(remEmoji)
        return df


    def GeneralCleansingFor(self, df, textcol):
        # Convert all text to lowercase
        # Remove <br />, Punctution, URLs, @Mentions, #Hashtags
        df["newReview"] = df[textcol]
        for value in config.dataCleansing.values():
            df["newReview"] = df["newReview"].replace(value," ", regex=True)
        df["newReview"] = df["newReview"].str.lower()
        return df
    

    def RemoveStopWordsFor(self, df):
        # Remove stopwords
        stopword = stopwords.words("english")
        remove = lambda x: " ".join(x for x in x.split() if x not in stopword)
        df["newReview"] = df["newReview"].apply(remove)
        return df


    def LemmatizeTextFor(self, df):
        # Perform Lemmitisation
        lemmatizer = WordNetLemmatizer()
        lem = lambda x: " ".join(lemmatizer.lemmatize(x) for x in x.split())
        df["newReview"] = df["newReview"].apply(lem)
        return df
    
    def POSLemmatizeTextFor(self, df):
        lemmatizer = WordNetLemmatizer()
        lem = lambda x: " ".join(lemmatizer.lemmatize(x, 
                                                      self.getTag(x)) for 
                                                      x in x.split() if 
                                                      self.getTag(x) != "")
        df["newReview"] = df["newReview"].apply(lem)
        return df
    
    def StemTextFor(self, df):
        snowballstem = SnowballStemmer("english")
        stemmer = lambda x: " ".join(snowballstem.stem(x) for x in x.split())
        df["newReview"] = df["newReview"].apply(stemmer)
        return df
          
    def RemoveEmoticonsFor(self, df):
        # Remove Emoticons
        remEmoji = lambda x: " ".join(self.remEmoji(x) for x in str(x).split())
        df["newReview"] = df["newReview"].apply(remEmoji)
        return df