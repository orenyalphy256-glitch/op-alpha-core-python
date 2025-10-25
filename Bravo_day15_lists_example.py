"""Bravo_day15_lists_example.py - Demonstrate list operations in python."""
# Bravo_day15_lists_example.py
# Purpose: demonstrate list creation, indexing, append, insert, remove, and slicing.

# Create a list of devices
devices = ["router", "laptop", "phone", "tablet"]
print("Initial list:", devices)

# Access first and last
first = devices[0]
last = devices[-1]
print("First:", first)
print("Last:", last)

# Add a device to end
devices.append("printer")
print("After append:", devices)

# Insert at second position (index 1)
devices.insert(1, "smartwatch")
print("After insert:", devices)

# Remove an item by value
devices.remove("phone")
print("After remove:", devices)

# Slicing: get first three items
slice_first_three = devices[0:3]
print("First three;", slice_first_three)
