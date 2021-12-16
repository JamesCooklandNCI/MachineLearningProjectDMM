import Packages.DataPreperation as prep
import re
import pandas as pd
import numpy as np
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS
from textblob import TextBlob as txt

imdbDF = pd.read_csv(r"Data/IMDB Dataset.csv")

class Initialise(object):
    def __init__(self, path):
        self.path = path
    def GetDF(self):
        df = pd.read_csv(self.path)
        return df
    def CleanData(self, df):
        cleanDf = prep.CleanData(df).CleanText()