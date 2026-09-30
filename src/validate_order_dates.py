import pandas as pd


file_path = "data/raw/olist_orders_dataset.csv"

df = pd.read_csv(file_path)


# Convert date columns to datetime
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in date_columns:
    df[column] = pd.to_datetime(df[column])


print("DATE RANGE:")
for column in date_columns:
    print(
        column,
        "->",
        df[column].min(),
        "to",
        df[column].max()
    )


# 1. Approval before purchase
invalid_approval = df[
    df["order_approved_at"].notna()
    & (
        df["order_approved_at"]
        < df["order_purchase_timestamp"]
    )
]

print("\nAPPROVAL BEFORE PURCHASE:")
print(len(invalid_approval))


# 2. Carrier date before purchase
invalid_carrier = df[
    df["order_delivered_carrier_date"].notna()
    & (
        df["order_delivered_carrier_date"]
        < df["order_purchase_timestamp"]
    )
]

print("\nCARRIER DATE BEFORE PURCHASE:")
print(len(invalid_carrier))


# 3. Customer delivery before purchase
invalid_delivery = df[
    df["order_delivered_customer_date"].notna()
    & (
        df["order_delivered_customer_date"]
        < df["order_purchase_timestamp"]
    )
]

print("\nCUSTOMER DELIVERY BEFORE PURCHASE:")
print(len(invalid_delivery))


# 4. Customer delivery before carrier handover
invalid_delivery_sequence = df[
    df["order_delivered_customer_date"].notna()
    & df["order_delivered_carrier_date"].notna()
    & (
        df["order_delivered_customer_date"]
        < df["order_delivered_carrier_date"]
    )
]

print("\nCUSTOMER DELIVERY BEFORE CARRIER DATE:")
print(len(invalid_delivery_sequence))


# 5. Delivered date after estimated delivery date
delivered_after_estimated = df[
    df["order_delivered_customer_date"].notna()
    & (
        df["order_delivered_customer_date"]
        > df["order_estimated_delivery_date"]
    )
]

print("\nDELIVERED AFTER ESTIMATED DELIVERY DATE:")
print(len(delivered_after_estimated))


print("\nDATE VALIDATION COMPLETED")