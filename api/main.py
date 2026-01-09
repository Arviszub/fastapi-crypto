from fastapi import FastAPI
import random
import requests
app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/api/random-number")
def random_number(a: int, b: int):
    return {
        random.randint(a, b)
    }
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
@app.get("/api/health")
def health_check():
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(crypto_ids)}&vs_currencies={','.join(fiats)}"
    headers = {"x-cg-demo-api-key": "CG-XKRuMT9EEd72qU8ASpKci4Wt"}
    data = requests.get(url, headers=headers).json()
    return data

