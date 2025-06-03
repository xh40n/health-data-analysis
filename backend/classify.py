# Simple rule-based classification (no ML model)
data = [
    {"sleep": 7, "heart_rate": 72, "steps": 8000},
    {"sleep": 5, "heart_rate": 85, "steps": 3000}
]

for record in data:
    if record["sleep"] >= 7 and record["heart_rate"] < 80:
        print(f"Day {data.index(record)+1}: Good")
    elif record["sleep"] >= 5:
        print(f"Day {data.index(record)+1}: Moderate")
    else:
        print(f"Day {data.index(record)+1}: Poor")
