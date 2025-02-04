import datetime
import os
import time
import random

from typing import List

import numpy
import requests
from dotenv import load_dotenv
from app.api.models.city_page_model import CityPage
from app.api.sale.sale_api import get_sale_houses_by_city_page

import toolz as t

from app.assets import data_sale_new
from app.db.mongo_db.models.apartment_ad_model import Ad
from app.utils.add_util import convert_to_ad
from app.utils.algo_util import rate_data_and_sort

link = os.getenv("YAD2_HOUSE")
def get_from_api_by_city_page(*city_page_list):
    for city_page in city_page_list:
        for _ in range(city_page.page, city_page.pages + 1):
            data = get_sale_houses_by_city_page(city_page).get("data", {}).get("markers", [])




# a = get_from_api_by_city_page(CityPage(**{"city" : "0031", "pages": 22}))
# # b : List[Ad] = [convert_to_ad(a) for a in a]
# # b = list(filter(lambda el : el.price != 0 and el.additionalDetails.squareMeter != 0))
# # c = sorted(b, key=lambda el: el.price / el.additionalDetails.squareMeter)
# print(a)

a = data_sale_new
c = rate_data_and_sort(a)
links = [link + d.get("token") for d in c]
for l in links:
    print(l)


# print(calc_and_sorted(get_rent_houses_by_city(1)))

def calc(house):
    meter = house.get("additionalDetails", {}).get("squareMeter", None)
    price = house.get("price", None)
    if meter is None or price is None or price == 0:
        return float('inf')  # High value to push invalid houses to the end
    return price / meter


def filter_and_sorted_for_city(houses):
    # Filter out houses with invalid data
    filtered_houses = list(filter(lambda h: h.get("adType") == "private", houses))
    if not filtered_houses:
        return None  # Return None if no valid houses found
    # Sort houses using calc, with invalid ones pushed to the end
    a_list_sorted = sorted(filtered_houses, key=calc)
    return a_list_sorted  # Return the house with the best price/meter ratio



