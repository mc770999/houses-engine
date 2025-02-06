import functools
import os
import random
import time
import requests
from dotenv import load_dotenv

from app.api.util.decorator_util import add_delay
from app.models.city_model import City
from app.utils.city_page import next_page
from fake_useragent import UserAgent

load_dotenv()

ua = UserAgent()

SALE_URL = os.getenv("YAD2_API_SALE")


@add_delay(delay=3)
def get_from_external_api(url: str) -> dict:
    headers = {"User-Agent": ua.random}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception("get_sale_houses_by_city_page Failed too retrieve data")





# data = get_sale_houses_by_city_page(CityPage(city="7400",page=1,pages=3))
