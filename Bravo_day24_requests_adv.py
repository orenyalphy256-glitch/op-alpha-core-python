""" Bravo_day24_requests_adv.py - Example of making an advanced HTTP GET request using the requests library"""
# Bravo_day24_requests_adv.py

# Import the requests library
import requests

# Define the URL and parameters for the GET request
url = "https://httpbin.org/get"
params = {"q": "python", "page": 1}
headers = {"User-Agent": "my-app/0.0.1"}

# Make the GET request with parameters and headers
r = requests.get(url, params=params, headers=headers, timeout=10)
print("URL requested:", r.url)
print("Status code:", r.status_code)
print("Response keys:", list(r.json().keys()))