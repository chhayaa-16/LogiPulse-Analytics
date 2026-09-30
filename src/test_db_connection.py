import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="logipulse_db",
    user="postgres",
    password=input("Enter PostgreSQL password: ")
)

print("Database connection successful!")

connection.close()
print("Database connection closed.")