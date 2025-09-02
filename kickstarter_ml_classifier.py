# kickstarter_ml_classifier.py
# ML project: classify Kickstarter project success using Neural Networks, Decision Trees, and KNN

import nltk
import requests
import csv
import sklearn.metrics
import sklearn.model_selection
import sklearn.tree
import sklearn.neural_network
import sklearn.feature_extraction.text
from nltk.corpus import stopwords

nltk.download("stopwords")

# Download Kickstarter dataset
response = requests.get("https://dgoldberg.sdsu.edu/515/kickstarter_data_full.csv")

if response:
    with open("kickstarter_data_full.csv", "w", encoding="latin-1") as file:
        file.write(response.text)
    print("Data downloaded successfully.")

    with open("kickstarter_data_full.csv", "r", encoding="latin-1") as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    print("Data loaded successfully.")

    # Extract features and labels
    x = []
    y = []
    for row in data:
        description = row["Description"]
        status = row["Status"]
        x.append(description)
        y.append(1 if status == "Funding Successful" else 0)

    # Vectorize text
    vectorizer = sklearn.feature_extraction.text.CountVectorizer(stop_words=stopwords.words("english"))
    vectors = vectorizer.fit_transform(x)
    x = vectors.toarray()

    # Split dataset
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y)

    # Neural Network
    clf = sklearn.neural_network.MLPClassifier()
    clf.fit(x_train, y_train)
    predictions = clf.predict(x_test)
    accuracy = sklearn.metrics.accuracy_score(y_test, predictions)
    print("Neural network accuracy:", accuracy)

    # Decision Tree
    dt_clf = sklearn.tree.DecisionTreeClassifier()
    dt_clf.fit(x_train, y_train)
    dt_predictions = dt_clf.predict(x_test)
    dt_accuracy = sklearn.metrics.accuracy_score(y_test, dt_predictions)
    print("Decision tree accuracy:", dt_accuracy)

    # KNN
    knn_clf = sklearn.neighbors.KNeighborsClassifier(7)
    knn_clf.fit(x_train, y_train)
    knn_predictions = knn_clf.predict(x_test)
    knn_accuracy = sklearn.metrics.accuracy_score(y_test, knn_predictions)
    print("KNN Accuracy:", knn_accuracy)

else:
    print("Connection error.")
