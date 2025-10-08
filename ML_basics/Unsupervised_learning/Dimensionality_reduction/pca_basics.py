import numpy as np
from sklearn.decomposition import PCA

# Generate simple 2D data
np.random.seed(0)
X = np.random.rand(10, 3)

pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

print("Original Shape:", X.shape)
print("Reduced Shape:", X_reduced.shape)
print("Explained Variance Ratio:", pca.explained_variance_ratio_)
