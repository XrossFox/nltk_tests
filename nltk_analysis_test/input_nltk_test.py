#Read user input
#Clean string
#Analyze sentiment
#Output result

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob

def clean_my_string(a_string):
    a_string = word_tokenize(a_string)
    not_stop_words = [word for word in a_string 
                        if word not in stopwords.words("english")]
    clean_string = " ".join(not_stop_words)
    return clean_string
    
def analyze(string_to_analyze):
    an = TextBlob(string_to_analyze)
    sentiment = lambda x: "Positive" if an.sentiment.polarity > 0 else "Neutral" if an.sentiment.polarity == 0 else "Negative"
    return "'{string_to_analyze}' is a {sentiment} comment with a polarity of {polarity}".format(
                string_to_analyze=string_to_analyze,
                sentiment=sentiment(an.sentiment.polarity),
                polarity=str(an.sentiment.polarity))

def main():
    user_input = input("Key something! ")
    clean_words = clean_my_string(user_input)
    print(analyze(clean_words))

if __name__ == "__main__":
    main()