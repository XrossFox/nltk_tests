import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

sentence = "The Quick brown fox, jumps over the lazy little dog. Hello World"
#print(sentence.split())

"""Tokenizer divide las sentencias en palabras y signos de puntuacion"""
#print(word_tokenize(sentence))

"""Tambien se puede detectar que partes de la sentencia son sustantivos, adverbios, verbos, etc."""
w = word_tokenize(sentence)
#print(nltk.pos_tag(w))
#print("---")
#print(nltk.help.upenn_tagset())

"""Puede buscar significados de palabras, ejemplos, palabras similares y antonimos"""
syn = wordnet.synsets("Computer")
#print(syn)
#print(syn[0].name())
#print(syn[0].definition())
#print(syn[1].name())
#print(syn[1].definition())

syn = wordnet.synsets("talk")

"""Tambien detecta Hypernyms e hiponios"""
#print(syn[0].examples())

#print("---")
#syn = wordnet.synsets("speak")[0]

#print(syn.hypernyms())

#print(syn.hyponyms())

#print("+++")


"""Antonimos. Los lemmas son los terminos internos de nltk para palabras unicas.
Se pueden usar para encontrar palabras similares"""
syn = wordnet.synsets("good")
for s in syn:
    for l in s.lemmas():
        if(l.antonyms()):
            print(l.antonyms())

print("---")
syn = wordnet.synsets("book")
for s in syn:
        print(s.lemmas())
