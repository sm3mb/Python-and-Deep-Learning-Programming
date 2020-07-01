#importing the datasets from sklearn
from sklearn.datasets import fetch_20newsgroups

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

from sklearn import metrics

from sklearn.svm import SVC
# Taking only specific categories
categories = ['rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey', 'sci.crypt', 'sci.electronics']

# Reading the train data from datasets from fetch_20newsgroups og given categories
twenty_train = fetch_20newsgroups(subset='train', shuffle=True, categories=categories)

# Converts raw data into feature vectors
tfidf_Vect = TfidfVectorizer()

X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)

svc = SVC()
# Training the model
svc.fit(X_train_tfidf, twenty_train.target)

# Reading the test data from datasets from fetch_20newsgroups og given categories
twenty_test = fetch_20newsgroups(subset='test', shuffle=True, categories=categories)

X_test_tfidf = tfidf_Vect.transform(twenty_test.data)

predicted = svc.predict(X_test_tfidf)

# Bigram
tfidf_Vect1 = TfidfVectorizer(ngram_range=(1,2))
X_train_tfidf1 = tfidf_Vect1.fit_transform(twenty_train.data)

svc1 = SVC()
svc1.fit(X_train_tfidf1, twenty_train.target)
X_test_tfidf1 = tfidf_Vect1.transform(twenty_test.data)
predicted1 = svc1.predict(X_test_tfidf1)

# Stop_words='english'
tfidf_Vect2 = TfidfVectorizer(stop_words='english')
X_train_tfidf2 = tfidf_Vect2.fit_transform(twenty_train.data)

svc2 = SVC()
svc2.fit(X_train_tfidf2, twenty_train.target)
X_test_tfidf2 = tfidf_Vect2.transform(twenty_test.data)
predicted2 = svc2.predict(X_test_tfidf2)

# Evaluated the model with SVC
score = metrics.accuracy_score(twenty_test.target, predicted)
print('SVC score is ' + str(round(score * 100 , 2)))

# Evaluating the model by considering Npgram
score1 = metrics.accuracy_score(twenty_test.target, predicted1)
print('Using npgram score is ' + str(round(score1 * 100 , 2)))

# Evaluating the model by considering Stop words
score2 = metrics.accuracy_score(twenty_test.target, predicted2)
print('Using stop words score is ' + str(round(score2 * 100 , 2)))