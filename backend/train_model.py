import pandas as pd
import random
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

data = []

for _ in range(3000):
    cost = random.randint(50, 300)
    price = random.randint(cost + 10, cost + 250)
    sold = random.randint(5, 120)
    discount = random.randint(0, 40)

    revenue = price * sold
    profit = (price - cost) * sold

    # Avoid divide by zero
    margin = profit / revenue if revenue != 0 else 0

    # Realistic trend generation
    if profit > 6000 and sold > 60 and margin > 0.25:
        trend = 2   # Up
    elif profit > 2000 and sold > 25:
        trend = 1   # Stable
    else:
        trend = 0   # Down

    data.append([
        cost, price, sold, discount, profit, margin, trend
    ])

df = pd.DataFrame(data, columns=[
    "cost", "price", "sold", "discount", "profit", "margin", "trend"
])

X = df[["cost", "price", "sold", "discount", "profit", "margin"]]
y = df["trend"]

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X, y)

dump(model, "model.pkl")

print("✅ Smart sales trend model trained successfully!")
