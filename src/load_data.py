import psycopg2
import pandas as pd

password = input("Enter PostgreSQL password: ")

connection = psycopg2.connect(
    host="localhost",
    database="logipulse_db"
    user="postgres",
    password=password
)

query = """
SELECT DISTINCT
    o.order_id,
    o.order_status,
    o.order_purchase_timestamp,
    o.order_delivered_customer_date,
    o.order_estimated_delivery_date,
    p.product_category_name
FROM orders o
INNER JOIN order_items oi
    ON o.order_id = oi.order_id
INNER JOIN products p
    ON oi.product_id = p.product_id;
"""

orders_df = pd.read_sql(query, connection)

orders_df["order_estimated_delivery_date"] = pd.to_datetime(
    orders_df["order_estimated_delivery_date"],
    errors="coerce"
)

orders_df["delivery_time_days"] = (
    orders_df["order_delivered_customer_date"]
    - orders_df["order_purchase_timestamp"]
).dt.total_seconds() / 86400

orders_df["on_time_delivery_flag"] = (
    (orders_df["order_status"] == "delivered")
    & (orders_df["order_delivered_customer_date"].notna())
    & (
        orders_df["order_delivered_customer_date"].dt.date
        <= orders_df["order_estimated_delivery_date"].dt.date
    )
)

orders_df["late_delivery_flag"] = (
    (orders_df["order_status"] == "delivered")
    & (orders_df["order_delivered_customer_date"].notna())
    & (
        orders_df["order_delivered_customer_date"].dt.date
        > orders_df["order_estimated_delivery_date"].dt.date
    )
)

delivered_df = orders_df[
    (orders_df["order_status"] == "delivered")
    & (orders_df["order_delivered_customer_date"].notna())
].copy()

category_delivery = (
    delivered_df
    .groupby("product_category_name")
    .agg(
        total_orders=("order_id", "nunique"),
        on_time_orders=("on_time_delivery_flag", "sum"),
        late_orders=("late_delivery_flag", "sum"),
        average_delivery_days=("delivery_time_days", "mean")
    )
    .reset_index()
)

category_delivery["on_time_rate_pct"] = (
    category_delivery["on_time_orders"]
    / category_delivery["total_orders"]
    * 100
)

category_delivery["late_rate_pct"] = (
    category_delivery["late_orders"]
    / category_delivery["total_orders"]
    * 100
)

category_delivery["average_delivery_days"] = (
    category_delivery["average_delivery_days"].round(2)
)

category_delivery["on_time_rate_pct"] = (
    category_delivery["on_time_rate_pct"].round(2)
)

category_delivery["late_rate_pct"] = (
    category_delivery["late_rate_pct"].round(2)
)

category_delivery = category_delivery.sort_values(
    "late_rate_pct",
    ascending=False
)

print("\n========== PRODUCT CATEGORY DELIVERY PERFORMANCE ==========")

print(category_delivery.to_string(index=False))

connection.close()

print("\nDatabase connection closed.")