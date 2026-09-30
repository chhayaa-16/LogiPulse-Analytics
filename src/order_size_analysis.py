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
WITH order_size AS (
    SELECT
        oi.order_id,
        COUNT(*) AS item_count
    FROM order_items oi
    GROUP BY oi.order_id
)

SELECT
    CASE
        WHEN item_count = 1 THEN '1 Item'
        WHEN item_count = 2 THEN '2 Items'
        WHEN item_count = 3 THEN '3 Items'
        ELSE '4+ Items'
    END AS order_size_category,

    COUNT(*) AS total_orders,

    ROUND(
        AVG(item_count),
        2
    ) AS average_items_per_order

FROM order_size

GROUP BY
    CASE
        WHEN item_count = 1 THEN '1 Item'
        WHEN item_count = 2 THEN '2 Items'
        WHEN item_count = 3 THEN '3 Items'
        ELSE '4+ Items'
    END

ORDER BY
    MIN(item_count);
"""

order_size_df = pd.read_sql(query, connection)

print("\n========== ORDER SIZE ANALYSIS ==========")
print(order_size_df.to_string(index=False))

connection.close()

print("\nDatabase connection closed.")