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
    p.payment_type,

    COUNT(DISTINCT p.order_id) AS total_orders,

    SUM(p.payment_value) AS total_payment_value,

    ROUND(
        AVG(p.payment_value),
        2
    ) AS average_payment_value,

    ROUND(
        AVG(p.payment_installments),
        2
    ) AS average_installments

FROM payments p

GROUP BY
    p.payment_type

ORDER BY
    total_payment_value DESC;
"""

payment_df = pd.read_sql(query, connection)

print("\n========== PAYMENT PERFORMANCE ==========")
print(payment_df.to_string(index=False))

connection.close()

print("\nDatabase connection closed.")