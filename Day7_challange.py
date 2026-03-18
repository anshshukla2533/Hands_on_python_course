readings = []
n = int(input("Enter how many readings you have: "))

for i in range(n):
    readings.append(int(input(f"Enter Energy reading of building {i+1}: ")))

categories = {
    "efficient": [],
    "moderate": [],
    "high": [],
    "invalid": []
}

for energy in readings:
    if energy < 0:
        categories["invalid"].append(energy)
    elif 0 <= energy <= 50:
        categories["efficient"].append(energy)
    elif 51 <= energy <= 150:
        categories["moderate"].append(energy)
    else:
        categories["high"].append(energy)

valid_readings = [energy for energy in readings if energy >= 0]

total_consumpt = 0
for energy in valid_readings:
    total_consumpt += energy

efficient_count = len(categories["efficient"])
moderate_count = len(categories["moderate"])
high_count = len(categories["high"])

if total_consumpt > 600:
    result = "Energy Waste Detected"
elif high_count > 3:
    result = "Overconsumption"
elif abs(efficient_count - moderate_count) <= 1:
    result = "Balanced Usage"
elif efficient_count > moderate_count:
    result = "Efficient Campus"
else:
    result = "Moderate Usage"

stats = (total_consumpt, len(readings), result)

print("\n--- Energy Report ---\n")
print("Categorized Readings:")
print(categories)

print("\nTotal Energy Consumption: {stats[0]}")
print("Buildings Count: {stats[1]}")
print("Efficiency Result: {stats[2]}")
