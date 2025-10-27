import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.decomposition import PCA
import pandas as pd

# Load Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target
labels = iris.target_names

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Create a DataFrame for visualization
df = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
df["Target"] = y


# Plot PCA-reduced data
plt.figure(figsize=(8, 6))
sns.scatterplot(x="PC1", y="PC2", hue="Target", palette="Set2", data=df)
plt.title("PCA on Iris Dataset")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()
