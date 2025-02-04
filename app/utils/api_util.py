import os
from dotenv import load_dotenv

load_dotenv()

def get_yad2_url_rent(city, page):
    return f"{os.getenv("YAD2_API_RENT")}city={city}&page={page}"

def get_yad2_url_sale(city, page):
    return f"{os.getenv("YAD2_API_SALE")}city={city}&page={page}"


