# Beauty_E-Retail
# UK E-Commerce Beauty Retail: Customer Segmentation & RFM Analytics


![Tableau Dashboard Status](https://img.shields.io/badge/Tableau_Public-Published-blue?logo=tableau)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white)

## Executive Summary
An end-to-end customer analytics project designed for a UK-based e-commerce beauty & skincare retailer. Using transactional data from 1,500+ UK customers (£), this project applies **RFM (Recency, Frequency, Monetary) Segmentation** to identify high-value customer groups, detect churn risks, and deliver actionable marketing strategies to optimize Customer Lifetime Value (LTV) and Retention.



## Interactive Dashboard
🔗 **[View Interactive Tableau Dashboard]((https://public.tableau.com/app/profile/ekaterina.korobkova/viz/UKBeautyRetail-RFMAnalyticsDashboard/Dashboard1?publish=yes)

### Key Dashboard Insights:
1. **Customer Count by Segment:** Identifies the distribution of unique customers across 5 main behavioral segments (`Champions`, `Loyal Customers`, `At-Risk`, `New Customers`, `Hibernating/Lost`).
2. **Total Revenue by Segment:** Highlights which customer groups drive the highest monetary value (£) for the business.

---
## Model Interpretation & Business Insights

Our Logistic Regression model achieved a **94% overall accuracy**, highlighting key drivers of customer churn in the UK Beauty Retail sector[cite: 15]:

* **Frequency is King:** The coefficient for purchase frequency (-0.188)[cite: 15] demonstrates that keeping customers engaged on a regular basis is the single most effective way to prevent churn. 
* **Actionable Takeaway:** Instead of focusing marketing budget exclusively on high-spending VIPs, retention campaigns should target customers whose purchase *frequency* begins to drop, triggering automated re-engagement workflows before they completely churn.

## Tech Stack & Workflow

1. **SQL (SQLite):**
   * Aggregated transactional logs to calculate base $R, F, M$ metrics per customer.
   * Applied quantile scoring (1–5) and conditional segment assignment rules.

2. **Python (Pandas):**
   * Automated data processing, cleaning, and export pipelines (`scripts/rfm_pipeline.py`).
   * Generated structured datasets for BI tools.

3. **Data Visualization (Tableau Public):**
   * Designed an intuitive, multi-chart interactive dashboard highlighting key performance indicators.

---

## Key Segment Recommendations

| Segment | Strategy & Marketing Action |
| :--- | :--- |
| **Champions** | VIP loyalty perks, early access to new product launches, brand advocacy. |
| **Loyal Customers** | Cross-selling / up-selling campaigns, tailored product recommendations. |
| **New Customers** | Onboarding welcome email sequences, 2nd-purchase discount incentives. |
| **At-Risk** | Personalized win-back campaigns, limited-time special discounts. |
| **Hibernating / Lost** | Low-cost automated reactivation or database cleanup. |

---

Beauty_E-Retail/
├── data/
│   └── uk_beauty_rfm_segments.csv
├── scripts/
│   ├── generate_beauty_retail_data.py
│   ├── rfm_analysis.py
│   └── churn_prediction.py
└── README.md


