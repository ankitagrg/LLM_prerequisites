import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data/customers.csv") 
X = data[["Annual_Income", "Spending_Score"]]

# K-Means clustering
kmeans = KMeans(n_clusters=5, random_state=42)
data["Cluster"] = kmeans.fit_predict(X)

# Plot results
plt.figure(figsize=(8,6))
plt.scatter(X["Annual_Income"], X["Spending_Score"], c=data["Cluster"], cmap="rainbow")
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], color="black", marker="x", s=100)
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1–100)")
plt.title("Customer Segmentation with K-Means")
plt.show()
