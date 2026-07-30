import pandas as pd
import os
# Load Dataset
df = pd.read_csv(r"C:\Users\smart\OneDrive\Desktop\Smart_Ecommerce_webscarpping\Dataset\books_dataset.csv")

print("=" * 50)
print("DATASET INFORMATION")
print("=" * 50)

print("\nTotal Rows and Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Create folder if it doesn't exist
os.makedirs("../Cleaned_Dataset", exist_ok=True)

# Save cleaned dataset
df.to_csv(r"C:\Users\smart\OneDrive\Desktop\Smart_Ecommerce_webscarpping/Cleaned_dataset/cleaned_books_dataset.csv", index=False)

print("\n✅ Cleaned dataset saved successfully!")
