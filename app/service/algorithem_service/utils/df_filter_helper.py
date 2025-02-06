import pandas as pd
from app.service.algorithem_service.utils.df_get_halper import get_square_meter


def base_filtering(df: pd.DataFrame):
    return df[df["price"].notna() & (df["price"] != 0) & (get_square_meter(df) != 0)]
