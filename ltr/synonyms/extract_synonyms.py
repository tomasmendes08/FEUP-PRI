import pandas as pd
import nltk

fileName = "../dataset/Refined/rt_reviews.csv"

reviews = pd.read_csv(fileName)



File = open(fileName) #open file
lines = File.read() #read all lines
sentences = nltk.sent_tokenize(lines) #tokenize sentences
nouns = [] #empty to array to hold all nouns

for sentence in sentences:
     for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
         if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
             nouns.append(word)


