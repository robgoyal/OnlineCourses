import requests

url = "https://icanhazdadjoke.com/"

resp = requests.get(url, headers={"Accept": "application/json"})

data = resp.json()
print(data["joke"])
