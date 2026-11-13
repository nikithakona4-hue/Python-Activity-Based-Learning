seats = [[101, 102, 0], [103, 101, 105]]
reserved = [(0, 2)]
seen = set()
for i, row in enumerate(seats):
    for j, roll in enumerate(row):
        if (i, j) in reserved: print("Reserved:", i, j)
        elif roll == 0: print("Empty:", i, j)
        elif roll < 100 or roll > 110: print("Invalid:", roll)
        elif roll in seen: print("Duplicate:", roll)
        else: seen.add(roll); print("Valid:", roll)
