import os
import requests
from dotenv import load_dotenv

from app.api.yad2_const import yad2_api_rent

load_dotenv()


def get_rent_houses(filters):
    response = requests.get(f"{yad2_api_rent}{filters}")
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"API Error: {response.status_code}, Message: {str(response)}")
