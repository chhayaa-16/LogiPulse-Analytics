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
        s.seller_city,
        s.seller_state,

        COUNT(DISTINCT o.order_id) AS total_orders,

        ROUND(
            100.0 *
            COUNT(
                DISTINCT CASE
                    WHEN o.order_delivered_customer_date
                         <= o.order_estimated_delivery_date
                    THEN o.order_id
                END
            ) / NULLIF(COUNT(DISTINCT o.order_id), 0),
            2
        ) AS on_time_rate_pct

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
)

SELECT
    seller_id,
    seller_city,
    seller_state,
    total_orders,
    on_time_rate_pct,

    CASE
        WHEN on_time_rate_pct >= 95
            THEN 'Excellent'
        WHEN on_time_rate_pct >= 85
            THEN 'Good'
        WHEN on_time_rate_pct >= 70
            THEN 'Needs Attention'
        ELSE 'High Risk'
    END AS performance_risk

FROM seller_performance

ORDER BY
    on_time_rate_pct ASC;
"""

seller_df = pd.read_sql(query, connection)

print("\n========== SELLER PERFORMANCE RISK BUCKETS ==========")
print(seller_df.to_string(index=False))

connection.close()

print("\nDatabase connection closed.")