def get_family_best_mapping(
        private_house_cottage: float = 1.2,  # Usually the best for families due to space and garden
        garden_apartment: float = 1.0,  # More space and accessibility
        semi_detached: float = 1.1,  # Suitable for families due to divided living spaces
        duplex: float = 1.1,  # Good option, but layout may not always be ideal
        apartment: float = 1.1,  # Standard apartment, can be a bit cramped
        penthouse: float = 0.9,  # Beautiful view, but layout/access may not be ideal for families
        housing_unit: float = 0.8,  # Typically small, not ideal for a family
        studio_loft: float = 0.7
) -> dict:  # Open space, lacks separation, less suitable for families
    return {
        "בית פרטי/ קוטג'": private_house_cottage,
        "דירת גן": garden_apartment,
        "דו משפחתי": semi_detached,
        "דופלקס": duplex,
        "דירה": apartment,
        "גג/ פנטהאוז": penthouse,
        "יחידת דיור": housing_unit,
        "סטודיו/ לופט": studio_loft,
    }


