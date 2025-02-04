import os

from dotenv import load_dotenv

load_dotenv()

URL_YAD2_SALE = os.getenv("YAD2_API_SALE")

def get_by_city(city):
    filteres = {
        "city": "0070",
        "propertyGroup": [
            "apartments",
            "2Chouses"
        ],
        "price": "-1-3000000",
        "squaremeter": "-1-200",
        "floor": "-1-3",
        "imageOnly": 1,
        "priceOnly": 1
    }




