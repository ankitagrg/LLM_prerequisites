import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.decomposition import PCA

# Generate synthetic data
X, y = make_classification(n_samples=200, n_features=10, random_state=42)

# Reduce dimensions
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# Plot
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, cmap='viridis', s=30)
plt.title("PCA Visualization of Synthetic Data")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()
