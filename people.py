import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/people.csv")

print(df)
print("\nAverage age:")
print(df["age"].mean())
print("------------------------------")

print("\nPeople from Caloocan:")
print(df[df["city"] == "Caloocan"])
print("------------------------------")

print("\nPeople older than 22:")
print(df[df["age"] > 22])
print("------------------------------")

print("\nCount of people by city:")
print(df["city"].value_counts())

df["friend"].value_counts().plot(kind="bar")
plt.title("Friend vs Non-Friend Count")
plt.xlabel("Friend (1 = Yes, 0 = No)")
plt.ylabel("Number of People")
plt.show()



