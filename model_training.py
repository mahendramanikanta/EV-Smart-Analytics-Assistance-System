# model_training.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
ev_data = pd.read_csv("data/ev_data.csv")

# Select useful columns
features = ['Model Year', 'Base MSRP']
target = 'Electric Range'

# Drop rows with missing values
ev_data = ev_data[features + [target]].dropna()

# Split data
X = ev_data[features]
y = ev_data[target]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
model = LinearRegression()
model.fit(X_scaled, y)

# Save model and scaler
pickle.dump(model, open('models/model.pkl', 'wb'))
pickle.dump(scaler, open('models/scaler.pkl', 'wb'))

print("✅ Model and Scaler saved successfully!")
