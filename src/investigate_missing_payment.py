import pandas as pd


# Load tables
orders = pd.read_csv(
    "data/raw/olist_orders_dataset.csv"
)

payments = pd.read_csv(
    "data/raw/olist_order_payments_dataset.csv"
)

order_items = pd.read_csv(
    "data/raw/olist_order_items_dataset.csv"
)


# Find orders that do not have payment records
missing_payment_orders = orders[
    ~orders["order_id"].isin(payments["order_id"])
]


print("ORDERS WITHOUT PAYMENT RECORD:")
print(missing_payment_orders)


print("\nNUMBER OF ORDERS WITHOUT PAYMENT:")
print(len(missing_payment_orders))


# Show order items for the affected order(s)
affected_order_ids = missing_payment_orders["order_id"]

affected_items = order_items[
    order_items["order_id"].isin(affected_order_ids)
]


print("\nORDER ITEMS FOR AFFECTED ORDERS:")
print(affected_items)


# Show payment records for the affected order(s)
affected_payments = payments[
    payments["order_id"].isin(affected_order_ids)
]


print("\nPAYMENT RECORDS FOR AFFECTED ORDERS:")
print(affected_payments)


print("\nINVESTIGATION COMPLETED")