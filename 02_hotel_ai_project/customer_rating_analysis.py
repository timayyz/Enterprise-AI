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
# 1. Data Preparation

df=pd.DataFrame(data)

# 2. Customer Classification

def classify_customer(rating_score):
    if rating_score >= 4:
        return "VIP"
    else:
        return "Normal"

print("Average rating:",df["rating_score"].mean())
best_customer = df.loc[df["rating_score"].idxmax()]
print("Best customer:", best_customer["customer_id"])
print("Service:", best_customer["service_level"])
df["customer_type"] = df["rating_score"].apply(classify_customer)
print(df[["customer_id", "rating_score", "customer_type"]])

# 3. Basic Statistical Analysis

print(df.describe())

# 4. Service Level Analysis

# Convert service level into numerical rating
df["service_rating"]=df["service_level"].map(rating_map)
service_analysis = df.groupby(
    "service_level"
)["rating_score"].mean()

print(service_analysis)

# 5. Room Type Analysis

room_analysis=df.groupby(
    "room_type"
)["rating_score"].mean()

print(room_analysis)

# 6. Customer Type Analysis

customer_analysis = df.groupby("customer_type")["rating_score"].mean()

print(customer_analysis)

# 7. Advanced Analysis

room_customer_analysis = df.groupby(
    ["room_type","customer_type"]
)["rating_score"].mean()

print(room_customer_analysis)