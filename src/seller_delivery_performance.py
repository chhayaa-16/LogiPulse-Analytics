import pandas as pd
import psycopg2


connection = psycopg2.connect(
    host="localhost",
    database="logipulse_db",
    user="postgres",
    password=input("Enter PostgreSQL password: ")
)

query = """
SELECT
    s.seller_id,
    s.seller_city,
    s.seller_state,
    COUNT(DISTINCT o.order_id) AS total_orders,

    COUNT(
        DISTINCT CASE
            WHEN o.order_delivered_customer_date <= o.order_estimated_delivery_date
            THEN o.order_id
        END
    ) AS on_time_orders,

    COUNT(
        DISTINCT CASE
            WHEN o.order_delivered_customer_date > o.order_estimated_delivery_date
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
        )::numeric,
        2
    ) AS average_delivery_days,

    ROUND(
        100.0 *
        COUNT(
            DISTINCT CASE
                WHEN o.order_delivered_customer_date <= o.order_estimated_delivery_date
                THEN o.order_id
            END
        ) / NULLIF(COUNT(DISTINCT o.order_id), 0),
        2
    ) AS on_time_rate_pct,

    ROUND(
        100.0 *
        COUNT(
            DISTINCT CASE
                WHEN o.order_delivered_customer_date > o.order_estimated_delivery_date
                THEN o.order_id
            END
        ) / NULLIF(COUNT(DISTINCT o.order_id), 0),
        2
    ) AS late_rate_pct

FROM sellers s
JOIN order_items oi
    ON s.seller_id = oi.seller_id
JOIN orders o
    ON oi.order_id = o.order_id

WHERE o.order_status = 'delivered'
  AND o.order_delivered_customer_date IS NOT NULL

GROUP BY
    s.seller_id,
    s.seller_city,
    s.seller_state

ORDER BY
    late_rate_pct DESC;
"""

seller_df = pd.read_sql(query, connection)

print("\n========== SELLER DELIVERY PERFORMANCE ==========")
print(seller_df.to_string(index=False))

connection.close()
print("\nDatabase connection closed.")