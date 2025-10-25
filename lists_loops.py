"""lists_loops.py - Demonstrates list and dictionary operations along with loops in Python."""

# lists_loops.py

students = ["Asha", "Brian", "Carol"]
grades = {"Asha": 82, "Brian": 90, "Carol": 76}

# iterate list
for s in students:
    print("Student:", s)

# iterate with index
for i, s in enumerate(students, start=1):
    print(f"{i}. {s}")

# list operations
students.append("Diana")
students.remove("Carol")  # removes first match

# iterate dict
for name, score in grades.items():
    print(f"{name} -> {score}")

# list comprehension example: students with scores
passed = [name for name, score in grades.items() if score >= 80]
print("Passed:", passed)



