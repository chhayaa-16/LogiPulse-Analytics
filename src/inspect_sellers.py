import pandas as pd

file_path = "data/raw/olist_sellers_dataset.csv"

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

print("\nUNIQUE SELLER IDs:")
print(df["seller_id"].nunique())

print("\nDUPLICATE SELLER IDs:")
print(df["seller_id"].duplicated().sum())

print("\nFIRST 5 ROWS:")
print(df.head())