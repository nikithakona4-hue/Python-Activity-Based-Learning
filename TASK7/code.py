orders = [100, 80, 120]
dispatched = [80, 70, 130]
returned = [10, 5, 10]
inventory = [50, 40, 60]
for i in range(3):
    if dispatched[i] > orders[i] or returned[i] > dispatched[i]:
        print("Inconsistent Record:", i+1)
    else:
        print("Outstanding:", orders[i]-dispatched[i], "Inventory:", inventory[i]+returned[i])
print("Order Analysis Completed")
