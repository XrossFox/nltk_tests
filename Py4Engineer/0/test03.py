import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

"""Para armar la entrada segun Naibe Bayes la espera"""
def create_word_features(words):
    #Elimina Stop words
    useful_words = [word for word in words if word not in stopwords.words("english")]
    #Crea diccionario [llave,true]. Ademas en los diccionarios no hay terminos repetidos
    my_dict = dict([(word, True) for word in useful_words])
    return my_dict

#print(create_word_features(["the","quick","brown","a","fox"]))
"""Una lista de review negativos"""
neg_reviews = []
for fileid in movie_reviews.fileids("neg"):
    words = movie_reviews.words(fileid)
    neg_reviews.append((create_word_features(words), "negative"))

print(neg_reviews[0])
print(len(neg_reviews))

"""Una lista de reviews positivas"""
pos_reviews = []
for fileid in movie_reviews.fileids("pos"):
    words = movie_reviews.words(fileid)
    pos_reviews.append((create_word_features(words),"positive"))

print(len(pos_reviews))

"""Entrenando el clasificador"""
train_set = neg_reviews[:750] + pos_reviews[:750]
test_set = neg_reviews[750:] + pos_reviews[750:]
print(len(train_set), len(test_set))

"""Clasificador Naive Bayes"""
classifier = NaiveBayesClassifier.train(train_set)

"""La prueba"""
accuracy = nltk.classify.util.accuracy(classifier, test_set)
print(accuracy * 100)

"""Clasificando un solo comentario"""


review_santa = '''
 
It would be impossible to sum up all the stuff that sucks about this film, so I'll break it down into what I remember most strongly: a man in an ingeniously fake-looking polar bear costume (funnier than the "bear" from Hercules in New York); an extra with the most unnatural laugh you're ever likely to hear; an ex-dope addict martian with tics; kid actors who make sure every syllable of their lines are slowly and caaarreee-fulll-yyy prrooo-noun-ceeed; a newspaper headline stating that Santa's been "kidnaped", and a giant robot. Yes, you read that right. A giant robot.
 
The worst acting job in here must be when Mother Claus and her elves have been "frozen" by the "Martians'" weapons. Could they be *more* trembling? I know this was the sixties and everyone was doped up, but still.
'''
print(review_santa )

words = word_tokenize(review_santa)
words = create_word_features(words)
classifier.classify(words)