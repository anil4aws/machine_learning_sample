from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import pandas as pd
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('D:\kb\machine_learning_sample\mathematics_for_ai/amazon_sls/amazon_sales_dataset.csv')

numeric_cols = ['price', 'discount_percent', 'quantity_sold', 'rating',
                'review_count', 'discounted_price', 'total_revenue']

data_numeric = data[numeric_cols]


scalar = StandardScaler()
data_std = scalar.fit_transform(data_numeric)

pca = PCA(n_components=3)
principal_components = pca.fit_transform(data_std)

print("Principal Components:", principal_components)
print("Explained Variance Ratio:", pca.explained_variance_ratio_)
print("Principal Axes (Eigenvectors):", pca.components_)

features = numeric_cols # data_std.columns
# components = [f'PC{i+1}' for i in range(principal_components.shape[0])]
data_df = pd.DataFrame(pca.components_, columns=numeric_cols, index=[f'PC{i+1}' for i in range(3)])



import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
sns.heatmap(data_df, annot=True, cmap='coolwarm', center=0)
plt.title("PCA Component Loadings Heatmap")
plt.show()



############### solution  given in the course
# Compute the first 3 principal components
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

pca = PCA(n_components=3)
X_pca = pca.fit_transform(X)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(X_pca[:, 0], X_pca[:, 1], X_pca[:, 2], c=y, cmap='viridis')
legend1 = ax.legend(*scatter.legend_elements(), title="Classes")
ax.add_artist(legend1)
ax.set_title('True Clusters of Iris Dataset')
plt.show()