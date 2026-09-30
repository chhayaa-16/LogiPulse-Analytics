import pandas as pd

file_path = "data/raw/olist_order_reviews_dataset.csv"

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

print("\nUNIQUE REVIEW IDs:")
print(df["review_id"].nunique())

print("\nDUPLICATE REVIEW IDs:")
print(df["review_id"].duplicated().sum())

print("\nUNIQUE ORDER IDs:")
print(df["order_id"].nunique())

print("\nDUPLICATE ORDER IDs:")
print(df["order_id"].duplicated().sum())

print("\nFIRST 5 ROWS:")
print(df.head())