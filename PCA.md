# PCA 
PCA (Principal Component Analysis) are common steps for dimensionality reduction and feature extraction.

### Step 1: Standardize the data
 PCA is affected by scale, so standardizing ensures each feature contributes equally
 PCA is sensitive to the magnitude of features. Standardization rescales features to have mean = 0 and standard deviation = 1


`scaler = StandardScaler()
data_std = scaler.fit_transform(data)
`

### Step 2: Apply PCA
Choose the number of principal components you want to keep. Here, n_components=2
PCA(n_components=k) reduces the dataset to k principal components.
fit_transform() computes the principal components and projects the original standardized data onto them.
`pca = PCA(n_components=2)
principal_components = pca.fit_transform(data_std)
`

### Step 3: View PCA results
principal_components contains the transformed data in the reduced space.
explained_variance_ratio_ shows the proportion of total variance captured by each principal component.
components_ gives the principal axes in terms of the original feature space (eigenvectors).
`
print("Principal Components:", principal_components)
print("Explained Variance Ratio:", pca.explained_variance_ratio_)
print("Principal Axes (Eigenvectors):", pca.components_)
`


### Step 4: Optional - Reconstructing data approximation using selected components
You can use inverse_transform() to reconstruct an approximation of the original data from the reduced components.
`
data_approx = pca.inverse_transform(principal_components)
print("Approximation of original data using 2 components:", data_approx)
`
### step 5 :Convert to DataFrame for Heatmap
import numpy as np

Create a DataFrame for easier visualization
`
import pandas as pd
features = numeric_data.columns
components = [f'PC{i+1}' for i in range(loadings.shape[0])]
loadings_df = pd.DataFrame(loadings, columns=features, index=components)
`

# Step 5 — Plot Heatmap
`
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
sns.heatmap(loadings_df, annot=True, cmap='coolwarm', center=0)
plt.title("PCA Component Loadings Heatmap")
plt.show()
`