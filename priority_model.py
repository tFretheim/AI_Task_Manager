import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Dummy training data
data = [
    ("Finish project report", 2),
    ("Buy groceries", 1),
    ("Prepare for exam", 3),
    ("Call mom", 1),
    ("Fix the bug in code", 2)
]

# Preprocessing
texts, priorities = zip(*data)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
y = np.array(priorities)

# Train model
model = MultinomialNB()
model.fit(X, y)

# Save model and vectorizer
with open("model.pkl", "wb") as model_file:
    pickle.dump((vectorizer, model), model_file)

def predict_priority(title, description):
    with open("model.pkl", "rb") as model_file:
        vectorizer, model = pickle.load(model_file)
    task_text = title + " " + description
    X_new = vectorizer.transform([task_text])
    return model.predict(X_new)[0]
