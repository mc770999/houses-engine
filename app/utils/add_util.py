from app.db.mongo_db.models.apartment_ad_model import Ad, Address, House, Coords, \
    AdditionalDetails,  PropertyCondition

convert_to_ad = lambda data:  Ad(
    address=Address(
        city=data.get("address", {}).get("city", {}).get("text"),
        area=data.get("address", {}).get("area", {}).get("text"),
        neighborhood=data.get("address", {}).get("neighborhood", {}).get("text"),
        street=data.get("address", {}).get("street", {}).get("text"),
        house=House(
            number=data.get("address", {}).get("house", {}).get("number"),
            floor=data.get("address", {}).get("house", {}).get("floor"),
        ),
        coords=Coords(
            lon=data.get("address", {}).get("coords", {}).get("lon"),
            lat=data.get("address", {}).get("coords", {}).get("lat"),
        ),
    ),
    subcategoryId=data.get("subcategoryId"),
    categoryId=data.get("categoryId"),
    adType=data.get("adType"),
    price=data.get("price"),
    token=data.get("token"),
    additionalDetails=AdditionalDetails(
        property=data.get("additionalDetails", {}).get("property", {}).get("text"),
        roomsCount=data.get("additionalDetails", {}).get("roomsCount"),
        squareMeter=data.get("additionalDetails", {}).get("squareMeter"),
        propertyCondition=PropertyCondition(
            id=data.get("additionalDetails", {})
            .get("propertyCondition", {})
            .get("id")
        ),
    ),
)