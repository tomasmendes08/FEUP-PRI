import pandas as pd
import nltk


fileName = "../dataset/Refined/rt_reviews.csv"

reviews_df = pd.read_csv(fileName)

reviews = reviews_df["review_content"].map(lambda x: x.lower())
word_dict = {}
words_checked = []
reviews_count = len(reviews)


# sentences = nltk.sent_tokenize(lines) #tokenize sentences
nouns = [] #empty to array to hold all nouns
count = 0

for desc in reviews:
    sentences = nltk.sent_tokenize(desc)
    nouns = []
    for sentence in sentences:
        for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
             if word.lower() not in words_checked:
                 if (pos == 'NN' or pos == 'NNS'): #common names (singular or plural)
                     nouns.append(word.lower())
                     words_checked.append(word.lower())
    for noun in nouns:
        synonyms = []
        for syn in nltk.corpus.wordnet.synsets(noun):
            for lm in syn.lemmas():
                synonyms.append(lm.name())#adding into synonyms 
        if len(synonyms) > 1:
            word_dict[noun] = synonyms

    percentage = count / reviews_count * 100
    count += 1
    
    print (f"{percentage} % done")
    
    
    
print("DONE! Writing to file")
    
list_synonyms = []
    
file = open("synonyms.txt", "w")

for k in word_dict.keys():
    matches = list(set([x for x in word_dict[k] if x != k]))
    list_synonyms = k + "," + ",".join(matches)
    file.write(list_synonyms + "\n")
    