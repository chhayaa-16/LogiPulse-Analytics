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
WITH seller_performance AS (
    SELECT
        s.seller_id,

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
        ) AS late_orders

    FROM sellers s
    JOIN order_items oi
        ON s.seller_id = oi.seller_id
    JOIN orders o
        ON oi.order_id = o.order_id

    WHERE o.order_status = 'delivered'
      AND o.order_delivered_customer_date IS NOT NULL

    GROUP BY
        s.seller_id
),

seller_metrics AS (
    SELECT
        seller_id,
        total_orders,
        on_time_orders,
        late_orders,

        ROUND(
            100.0 * on_time_orders
            / NULLIF(total_orders, 0),
            2
        ) AS on_time_rate_pct,

        ROUND(
            100.0 * late_orders
            / NULLIF(total_orders, 0),
            2
        ) AS late_rate_pct

    FROM seller_performance
)

SELECT
    seller_id,
    total_orders,
    on_time_orders,
    late_orders,
    on_time_rate_pct,
    late_rate_pct

FROM seller_metrics

WHERE on_time_rate_pct < 70
  AND total_orders >= 10

ORDER BY
    late_orders DESC,
    total_orders DESC;
"""

seller_df = pd.read_sql(query, connection)

print("\n========== HIGH RISK SELLERS - MEANINGFUL VOLUME ==========")
print(seller_df.to_string(index=False))

connection.close()

print("\nDatabase connection closed.")