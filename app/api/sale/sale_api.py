import functools
import os
import random
import time
import requests
from dotenv import load_dotenv
from app.api.models.city_page_model import CityPage
from app.api.models.filter_model import FilterApi
from app.utils.city_page_util import next_page
from fake_useragent import UserAgent

load_dotenv()

ua = UserAgent()

SALE_URL = os.getenv("YAD2_API_SALE")

def get_sale_houses_by_filter(filters: FilterApi):
    headers = {"User-Agent": ua.random}
    response = requests.get(f"{SALE_URL}{str(filters)}", headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"API Error: {response.status_code}, Message: {str(response)}")


def add_delay(delay):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            delay_this = random.uniform(1, delay)
            print(f"Waiting {delay_this} seconds before calling {func.__name__}...")
            time.sleep(delay)  # Pause execution for `seconds`
            return func(*args, **kwargs)
        return wrapper
    return decorator

@add_delay(delay=3)
def get_sale_houses_by_city_page(city_page: CityPage) -> dict:
    headers = {"User-Agent": ua.random}
    str_cp = next_page(city_page)
    response = requests.get(f"{SALE_URL}{str_cp}", headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception("get_sale_houses_by_city_page Failed too retrieve data")





# data = get_sale_houses_by_city_page(CityPage(city="7400",page=1,pages=3))
