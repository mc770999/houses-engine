from app.mappings.mapping_condition import get_mapping_condition
import pandas as pd
import json
from app.service.algorithem_service.utils.calc_score_halper import get_condition_score, get_property_type_factor_score, \
    get_price_per_sqm, get_price_score, get_under_avg_percent, get_deal_score, get_estimated_sale_price
from app.service.algorithem_service.utils.df_filter_helper import base_filtering
from app.service.algorithem_service.utils.df_get_halper import get_neighborhood, get_city, get_property_type, get_link
from app.mappings.all_weights_and_mapping import get_weights_main_mapping
from app.mappings.rent_best_mapping import get_rent_best_mapping
from app.mappings.capital_gain_mapping import get_capital_gain_mapping
from app.mappings.family_best_mapping import get_family_best_mapping
from app.api.yad2_const import link_item
from app.service.algorithem_service.utils.df_group_by_halper import get_avg_price_per_sqm_by_city_by_neighborhood


def algorithm_rate_data(
        data: list,
        weights: dict = None,
        rent_mapping: dict = None,
        capital_mapping: dict = None,
        family_mapping: dict = None,
        mapping_condition: dict = None,
        link: str = link_item
) -> list:

    weights = weights or get_weights_main_mapping()
    rent_mapping = rent_mapping or get_rent_best_mapping()
    capital_mapping = capital_mapping or get_capital_gain_mapping()
    family_mapping = family_mapping or get_family_best_mapping()
    mapping_condition = mapping_condition or get_mapping_condition()

    df = pd.DataFrame(data)

    df["city"] = get_city(df=df)

    df["neighborhood"] = get_neighborhood(df=df)

    df["property_type"] = get_property_type(df=df)

    df = base_filtering(df=df)

    df["price_per_sqm"] = get_price_per_sqm(df=df)

    df["avg_price_per_sqm_by_city_by_neighborhood"] = get_avg_price_per_sqm_by_city_by_neighborhood(df=df)

    df["price_score"] = get_price_score(df=df)

    df["under_avg_percent"] = get_under_avg_percent(df=df)

    df["condition_score"] = get_condition_score(df=df, mapping=mapping_condition)

    df["deal_score"] = get_deal_score(df=df, weights=weights)

    df["deal_score_for_rental"] = get_property_type_factor_score(df=df, weights=weights, mapping=rent_mapping)

    df["deal_score_for_capital_gain"] = get_property_type_factor_score(df=df, weights=weights, mapping=capital_mapping)

    df["deal_score_for_family"] = get_property_type_factor_score(df=df, weights=weights, mapping=family_mapping)

    df["estimated_sale_price"] = get_estimated_sale_price(df=df)

    df["link_to_item"] = get_link(df=df, link=link)

    return json.loads(df.to_json(orient='records'))
