import pandas as pd


def get_city(df: pd.DataFrame) -> pd.DataFrame:
    """מחזיר את שם העיר מתוך השדה address."""
    return df["address"].apply(lambda address: address.get("city", {}).get("text", None))


def get_neighborhood(df: pd.DataFrame) -> pd.DataFrame:
    """מחזיר את שם השכונה מתוך השדה address."""
    return df["address"].apply(lambda address: address.get("neighborhood", {}).get("text", None))


def get_property_type(df: pd.DataFrame) -> pd.DataFrame:
    """מחזיר את שם השכונה מתוך השדה address."""
    return df["additionalDetails"].apply(lambda d: d.get("property", {}).get("text", ""))


def get_square_meter(df: pd.DataFrame) -> pd.DataFrame:
    """    # חישוב מחיר למ"ר."""
    return df["additionalDetails"].apply(lambda details: details.get("squareMeter", 0))


def get_floor(df: pd.DataFrame) -> pd.DataFrame:
    """מחזיר את הקומה מתוך address.house (אם קיימת)."""
    return df["address"].apply(lambda address: address.get("house", {}).get("floor", None))


def get_link(df: pd.DataFrame, link: str) -> pd.DataFrame:
    # הוספת קישור ישיר לנכס
    return link + df["token"]
