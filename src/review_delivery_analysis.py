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
    CASE
        WHEN o.order_delivered_customer_date
             <= o.order_estimated_delivery_date
        THEN 'On Time'
        WHEN o.order_delivered_customer_date
             > o.order_estimated_delivery_date
        THEN 'Late'
    END AS delivery_status,

    r.review_score,

    COUNT(DISTINCT o.order_id) AS total_orders,

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

INNER JOIN reviews r
    ON o.order_id = r.order_id

WHERE o.order_status = 'delivered'
  AND o.order_delivered_customer_date IS NOT NULL
  AND r.review_score IS NOT NULL

GROUP BY
    CASE
        WHEN o.order_delivered_customer_date
             <= o.order_estimated_delivery_date
        THEN 'On Time'
        WHEN o.order_delivered_customer_date
             > o.order_estimated_delivery_date
        THEN 'Late'
    END,
    r.review_score

ORDER BY
    delivery_status,
    r.review_score;
"""

review_df = pd.read_sql(query, connection)

print("\n========== REVIEW & DELIVERY ANALYSIS ==========")
print(review_df.to_string(index=False))

connection.close()

print("\nDatabase connection closed.")