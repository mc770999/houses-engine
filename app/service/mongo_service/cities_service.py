from typing import List
from pymongo.synchronous.collection import Collection
from app.db.client import db_yad2
from app.db.repository.doc_repository import insert_doc, find_all_docs, find_by_query, update_doc, delete_doc_by_query
from app.models.city_model import City
collection: Collection = db_yad2["COLLECTION_NAME"]


def create_city(city: City) -> str:
    """Insert a new city into the collection."""
    result = insert_doc(doc=city.__dict__, collection=collection)
    result_str = str(result.inserted_id)
    return result_str


# Read (Get All)
def get_all_cities() -> List[City]:
    """Retrieve all cities from the collection."""
    result = find_all_docs(collection=collection)
    cities = [City(**c) for c in result]
    return cities


# Read (Get By Name)
def get_by_name(name: str) -> City:
    """Retrieve cities by the 'name' field."""
    query = {"name": name}
    result = find_by_query(query=query, collection=collection)
    city = City(**result)
    return city


# Update
def update_pages_city_by_name(name: str, pages: int) -> str:
    """Update a city by its ObjectId."""
    query = {"name": name}
    update_page = {"pages": pages}
    result = update_doc(query=query, updated_data=update_page, collection=collection)
    return str(result)


# Delete
def delete_city_by_name(name: str) -> str:
    """Delete a city by its ObjectId."""
    query = {"name": name}
    result = delete_doc_by_query(query=query, collection=collection)
    return str(result)
