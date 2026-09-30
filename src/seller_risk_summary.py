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
        s.seller_id
),

risk_classification AS (
    SELECT
        seller_id,
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
)

SELECT
    performance_risk,
    COUNT(*) AS seller_count,
    SUM(total_orders) AS total_orders,
    ROUND(AVG(on_time_rate_pct), 2) AS average_on_time_rate_pct

FROM risk_classification

GROUP BY
    performance_risk

ORDER BY
    CASE performance_risk
        WHEN 'High Risk' THEN 1
        WHEN 'Needs Attention' THEN 2
        WHEN 'Good' THEN 3
        WHEN 'Excellent' THEN 4
    END;
"""

seller_df = pd.read_sql(query, connection)

print("\n========== SELLER RISK SUMMARY ==========")
print(seller_df.to_string(index=False))

connection.close()

print("\nDatabase connection closed.")