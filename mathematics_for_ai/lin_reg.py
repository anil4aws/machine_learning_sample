import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
import numpy as np

df = pd.read_csv('salary_data.csv')

# print(df.head(5))
df = df.drop(columns=['EmpNum'])

# corr_matrix = df.corr()

# salary_corr = corr_matrix['Salary'].drop('Salary').abs()

# # Sort and get top 3
# top_3 = salary_corr.sort_values(ascending=False).head(3)

# # Display the result
# print("Top 3 variables most correlated with Salary:")
# print(top_3)

# X = df[["JobGrade6", "JobGrade1", "YrsExper"]]
# y = df["Salary"]
y = df["Salary"]
X = df 

# for col in df.columns:
#     # df[col].fillna(df[col].mean(), inplace=True)
#     df.fillna({col: df[col].mean()}, inplace=True)
# X = df


pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),     # or 'median'
    ("model", LinearRegression())
])



# Step 4: Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.3,
                                                    random_state=42)



# # Step 5: Fit the model
# model = LinearRegression()
# model.fit(X_train, y_train)

# # Step 6: Extract coefficients
# intercept = model.intercept_
# coefs = dict(zip(X.columns, model.coef_))
# r2 = model.score(X_test, y_test)

pipeline.fit(X, y)
intercept = pipeline.named_steps["model"].intercept_
coefs = pipeline.named_steps["model"].coef_
r2 = pipeline.score(X_test, y_test)
print("Intercept:", intercept)
print("Coefs:", dict(zip(X.columns, coefs)))

print("Intercept:", intercept)
print("Coefficients:", coefs)
print("Test R²:", r2)