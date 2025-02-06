def get_weights_main_mapping(
    price_score: int = 55,  # Price impact up to 50%
    condition_score: int = 35,  # Property condition impact up to 20%
    property_type_factor: int = 10  # Property type impact up to 15%
) -> dict:
    return {
        "price_score": price_score,
        "condition_score": condition_score,
        "property_type_factor": property_type_factor,
    }