import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/ecommerce_sales.csv")

# Create figure
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# 1. Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()
axs[0, 0].bar(category_sales.index, category_sales.values)
axs[0, 0].set_title("Sales by Category")
axs[0, 0].tick_params(axis='x', rotation=20)

# 2. Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()
axs[0, 1].bar(region_sales.index, region_sales.values)
axs[0, 1].set_title("Sales by Region")

# 3. Payment Mode Distribution
payment = df["Payment_Mode"].value_counts()
axs[1, 0].pie(payment.values, labels=payment.index, autopct="%1.1f%%")
axs[1, 0].set_title("Payment Mode Distribution")

# 4. Sales vs Profit
axs[1, 1].scatter(df["Sales"], df["Profit"], alpha=0.5)
axs[1, 1].set_title("Sales vs Profit")
axs[1, 1].set_xlabel("Sales")
axs[1, 1].set_ylabel("Profit")

plt.suptitle("E-Commerce Sales Dashboard", fontsize=20)

plt.tight_layout(rect=[0,0,1,0.96])
plt.savefig("charts/dashboard.png")

plt.show()