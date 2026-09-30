# LogiPulse — Data Dictionary

## 1. Project Information

**Project:** LogiPulse — Logistics & Delivery Performance Analytics

**Dataset:** Olist Brazilian E-Commerce Public Dataset

**Purpose:**  
Define the meaning, data type, role, and analytical usage of important fields
used throughout the LogiPulse analytics project.

---

# 2. Orders Table

**Source:** `olist_orders_dataset.csv`

**Grain:** One row per order.

| Column | Data Type | Description | Analytical Use |
|---|---|---|---|
| `order_id` | String | Unique identifier for an order | Primary order identifier |
| `customer_id` | String | Identifier linking the order to a customer record | Customer analysis and relationships |
| `order_status` | String | Current/status category of the order | Order-status analysis |
| `order_purchase_timestamp` | Datetime | Date and time when the order was placed | Order trends and delivery-time calculations |
| `order_approved_at` | Datetime | Date and time when the order was approved | Order processing analysis |
| `order_delivered_carrier_date` | Datetime | Date and time the order was handed over to the carrier | Fulfillment timeline |
| `order_delivered_customer_date` | Datetime | Date and time the order was delivered to the customer | Actual delivery analysis |
| `order_estimated_delivery_date` | Datetime | Estimated delivery date | Delay and on-time analysis |

---

# 3. Customers Table

**Source:** `olist_customers_dataset.csv`

**Grain:** One row per customer/order customer record.

| Column | Data Type | Description | Analytical Use |
|---|---|---|---|
| `customer_id` | String | Identifier associated with an order's customer record | Relationship with Orders |
| `customer_unique_id` | String | Identifier representing the unique customer | Customer-level analysis |
| `customer_zip_code_prefix` | Integer | Customer ZIP code prefix | Geographic analysis |
| `customer_city` | String | Customer city | Geographic analysis |
| `customer_state` | String | Customer state | Regional analysis |

---

# 4. Order Items Table

**Source:** `olist_order_items_dataset.csv`

**Grain:** One row per item within an order.

| Column | Data Type | Description | Analytical Use |
|---|---|---|---|
| `order_id` | String | Identifier of the related order | Relationship with Orders |
| `order_item_id` | Integer | Sequential item identifier within an order | Item-level grain |
| `product_id` | String | Identifier of the purchased product | Product analysis |
| `seller_id` | String | Identifier of the seller fulfilling the item | Seller analysis |
| `shipping_limit_date` | Datetime | Seller shipping deadline for the item | Fulfillment analysis |
| `price` | Numeric | Price of the item | Sales/value analysis |
| `freight_value` | Numeric | Freight/shipping value associated with the item | Logistics cost analysis |

---

# 5. Sellers Table

**Source:** `olist_sellers_dataset.csv`

**Grain:** One row per seller.

| Column | Data Type | Description | Analytical Use |
|---|---|---|---|
| `seller_id` | String | Unique seller identifier | Seller relationship and analysis |
| `seller_zip_code_prefix` | Integer | Seller ZIP code prefix | Geographic analysis |
| `seller_city` | String | Seller city | Geographic analysis |
| `seller_state` | String | Seller state | Regional seller analysis |

---

# 6. Products Table

**Source:** `olist_products_dataset.csv`

**Grain:** One row per product.

| Column | Data Type | Description | Analytical Use |
|---|---|---|---|
| `product_id` | String | Unique product identifier | Product relationship |
| `product_category_name` | String | Product category name in source language | Product category analysis |
| `product_name_lenght` | Numeric | Length of product name | Product metadata |
| `product_description_lenght` | Numeric | Length of product description | Product metadata |
| `product_photos_qty` | Numeric | Number of product photos | Product metadata |
| `product_weight_g` | Numeric | Product weight in grams | Logistics/product analysis |
| `product_length_cm` | Numeric | Product length in centimeters | Logistics/product analysis |
| `product_height_cm` | Numeric | Product height in centimeters | Logistics/product analysis |
| `product_width_cm` | Numeric | Product width in centimeters | Logistics/product analysis |

---

# 7. Payments Table

**Source:** `olist_order_payments_dataset.csv`

**Grain:** One row per payment record associated with an order.

| Column | Data Type | Description | Analytical Use |
|---|---|---|---|
| `order_id` | String | Identifier of the related order | Relationship with Orders |
| `payment_sequential` | Integer | Sequential number of the payment within an order | Payment record identification |
| `payment_type` | String | Payment method/type | Payment-method analysis |
| `payment_installments` | Integer | Number of installments | Payment behavior analysis |
| `payment_value` | Numeric | Value of the payment | Payment/value analysis |

---

# 8. Reviews Table

**Source:** `olist_order_reviews_dataset.csv`

**Grain:** Review record associated with an order.

| Column | Data Type | Description | Analytical Use |
|---|---|---|---|
| `review_id` | String | Identifier associated with the review record | Review identification |
| `order_id` | String | Identifier of the reviewed order | Relationship with Orders |
| `review_score` | Integer | Customer review score | Customer satisfaction analysis |
| `review_comment_title` | String | Review title/comment | Textual review analysis if required |
| `review_comment_message` | String | Review message | Textual review analysis if required |
| `review_creation_date` | Datetime | Review creation date | Review trend analysis |
| `review_answer_timestamp` | Datetime | Timestamp associated with the review response | Review response analysis |

---

# 9. Geolocation Table

**Source:** `olist_geolocation_dataset.csv`

**Grain:** Geolocation record associated with a ZIP code prefix.

| Column | Data Type | Description | Analytical Use |
|---|---|---|---|
| `geolocation_zip_code_prefix` | Integer | ZIP code prefix | Geographic mapping |
| `geolocation_lat` | Numeric | Latitude | Geographic analysis |
| `geolocation_lng` | Numeric | Longitude | Geographic analysis |
| `geolocation_city` | String | City associated with the location | Geographic analysis |
| `geolocation_state` | String | State associated with the location | Geographic analysis |

**Note:**  
The geolocation table contains repeated ZIP code prefixes and exact duplicate
rows. It must therefore be handled carefully before joining it to transactional
tables.

---

# 10. Category Translation Table

**Source:** `product_category_name_translation.csv`

**Grain:** One row per translated product category.

| Column | Data Type | Description | Analytical Use |
|---|---|---|---|
| `product_category_name` | String | Original Portuguese product category | Relationship with Products |
| `product_category_name_english` | String | English translation of the product category | Dashboard and business reporting |

---

# 11. Important Business Fields

The following fields are particularly important for LogiPulse:

### Order Performance

- `order_id`
- `order_status`
- `order_purchase_timestamp`
- `order_delivered_carrier_date`
- `order_delivered_customer_date`
- `order_estimated_delivery_date`

### Customer

- `customer_id`
- `customer_unique_id`
- `customer_city`
- `customer_state`

### Product

- `product_id`
- `product_category_name`
- `product_weight_g`
- `product_length_cm`
- `product_height_cm`
- `product_width_cm`

### Seller

- `seller_id`
- `seller_city`
- `seller_state`

### Financial / Logistics

- `price`
- `freight_value`
- `payment_value`
- `payment_type`

### Customer Experience

- `review_score`
- `review_comment_title`
- `review_comment_message`

---

# 12. Important Data Modeling Notes

## Order Grain

The Orders table is at:

**Order level**

while Order Items is at:

**Order-item level**

Therefore, joining Order Items to Orders creates multiple rows for orders containing multiple items.

---

## Payment Grain

Payments can contain multiple records for the same order.

Therefore, payment values must be aggregated at the required business grain before combining them with other transactional data.

---

## Review Grain

Review records require additional investigation because repeated `review_id`
values were observed during data profiling.

---

## Geolocation Grain

Geolocation contains multiple records for the same ZIP code prefix.

It should not be directly joined to transaction tables without controlling the
join grain.

---

# 13. Data Type Transformation Plan

The raw files contain several date fields stored as strings.

During the processed-data stage, the following fields will be converted to
datetime:

- `order_purchase_timestamp`
- `order_approved_at`
- `order_delivered_carrier_date`
- `order_delivered_customer_date`
- `order_estimated_delivery_date`
- `shipping_limit_date`
- `review_creation_date`
- `review_answer_timestamp`

Numeric fields will be retained as numeric types.

Identifier fields such as `order_id`, `customer_id`, `product_id`, and
`seller_id` will remain identifiers rather than being treated as numeric
measures.

---

# 14. Raw Data Preservation Rule

The files inside:

`data/raw/`

will remain unchanged.

All cleaning, renaming, missing-value handling, type conversion, and
transformation will occur in the processed/final data layers.

---

# 15. Future Analytical Definitions

The final definitions of business KPIs will be established after the processed
data model is created.

Potential measures include:

- Total Orders
- Total Order Items
- On-Time Delivery Rate
- Late Delivery Rate
- Average Delivery Time
- Average Delay
- Total Item Value
- Total Freight Value
- Average Freight per Item
- Average Review Score

Each KPI will have a documented calculation and defined analytical grain.