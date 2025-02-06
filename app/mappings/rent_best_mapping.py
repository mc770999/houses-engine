def get_rent_best_mapping(
    housing_unit: float = 1.2,
    studio_loft: float = 1.2,
    apartment: float = 1.0,
    garden_apartment: float = 0.95,
    semi_detached: float = 0.95,
    duplex: float = 0.9,
    penthouse: float = 0.85,
    private_house_cottage: float = 0.85) -> dict:
    return {
        "יחידת דיור": housing_unit,
        "סטודיו/ לופט": studio_loft,
        "דירה": apartment,
        "דירת גן": garden_apartment,
        "דו משפחתי": semi_detached,
        "דופלקס": duplex,
        "גג/ פנטהאוז": penthouse,
        "בית פרטי/ קוטג'": private_house_cottage,
    }