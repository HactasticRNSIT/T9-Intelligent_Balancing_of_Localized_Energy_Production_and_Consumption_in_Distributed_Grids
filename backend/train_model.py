import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
data = pd.read_csv("energy_data.csv")

# Inputs
X = data[["time", "solar_output", "battery_level", "temperature"]]

# Output
y = data["demand"]

# Create AI model
model = LinearRegression()

# Train model
model.fit(X, y)

# Test prediction
prediction = model.predict([[14, 80, 70, 34]])

print("Predicted Demand:", prediction[0])

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("AI Model Saved")