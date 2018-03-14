import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import twitter_samples
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

"""Imprimir tipos de archivos"""
#print(twitter_samples.fileids())

"""Leyendo las muestras de los comentarios de twitter"""
#strings = twitter_samples.strings("negative_tweets.json")
#for string in strings[:5]:
#    print(string)

#strings = twitter_samples.strings("positive_tweets.json")
#for string in strings[:5]:
#    print(string)


"""Retirando los smileys del texto"""
def remove(string):    
    return string.replace(":","").replace(")","").replace("(","")

"""Para armar la entrada segun Naibe Bayes la espera"""
def create_word_features(words):
    #Elimina Stop words
    useful_words = [word for word in words if word not in stopwords.words("english")]
    #Crea diccionario [llave,true]. Ademas en los diccionarios no hay terminos repetidos
    my_dict = dict([(word, True) for word in useful_words])
    return my_dict

"""Test def arriba"""
#strings = twitter_samples.strings("negative_tweets.json")
#print(create_word_features(strings[:5]))

"""Hacer la lista de comentarios positivos y negativos"""
neg = list()
for string in twitter_samples.strings("negative_tweets.json"):
    words = word_tokenize(remove(string))
    neg.append((create_word_features(words), "negative") )

pos = list()
for string in twitter_samples.strings("positive_tweets.json"):
    words = word_tokenize(remove(string))
    pos.append((create_word_features(words),"positive"))


twitter_train = (pos[:3500] + neg[:3500])
#train sets
twitter_test = (pos[3500:] +neg[3500:])
print(len(twitter_train),len(twitter_test))

"""Naive Bayes"""
classifier = NaiveBayesClassifier.train(twitter_train)

certeza = nltk.classify.util.accuracy(classifier, twitter_test)
print(certeza * 100)



