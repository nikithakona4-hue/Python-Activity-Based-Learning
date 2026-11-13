appliances = ["Fan", "AC", "Light"]
before = [100, 300, 80]
after = [70, 180, 40]
savings = []
for i in range(3):
    saved = before[i] - after[i]
    percent = saved / before[i] * 100
    savings.append((appliances[i], percent))
    print(appliances[i], "Savings:", round(percent, 2), "%")
savings.sort(key=lambda x: x[1], reverse=True)
print("Ranking:", savings)
