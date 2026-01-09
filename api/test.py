import requests

r = requests.get("https://fastapi-crypto-kyth.onrender.com/api/api")
print(r.json())