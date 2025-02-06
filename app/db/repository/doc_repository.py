from typing import List

from pymongo.collection import Collection


# Create
def insert_doc(doc: dict, collection):
    """Insert a new city into the collection."""
    result = collection.insert_one(doc)
    return result


# Read (Get All)
def find_all_docs(collection):
    """Retrieve all cities from the collection."""
    cities = list(collection.find())
    return cities


# Read (Get By Name)

def find_by_query(query: dict, collection: Collection):
    """Retrieve cities by the 'name' field."""
    doc = collection.find_one(query)
    return doc


def insert_many_documents(documents: list, collection: Collection) -> List[str]:
    result = collection.insert_many(documents)
    return [str(id) for id in result.inserted_ids]

# Update
def update_doc(query: dict, updated_data: dict, collection: Collection):
    """Update a city by its ObjectId."""
    result = collection.update_one(
        query, {"$set": updated_data}
    )
    return result


# Delete
def delete_doc_by_query(query: dict, collection: Collection):
    """Delete a city query its ObjectId."""
    result = collection.delete_one(query)
    return result


def find_docs_by_query(query: dict, collection: Collection):
    result = collection.aggregate(query)
    return result
