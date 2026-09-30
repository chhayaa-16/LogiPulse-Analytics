import pandas as pd


RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"


files = [
    "olist_orders_dataset.csv",
    "olist_customers_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_sellers_dataset.csv",
    "olist_products_dataset.csv",
    "olist_order_payments_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_geolocation_dataset.csv",
    "product_category_name_translation.csv"
]


print("PROCESSED DATA VALIDATION")
print("=" * 50)


for file in files:

    raw_file = f"{RAW_PATH}/{file}"

    if file == "product_category_name_translation.csv":
        processed_file = (
            f"{PROCESSED_PATH}/"
            "product_category_translation_processed.csv"
        )
    else:
        processed_name = file.replace(
            "_dataset.csv",
            "_processed.csv"
        )

        processed_file = (
            f"{PROCESSED_PATH}/{processed_name}"
        )

    raw_df = pd.read_csv(raw_file)
    processed_df = pd.read_csv(processed_file)

    print()
    print(f"FILE: {file}")

    print(
        f"Raw rows: {len(raw_df)}"
    )

    print(
        f"Processed rows: {len(processed_df)}"
    )

    if len(raw_df) == len(processed_df):
        print("ROW COUNT: PASS")
    else:
        print("ROW COUNT: FAIL")

    raw_columns = list(raw_df.columns)
    processed_columns = list(processed_df.columns)

    missing_columns = [
        column
        for column in raw_columns
        if column not in processed_columns
    ]

    if len(missing_columns) == 0:
        print("ORIGINAL COLUMNS: PASS")
    else:
        print(
            "ORIGINAL COLUMNS: FAIL"
        )
        print(
            "Missing columns:",
            missing_columns
        )


print()
print("=" * 50)
print("VALIDATION COMPLETED")