import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/ecommerce_sales.csv")

# Group by Category
profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,6))

sns.barplot(
    x=profit.index,
    y=profit.values,
    hue=profit.index,
    palette="crest",
    legend=False
)

plt.title("Profit by Category", fontsize=18)
plt.xlabel("Category")
plt.ylabel("Total Profit")

plt.tight_layout()

plt.savefig("charts/profit_by_category.png")

plt.show()