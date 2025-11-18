# model_training.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
df = pd.read_csv("data/ev_data.csv")
df.columns = df.columns.str.strip()

# Feature selection
X = df[["Model Year", "Base MSRP"]]
y = df["Electric Range"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Save files
pickle.dump(model, open("models/model.pkl", "wb"))
pickle.dump(scaler, open("models/scaler.pkl", "wb"))

print("Model and Scaler saved successfully!")


from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Predictions
y_pred = model.predict(X_test)

# Metrics
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print("R² Score:", r2)
print("MAE:", mae)
print("MSE:", mse)

