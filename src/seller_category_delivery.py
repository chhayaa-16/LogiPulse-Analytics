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
    oi.seller_id,
    COALESCE(p.product_category_name, 'Unknown') AS product_category_name,

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
                EPOCH FROM
                (
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

FROM order_items oi

JOIN orders o
    ON oi.order_id = o.order_id

JOIN products p
    ON oi.product_id = p.product_id

WHERE o.order_status = 'delivered'
  AND o.order_delivered_customer_date IS NOT NULL

GROUP BY
    oi.seller_id,
    p.product_category_name

HAVING COUNT(DISTINCT o.order_id) >= 5

ORDER BY
    late_rate_pct DESC,
    total_orders DESC;
"""

seller_category_df = pd.read_sql(query, connection)

print("\n========== SELLER + CATEGORY DELIVERY PERFORMANCE ==========")
print(seller_category_df.to_string(index=False))

connection.close()

print("\nDatabase connection closed.")