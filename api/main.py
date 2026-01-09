from fastapi import FastAPI, HTTPException
import random
import requests
import time
app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running"}
_last_random = None
_last_time = 0

@app.get("/api/random-number")
@app.head("/api/random-number") 
def random_number(a: int = 1, b: int = 10):
    global _last_random, _last_time

    if a > b:
        raise HTTPException(status_code=400, detail="Parameter a must be <= b")
    
    # cache result for 5 seconds
    if time.time() - _last_time > 5:
        _last_random = random.randint(a, b)
        _last_time = time.time()

    return {"random_number": _last_random}
crypto_ids = [
    "bitcoin",
    "ethereum",
    "tether",
    "binancecoin",
    "cardano",
    "ripple",
    "solana",
    "dogecoin",
    "polkadot",
    "litecoin",
    "tron",
    "shiba-inu",
    "avalanche-2",
    "chainlink",
    "stellar",
    "vechain",
    "internet-computer",
    "filecoin",
    "polygon-ecosystem-token",
    "apecoin"
]
fiats = [
    "USD", "EUR", "GBP", "JPY", "AUD",
    "CAD", "CHF", "CNY", "SEK", "NZD",
    "MXN", "SGD", "HKD", "NOK", "KRW",
    "RUB", "INR", "BRL", "ZAR", "TRY"
]
@app.get("/api/api")
def api():
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(crypto_ids)}&vs_currencies={','.join(fiats)}"
    headers = {"x-cg-demo-api-key": "CG-XKRuMT9EEd72qU8ASpKci4Wt"}
    data = requests.get(url, headers=headers).json()
    return data

