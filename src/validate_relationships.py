import pandas as pd


# Load tables
orders = pd.read_csv("data/raw/olist_orders_dataset.csv")
customers = pd.read_csv("data/raw/olist_customers_dataset.csv")
order_items = pd.read_csv("data/raw/olist_order_items_dataset.csv")
products = pd.read_csv("data/raw/olist_products_dataset.csv")
sellers = pd.read_csv("data/raw/olist_sellers_dataset.csv")
payments = pd.read_csv("data/raw/olist_order_payments_dataset.csv")
reviews = pd.read_csv("data/raw/olist_order_reviews_dataset.csv")
translation = pd.read_csv(
    "data/raw/product_category_name_translation.csv"
)


# 1. Orders -> Customers
print("ORDERS -> CUSTOMERS")
missing_customers = orders[
    ~orders["customer_id"].isin(customers["customer_id"])
]

print("Orders with missing customer_id match:")
print(len(missing_customers))


# 2. Order Items -> Orders
print("\nORDER ITEMS -> ORDERS")
missing_orders = order_items[
    ~order_items["order_id"].isin(orders["order_id"])
]

print("Order items with missing order_id match:")
print(len(missing_orders))


# 3. Order Items -> Products
print("\nORDER ITEMS -> PRODUCTS")
missing_products = order_items[
    ~order_items["product_id"].isin(products["product_id"])
]

print("Order items with missing product_id match:")
print(len(missing_products))


# 4. Order Items -> Sellers
print("\nORDER ITEMS -> SELLERS")
missing_sellers = order_items[
    ~order_items["seller_id"].isin(sellers["seller_id"])
]

print("Order items with missing seller_id match:")
print(len(missing_sellers))


# 5. Payments -> Orders
print("\nPAYMENTS -> ORDERS")
missing_payment_orders = payments[
    ~payments["order_id"].isin(orders["order_id"])
]

print("Payments with missing order_id match:")
print(len(missing_payment_orders))


# 6. Reviews -> Orders
print("\nREVIEWS -> ORDERS")
missing_review_orders = reviews[
    ~reviews["order_id"].isin(orders["order_id"])
]

print("Reviews with missing order_id match:")
print(len(missing_review_orders))


# 7. Products -> Category Translation
print("\nPRODUCTS -> CATEGORY TRANSLATION")

product_categories = products[
    "product_category_name"
].dropna().unique()

translation_categories = translation[
    "product_category_name"
].unique()

missing_categories = [
    category
    for category in product_categories
    if category not in translation_categories
]

print("Product categories without translation:")
print(len(missing_categories))

print("\nCategory names without translation:")
print(missing_categories)


print("\nRELATIONSHIP VALIDATION COMPLETED")