import pandas as pd

file_path = "data/raw/product_category_name_translation.csv"

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

print("\nUNIQUE PORTUGUESE CATEGORY NAMES:")
print(df["product_category_name"].nunique())

print("\nDUPLICATE PORTUGUESE CATEGORY NAMES:")
print(df["product_category_name"].duplicated().sum())

print("\nUNIQUE ENGLISH CATEGORY NAMES:")
print(df["product_category_name_english"].nunique())

print("\nDUPLICATE ENGLISH CATEGORY NAMES:")
print(df["product_category_name_english"].duplicated().sum())

print("\nFIRST 5 ROWS:")
print(df.head())