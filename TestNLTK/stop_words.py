from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 
text = 'En este tutorial, Estoy aprendiendo NLTK. Es una interesante plataforma.'
stop_words = set(stopwords.words('spanish'))
words = word_tokenize(text)
 
new_sentence = []
 
for word in words:
    if word not in stop_words:
        new_sentence.append(word)
 
print(new_sentence)