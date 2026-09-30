import pandas as pd

file_path = "data/raw/olist_products_dataset.csv"

df = pd.read_csv(file_path)

print("SHAPE:")
print(df.shape)

print("\nCOLUMNS:")
print(df.columns.tolist())

print("\nDATA TYPES:")
print(df.dtypes)

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())

print("\nUNIQUE PRODUCT IDs:")
print(df["product_id"].nunique())

print("\nDUPLICATE PRODUCT IDs:")
print(df["product_id"].duplicated().sum())

print("\nFIRST 5 ROWS:")
print(df.head())