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
    p.payment_installments,

    COUNT(DISTINCT p.order_id) AS total_orders,

    SUM(p.payment_value) AS total_payment_value,

    ROUND(
        AVG(p.payment_value),
        2
    ) AS average_payment_value

FROM payments p

GROUP BY
    p.payment_installments

ORDER BY
    p.payment_installments;
"""

payment_df = pd.read_sql(query, connection)

print("\n========== PAYMENT INSTALLMENT ANALYSIS ==========")
print(payment_df.to_string(index=False))

connection.close()

print("\nDatabase connection closed.")