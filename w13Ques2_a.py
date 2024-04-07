from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np

# Load the iris dataset
iris = load_iris()

# Print the column names
print('Column names:', ', '.join(iris.feature_names + ['target']))

idx = np.random.permutation(len(iris.target))
data = iris.data[idx]
target = iris.target[idx]

# Print the first 5 samples
print('Data with target:')
for i in range(5):
    print('{:<3} {:<3} {:<3} {:<3} {}'.format(data[i][0], data[i][1], data[i][2], data[i][3], target[i]))


# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

# Create the KNN classifier object
knn = KNeighborsClassifier(n_neighbors=3)

# Fit the classifier to the training data
knn.fit(X_train, y_train)

accuracy = knn.score(X_test, y_test)
print('Accuracy:', accuracy)

# Test the classifier on new data
new_data = [[5.1, 3.5, 1.4, 0.2], [7.0, 3.2, 4.7, 1.4], [6.3, 3.3, 6.0, 2.5]]
predictions = knn.predict(new_data)

# Print the predicted classes
print('Predictions:', predictions)
