import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

categories = {
    "Electronics": ["Laptop", "Mobile", "Headphones", "Smart Watch"],
    "Fashion": ["Shirt", "Jeans", "Shoes", "Jacket"],
    "Home": ["Chair", "Table", "Lamp", "Sofa"],
    "Sports": ["Football", "Cricket Bat", "Tennis Racket", "Gym Bag"],
    "Books": ["Novel", "Biography", "Comics", "Dictionary"]
}

regions = ["North", "South", "East", "West"]
payment_modes = ["UPI", "Card", "Cash on Delivery", "Net Banking"]

start_date = datetime(2024, 1, 1)

rows = []

for order_id in range(1001, 6001):   # 5000 records
    category = random.choice(list(categories.keys()))
    product = random.choice(categories[category])
    region = random.choice(regions)

    quantity = random.randint(1, 5)
    price = random.randint(300, 5000)

    sales = quantity * price

    discount = random.choice([0, 5, 10, 15, 20])

    final_sales = sales - (sales * discount / 100)

    profit = round(final_sales * random.uniform(0.10, 0.30), 2)

    payment = random.choice(payment_modes)

    date = start_date + timedelta(days=random.randint(0, 364))

    rows.append([
        order_id,
        date.strftime("%Y-%m-%d"),
        region,
        category,
        product,
        quantity,
        price,
        discount,
        round(final_sales, 2),
        profit,
        payment
    ])

df = pd.DataFrame(rows, columns=[
    "Order_ID",
    "Date",
    "Region",
    "Category",
    "Product",
    "Quantity",
    "Unit_Price",
    "Discount(%)",
    "Sales",
    "Profit",
    "Payment_Mode"
])

df.to_csv("data/ecommerce_sales.csv", index=False)

print(df.head())
print("\nDataset Shape:", df.shape)
print("\nDataset saved successfully!")