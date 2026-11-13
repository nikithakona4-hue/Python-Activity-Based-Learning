products = ["Laptop", "Phone", "Tablet"]
prices = [[1000, 1200], [800, 760], [500, 600]]
threshold = 15
changes = []
for i in range(3):
    change = (prices[i][1]-prices[i][0])/prices[i][0]*100
    changes.append(abs(change))
    print(products[i], "Change:", round(change, 2), "%")
    if abs(change) > threshold: print("Flagged")
print("Maximum fluctuation:", products[changes.index(max(changes))])
