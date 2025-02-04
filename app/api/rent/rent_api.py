import os
import requests
from dotenv import load_dotenv

load_dotenv()

SALE_URL = os.getenv("YAD2_API_RENT")

def get_rent_houses(filters):
    response = requests.get(f"{SALE_URL}{filters}")
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"API Error: {response.status_code}, Message: {str(response)}")
