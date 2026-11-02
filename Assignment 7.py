import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
columns = [
    "mpg", "cylinders", "displacement", "horsepower",
    "weight", "acceleration", "model_year", "origin", "car_name"
]

df = pd.read_csv(
    url,
    names=columns,
    delim_whitespace=True,
    na_values="?"
)

df = df.drop(columns=["car_name"])
df["horsepower"] = df["horsepower"].fillna(df["horsepower"].median())

df = pd.get_dummies(df, columns=["origin"], drop_first=True, dtype=int)

X = df.drop(columns=["mpg"])
y = df["mpg"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("Model Evaluation Metrics:")
print(f"R-squared (R2) Score        : {r2:.4f}")
print(f"Mean Absolute Error (MAE)    : {mae:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")

coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
}).sort_values(by="Coefficient", ascending=False)

print("\nFeature Coefficients (Impact on MPG):")
print(coefficients.to_string(index=False))
print(f"\nIntercept: {model.intercept_:.4f}")


#Model Evaluation Metrics:
#R-squared (R2) Score        : 0.8449
#Mean Absolute Error (MAE)    : 2.2882
#Root Mean Squared Error (RMSE): 2.8877

#Feature Coefficients (Impact on MPG):
#     Feature  Coefficient
#    origin_2     2.946907
#    origin_3     2.671126
#  model_year     0.825969
#acceleration     0.067967
#displacement     0.019776
#      weight    -0.007047
#  horsepower    -0.014562
#   cylinders    -0.165664

#Intercept: -21.8577