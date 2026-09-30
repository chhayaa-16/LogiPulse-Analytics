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
    c.customer_city,

    COUNT(DISTINCT o.order_id) AS total_orders,

    COUNT(
        DISTINCT CASE
            WHEN o.order_delivered_customer_date
                 <= o.order_estimated_delivery_date
            THEN o.order_id
        END
    ) AS on_time_orders,

    COUNT(
        DISTINCT CASE
            WHEN o.order_delivered_customer_date
                 > o.order_estimated_delivery_date
            THEN o.order_id
        END
    ) AS late_orders,

    ROUND(
        AVG(
            EXTRACT(
                EPOCH FROM (
                    o.order_delivered_customer_date
                    - o.order_purchase_timestamp
                )
            ) / 86400
        ),
        2
    ) AS average_delivery_days,

    ROUND(
        100.0 *
        COUNT(
            DISTINCT CASE
                WHEN o.order_delivered_customer_date
                     <= o.order_estimated_delivery_date
                THEN o.order_id
            END
        )
        / NULLIF(COUNT(DISTINCT o.order_id), 0),
        2
    ) AS on_time_rate_pct,

    ROUND(
        100.0 *
        COUNT(
            DISTINCT CASE
                WHEN o.order_delivered_customer_date
                     > o.order_estimated_delivery_date
                THEN o.order_id
            END
        )
        / NULLIF(COUNT(DISTINCT o.order_id), 0),
        2
    ) AS late_rate_pct

FROM orders o

INNER JOIN customers c
    ON o.customer_id = c.customer_id

WHERE o.order_status = 'delivered'
  AND o.order_delivered_customer_date IS NOT NULL

GROUP BY
    c.customer_state,
    c.customer_city

HAVING COUNT(DISTINCT o.order_id) >= 20

ORDER BY
    late_rate_pct DESC;
"""

customer_df = pd.read_sql(query, connection)

print("\n========== CUSTOMER LOCATION DELIVERY PERFORMANCE ==========")
print(customer_df.to_string(index=False))

connection.close()

print("\nDatabase connection closed.")