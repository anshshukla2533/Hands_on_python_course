import random
import copy
import pandas as pd
import numpy as np
import math


def generate_data(n=15):
    data = []
    for i in range(1, n+1):
        record = {
            "zone": i,
            "metrics": {
                "traffic": random.randint(50, 200),
                "pollution": random.randint(30, 150),
                "energy": random.randint(100, 300)
            },
            "history": [random.randint(10, 100) for _ in range(5)]
        }
        data.append(record)
    return data



def rotate_data(data, k=3):
    return data[k:] + data[:k]



def to_dataframe(data):
    rows = []
    for d in data:
        rows.append({
            "zone": d["zone"],
            "traffic": d["metrics"]["traffic"],
            "pollution": d["metrics"]["pollution"],
            "energy": d["metrics"]["energy"]
        })
    return pd.DataFrame(rows)


# -------------------------------
# 4. Custom Risk Function
# -------------------------------
def custom_risk_score(t, p, e):
    return math.log(t + p + e)



def mutate_data(data):
    for d in data:
        d["metrics"]["traffic"] += 10
        d["history"].append(random.randint(50, 120))
        d["risk"] = custom_risk_score(
            d["metrics"]["traffic"],
            d["metrics"]["pollution"],
            d["metrics"]["energy"]
        )


def manual_correlation(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = math.sqrt(np.sum((x - x_mean)**2) * np.sum((y - y_mean)**2))

    return numerator / denominator



def analyze(df):
    traffic = df["traffic"].values
    pollution = df["pollution"].values

    mean = np.mean(traffic)
    std = np.std(traffic)
    variance = np.var(traffic)

    correlation = manual_correlation(traffic, pollution)

    anomalies = df[df["traffic"] > mean + std]["zone"].tolist()

    return mean, variance, correlation, anomalies


def stability_index(variance):
    return 1 / (variance + 1)



def detect_clusters(risk_list, threshold):
    clusters = []
    current = []

    for i, r in enumerate(risk_list):
        if r > threshold:
            current.append(i)
        else:
            if len(current) > 1:
                clusters.append(current)
            current = []

    if len(current) > 1:
        clusters.append(current)

    return clusters


data = generate_data()

print("\n--- ORIGINAL DATA ---")
print(data)

# Rotate (ODD rule)
data = rotate_data(data)

# Copies
assigned_copy = data
shallow_copy = copy.copy(data)
deep_copy = copy.deepcopy(data)

# Mutate shallow copy
mutate_data(shallow_copy)

print("\n--- AFTER MUTATION ---")
print("\nOriginal Data (check corruption):")
print(data)

print("\nShallow Copy:")
print(shallow_copy)

print("\nDeep Copy (safe):")
print(deep_copy)


df = to_dataframe(data)
print("\n--- DATAFRAME ---")
print(df)


mean, var, corr, anomalies = analyze(df)


risk_values = [d.get("risk", 0) for d in data]
max_risk = max(risk_values)
min_risk = min(risk_values)

stability = stability_index(var)

clusters = detect_clusters(risk_values, mean)


if stability > 0.5:
    decision = "System Stable"
elif len(anomalies) < 3:
    decision = "Moderate Risk"
elif len(anomalies) < 6:
    decision = "High Corruption Risk"
else:
    decision = "Critical Failure"


print("\n--- RESULTS ---")
print("Anomaly Zones:", anomalies)
print("Tuple Output:", (max_risk, min_risk, stability))
print("Clusters:", clusters)
print("Final Decision:", decision)
