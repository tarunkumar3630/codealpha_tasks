import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/ecommerce_sales.csv")

# Count payment modes
payment = df["Payment_Mode"].value_counts()

plt.figure(figsize=(8,8))

plt.pie(
    payment,
    labels=payment.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Payment Mode Distribution", fontsize=18)

plt.savefig("charts/payment_mode_distribution.png")

plt.show()
