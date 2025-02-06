import pandas
from app.service.algorithem_service.utils.df_get_halper import get_square_meter


def get_condition_score(df: pandas.DataFrame, mapping: dict) -> float:
    """
     חישוב ניקוד מצב הנכס
    מחשב ניקוד למצב הנכס לפי propertyCondition.id.
    ההתאמות מבוססות על ההשפעה האמיתית של מצב הנכס על ערכו בשוק.
    """
    condition_id = df["additionalDetails"].apply(lambda detail: detail.get("propertyCondition", {}).get("id", 0))
    return mapping.get(condition_id, 1.0)


def get_property_type_factor_score(df: pandas.DataFrame, weights: dict, mapping: dict) -> float:
    property_text = df["additionalDetails"].apply(lambda detail: detail.get("property", {}).get("text", ""))
    return (get_deal_score(df=df, weights=weights) *
            mapping.get(property_text, 1.0) ** weights["property_type_factor"])


def get_price_per_sqm(df: pandas.DataFrame):
    # חישוב ממוצע מחיר למ"ר לפי עיר ושכונה
    return df["price"] / get_square_meter(df)


def get_price_score(df: pandas.DataFrame):
    # חישוב "price_score": ככל שהנכס זול יותר ביחס לממוצע – יחס גבוה יותר
    return df["avg_price_per_sqm"] / df["price_per_sqm"]


def get_under_avg_percent(df: pandas.DataFrame):
    # חישוב אחוז ההפרש מהממוצע (לנוחות, ניתן להוסיף בונוס נוסף אם נדרש)
    return -((df["price_per_sqm"] - df["avg_price_per_sqm"]) / df["avg_price_per_sqm"]) * 100


def get_deal_score(df: pandas.DataFrame, weights: dict):
    # חישוב הציון הסופי (deal_score) בשיטת מכפלה עם משקלים (על ידי העלאת כל גורם לחזקת המשקל המתאים)
    return (df["price_score"] ** weights["price_score"]) * (df["condition_score"] ** weights["condition_score"])


def get_estimated_sale_price(df: pandas.DataFrame):
    # חישוב המחיר המשוער שבו ניתן למכור את הנכס:
    # נוסחא: שטח * (ממוצע מחיר למ"ר באזור) * (גורמי התאמה: מצב, סוג, קומה)
    return (
            get_square_meter(df) *
            df["avg_price_per_sqm"] *
            df["condition_score"]
    )
