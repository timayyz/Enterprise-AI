import pandas as pd
import matplotlib.pyplot as plt
data={
    "customer_id":["a","b","c","d","e"],
    "rating_score":[5,4,5,3,4],
    "service_level":["excellent","good","excellent","average","good"],
    "room_type":["deluxe","standard","deluxe","standard","deluxe"]
}


df=pd.DataFrame(data)

print(df)

service_analysis = df.groupby("service_level")["rating_score"].mean()

print(service_analysis)

service_analysis.plot(kind="bar")

plt.title("Average Rating by Service Level")

plt.xlabel("Service Level")

plt.ylabel("Average Rating")

plt.show()