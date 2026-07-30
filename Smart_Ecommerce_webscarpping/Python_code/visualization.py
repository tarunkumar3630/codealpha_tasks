import pandas as pd
import matplotlib.pyplot as plt
import os

# Load cleaned dataset
df = pd.read_csv(r"C:\Users\smart\OneDrive\Desktop\Smart_Ecommerce_webscarpping\Cleaned_Dataset\cleaned_books_dataset.csv")

# Create Charts folder
os.makedirs("../Charts", exist_ok=True)

# Convert price to numeric
df["Price"] = df["Price"].replace("£", "", regex=True).astype(float)

# -------------------------
# Chart 1: Top 10 Expensive Books
# -------------------------
top10 = df.sort_values("Price", ascending=False).head(10)

plt.figure(figsize=(12,6))
plt.bar(top10["Title"], top10["Price"])
plt.title("Top 10 Most Expensive Books")
plt.xlabel("Book Title")
plt.ylabel("Price (£)")
plt.xticks(rotation=75, ha="right")
plt.tight_layout()
plt.savefig("../Charts/top10_expensive_books.png")
plt.close()

# -------------------------
# Chart 2: Top 10 Cheapest Books
# -------------------------
cheap = df.sort_values("Price").head(10)

plt.figure(figsize=(12,6))
plt.bar(cheap["Title"], cheap["Price"])
plt.title("Top 10 Cheapest Books")
plt.xlabel("Book Title")
plt.ylabel("Price (£)")
plt.xticks(rotation=75, ha="right")
plt.tight_layout()
plt.savefig("../Charts/top10_cheapest_books.png")
plt.close()

# -------------------------
# Chart 3: Price Distribution
# -------------------------
plt.figure(figsize=(8,5))
plt.hist(df["Price"], bins=20)
plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("../Charts/price_distribution.png")
plt.close()

# -------------------------
# Chart 4: Stock Availability
# -------------------------
stock = df["instock"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(stock.values,
        labels=stock.index,
        autopct="%1.1f%%")
plt.title("Book Availability")
plt.savefig("../Charts/stock_availability.png")
plt.close()

print("✅ All charts created successfully!")