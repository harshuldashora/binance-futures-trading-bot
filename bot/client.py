import os

from dotenv import load_dotenv
from binance.client import Client


load_dotenv()


def get_client():

    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    if not api_key or not api_secret:
        raise ValueError(
            "API credentials not found in .env file"
        )

    client = Client(
        api_key=api_key,
        api_secret=api_secret,
        testnet=True
    )

    client.FUTURES_URL = (
        "https://testnet.binancefuture.com/fapi"
    )

    return client