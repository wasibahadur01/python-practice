import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
# Load the dataset
df = pd.read_csv('dataset.csv')
# Create a CountVectorizer to convert text to a matrix of token counts
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])
lm.fit(df['text'], df['label'])
# Train a Multinomial Naive Bayes classifier
model = MultinomialNB()
model.fit(X, df['label'])
# Make predictions on new data
new_text = ["This is a new text to classify"]
new_X = vectorizer.transform(new_text)
predicted_label = model.predict(new_X)
print(predicted_label)
