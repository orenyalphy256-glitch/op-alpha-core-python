""" Bravo_day17_dicts.py - Demonstrate dictionary operations."""
# Bravo_day17_dicts.py

# create a dictionary
scores = {"Asha": 82, "Brian": 90, "Carol": 76}
print("All keys:", list(scores.keys()))
print("All values:", list(scores.values()))
print("Asha's score:", scores.get("Asha"))
          
# Safe access with default
print("Nonexistent:", scores.get("Daniel", "No score"))

# iterate key, value
for name, score in scores.items():
        print(f"{name} -> {score}")

# update a value
scores["Carol"] = 80
print("Updated Carol:", scores["Carol"])