"""
Stock Market Prediction using Scikit-Learn

Requirements:
    pip install pandas numpy yfinance scikit-learn matplotlib

Usage:
    python stock_predictor.py

Change STOCK_SYMBOL below to predict another stock.
"""

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# --------------------------------------------------
# Configuration
# --------------------------------------------------

STOCK_SYMBOL = "AAPL"

START_DATE = "2018-01-01"
END_DATE = None

TEST_SIZE = 0.20

RANDOM_STATE = 42


# --------------------------------------------------
# Download Data
# --------------------------------------------------

print(f"Downloading {STOCK_SYMBOL} historical data...")

data = yf.download(
    STOCK_SYMBOL,
    start=START_DATE,
    end=END_DATE,
    progress=False
)

if len(data) == 0:
    raise Exception("No data downloaded.")

print(f"{len(data)} trading days downloaded.\n")


# --------------------------------------------------
# Feature Engineering
# --------------------------------------------------

data["Daily_Return"] = data["Close"].pct_change()

data["MA5"] = data["Close"].rolling(5).mean()
data["MA10"] = data["Close"].rolling(10).mean()
data["MA20"] = data["Close"].rolling(20).mean()
data["MA50"] = data["Close"].rolling(50).mean()

data["Volatility"] = data["Daily_Return"].rolling(10).std()

data["Momentum"] = data["Close"] - data["Close"].shift(10)

data["High_Low"] = data["High"] - data["Low"]

data["Open_Close"] = data["Open"] - data["Close"]

# Target:
# 1 = Tomorrow closes higher
# 0 = Tomorrow closes lower

data["Target"] = (
    data["Close"].shift(-1) > data["Close"]
).astype(int)

data.dropna(inplace=True)


# --------------------------------------------------
# Prepare Dataset
# --------------------------------------------------

features = [
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
    "Daily_Return",
    "MA5",
    "MA10",
    "MA20",
    "MA50",
    "Momentum",
    "Volatility",
    "High_Low",
    "Open_Close"
]

X = data[features]
y = data["Target"]

split = int(len(data) * (1 - TEST_SIZE))

X_train = X.iloc[:split]
X_test = X.iloc[split:]

y_train = y.iloc[:split]
y_test = y.iloc[split:]


# --------------------------------------------------
# Train Model
# --------------------------------------------------

print("Training Random Forest...")

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=10,
    random_state=RANDOM_STATE
)

model.fit(X_train, y_train)


# --------------------------------------------------
# Evaluate
# --------------------------------------------------

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\n==============================")
print("MODEL PERFORMANCE")
print("==============================")

print(f"Accuracy : {accuracy:.2%}")

print("\nClassification Report")
print(classification_report(y_test, predictions))

print("Confusion Matrix")
print(confusion_matrix(y_test, predictions))


# --------------------------------------------------
# Feature Importance
# --------------------------------------------------

importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    "Importance",
    ascending=False
)

print("\nMost Important Features\n")
print(importance)


# --------------------------------------------------
# Predict Tomorrow
# --------------------------------------------------

latest = X.iloc[-1:]

prediction = model.predict(latest)[0]
probability = model.predict_proba(latest)[0]

print("\n==============================")
print("NEXT DAY PREDICTION")
print("==============================")

if prediction == 1:
    print("Prediction : UP")
else:
    print("Prediction : DOWN")

print(f"Probability DOWN : {probability[0]:.2%}")
print(f"Probability UP   : {probability[1]:.2%}")


# --------------------------------------------------
# Plot Actual vs Prediction
# --------------------------------------------------

test_dates = data.index[split:]

plt.figure(figsize=(12,6))

plt.plot(
    test_dates,
    y_test.values,
    label="Actual",
    linewidth=2
)

plt.plot(
    test_dates,
    predictions,
    label="Predicted",
    alpha=0.7
)

plt.title(f"{STOCK_SYMBOL} Direction Prediction")

plt.xlabel("Date")
plt.ylabel("Direction (0=Down, 1=Up)")
plt.legend()

plt.tight_layout()

plt.show()