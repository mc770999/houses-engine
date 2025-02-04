import json

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# נתוני הדירות בפורמט JSON
def rate_data_and_sort(data : list):
    # המרת JSON ל- DataFrame
    df = pd.DataFrame(data)

    df = df[
        df["price"].notna() & (df["price"] != 0) &
        df["additionalDetails"].apply(lambda x: x.get("squareMeter", 0) != 0)
        ]
    # חישוב מחיר למ"ר
    df["price_per_sqm"] = df["price"] / df["additionalDetails"].apply(lambda x: x["squareMeter"])

    average_price_per_sqm = df["price_per_sqm"].min()

    print(average_price_per_sqm)

    # מאפיינים בינאריים (חניה, מחסן, כיווני אוויר)
    df["has_parking"] = df["tags"].apply(lambda tags: any(tag["name"] == "חניה" for tag in tags) if isinstance(tags, list) else False).astype(int)
    df["has_storage"] = df["tags"].apply(lambda tags: any(tag["name"] == "מחסן" for tag in tags)if isinstance(tags, list) else False).astype(int)
    df["air_directions"] = df["tags"].apply(lambda tags: sum(1 for tag in tags if "כיווני אוויר" in tag["name"])if isinstance(tags, list) else False).astype(
        int)

    # ניקוד מצב הדירה
    df["condition_score"] = df["additionalDetails"].apply(lambda x: 1 if x["propertyCondition"]["id"] == 1 else 0)

    # ניקוד קומה (מנרמלים לטווח 0-1)
    df["floor_score"] = df["address"].apply(lambda x: min(x["house"]["floor"] / 10, 1))

    # ניקוד לפי זמן שהות בשוק (דירות חדשות מקבלות עדיפות)
    # df["market_score"] = df["days_on_market"].apply(lambda x: 1 if x < 60 else 0)

    # נורמליזציה של כל הפרמטרים בעזרת MinMaxScaler
    scaler = MinMaxScaler()
    df[["price_per_sqm", "air_directions", "floor_score"]] = scaler.fit_transform(
        df[["price_per_sqm", "air_directions", "floor_score"]]
    )

    # הופכים מחיר למ"ר (ככל שנמוך יותר, עדיף יותר)
    df["normalized_price"] = 1 - df["price_per_sqm"]

    # שקלול הציון הכולל
    weights = {
        "normalized_price": 10.8,  # מחיר נמוך יותר = עסקה טובה יותר
        "has_parking": 0.15,  # חניה = יתרון
        "has_storage": 0.2,  # מחסן = יתרון
        "air_directions": 0.1,  # יותר כיווני אוויר = יותר טוב
        "condition_score": 0.2,  # דירה חדשה = יתרון
        "floor_score": 0.15,  # קומה גבוהה = יתרון
        # "market_score": 0.1,  # זמן קצר בשוק = יתרון
    }

    df["deal_score"] = (
            df["normalized_price"] * weights["normalized_price"] +
            df["has_parking"] * weights["has_parking"] +
            df["has_storage"] * weights["has_storage"] +
            df["air_directions"] * weights["air_directions"] +
            df["condition_score"] * weights["condition_score"] +
            df["floor_score"] * weights["floor_score"]
            # df["market_score"] * weights["market_score"]
    )

    # מיון הדירות מהדיל הכי משתלם לפחות משתלם
    # df = df.sort_values(by="deal_score", ascending=False)

    return json.loads(df.to_json(orient='records'))



def rate_data_and_sort(data: list, link):
    # המרת JSON ל- DataFrame
    df = pd.DataFrame(data)

    # סינון נתונים לא תקינים
    df = df[
        df["price"].notna() & (df["price"] != 0) &
        df["additionalDetails"].apply(lambda x: x.get("squareMeter", 0) != 0)
    ]

    # חישוב מחיר למ"ר
    df["price_per_sqm"] = df["price"] / df["additionalDetails"].apply(lambda x: x["squareMeter"])

    # חישוב ממוצע מחיר למ"ר לכל שכונה
    df["avg_price_per_sqm"] = df.groupby(["city", "neighborhood"])["price_per_sqm"].transform("mean")

    # חישוב סטייה של הדירה מהממוצע בשכונה
    df["under_avg_percent"] = ((df["price_per_sqm"] - df["avg_price_per_sqm"]) / df["avg_price_per_sqm"]) * 100

    # ניקוד מצב הדירה
    df["condition_score"] = df["additionalDetails"].apply(lambda x: 1 if x["propertyCondition"]["id"] == 1 else 0)

    # ניקוד קומה (מנרמלים לטווח 0-1)
    # df["floor_score"] = df["address"].apply(lambda x: min(x["house"]["floor"] / 10, 1))

    df["link"] = link + df["token"] # link = http://yad/item/


    # שקלול הציון הכולל
    weights = {
        "price_per_sqm": 10.8,  # מחיר נמוך יותר = עסקה טובה יותר
        "condition_score": 0.2,  # דירה חדשה = יתרון
        # "floor_score": 0.15,  # קומה גבוהה = יתרון
        "under_avg_percent": 2.0,  # דירות שזולות מהממוצע בשכונה יקבלו ציון גבוה יותר
    }

    df["deal_score"] = (
        df["price_per_sqm"] * weights["price_per_sqm"] +
        df["condition_score"] * weights["condition_score"] +
        df["floor_score"] * weights["floor_score"] +
        df["under_avg_percent"] * weights["under_avg_percent"]
    )

    # מיון הדירות מהדיל הכי משתלם לפחות משתלם
    df = df.sort_values(by="deal_score", ascending=False)

    return json.loads(df.to_json(orient='records'))