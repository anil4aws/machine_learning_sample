from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


iris = load_iris()  # load the dataset
# X = iris.data       # extract feature vectors
# y = iris.target     # extract labels
iris = load_iris()
X, y = iris['data'], iris['target']

# print(type(X))
# print(len(X))
#print(y)

X_train, X_test, y_train, y_test = train_test_split(    X, y, test_size=0.25, random_state=42)

# X_test.head(5)
#
# y_train.head(5)
#
print(y_test)

#
# for i, label in enumerate(iris.target_names):
#   plt.scatter(X[y == i, 1], X[y == i, 3], label=label)
#
#
# plt.legend()
# plt.xlabel(iris.feature_names[1])
# plt.ylabel(iris.feature_names[3])
# plt.title("Scatter plot of Iris dataset")
# plt.show()



neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y)

y_pred = knn.predict(X_test)

#################################

from sklearn.metrics import accuracy_score
y_pred = [0, 2, 1, 3]
y_true = [0, 1, 2, 3]
accuracy_score(y_true, y_pred)




from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report


# Evaluate the classifier
print("Accuracy :", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, average='macro'))
print("Recall   :", recall_score(y_test, y_pred, average='macro'))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))


