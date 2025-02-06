from app.models.city_model import City


def url_page_city(url: str, pages: int, code: str, page: int):
    """Generate URLs for paginated city listings."""
    for current_page in range(page, pages + 1):
        yield {"url": f"{url}?city={code}&page={current_page}", "next_page": current_page + 1}

a = url_page_city("dfdf", 5, "dfd",1)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
# print(next(a))
def next_page(city_page: City) -> str:
    str_cp = city_page
    city_page.page += 1
    return str_cp
