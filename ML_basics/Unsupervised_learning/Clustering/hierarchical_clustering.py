from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data

Z = linkage(X, 'ward')
plt.figure(figsize=(10, 5))
dendrogram(Z, truncate_mode="lastp", p=20, leaf_rotation=45., leaf_font_size=10., show_contracted=True)
plt.title("Hierarchical Clustering Dendrogram")
plt.show()
