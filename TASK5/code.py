activities = ["Sports", "Library", "Lab"]
demand = [50, 30, 40]
available = 90
priority = [0, 1, 2]
allocation = [0, 0, 0]
for i in priority:
    allocation[i] = min(demand[i], available)
    available -= allocation[i]
    print(activities[i], "Allocated:", allocation[i], "Shortage:", demand[i]-allocation[i])
print("Remaining resources:", available)
