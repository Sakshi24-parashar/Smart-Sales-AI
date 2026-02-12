import pandas as pd
import random
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

data = []

for _ in range(2000):
    cost = random.randint(50, 300)
    price = random.randint(cost+10, cost+200)
    sold = random.randint(1, 100)
    discount = random.randint(0, 30)

    profit = (price - cost) * sold

    if sold > 60:
        trend = 2   # Up
    elif sold > 30:
        trend = 1   # Stable
    else:
        trend = 0   # Down

    data.append([cost, price, sold, discount, profit, trend])

df = pd.DataFrame(data, columns=[
    "cost","price","sold","discount","profit","trend"
])

X = df[["cost","price","sold","discount","profit"]]
y = df["trend"]

model = RandomForestClassifier()
model.fit(X, y)

dump(model, "model.pkl")

print("Model trained and saved!")
