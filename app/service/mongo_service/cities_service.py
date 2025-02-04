from app.db.mongo_db.models.city_model import City, CityUpdate
from app.db.mongo_db.repository.cities_repository import *

def create_city(city: dict):
    """Insert a new city into the collection."""
    result = insert_city(City(**city))
    result_str = str(result.inserted_id)
    return result_str

# Read (Get All)
def get_all_cities():
    """Retrieve all cities from the collection."""
    result = find_all_cities()
    cities = [City(**c) for c in result]
    return cities

# Read (Get By Name)
def get_by_name(name):
    """Retrieve cities by the 'name' field."""
    result = find_by_name(name)
    city = City(**result)
    return city

# Update
def update_pages_city_by_name(city_update:CityUpdate):
    """Update a city by its ObjectId."""
    result = update_city(city_update.name, {"pages": city_update.pages})
    return str(result)

# Delete
def delete_city_by_name(name):
    """Delete a city by its ObjectId."""
    result = delete_city(name)
    return result

