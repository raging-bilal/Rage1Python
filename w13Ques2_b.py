from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
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

# Initialize KMeans algorithm with 3 clusters
kmeans = KMeans(n_clusters=3)

# Fit the model to the data
kmeans.fit(iris.data)

# Define a new data point
new_data = [[5.0, 3.5, 1.3, 0.2]]
# new_data = [[6.8, 2.8, 4.8, 1.4]]
# new_data = [[6.9, 3.1, 5.4, 2.1]]

# Use the model to predict the cluster of the new data point
new_cluster = kmeans.predict(new_data)

print(new_cluster)

# Plot the clusters
plt.scatter(iris.data[:, 0], iris.data[:, 1], c=kmeans.labels_)
plt.scatter(new_data[0][0], new_data[0][1], marker='x', s=200, linewidths=3, color='r')
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("KMeans Clustering of Iris Dataset")
plt.show()

print("Predicted cluster for new data point:", new_cluster)
