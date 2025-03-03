# Modify the API retry example to log exceptions to a file.

import requests
import time
import logging

# Set up basic logging to a file named 'errors.log'
logging.basicConfig(filename='errors.log', level=logging.ERROR)

def fetch_api(url, retries=3):
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise error for bad responses
            return response.json()       # Assume API returns JSON
        except Exception as e:
            logging.error(f"Attempt {attempt} failed: {e}")
            print(f"Attempt {attempt} failed: {e}")
            time.sleep(1)  # Wait for 1 second before retrying
    return None

# Example usage
data = fetch_api("https://api.example.com/data")  # Replace with a real API URL
if data:
    print("Data fetched successfully!")
else:
    print("Failed to fetch data after several attempts.")
