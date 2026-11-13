students = [("Asha", 90, 85, 100000), ("Ravi", 80, 90, 150000), ("Priya", 95, 95, 80000), ("John", 60, 70, 200000)]
quota = 2
eligible = []
for name, marks, attendance, income in students:
    if marks >= 70 and attendance >= 75 and income <= 150000:
        eligible.append((name, marks))
eligible.sort(key=lambda x: x[1], reverse=True)
selected = eligible[:quota]
print("Eligible:", eligible)
print("Scholarship Selected:")
for student in selected:
    print(student)
