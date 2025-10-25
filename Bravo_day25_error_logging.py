""" Bravo_day25_error_logging.py - Example of logging errors to a file with timestamps."""
# Bravo_day25_error_logging.py

# Import necessary libraries
import time
import requests

# Define the log file name
LOGFILE = "errors_bravo.txt"

# Function to log errors with a timestamp
def log_error(msg):
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(f"{ts} - {msg}\n")

# Example usage: Log an error message
try:
    r= requests.get("https://httpbin.org/status/500", timeout=5)
    r.raise_for_status()
except requests.RequestException as e:
    print("Request failed:", e)
    log_error(str(e))