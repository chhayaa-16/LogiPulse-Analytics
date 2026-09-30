import pandas as pd

file_path = "data/raw/olist_orders_dataset.csv"

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

print("\nFIRST 5 ROWS:")
print(df.head())


print("\nUNIQUE ORDER IDs:")
print(df["order_id"].nunique())

print("\nDUPLICATE ORDER IDs:")
print(df["order_id"].duplicated().sum())


print("\nORDER STATUS COUNTS:")
print(df["order_status"].value_counts())

print("\nUNIQUE ORDER STATUSES:")
print(df["order_status"].unique())

print("\nMISSING CUSTOMER DELIVERY DATE BY ORDER STATUS:")

missing_delivery = df["order_delivered_customer_date"].isnull()

print(
    df.loc[missing_delivery, "order_status"]
    .value_counts()
)

print("\nDELIVERED ORDERS WITH MISSING CUSTOMER DELIVERY DATE:")

delivered_missing_date = df[
    (df["order_status"] == "delivered")
    & (df["order_delivered_customer_date"].isnull())
]

print(delivered_missing_date.to_string(index=False))