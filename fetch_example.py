"""fetch_example.py — fetch JSON from httpbin.org and print key info."""

import requests

def fetch():
    url = "https://httpbin.org/get"
    try:
        r = requests.get(url, timeout=10)   # 10 second timeout
        print("Status:", r.status_code)
        if r.status_code != 200:
            print("Non-OK status, body preview:", r.text[:200])
            return
        data = r.json()                      # parse JSON to python dict
        print("Origin (your IP):", data.get("origin"))
        headers = data.get("headers", {})
        print("User-Agent:", headers.get("User-Agent"))
        print("All header keys:", list(headers.keys()))
    except requests.Timeout:
        print("Request timed out.")
    except requests.RequestException as e:
        print("Request failed:", e)

if __name__ == "__main__":
    fetch()
    