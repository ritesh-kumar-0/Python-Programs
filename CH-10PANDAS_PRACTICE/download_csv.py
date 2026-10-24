import requests

# Paste the CSV URL provided by Coursera
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"

# Download the file
response = requests.get(url, timeout=30)

# Check whether the request succeeded
response.raise_for_status()

# Save the CSV file on your computer
with open("Product-sales.csv", "wb") as file:
    file.write(response.content)

print("CSV downloaded successfully!")