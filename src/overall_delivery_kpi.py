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
    COUNT(DISTINCT o.order_id) AS total_delivered_orders,

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
    ) AS overall_on_time_rate_pct,

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
    ) AS overall_late_rate_pct,

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
    ) AS average_delivery_days

FROM orders o

WHERE o.order_status = 'delivered'
  AND o.order_delivered_customer_date IS NOT NULL;
"""

kpi_df = pd.read_sql(query, connection)

print("\n========== OVERALL DELIVERY KPI ==========")
print(kpi_df.to_string(index=False))

connection.close()

print("\nDatabase connection closed.")