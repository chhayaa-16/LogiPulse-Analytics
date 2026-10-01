# LogiPulse Analytics

## End-to-End Logistics Data Analytics Project

LogiPulse Analytics is an end-to-end Data Analytics project designed to analyze e-commerce logistics performance, delivery efficiency, customer satisfaction, seller performance, freight costs, payments, and operational risks.

The project follows a real-world analytics workflow from data collection and preprocessing to SQL analysis, business insights, and Power BI dashboard development.

---

## Business Problem

E-commerce logistics teams need to monitor delivery performance, identify delays, understand customer dissatisfaction, evaluate seller performance, and control logistics-related costs.

LogiPulse Analytics analyzes these areas to answer key business questions such as:

* How efficiently are orders being delivered?
* How frequently are orders delivered late?
* How does delivery performance affect customer reviews?
* Which sellers have weaker delivery performance?
* How do freight costs vary across states and categories?
* What are the major operational risks?
* Which areas require business attention?

---

## Project Objectives

* Analyze overall order and delivery performance.
* Measure on-time and delayed deliveries.
* Understand the relationship between delivery delays and customer satisfaction.
* Identify high-risk sellers and locations.
* Analyze freight and order values.
* Examine payment and installment behavior.
* Perform data quality and relationship validation.
* Build an interactive Power BI dashboard.
* Generate actionable business insights and recommendations.

---

## Dataset

The project uses an Olist-style Brazilian e-commerce dataset containing information about:

* Customers
* Orders
* Order items
* Payments
* Reviews
* Products
* Sellers
* Product categories
* Geolocation

The original raw datasets are kept locally and are excluded from GitHub using `.gitignore`.

Processed datasets used for analysis are included in the repository.

---

## Technology Stack

| Area                   | Tools         |
| ---------------------- | ------------- |
| Programming            | Python        |
| Data Processing        | Pandas, NumPy |
| Database               | PostgreSQL    |
| Query Language         | SQL           |
| Visualization          | Power BI      |
| Dashboard Calculations | DAX           |
| Documentation          | Markdown      |
| Version Control        | Git & GitHub  |

---

## Project Workflow

```text
Raw Dataset
     ↓
Data Inspection
     ↓
Data Cleaning & Preprocessing
     ↓
Data Validation
     ↓
PostgreSQL Database
     ↓
SQL Analysis
     ↓
Business KPI Development
     ↓
Power BI Data Model
     ↓
Interactive Dashboard
     ↓
Business Insights & Recommendations
```

---

## Project Structure

```text
LogiPulse-Analytics/
│
├── data/
│   ├── raw/                  # Original datasets - excluded from GitHub
│   ├── processed/            # Cleaned datasets used for analysis
│   └── final/                # Final output datasets
│
├── src/
│   ├── clean_data.py
│   ├── load_data.py
│   ├── inspect_*.py
│   ├── validate_*.py
│   ├── *_delivery_*.py
│   ├── *_risk_*.py
│   ├── *_freight_*.py
│   └── *_payment_*.py
│
├── docs/
│   └── business_insights.md
│
├── documentation/
│   ├── data_dictionary.md
│   └── data_quality_report.md
│
├── powerbi/
│   └── Power BI dashboard files
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Key KPIs

The analysis focuses on logistics and customer experience KPIs including:

* Total Orders
* Delivered Orders
* Delivery Delay Rate
* On-Time Delivery Rate
* Average Delivery Time
* Average Freight Value
* Average Order Value
* Customer Review Score
* Low Review Rate
* Seller On-Time Performance
* Cancelled & Unavailable Order Rate
* Payment Value
* Installment Behavior

---

## Key Business Insights

### Delivery Performance

* 99,441 total orders were analyzed.
* 96,478 orders were delivered.
* 7,827 delivered orders were delivered after the estimated delivery date.
* Delivery delays have a strong relationship with lower customer review scores.

### Customer Satisfaction

* Overall average review score was 4.09.
* 57.78% of reviews received a score of 5.
* Late deliveries had an average review score of 2.27.
* On-time deliveries had an average review score of 4.29.
* 62.40% of late-delivery reviews were low scores (≤2).

### Seller Performance

* 1,237 sellers were analyzed for delivery performance.
* Average seller on-time performance was 93.49%.
* 9 sellers had an on-time rate below 70%.
* These low-performing sellers accounted for 247 delivered orders, with approximately 34.01% delivered late.

### Order Status

* Cancelled and unavailable orders together represented approximately 1.24% of all orders.

### Payments

* 99,440 orders had payment records.
* Total order payment value analyzed was approximately 16.01 million.
* Average order payment value was approximately 160.99.

---

## Business Recommendations

Based on the analysis:

1. Monitor sellers with consistently low delivery performance.
2. Investigate operational causes of long delivery delays.
3. Prioritize high-delay locations for logistics improvement.
4. Track freight costs across product categories and locations.
5. Monitor customer satisfaction alongside delivery KPIs.
6. Establish alerts for repeated seller or regional delivery issues.
7. Use Power BI dashboards for continuous logistics performance monitoring.

---

## Power BI Dashboard

The Power BI dashboard provides an interactive view of logistics performance through KPIs, charts, delivery analysis, seller performance, customer satisfaction, freight analysis, and operational insights.

The dashboard is designed to help business stakeholders quickly identify performance trends and areas requiring attention.

---

## Data Quality & Validation

Data quality checks were performed before analysis, including:

* Missing-value analysis
* Duplicate detection
* Date validation
* Relationship validation
* Order-level grain checks
* Payment record checks
* Review record checks
* Product-category validation

Detailed documentation is available in:

* `documentation/data_dictionary.md`
* `documentation/data_quality_report.md`

---

## Business Insights Documentation

Detailed findings and recommendations are available in:

`docs/business_insights.md`

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/chhayaa-16/LogiPulse-Analytics.git
cd LogiPulse-Analytics
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. PostgreSQL

Create the PostgreSQL database and load the processed datasets before running the database analysis scripts.

Database credentials are entered interactively by the Python scripts and are not stored in the repository.

---

## Skills Demonstrated

This project demonstrates practical experience with:

* Python
* Pandas
* NumPy
* Data Cleaning
* Exploratory Data Analysis
* Data Validation
* PostgreSQL
* SQL
* KPI Development
* Business Analysis
* Power BI
* DAX
* Data Visualization
* Dashboard Development
* Business Storytelling
* Git & GitHub
* Technical Documentation

---

## Author

**Chhaya Patil**

Data Analyst | Python | SQL | Power BI | PostgreSQL

---

## Project Status

**Completed**

This project was developed as a portfolio-level end-to-end Data Analytics project with a focus on logistics and e-commerce operations.
