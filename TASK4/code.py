regs = [(101, "Python"), (102, "Java"), (101, "Python"), (103, "Python")]
seen = set()
for student, course in regs:
    if (student, course) in seen:
        print("Duplicate:", student, course)
    else:
        seen.add((student, course))
    if course == "Java" and student == 101:
        print("Rule Violation:", student)
    else:
        print("Valid:", student, course)

