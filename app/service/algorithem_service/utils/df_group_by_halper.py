import pandas


def get_avg_price_per_sqm_by_city_by_neighborhood(df: pandas.DataFrame):
    return df.groupby(["city", "neighborhood"])["price_per_sqm"].transform("mean")
