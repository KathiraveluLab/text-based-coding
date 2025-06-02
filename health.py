# python -m pip install scikit-learn pandas numpy

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Simulated healthcare dataset
data = {
    'age': [25, 45, 35, 50, 23, 40, 60, 48, 33, 55],
    'blood_pressure': [120, 140, 130, 150, 118, 135, 160, 145, 128, 155],
    'cholesterol': [200, 250, 230, 270, 190, 240, 280, 260, 220, 275],
    'has_disease': [0, 1, 1, 1, 0, 1, 1, 1, 0, 1]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Features and target
X = df[['age', 'blood_pressure', 'cholesterol']]
y = df['has_disease']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Normalize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train_scaled, y_train)

# Make predictions
y_pred = model.predict(X_test_scaled)

# Print predictions and actual values
print("Predicted labels:", y_pred)
print("Actual labels:", y_test.values)

# Compare in DataFrame
comparison_df = pd.DataFrame({'Actual': y_test.values, 'Predicted': y_pred})
print("\nActual vs Predicted Labels:\n", comparison_df)

# Evaluate the model
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
