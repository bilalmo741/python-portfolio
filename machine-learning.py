# Kickstarter ML Classifier

import nltk, requests, sklearn.metrics, sklearn.model_selection, sklearn.tree, csv, sklearn.neural_network, sklearn.feature_extraction.text
nltk.download("stopwords")
from nltk.corpus import stopwords

response = requests.get("https://dgoldberg.sdsu.edu/515/kickstarter_data_full.csv")

if response:
    with open("kickstarter_data_full.csv", "w", encoding="latin-1") as file:
        file.write(response.text)
    with open("kickstarter_data_full.csv", "r", encoding="latin-1") as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]

    x = []
    y = []
    for row in data:
        description = row["Description"]
        status = row["Status"]
        x.append(description)
        y.append(1 if status == "Funding Successful" else 0)

    vectorizer = sklearn.feature_extraction.text.CountVectorizer(stop_words=stopwords.words("english"))
    vectors = vectorizer.fit_transform(x)
    x = vectors.toarray()

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
    print("Decision tree accuracy: ", dt_accuracy)
    
    # KNN
    knn_clf = sklearn.neighbors.KNeighborsClassifier(7)
    knn_clf.fit(x_train, y_train)
    knn_predictions = knn_clf.predict(x_test)
    knn_accuracy = sklearn.metrics.accuracy_score(y_test, knn_predictions)
    print("KNN Accuracy: ", knn_accuracy)

else:
    print("Connection error.")


# Wholesale Clustering

import csv
import matplotlib.pyplot as plt
import sklearn.cluster
import sklearn.metrics
import warnings

warnings.filterwarnings("ignore")

with open("Wholesale customers data.csv", "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)

x = []
fresh = []
milk = []
grocery = []
frozen = []
detergents_paper = []
delicatessen = []

for line in data:
    fresh_val = float(line["Fresh"])
    milk_val = float(line["Milk"])
    grocery_val = float(line["Grocery"])
    frozen_val = float(line["Frozen"])
    detergents_paper_val = float(line["Detergents_Paper"])
    delicatessen_val = float(line["Delicassen"])
    inner_list = [fresh_val, milk_val, grocery_val, frozen_val, detergents_paper_val, delicatessen_val]
    x.append(inner_list)
    fresh.append(fresh_val)
    milk.append(milk_val)
    grocery.append(grocery_val)
    frozen.append(frozen_val)
    detergents_paper.append(detergents_paper_val)
    delicatessen.append(delicatessen_val)

kmeans = sklearn.cluster.KMeans(4, random_state=0)
kmeans.fit(x)

colors = ["red" if l==0 else "blue" if l==1 else "green" if l==2 else "orange" for l in kmeans.labels_]

plt.scatter(fresh, milk, color=colors)
plt.xlabel("Fresh")
plt.ylabel("Milk")
plt.title("K-Means Clustering (4 Clusters)")
plt.show()
