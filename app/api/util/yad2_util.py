from app.api.yad2_const import yad2_api_rent


def get_yad2_url_rent(city, page):
    return f"{yad2_api_rent}city={city}&page={page}"


def get_yad2_url_sale(city, page):
    return f"{yad2_api_sale}city={city}&page={page}"
