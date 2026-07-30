import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/ecommerce_sales.csv")

plt.figure(figsize=(10,6))

sns.scatterplot(
    data=df,
    x="Sales",
    y="Profit",
    alpha=0.6,
    color="blue"
)

plt.title("Sales vs Profit", fontsize=18)
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.grid(True)

plt.tight_layout()

plt.savefig("charts/sales_vs_profit.png")

plt.show()