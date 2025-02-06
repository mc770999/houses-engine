import os
from app.api.ebdpoints.sale_api import get_from_external_api
from app.db.client import db_yad2
from app.db.repository.doc_repository import insert_many_documents, update_doc, find_by_query
from app.utils.city_page import url_page_city
from pymongo.collection import Collection

collection_name = os.getenv("SALE_ADS_COLLECTION")

base_url = os.getenv("YAD2_API_SALE")

collection = db_yad2[collection_name]


def update_real_estate_sales_ads(
        city_code: str, total_pages: int, start_page: int = 1
) -> None:
    page_generator = url_page_city(url=base_url, code=city_code, pages=total_pages, page=start_page)

    while True:
        try:
            page_info = next(page_generator)
            api_response = get_from_external_api(page_info["url"])

            ads_data = api_response.get("data", {}).get("markers", [])

            insert_many_documents(collection=collection, documents=ads_data)

            next_page_number = page_info["next_page"]

            update_sale_ad_page(code=city_code, page=next_page_number)

        except StopIteration:
            break


def update_sale_ads(city_code: str) -> None:
    print()


def update_sale_ad_page(code: str, page: int):
    query = {"code": code}
    updated_data = {"page": page}
    update_doc(query=query, updated_data=updated_data, collection=collection)


def get_sale_ad_page_by_name(name: str):
    query = {"name": name}
    result = find_by_query(query=query, collection=collection)
    return result
