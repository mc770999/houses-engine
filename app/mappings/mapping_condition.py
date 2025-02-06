def get_mapping_condition(
    new_from_contractor: float = 1.3,  # Brand new - significantly higher price
    renovated: float = 1.15,  # Renovated - major advantage
    well_preserved: float = 0.9,  # Well-maintained - less attractive
    needs_renovation: float = 0.75,  # Requires renovation - discount required
    new_up_to_10_years: float = 1.2  # Up to 10 years old - retains high value
) -> dict:
    return {
        1: new_from_contractor,
        2: renovated,
        3: well_preserved,
        5: needs_renovation,
        6: new_up_to_10_years,
    }
