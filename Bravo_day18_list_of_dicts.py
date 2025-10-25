""" bravo_day18_list_of_dicts.py - examples of list of dictionaries"""
# Bravo_day18_list_of_dicts.py

# list of dictionaries
students = [{"name": "Asha", "score": 82}, {"name": "Brian", "score": 90}, {"name": "Carol", "score": 76}]

# print names who passed (>=80)
passed = [s["name"] for s in students if s["score"] >=80]
print("Passed:", passed)

# sort students by score descending
students_sorted = sorted(students, key=lambda s: s["score"], reverse=True)
print("Top student:", students_sorted[0]["name"], students_sorted[0]["score"])
