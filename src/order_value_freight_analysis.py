import pandas as pd
import psycopg2

password = input("Enter PostgreSQL password: ")

connection = psycopg2.connect(
    host="localhost",
    database="logipulse_db",
    user="postgres",
    password=password
)

query = """
SELECT
    COUNT(DISTINCT oi.order_id) AS total_orders,

    ROUND(
        SUM(oi.price)::numeric,
        2
    ) AS total_product_value,

    ROUND(
        SUM(oi.freight_value)::numeric,
        2
    ) AS total_freight_value,

    ROUND(
        AVG(oi.price)::numeric,
        2
    ) AS average_product_price,

    ROUND(
        AVG(oi.freight_value)::numeric,
        2
    ) AS average_freight_value,

    ROUND(
        100.0 * SUM(oi.freight_value)
        / NULLIF(SUM(oi.price), 0),
        2
    ) AS freight_to_product_value_pct

FROM order_items oi;
"""

order_value_df = pd.read_sql(query, connection)

print("\n========== ORDER VALUE & FREIGHT ANALYSIS ==========")
print(order_value_df.to_string(index=False))

connection.close()

print("\nDatabase connection closed.")