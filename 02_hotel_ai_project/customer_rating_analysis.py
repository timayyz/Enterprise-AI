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
print("Highest rating customer:",df.loc[df["rating_score"].idxmax()]["customer_id"])

best_customer = df.loc[df["rating_score"].idxmax()]

print("Best customer:", best_customer["customer_id"])
print("Score:", best_customer["rating_score"])
print("Service:", best_customer["service_level"])

service_analysis = df.groupby("service_level")["rating_score"].mean()
print(service_analysis)   
room_analysis = df.groupby("room_type")["rating_score"].mean()
print(room_analysis)

def classify_customer(rating_score):
    if rating_score >= 4:
        return "VIP"
    else:
        return "Normal"
df["customer_type"] = df["rating_score"].apply(classify_customer)
print(df[["customer_id", "rating_score", "customer_type"]])


print(df["customer_type"].value_counts())
if best_customer["rating_score"] >= 4:
    print("Status: VIP")
else:
    print("Status: Normal")



print("Insight: Excellent service has the highest customer satisfaction.")