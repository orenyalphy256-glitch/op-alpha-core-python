"""exceptions_example.py — demo of try/except/else/finally and error logging."""

import time

LOGFILE = "errors_day11.txt"

def read_int(prompt):
    """Prompt until the user enters a valid integer. Log invalid attempts."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError as e:
            print("Please enter a whole number (e.g., 27).")
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            with open(LOGFILE, "a", encoding="utf-8") as log:
                log.write(f"{timestamp} - ValueError: {e}\n")
            # loop continues to ask again
        else:
            return value
        finally:
            # optional: you can add cleanup actions here
            pass

if __name__ == "__main__":
    age = read_int("Enter your age: ")
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")