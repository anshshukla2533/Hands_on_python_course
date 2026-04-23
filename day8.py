import random
import pandas as pd
import numpy as np
import math
def generate_data(n):
    data = []
    for i in range(1, n+1):
        record = {
            "zone": i,
            "traffic": random.randint(0, 100),
            "air_quality": random.randint(0, 300),
            "energy": random.randint(0, 500)
        }
        data.append(record)
    return data
def custom_sort(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i]["traffic"] > data[j]["traffic"]:
                data[i], data[j] = data[j], data[i]
    return data
def classify_zones(data):
    result = {}
    for d in data:
        if d["air_quality"] > 200 or d["traffic"] > 80:
            result[d["zone"]] = "High Risk"
        elif d["energy"] > 400:
            result[d["zone"]] = "Energy Critical"
        elif d["traffic"] < 30 and d["air_quality"] < 100:
            result[d["zone"]] = "Safe Zone"
        else:
            result[d["zone"]] = "Moderate"
    return result
def calculate_risk(df):
    df["risk_score"] = df["traffic"]*0.45 + df["air_quality"]*0.35 + df["energy"]*0.2
    df["risk_transform"] = df["risk_score"].apply(lambda x: math.sqrt(x))
    return df
def analyze(df):
    arr = df[["traffic", "air_quality", "energy"]].values
    mean_vals = np.mean(arr, axis=0)
    top3 = df.sort_values(by="risk_score", ascending=False).head(3)
    max_risk = df["risk_score"].max()
    avg_risk = df["risk_score"].mean()
    min_risk = df["risk_score"].min()
    return mean_vals, top3, (max_risk, avg_risk, min_risk)

def system_decision(avg):
    if avg < 100:
        return "City Stable"
    elif avg < 200:
        return "Moderate Risk"
    elif avg < 300:
        return "High Alert"
    else:
        return "Critical Emergency"
def main():
    roll = 24110011321
    data = generate_data(18)
    data = custom_sort(data)
    categories = classify_zones(data)
    df = pd.DataFrame(data)
    df = calculate_risk(df)
    mean_vals, top3, stats = analyze(df)
    decision = system_decision(stats[1])
    print("Data:\n", df)
    print("\nCategories:\n", categories)
    print("\nTop 3 Risk Zones:\n", top3)
    print("\nStats (max, avg, min):", stats)
    print("\nDecision:", decision)
    
