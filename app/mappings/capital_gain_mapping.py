def get_capital_gain_mapping(
    private_house_cottage: float = 1.2,
    penthouse: float = 1.15,
    garden_apartment: float = 1.1,
    semi_detached: float = 1.1,
    duplex: float = 1.05,
    apartment: float = 1.0,
    housing_unit: float = 0.95,
    studio_loft: float = 0.95) -> dict:
    return {
        "בית פרטי/ קוטג'": private_house_cottage,
        "גג/ פנטהאוז": penthouse,
        "דירת גן": garden_apartment,
        "דו משפחתי": semi_detached,
        "דופלקס": duplex,
        "דירה": apartment,
        "יחידת דיור": housing_unit,
        "סטודיו/ לופט": studio_loft,
    }
