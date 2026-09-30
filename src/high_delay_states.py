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
                     > o.order_estimated_delivery_date
                THEN o.order_id
            END
        )
        / NULLIF(COUNT(DISTINCT o.order_id), 0),
        2
    ) AS late_rate_pct

FROM orders o

JOIN customers c
    ON o.customer_id = c.customer_id

WHERE o.order_status = 'delivered'
  AND o.order_delivered_customer_date IS NOT NULL

GROUP BY
    c.customer_state

HAVING
    COUNT(DISTINCT o.order_id) >= 100

    AND
    100.0 *
    COUNT(
        DISTINCT CASE
            WHEN o.order_delivered_customer_date
                 > o.order_estimated_delivery_date
            THEN o.order_id
        END
    )
    / NULLIF(COUNT(DISTINCT o.order_id), 0) > 10

ORDER BY
    late_rate_pct DESC;
"""

state_df = pd.read_sql(query, connection)

print("\n========== HIGH-DELAY STATES - MEANINGFUL VOLUME ==========")
print(state_df.to_string(index=False))

connection.close()

print("\nDatabase connection closed.")