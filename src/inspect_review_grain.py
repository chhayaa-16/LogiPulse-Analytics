import pandas as pd


file_path = "data/raw/olist_order_reviews_dataset.csv"

df = pd.read_csv(file_path)


# Find duplicated review IDs
duplicate_review_ids = df[
    df["review_id"].duplicated(keep=False)
].sort_values("review_id")


print("NUMBER OF DUPLICATED REVIEW IDs:")
print(duplicate_review_ids["review_id"].nunique())


print("\nNUMBER OF ROWS WITH DUPLICATED REVIEW IDs:")
print(len(duplicate_review_ids))


print("\nSAMPLE DUPLICATED REVIEW IDs:")
print(
    duplicate_review_ids[
        ["review_id", "order_id", "review_score"]
    ].head(20)
)


# Check how many orders have multiple review records
review_count_per_order = (
    df.groupby("order_id")
    .size()
    .reset_index(name="review_record_count")
)


multiple_review_orders = review_count_per_order[
    review_count_per_order["review_record_count"] > 1
]


print("\nORDERS WITH MULTIPLE REVIEW RECORDS:")
print(len(multiple_review_orders))


print("\nTOTAL REVIEW RECORDS BELONGING TO THESE ORDERS:")
print(
    multiple_review_orders["review_record_count"].sum()
)


# Show sample orders with multiple review records
sample_order_ids = multiple_review_orders[
    "order_id"
].head(10)


sample_multiple_reviews = df[
    df["order_id"].isin(sample_order_ids)
].sort_values("order_id")


print("\nSAMPLE ORDERS WITH MULTIPLE REVIEW RECORDS:")
print(
    sample_multiple_reviews[
        [
            "review_id",
            "order_id",
            "review_score",
            "review_comment_title",
            "review_comment_message"
        ]
    ]
)


print("\nREVIEW GRAIN INVESTIGATION COMPLETED")