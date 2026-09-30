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
    c.customer_state,

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
        AVG(oi.freight_value)::numeric,
        2
    ) AS average_freight_value,

    ROUND(
        100.0 * SUM(oi.freight_value)
        / NULLIF(SUM(oi.price), 0),
        2
    ) AS freight_to_product_value_pct

FROM order_items oi

INNER JOIN orders o
    ON oi.order_id = o.order_id

INNER JOIN customers c
    ON o.customer_id = c.customer_id

GROUP BY
    c.customer_state

ORDER BY
    freight_to_product_value_pct DESC;
"""

freight_df = pd.read_sql(query, connection)

print("\n========== STATE FREIGHT ANALYSIS ==========")
print(freight_df.to_string(index=False))

connection.close()

print("\nDatabase connection closed.")