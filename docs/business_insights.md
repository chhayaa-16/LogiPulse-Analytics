# LogiPulse Analytics – Business Insights

## 1. Executive Summary


## 1. Executive Summary

LogiPulse Analytics analyzes e-commerce logistics performance across orders, deliveries, sellers, freight costs, payments, and customer reviews.

The analysis shows that delivery performance has a significant relationship with customer satisfaction. On-time deliveries receive substantially higher review scores, while delayed and undelivered orders are associated with lower customer ratings.

The project also identifies variation in seller delivery performance, freight costs, order values, and order outcomes. These insights can help logistics and operations teams monitor delivery reliability, identify underperforming sellers, control logistics costs, and improve customer experience.

The dashboard provides an interactive view of these KPIs and enables business users to identify operational patterns across time, geography, sellers, and order status.

## 2. Delivery Performance



## 2. Delivery Performance

### Key Findings

- A large majority of orders were successfully delivered, indicating strong overall order fulfillment.
- Among delivered orders, **7,827 orders were delivered after the estimated delivery date**, highlighting a significant opportunity to improve delivery reliability.
- **166 orders** had a carrier delivery date earlier than the purchase timestamp, indicating data-quality anomalies that should be monitored during operational reporting.
- **23 orders** had a customer delivery date earlier than the carrier delivery date, representing another data-quality inconsistency.
- Seller-level analysis showed considerable variation in delivery performance. The average seller on-time delivery rate was approximately **93.49%**.
- The lowest-performing sellers had substantially higher late-delivery rates, indicating that seller-level monitoring can help identify operational bottlenecks.

### Business Impact

Late deliveries can negatively affect customer experience and may contribute to lower review scores. Monitoring delivery performance by seller, location, and time period can help identify recurring delays and improve fulfillment reliability.

### Recommended Action

- Monitor seller-level on-time delivery rates regularly.
- Investigate sellers with consistently low delivery performance.
- Track estimated-vs-actual delivery time as a core logistics KPI.
- Investigate timestamp anomalies before using the data for operational decisions.

## 3. Customer Satisfaction

## 3. Customer Satisfaction

### Key Findings

- The overall average review score was **4.09 out of 5**.
- **57.78%** of reviews received a score of 5.
- **14.69%** of reviews were low ratings (score ≤ 2).
- On-time deliveries had an average review score of approximately **4.29**.
- Late deliveries had an average review score of approximately **2.27**.
- Orders that were not delivered had an average review score of approximately **1.76**.
- Low ratings were much more common among delayed and undelivered orders:
  - On Time: **9.28%**
  - Late: **62.40%**
  - Not Delivered: **77.66%**

### Delay and Customer Satisfaction

The analysis shows a clear association between delivery delays and customer review scores. As delivery delays increase, average review scores generally decline.

| Delivery Category | Average Review Score | Low Rating % |
|---|---:|---:|
| On Time | 4.29 | 9.28% |
| Late | 2.27 | 62.40% |
| Not Delivered | 1.76 | 77.66% |

### Business Impact

Delivery reliability is closely associated with customer experience in this dataset. Reducing late and undelivered orders may therefore be an important operational area for improving customer satisfaction.

### Recommended Action

- Prioritize investigation of late and undelivered orders.
- Monitor customer reviews alongside delivery KPIs.
- Create alerts for orders approaching their estimated delivery date.
- Identify recurring causes of delays and address them at the seller or logistics level.

## 4. Seller Performance

## 4. Seller Performance

### Key Findings

- The seller analysis covered **1,237 sellers** with delivered-order performance data.
- The average seller on-time delivery rate was approximately **93.49%**.
- Seller performance varied considerably, with the highest observed on-time rate at **100%** and the lowest at approximately **35.71%**.
- **9 sellers** had an on-time delivery rate below **70%**.
- These 9 sellers accounted for **247 delivered orders**, of which **84 were late**, resulting in a late-delivery rate of approximately **34.01%**.

### Business Impact

Seller-level performance varies significantly. A small group of consistently underperforming sellers can create a disproportionate number of delivery problems and negatively affect the overall customer experience.

### Recommended Action

- Track seller-level on-time delivery rate as a regular KPI.
- Investigate sellers with on-time performance below 70%.
- Compare seller performance by order volume before taking operational action.
- Work with consistently underperforming sellers to identify causes of delays.
- Include seller performance monitoring in periodic logistics reviews.

## 5. Freight & Order Value



## 5. Freight & Order Value

### Key Findings

- Order-level logistics analysis includes both product price and freight value.
- Freight value represents an important component of the total order cost and should be monitored alongside order value.
- Monthly order-value analysis can be used to identify changes in sales activity and logistics value over time.
- Freight costs can vary across orders depending on factors such as seller, product, destination, and order characteristics.

### Business Impact

Freight costs directly affect the economics of fulfilling an order. Monitoring freight value alongside order value helps identify orders, sellers, or locations where logistics costs may be relatively high.

### Recommended Action

- Monitor freight value as a percentage of order value.
- Compare freight costs across sellers and geographic locations.
- Identify locations or sellers with consistently high freight costs.
- Track freight-cost trends over time.
- Use freight analysis when evaluating logistics efficiency and operational costs.


## 6. Order Status Analysis



## 6. Order Status Analysis

### Key Findings

The order-status analysis shows that most orders reached the delivered stage, while a smaller proportion experienced cancellation, unavailability, or other intermediate statuses.

The dataset contains the following order statuses:

| Order Status | Orders |
|---|---:|
| Delivered | 96,478 |
| Shipped | 1,107 |
| Canceled | 625 |
| Unavailable | 609 |
| Invoiced | 314 |
| Processing | 301 |
| Created | 5 |
| Approved | 2 |

- Delivered orders represent the dominant order outcome.
- **625 orders were canceled**.
- **609 orders were marked unavailable**.
- Combined, canceled and unavailable orders totaled **1,234 orders**, approximately **1.24%** of all orders.

### Business Impact

Although canceled and unavailable orders represent a relatively small proportion of total orders, they still represent lost fulfillment opportunities and can affect customer experience.

### Recommended Action

- Monitor cancellation and unavailable-order rates regularly.
- Analyze cancellation and unavailability by seller, product category, and location.
- Investigate recurring operational reasons behind unavailable orders.
- Track order-status trends over time to identify changes in fulfillment performance.

## 7. Geographic Analysis

## 7. Geographic Analysis

### Key Findings

The geographic analysis examines logistics performance across customer locations, including states and cities.

Geographic comparisons can reveal differences in:

- Order volume
- Delivery performance
- Freight value
- Customer satisfaction
- Order outcomes

The analysis indicates that logistics performance is not uniform across all geographic areas. Differences in distance, seller location, transportation routes, and regional logistics infrastructure can contribute to variations in delivery performance and freight costs.

### Business Impact

Geographic analysis helps identify locations where delivery delays or higher logistics costs may require additional operational attention.

### Recommended Action

- Monitor delivery performance by customer state and city.
- Compare freight costs across geographic regions.
- Identify regions with consistently higher late-delivery rates.
- Investigate whether high-delay regions are associated with specific sellers or logistics routes.
- Use geographic KPIs to support logistics planning and resource allocation.

## 8. Key Business Problems

## 8. Key Business Problems

Based on the analysis, the major logistics-related business problems identified are:

### 1. Late Deliveries

A significant number of delivered orders were completed after the estimated delivery date, indicating an opportunity to improve delivery reliability.

### 2. Seller Performance Variation

Seller on-time delivery performance varies considerably. A small group of sellers has substantially lower delivery performance and requires closer monitoring.

### 3. Customer Satisfaction Impact

Late and undelivered orders are associated with considerably lower customer review scores compared with on-time deliveries.

### 4. Freight Cost Management

Freight value varies across orders, sellers, and geographic areas. Without monitoring freight costs relative to order value, potentially inefficient logistics patterns may remain unidentified.

### 5. Order Cancellations and Unavailability

Although canceled and unavailable orders represent approximately 1.24% of all orders, they still represent fulfillment opportunities that were not successfully completed.

### 6. Data Quality Issues

Timestamp inconsistencies were identified in some orders, including cases where carrier or customer delivery timestamps occur before logically preceding events. These records should be monitored during future analytics and reporting.

## 9. Business Recommendations

## 9. Business Recommendations

### 1. Improve Delivery Reliability

Monitor estimated versus actual delivery dates and identify recurring causes of late deliveries. Orders approaching their estimated delivery date can be prioritized for operational follow-up.

### 2. Implement Seller Performance Monitoring

Create a regular seller-performance review using KPIs such as:

- On-Time Delivery Rate
- Late Delivery Rate
- Delivered Orders
- Average Delivery Time

Sellers with consistently lower performance can be investigated to identify operational causes.

### 3. Monitor Customer Satisfaction

Track customer review scores together with delivery performance. The strong difference in review scores between on-time, late, and undelivered orders indicates that delivery reliability should be considered when improving customer experience.

### 4. Control Freight Costs

Monitor freight value relative to order value and compare logistics costs across sellers and geographic regions. This can help identify areas where transportation costs require further investigation.

### 5. Reduce Cancellations and Unavailable Orders

Track canceled and unavailable orders by seller, product category, and geographic region. Identifying recurring patterns can help operations teams investigate fulfillment issues.

### 6. Strengthen Data Quality Checks

Implement validation rules for important timestamps and business events. Records containing logically inconsistent dates should be flagged before being used in operational reporting.

### 7. Use the Dashboard for Continuous Monitoring

The Power BI dashboard can be used as a recurring management-reporting tool to monitor logistics KPIs, identify emerging issues, and support data-driven operational decisions.

## 10. Conclusion

## 10. Conclusion

LogiPulse Analytics provides a comprehensive view of e-commerce logistics performance by combining order, delivery, seller, freight, geographic, payment, and customer-review data.

The analysis highlights delivery reliability, seller performance, customer satisfaction, freight costs, and order outcomes as important areas for logistics monitoring.

The findings show a clear association between delivery performance and customer review outcomes, while seller-level analysis reveals meaningful variation in operational performance.

The Power BI dashboard converts these findings into an interactive reporting solution that enables business users to monitor KPIs, identify operational patterns, and investigate areas requiring attention.

Overall, the project demonstrates an end-to-end data analytics workflow:

**Data → Cleaning → SQL Analysis → Data Modeling → Power BI Dashboard → Business Insights → Recommendations**