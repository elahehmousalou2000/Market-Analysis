import pandas as pd

df = pd.read_csv("market.csv")

print("Average price:", df["price"].mean())
print("Maximum price:", df["price"].max())
print("Minimum price:", df["price"].min())
print("\nCorrelation:")
print(df[["price", "volume"]].corr())
