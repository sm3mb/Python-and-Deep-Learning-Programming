import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
# from collections import Counter
from nltk.stem import SnowballStemmer
from nltk.stem import LancasterStemmer
from nltk import wordpunct_tokenize, pos_tag, ne_chunk

file_content = open("output.txt").read()
wtokens = nltk.word_tokenize(file_content)
print('Tokens :')
for t in wtokens:
    print(t)

print('-----------------***------------------------')

print('POS:',nltk.pos_tag(wtokens))

print('-----------------***------------------------')

# Porter Stemmer
pStemmer = PorterStemmer()
print('Porter Stemmer :')
for t in wtokens:
    print(t, pStemmer.stem(t.lower()))

print('-----------------***------------------------')

# Lancaster Stemmer
lStemmer = LancasterStemmer()
print('Lancaster Stemmer :')
for t in wtokens:
    print(t, lStemmer.stem(t.lower()))

print('-----------------***------------------------')

# Snowball Stemmer
snowball = SnowballStemmer('english')
print('Snowball Stemmer :')
for t in wtokens:
    print(t, snowball.stem(t.lower()))

print('-----------------***------------------------')

# Lemmatizer
lemmatizer = WordNetLemmatizer()
print('Lemmatizer:')
for t in wtokens:
    print(t, lemmatizer.lemmatize(t.lower()))

print('-----------------***------------------------')

# Trigrams
trigrams = list(ngrams(wtokens, 3))
print('Trigrams',trigrams)

print('-----------------***------------------------')

# named entity recognition
print('Named Entity Recognition:',ne_chunk(pos_tag(wordpunct_tokenize(file_content))))