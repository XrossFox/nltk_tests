import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

"""Stopwords, son palabras que ofrecen poco o nulo valor, pero son muy comunes. Toman una gran parte 
de la oracion, pero no agregan contexto o informacion. NLTK tiene una lista de stopwords para los principales lenguajes"""

"""Primeras 16 stopwords"""
#print(stopwords.words('english')[:16])

"""Oracion original"""
para = ("The program was open to all women between the ages of 17 and 35, in good health, " +
        "who had graduated from an accredited high school. ")
words = word_tokenize(para)
#print(words)

"""Oracion sin stopwords"""
useful_words = [word for word in words if word not in stopwords.words("english")]
#print(useful_words)

"""Las 20 palabras mas comunes en el data set de movie reviews, de las cuales, la mayoria son stopwords"""
all_words = movie_reviews.words()
freq_dist = nltk.FreqDist(all_words)
print(freq_dist.most_common(20))