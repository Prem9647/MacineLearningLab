# Sentiment Analysis using Naive Bayes (From Scratch)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
texts = [
    "This movie is very good",
    "I love this product",
    "The service was excellent",
    "I am happy with the result",
    "This is a great experience",
    "This movie is very bad",
    "I hate this product",
    "The service was terrible",
    "I am unhappy with the result",
    "This is a horrible experience"
]

labels = ["Positive","Positive","Positive","Positive","Positive",
          "Negative","Negative","Negative","Negative","Negative"]

# Convert text to numeric form
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train Naive Bayes model
model = MultinomialNB()
model.fit(X, labels)

# Test sentence
test_sentence = ["This product is good"]
test_vector = vectorizer.transform(test_sentence)

prediction = model.predict(test_vector)
print("Prediction:", prediction[0])

