import pandas as pd


data = {
    "customer_id":["a","b","c","d","e","f","g"],
    "rating_score":[5,4,None,3,6,4,5],
    "service_level":["excellent","good","excellent",None,"bad","good","excellent"],
    "room_type":["deluxe","standard","deluxe","standard",None,"deluxe","standard"]
}


df = pd.DataFrame(data)

df["rating_score"]=df["rating_score"].clip(1,5)

print(df.isnull().sum())
df["rating_score"]=df["rating_score"].fillna(
    df["rating_score"].mean()
)


df["service_level"]=df["service_level"].fillna(
    df["service_level"].mode()[0]
)


df["room_type"]=df["room_type"].fillna(
    df["room_type"].mode()[0]
)


print(df)

df.to_csv("clean_hotel_data.csv", index=False)
