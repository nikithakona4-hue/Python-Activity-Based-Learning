areas = ["Area A", "Area B", "Area C"]
demand = [[100, 120], [150, 160], [130, 140]]
supply = [[80, 100], [100, 110], [120, 130]]
shortage = []
for i in range(3):
    shortage.append(sum(demand[i]) - sum(supply[i]))
    print(areas[i], "Shortage:", shortage[i])
worst = shortage.index(max(shortage))
print("Most underserved area:", areas[worst])

