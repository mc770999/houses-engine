from app.api.models.city_page_model import CityPage


def next_page(city_page: CityPage) -> str:
    str_cp = str(city_page)
    city_page.page += 1
    return str_cp
