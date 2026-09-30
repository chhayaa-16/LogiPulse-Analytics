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
WITH delivery_delay AS (
    SELECT
        o.order_id,

        EXTRACT(
            EPOCH FROM (
                o.order_delivered_customer_date
                - o.order_estimated_delivery_date
            )
        ) / 86400 AS delay_days

    FROM orders o

    WHERE o.order_status = 'delivered'
      AND o.order_delivered_customer_date IS NOT NULL
      AND o.order_delivered_customer_date
          > o.order_estimated_delivery_date
)

SELECT
    CASE
        WHEN delay_days <= 3 THEN '1-3 Days Late'
        WHEN delay_days <= 7 THEN '4-7 Days Late'
        WHEN delay_days <= 14 THEN '8-14 Days Late'
        ELSE '15+ Days Late'
    END AS delay_category,

    COUNT(DISTINCT order_id) AS total_orders,

    ROUND(
        AVG(delay_days),
        2
    ) AS average_delay_days

FROM delivery_delay

GROUP BY
    CASE
        WHEN delay_days <= 3 THEN '1-3 Days Late'
        WHEN delay_days <= 7 THEN '4-7 Days Late'
        WHEN delay_days <= 14 THEN '8-14 Days Late'
        ELSE '15+ Days Late'
    END

ORDER BY
    MIN(delay_days);
"""

delay_df = pd.read_sql(query, connection)

print("\n========== DELIVERY DELAY SEVERITY ==========")
print(delay_df.to_string(index=False))

connection.close()

print("\nDatabase connection closed.")