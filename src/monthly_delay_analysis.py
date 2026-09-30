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
    DATE_TRUNC(
        'month',
        o.order_purchase_timestamp
    ) AS order_month,

    COUNT(DISTINCT o.order_id) AS late_orders,

    ROUND(
        AVG(
            EXTRACT(
                EPOCH FROM (
                    o.order_delivered_customer_date
                    - o.order_estimated_delivery_date
                )
            ) / 86400
        ),
        2
    ) AS average_delay_days,

    ROUND(
        MAX(
            EXTRACT(
                EPOCH FROM (
                    o.order_delivered_customer_date
                    - o.order_estimated_delivery_date
                )
            ) / 86400
        ),
        2
    ) AS maximum_delay_days

FROM orders o

WHERE o.order_status = 'delivered'
  AND o.order_delivered_customer_date IS NOT NULL
  AND o.order_delivered_customer_date
      > o.order_estimated_delivery_date

GROUP BY
    DATE_TRUNC(
        'month',
        o.order_purchase_timestamp
    )

ORDER BY
    order_month;
"""

delay_df = pd.read_sql(query, connection)

print("\n========== MONTHLY DELIVERY DELAY ANALYSIS ==========")
print(delay_df.to_string(index=False))

connection.close()

print("\nDatabase connection closed.")