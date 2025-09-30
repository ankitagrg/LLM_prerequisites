import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Generate dummy data
X = np.array([[1,2],[1,4],[1,0],
              [10,2],[10,4],[10,0]])

kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)

print("Cluster Centers:", kmeans.cluster_centers_)
print("Labels:", kmeans.labels_)

plt.scatter(X[:,0], X[:,1], c=kmeans.labels_, cmap="rainbow")
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], color="black", marker="x", s=100)
plt.title("Basic K-Means Clustering")
plt.show()
