# import copy

def generate_data():
    return [
        {"id": 1, "data": {"files": ["a.txt", "b.txt"], "usage": 500}},
        {"id": 2, "data": {"files": ["c.txt"], "usage": 300}}
    ]

def replicate_data(users):
    assigned = users
    shallow = list(users)
    deep = copy.deepcopy(users)
    return assigned, shallow, deep

def modify_data(data):
    for user in data:
        user["data"]["files"].append("new_file.txt")
        user["data"]["usage"] += 100

def check_integrity(original, shallow, deep):
    leakage = 0
    safe = 0
    overlap_total = 0

    for i in range(len(original)):
        o = original[i]["data"]["files"]
        s = shallow[i]["data"]["files"]
        d = deep[i]["data"]["files"]

        if o == s:
            leakage += 1

        if o != d:
            safe += 1

        overlap_total += len(set(o) & set(d))

    return (leakage, safe, overlap_total)

def main():
    original = generate_data()
    print("Before:", original)

    assigned, shallow, deep = replicate_data(original)

    modify_data(shallow)

    print("\nAfter:")
    print("Original:", original)
    print("Shallow:", shallow)
    print("Deep:", deep)

    report = check_integrity(original, shallow, deep)
    print("\nReport:", report)

main()
