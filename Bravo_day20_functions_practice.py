""" Bravo_day20_functions_practice.py - examples of defining and using functions"""
# Bravo_day20_functions_practice.py

# define functions
def greet(name):
    """Return greeting for given name."""
    return f"Hello, {name}"

# function to calculate average
def average(nums):
    """Return average of list of numbers. Return None if empty."""
    if not nums:
        return None
    return sum(nums) / len(nums)

# usage
print(greet("Alphonce"))
print("Average of [10, 20, 30]:", average([10, 20, 30]))
print("Average of []:", average([]))
