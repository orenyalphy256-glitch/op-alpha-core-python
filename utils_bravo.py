""" utils_bravo.py - Utility functions for formatting names"""
# utils_bravo.py

# Function to format names
def format_name(first, last):
    """Return properly formatted full name."""
    return f"{first.strip().title()} {last.strip().title()}"