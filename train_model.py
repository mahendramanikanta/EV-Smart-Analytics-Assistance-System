import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pickle
import os

# Load your dataset (update filename if needed)
df = pd.read_csv('data/ev_data.csv')

# Select relevant numeric columns
df = df[['Model Year', 'Base MSRP', 'Electric Range']].dropna()

# Features (X) and Target (y)
X = df[['Model Year', 'Base MSRP']]
y = df['Electric Range']

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Create models folder if not exists
os.makedirs('models', exist_ok=True)

# Save the model and scaler
pickle.dump(model, open('models/model.pkl', 'wb'))
pickle.dump(scaler, open('models/scaler.pkl', 'wb'))

print("✅ Model and scaler saved successfully in 'models/' folder!")
