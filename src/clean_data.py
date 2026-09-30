import os
import pandas as pd


RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"


os.makedirs(PROCESSED_PATH, exist_ok=True)


# -----------------------------
# ORDERS
# -----------------------------

orders = pd.read_csv(
    f"{RAW_PATH}/olist_orders_dataset.csv"
)

order_date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in order_date_columns:
    orders[column] = pd.to_datetime(
        orders[column],
        errors="coerce"
    )


orders["carrier_before_purchase_flag"] = (
    orders["order_delivered_carrier_date"]
    < orders["order_purchase_timestamp"]
)

orders["delivery_before_carrier_flag"] = (
    orders["order_delivered_customer_date"]
    < orders["order_delivered_carrier_date"]
)


orders.to_csv(
    f"{PROCESSED_PATH}/olist_orders_processed.csv",
    index=False
)


# -----------------------------
# CUSTOMERS
# -----------------------------

customers = pd.read_csv(
    f"{RAW_PATH}/olist_customers_dataset.csv"
)

customers.to_csv(
    f"{PROCESSED_PATH}/olist_customers_processed.csv",
    index=False
)


# -----------------------------
# ORDER ITEMS
# -----------------------------

order_items = pd.read_csv(
    f"{RAW_PATH}/olist_order_items_dataset.csv"
)

order_items["shipping_limit_date"] = pd.to_datetime(
    order_items["shipping_limit_date"],
    errors="coerce"
)

order_items.to_csv(
    f"{PROCESSED_PATH}/olist_order_items_processed.csv",
    index=False
)


# -----------------------------
# SELLERS
# -----------------------------

sellers = pd.read_csv(
    f"{RAW_PATH}/olist_sellers_dataset.csv"
)

sellers.to_csv(
    f"{PROCESSED_PATH}/olist_sellers_processed.csv",
    index=False
)


# -----------------------------
# PRODUCTS
# -----------------------------

products = pd.read_csv(
    f"{RAW_PATH}/olist_products_dataset.csv"
)

products.to_csv(
    f"{PROCESSED_PATH}/olist_products_processed.csv",
    index=False
)


# -----------------------------
# PAYMENTS
# -----------------------------

payments = pd.read_csv(
    f"{RAW_PATH}/olist_order_payments_dataset.csv"
)

payments.to_csv(
    f"{PROCESSED_PATH}/olist_order_payments_processed.csv",
    index=False
)


# -----------------------------
# REVIEWS
# -----------------------------

reviews = pd.read_csv(
    f"{RAW_PATH}/olist_order_reviews_dataset.csv"
)

review_date_columns = [
    "review_creation_date",
    "review_answer_timestamp"
]

for column in review_date_columns:
    reviews[column] = pd.to_datetime(
        reviews[column],
        errors="coerce"
    )


reviews.to_csv(
    f"{PROCESSED_PATH}/olist_order_reviews_processed.csv",
    index=False
)


# -----------------------------
# GEOLOCATION
# -----------------------------

geolocation = pd.read_csv(
    f"{RAW_PATH}/olist_geolocation_dataset.csv"
)

geolocation.to_csv(
    f"{PROCESSED_PATH}/olist_geolocation_processed.csv",
    index=False
)


# -----------------------------
# CATEGORY TRANSLATION
# -----------------------------

category_translation = pd.read_csv(
    f"{RAW_PATH}/product_category_name_translation.csv"
)

category_translation.to_csv(
    f"{PROCESSED_PATH}/product_category_translation_processed.csv",
    index=False
)


print("DATA CLEANING COMPLETED")
print()
print("Processed files saved to:")
print(PROCESSED_PATH)