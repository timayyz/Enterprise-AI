import pandas as pd

data={
    "customer_id":["a","b","c","d","e"],
    "rating_score":[5,4,5,3,4],
    "service_level":["excellent","good","excellent","average","good"],
    "room_type":["deluxe","standard","deluxe","standard","deluxe"]
}
rating_map = {
    "excellent": 5,
    "good": 4,
    "average": 3,
    "bad": 2
}
df=pd.DataFrame(data)
df["service_rating"]=df["service_level"].map(rating_map)
print(df)



print("Average rating:",df["rating_score"].mean())
print("Average service rating:",df["service_rating"].mean())
print("Highest rating customer:")

best_customer = df.loc[df["rating_score"].idxmax()]

print("Best customer:", best_customer["customer_id"])
print("Score:", best_customer["rating_score"])
print("Service:", best_customer["service_level"])

if best_customer["rating_score"] >= 4:
    print("Status: VIP")
else:
    print("Status: Normal")