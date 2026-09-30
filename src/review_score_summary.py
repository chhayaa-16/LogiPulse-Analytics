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
    r.review_score,

    COUNT(DISTINCT r.order_id) AS total_orders,

    ROUND(
        100.0 *
        COUNT(DISTINCT r.order_id)
        / NULLIF(
            SUM(COUNT(DISTINCT r.order_id)) OVER (),
            0
        ),
        2
    ) AS order_share_pct

FROM reviews r

GROUP BY
    r.review_score

ORDER BY
    r.review_score;
"""

review_df = pd.read_sql(query, connection)

print("\n========== REVIEW SCORE SUMMARY ==========")
print(review_df.to_string(index=False))

connection.close()

print("\nDatabase connection closed.")