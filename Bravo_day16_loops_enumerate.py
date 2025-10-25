""" Bravo_day16_loops_enumerate.py - Demonstrate loops and enumerate function."""
# Bravo_day16_loops_enumerate.py
# Purpose: demonstrate loops and enumerate function.

# List of items to iterate over
items = ["alpha", "bravo", "charlie"]

# simple loop
for item in items:
    print("Item:", item)

    # loop with index (zero-based)
    for i in range(len(items)):
        print(f"Index {i} -> {items[i]}")

        # enumerate (human-friendly starting at 1)
        for idx, value in enumerate(items, start=1):
            print(f"{idx}. {value}")