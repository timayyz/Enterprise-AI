import pandas as pd
import matplotlib.pyplot as plt


# 1. Data Preparation

data = {
    "customer_id": ["a", "b", "c", "d", "e"],
    "rating_score": [5, 4, 5, 3, 4],
    "service_level": [
        "excellent",
        "good",
        "excellent",
        "average",
        "good"
    ],
    "room_type": [
        "deluxe",
        "standard",
        "deluxe",
        "standard",
        "deluxe"
    ]
}


df = pd.DataFrame(data)


# 2. Customer Classification

def classify_customer(rating_score):
    if rating_score >= 4:
        return "VIP"
    else:
        return "Normal"


df["customer_type"] = df["rating_score"].apply(classify_customer)



# 3. Rating Distribution

rating_count = df["rating_score"].value_counts().sort_index()

plt.figure(figsize=(6,4))

plt.bar(
    rating_count.index,
    rating_count.values
)

plt.title("Customer Rating Distribution")
plt.xlabel("Rating Score")
plt.ylabel("Number of Customers")
plt.savefig("images/rating_distribution.png")
plt.show()



# 4. Service Level Analysis

service_analysis = df.groupby(
    "service_level"
)["rating_score"].mean()


plt.figure(figsize=(6,4))

plt.bar(
    service_analysis.index,
    service_analysis.values
)

plt.title("Average Rating by Service Level")
plt.xlabel("Service Level")
plt.ylabel("Average Rating")
plt.savefig("images/service_level_rating.png")
plt.show()



# 5. Room Type Analysis

room_analysis = df.groupby(
    "room_type"
)["rating_score"].mean()


plt.figure(figsize=(6,4))

plt.bar(
    room_analysis.index,
    room_analysis.values
)

plt.title("Average Rating by Room Type")
plt.xlabel("Room Type")
plt.ylabel("Average Rating")
plt.savefig("images/room_type_rating.png")
plt.show()



# 6. Customer Type Analysis

customer_analysis = df.groupby(
    "customer_type"
)["rating_score"].mean()


plt.figure(figsize=(6,4))

plt.bar(
    customer_analysis.index,
    customer_analysis.values
)

plt.title("VIP vs Normal Customer Satisfaction")
plt.xlabel("Customer Type")
plt.ylabel("Average Rating")
plt.savefig("images/customer_type_rating.png")
plt.show()