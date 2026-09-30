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
WITH state_performance AS (
    SELECT
        c.customer_state,

        COUNT(DISTINCT o.order_id) AS total_orders,

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
        ) AS average_delivery_days

    FROM orders o

    JOIN customers c
        ON o.customer_id = c.customer_id

    WHERE o.order_status = 'delivered'
      AND o.order_delivered_customer_date IS NOT NULL

    GROUP BY
        c.customer_state
),

state_metrics AS (
    SELECT
        customer_state,
        total_orders,
        late_orders,
        average_delivery_days,

        ROUND(
            100.0 * late_orders
            / NULLIF(total_orders, 0),
            2
        ) AS late_rate_pct

    FROM state_performance
),

state_risk AS (
    SELECT
        customer_state,
        total_orders,
        late_orders,
        average_delivery_days,
        late_rate_pct,

        CASE
            WHEN late_rate_pct > 15
                THEN 'Critical Risk'
            WHEN late_rate_pct >= 10
                THEN 'High Risk'
            WHEN late_rate_pct >= 5
                THEN 'Moderate Risk'
            ELSE 'Low Risk'
        END AS delivery_risk

    FROM state_metrics
)

SELECT
    customer_state,
    total_orders,
    late_orders,
    average_delivery_days,
    late_rate_pct,
    delivery_risk

FROM state_risk

ORDER BY
    CASE delivery_risk
        WHEN 'Critical Risk' THEN 1
        WHEN 'High Risk' THEN 2
        WHEN 'Moderate Risk' THEN 3
        WHEN 'Low Risk' THEN 4
    END,
    late_rate_pct DESC;
"""

state_df = pd.read_sql(query, connection)

print("\n========== STATE RISK DETAIL ==========")
print(state_df.to_string(index=False))

connection.close()

print("\nDatabase connection closed.")