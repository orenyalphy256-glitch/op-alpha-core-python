"""fetch_example_offline.py — simulate API response for offline testing."""

def fetch_offline():
    sample = {
        "origin": "127.0.0.1",
        "headers": {"User-Agent": "offline-test-agent"},
    }
    print("Status: 200")
    print("Origin:", sample["origin"])
    print("User-Agent:", sample["headers"]["User-Agent"])
    print("All header keys:", list(sample["headers"].keys()))

if __name__ == "__main__":
    fetch_offline()
    