import requests

url = "http://www.google.com"
resp = requests.get(url)

print(f"Your request to {url} came back with status: {resp.status_code}")
