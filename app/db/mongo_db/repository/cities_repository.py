import os
from pymongo.collection import Collection
from app.db.mongo_db.models.city_model import City
from app.db.mongo_db.client import db_yad2


collection: Collection = db_yad2["COLLECTION_NAME"]

# Create
def insert_doc(doc, collection):
    """Insert a new city into the collection."""
    result = collection.insert_one(doc)
    return result

# Read (Get All)
def find_all_docs(collection):
    """Retrieve all cities from the collection."""
    cities = list(collection.find())
    return cities

# Read (Get By Name)
def find_by_name(by, collection):
    """Retrieve cities by the 'name' field."""
    city = collection.find_one({by[0]: by[1]})
    return city

# Update
def update_doc(by, updated_data, collection):
    """Update a city by its ObjectId."""
    result = collection.update_one(
        {by[0]: by[1]}, {"$set": updated_data}
    )
    return result

# Delete
def delete_doc(by : tuple, collection):
    """Delete a city by its ObjectId."""
    result = collection.delete_one({by[0]: by[1]})
    return result

def find_docs_by_query(query, collection):
    result = collection.aggregate(query)
    return result


