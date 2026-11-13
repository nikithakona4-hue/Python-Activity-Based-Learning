names = ["Asha", "Ravi", "Priya"]
marks = [35, 75, 45]
attendance = [60, 90, 70]
lab = [30, 80, 40]
for i in range(3):
    risks = [marks[i] < 40, attendance[i] < 75, lab[i] < 40]
    count = sum(risks)
    level = "High" if count >= 2 else "Medium" if count == 1 else "Low"
    print(names[i], "Risk:", level, "Factors:", count)
print("High risk students:", sum(1 for i in range(3) if sum([marks[i]<40, attendance[i]<75, lab[i]<40]) >= 2))
