# LogiPulse — Data Quality Report

## 1. Project

**Project Name:** LogiPulse — Logistics & Delivery Performance Analytics

**Dataset:** Olist Brazilian E-Commerce Public Dataset

**Purpose:**  
To assess the quality, completeness, consistency, and relationships of the raw
data before performing cleaning, transformation, SQL analysis, and Power BI
reporting.

---

# 2. Raw Tables Inspected

The following raw tables were inspected:

1. olist_orders_dataset.csv
2. olist_customers_dataset.csv
3. olist_order_items_dataset.csv
4. olist_order_payments_dataset.csv
5. olist_order_reviews_dataset.csv
6. olist_products_dataset.csv
7. olist_sellers_dataset.csv
8. olist_geolocation_dataset.csv
9. product_category_name_translation.csv

---

# 3. Orders Table

**Rows:** 99,441

**Columns:** 8

### Key findings

- No missing `order_id`
- No duplicate `order_id`
- No exact duplicate rows
- 160 missing `order_approved_at`
- 1,783 missing `order_delivered_carrier_date`
- 2,965 missing `order_delivered_customer_date`
- 8 delivered orders have missing customer delivery dates

### Date validation

- 0 approval dates occur before purchase dates
- 166 carrier dates occur before purchase dates
- 0 customer delivery dates occur before purchase dates
- 23 customer delivery dates occur before carrier dates
- 7,827 delivered orders occurred after the estimated delivery date

### Treatment

- Missing dates will not be fabricated.
- Estimated delivery dates will not be used as actual delivery dates.
- Date-sequence exceptions will be documented and handled during transformation.
- Late deliveries will be retained because they represent potential business-performance observations.


# 4. Customers Table

**Rows:** 99,441

**Columns:** 5

### Key findings

- No missing values
- No exact duplicate rows
- `customer_id` is unique
- `customer_unique_id` is retained as a separate customer identifier

### Treatment

- No immediate cleaning required.


# 5. Order Items Table

**Rows:** 112,650

**Columns:** 7

### Key findings

- No missing values
- No exact duplicate rows
- `order_id` is repeated because an order can contain multiple items
- `(order_id, order_item_id)` is unique

### Treatment

- Repeated `order_id` values will not be removed.
- Table grain will be preserved as order-item level.
- Care will be taken to avoid row multiplication during joins.


# 6. Sellers Table

**Rows:** 3,095

**Columns:** 4

### Key findings

- No missing values
- No exact duplicate rows
- `seller_id` is unique

### Treatment

- No immediate cleaning required.


# 7. Products Table

**Rows:** 32,951

**Columns:** 9

### Key findings

- No missing `product_id`
- No duplicate `product_id`
- 610 missing values in product descriptive fields
- 2 missing values in each of the following physical attributes:
  - `product_weight_g`
  - `product_length_cm`
  - `product_height_cm`
  - `product_width_cm`
- Source column `product_name_lenght` contains the original dataset spelling

### Treatment

- Missing product information will not be fabricated.
- Physical attributes will be handled according to their analytical use.
- Original raw column names will not be changed in the raw layer.
- Any naming corrections will be performed only in the processed layer if required.


# 8. Payments Table

**Rows:** 103,886

**Columns:** 5

### Key findings

- No missing values
- No exact duplicate rows
- `order_id` can repeat because an order may contain multiple payment records
- One order from the Orders table has no payment record

### Affected Order

`bfbd0f9bdef84302105ad712db648a6c`

The order has 3 order-item records but no payment record.

### Treatment

- The order will not be deleted.
- No payment value will be fabricated.
- Payment-based analysis will account for the missing payment record.


# 9. Reviews Table

**Rows:** 99,224

**Columns:** 7

### Key findings

- No missing `review_id`
- No missing `order_id`
- No missing `review_score`
- 87,656 missing review titles
- 58,247 missing review messages
- 814 duplicate `review_id` values
- `order_id` can repeat

### Treatment

- Missing review text will not be fabricated.
- Review score will be retained.
- Review table grain and duplicate review identifiers will be investigated before final modeling.


# 10. Geolocation Table

**Rows:** 1,000,163

**Columns:** 5

### Key findings

- No missing values
- 261,831 exact duplicate rows
- ZIP code prefixes are repeated extensively
- 19,015 unique ZIP code prefixes

### Treatment

- Duplicate geolocation rows will not automatically be treated as errors.
- The table will not be directly joined to transactional tables without considering potential many-to-many relationships.
- Geographic analysis will use an appropriate aggregated or reference structure.


# 11. Category Translation Table

**Rows:** 71

**Columns:** 2

### Key findings

- No missing values
- No exact duplicate rows
- 71 unique Portuguese category names
- 71 unique English category names
- 2 product categories do not have translations:
  - `pc_gamer`
  - `portateis_cozinha_e_preparadores_de_alimentos`

### Treatment

- Original category names will be preserved.
- Missing translations will not cause product records to be deleted.
- Translation handling will occur during the processed-data transformation stage.


# 12. Relationship Validation

The following relationships were validated:

| Relationship | Result |
|---|---|
| Orders → Customers | Valid |
| Order Items → Orders | Valid |
| Order Items → Products | Valid |
| Order Items → Sellers | Valid |
| Payments → Orders | Valid in payment-to-order direction |
| Reviews → Orders | Valid |
| Products → Category Translation | 2 categories without translation |

---

# 13. Important Data Quality Findings

| Finding | Count | Classification |
|---|---:|---|
| Missing order approval dates | 160 | Missing data |
| Missing carrier dates | 1,783 | Missing data |
| Missing customer delivery dates | 2,965 | Missing data |
| Delivered orders missing customer delivery date | 8 | Important exception |
| Carrier date before purchase | 166 | Date-sequence exception |
| Customer delivery before carrier date | 23 | Date-sequence exception |
| Deliveries after estimated date | 7,827 | Business observation |
| Product categories without translation | 2 | Mapping exception |
| Orders without payment records | 1 | Relationship exception |
| Exact duplicate geolocation rows | 261,831 | Structural/reference duplication |
| Duplicate review IDs | 814 | Identifier/grain issue |

---

# 14. Data Cleaning Principles

The following principles will be followed during the cleaning phase:

1. Raw data will never be overwritten.
2. Missing values will not be fabricated.
3. Business exceptions will not automatically be treated as errors.
4. Duplicate records will only be removed when their duplication is confirmed to be invalid.
5. Table grain will be preserved.
6. Joins will be designed to avoid row multiplication.
7. Date-based KPIs will use only valid and available timestamps.
8. Payment-based metrics will not assume missing payment values.
9. Category translation gaps will be handled explicitly.
10. All major cleaning decisions will be documented.

---

# 15. Data Lineage

The project will follow this structure:

RAW DATA
    ↓
DATA VALIDATION
    ↓
PROCESSED DATA
    ↓
FINAL ANALYTICAL DATA
    ↓
SQL DATABASE
    ↓
POWER BI
    ↓
BUSINESS INSIGHTS

The raw data layer will remain unchanged and reproducible.

---

# 16. Current Status

Data profiling and initial data-quality validation are complete.

The next stage is to create the project data dictionary and then perform controlled data cleaning and transformation.