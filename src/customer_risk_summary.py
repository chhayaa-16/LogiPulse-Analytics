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
WITH customer_performance AS (
    SELECT
        c.customer_state,
        c.customer_city,

        COUNT(DISTINCT o.order_id) AS total_orders,

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
),

customer_risk AS (
    SELECT
        customer_state,
        customer_city,
        total_orders,
        late_orders,
        late_rate_pct,

        CASE
            WHEN late_rate_pct > 20 THEN 'Critical Risk'
            WHEN late_rate_pct >= 10 THEN 'High Risk'
            WHEN late_rate_pct >= 5 THEN 'Moderate Risk'
            ELSE 'Low Risk'
        END AS customer_delivery_risk

    FROM customer_performance
)

SELECT
    customer_delivery_risk,
    COUNT(*) AS city_count,
    SUM(total_orders) AS total_orders,
    SUM(late_orders) AS total_late_orders,

    ROUND(
        AVG(late_rate_pct),
        2
    ) AS average_late_rate_pct

FROM customer_risk

GROUP BY
    customer_delivery_risk

ORDER BY
    CASE customer_delivery_risk
        WHEN 'Critical Risk' THEN 1
        WHEN 'High Risk' THEN 2
        WHEN 'Moderate Risk' THEN 3
        WHEN 'Low Risk' THEN 4
    END;
"""

customer_df = pd.read_sql(query, connection)

print("\n========== CUSTOMER DELIVERY RISK SUMMARY ==========")
print(customer_df.to_string(index=False))

connection.close()

print("\nDatabase connection closed.")