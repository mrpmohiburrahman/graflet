---
title: "Calculating Churn Rate"
url: "https://freemius.com/help/documentation/analytics/calculating-churn-rate/"
source: "docs"
section: "Docs"
category: "Analytics"
scraped_at: "2026-04-09T19:58:36+06:00"
word_count: 1192
---

Churn rate represents the percentage of customers who cancel their subscriptions within a given period. This guide will walk you through different approaches to calculating churn using data from Freemius.

## Churn as a Key Business Metric[​](#churn-as-a-key-business-metric "Direct link to Churn as a Key Business Metric")

Understanding churn is critical for measuring the retention of your software subscribers. It is a key metric often evaluated during an acquisition process, as it helps potential buyers assess the health of a subscription-based business. High churn rates can indicate retention issues, while low churn suggests strong customer loyalty and sustainable growth.

## 1. Types of Churn[​](#1-types-of-churn "Direct link to 1. Types of Churn")

There are different ways to define and measure churn. The most common types include:

### 1.1. Subscription Churn[​](#11-subscription-churn "Direct link to 1.1. Subscription Churn")

Subscription churn measures the percentage of individual subscriptions that are canceled, regardless of whether the subscriber has other active subscriptions. This metric focuses on the total number of subscriptions lost rather than the number of unique subscribers lost.

For example, if a customer has three subscriptions and cancels one, it contributes to subscription churn but not subscriber churn.

### 1.2. Customer Churn (or Subscriber Churn)[​](#12-customer-churn-or-subscriber-churn "Direct link to 1.2. Customer Churn (or Subscriber Churn)")

Customer churn measures the percentage of subscribers lost over a specific period.

- **Monthly Churn:** Percentage of subscribers lost in a given month.
- **Annual Churn:** Percentage of subscribers lost over a 12-month period.
- **Cohort-Based Churn:** Tracks churn based on when customers originally subscribed (e.g., tracking all subscriptions created in January 2024 and how many remain active after 12 months).

### 1.3. Revenue Churn[​](#13-revenue-churn "Direct link to 1.3. Revenue Churn")

Revenue churn measures the percentage of recurring revenue lost due to cancellations, downgrades, or non-renewals. It is particularly useful for businesses with variable pricing models.

## 2. Formula for Customer Churn Rate The standard churn formula is:[​](#2-formula-for-customer-churn-rate-the-standard-churn-formula-is "Direct link to 2. Formula for Customer Churn Rate The standard churn formula is:")

However, for subscription-based models, cohort-based churn analysis is often more insightful.

## 3. How to Calculate Churn Using Freemius Data[​](#3-how-to-calculate-churn-using-freemius-data "Direct link to 3. How to Calculate Churn Using Freemius Data")

If you want to calculate annual churn for subscriptions created in January 2024, follow these steps:

### 3.1. Export Subscription Data[​](#31-export-subscription-data "Direct link to 3.1. Export Subscription Data")

Go to your Freemius dashboard and export the **Subscriptions** report.

### 3.2. Identify Relevant Columns[​](#32-identify-relevant-columns "Direct link to 3.2. Identify Relevant Columns")

`created` (subscription start date) `canceled\_at` (cancellation date)

### 3.3. Count Subscriptions Created in January 2024[​](#33-count-subscriptions-created-in-january-2024 "Direct link to 3.3. Count Subscriptions Created in January 2024")

Using Google Sheets, you can count the number of subscriptions created in January 2024 using the following formula:

`=COUNTIFS(A:A, ">=2024-01-01", A:A, "<=2024-01-31")`

where **column A** represents `created_at` formatted as a date.

### 3.4. Count Canceled Subscriptions[​](#34-count-canceled-subscriptions "Direct link to 3.4. Count Canceled Subscriptions")

To count how many of these subscriptions were canceled within 12 months, use:

`=COUNTIFS(A:A, ">=2024-01-01", A:A, "<=2024-01-31", B:B, "<=2025-01-31")`

where **column B** represents `canceled_at` formatted as a date.

### 3.5. Apply the Formula[​](#35-apply-the-formula "Direct link to 3.5. Apply the Formula")

### 3.6. Calculate Average Annual Churn[​](#36-calculate-average-annual-churn "Direct link to 3.6. Calculate Average Annual Churn")

- Repeat this calculation for each month (Feb, Mar, etc.).
- Take the average of the monthly churn percentages to determine the overall annual churn.

## 4. Calculating Revenue Churn[​](#4-calculating-revenue-churn "Direct link to 4. Calculating Revenue Churn")

Revenue churn measures the loss of recurring revenue over a specific period. The formula is:

To calculate revenue churn using Google Sheets:

### 4.1. Sum of Renewal Amounts at the Start of Period[​](#41-sum-of-renewal-amounts-at-the-start-of-period "Direct link to 4.1. Sum of Renewal Amounts at the Start of Period")

`=SUMIFS(C:C, A:A, ">=2024-01-01", A:A, "<=2024-01-31")`

where **column A** is `created_at` and **column C** is `renewal_amount`.

### 4.2. Sum of Lost Revenue Due to Cancellations[​](#42-sum-of-lost-revenue-due-to-cancellations "Direct link to 4.2. Sum of Lost Revenue Due to Cancellations")

`=SUMIFS(C:C, A:A, ">=2024-01-01", A:A, "<=2024-01-31", B:B, "<=2025-01-31")`

where **column B** represents `canceled_at`.

### 4.3. Apply the Formula[​](#43-apply-the-formula "Direct link to 4.3. Apply the Formula")

## 5. Incorporating Trials into Churn Calculations[​](#5-incorporating-trials-into-churn-calculations "Direct link to 5. Incorporating Trials into Churn Calculations")

Freemius provides a `trial_ends` column in the subscription export, which represents the expected first payment date for trial users (or ***null*** for subscriptions without a trial). This column can be used to track trial conversions and calculate churn more accurately by determining how many trials successfully converted to paid subscriptions.

Trials can significantly impact churn calculations depending on how they are handled. There are two common approaches to incorporating trials into churn calculations:

### 5.1. Excluding Trials from Churn Calculations[​](#51-excluding-trials-from-churn-calculations "Direct link to 5.1. Excluding Trials from Churn Calculations")

In this approach, only paid subscriptions are considered. Churn is calculated based on users who have paid at least once. This method is useful when trials have a low conversion rate and could distort churn figures.

### 5.2. Including Trials in Churn Calculations[​](#52-including-trials-in-churn-calculations "Direct link to 5.2. Including Trials in Churn Calculations")

This method treats trial users as part of the subscriber base. If a user starts a trial and does not convert, they are counted as churned. This approach gives a more comprehensive view of user retention but can inflate churn rates.

## 6. Industry Churn Benchmarks[​](#6-industry-churn-benchmarks "Direct link to 6. Industry Churn Benchmarks")

Understanding how your churn rates compare to industry standards can provide valuable insights.

### 6.1. Monthly Churn Benchmarks[​](#61-monthly-churn-benchmarks "Direct link to 6.1. Monthly Churn Benchmarks")

#### SaaS Monthly Churn Benchmarks[​](#saas-monthly-churn-benchmarks "Direct link to SaaS Monthly Churn Benchmarks")

- SaaS businesses typically see monthly churn rates between **3% and 8%**.
- High-performing SaaS businesses aim for churn rates **below 3%**.
- Consumer-oriented subscriptions often experience higher churn rates, sometimes exceeding **10%**.

#### WordPress-Specific Monthly Churn Benchmarks[​](#wordpress-specific-monthly-churn-benchmarks "Direct link to WordPress-Specific Monthly Churn Benchmarks")

- The average annual churn rate for monthly licenses of WordPress plugins is **10.32%**.
- The average annual churn rate for monthly licenses of WordPress add-ons is **10.46%**.
- The average annual churn rate for monthly licenses of WordPress themes is **13.16%**.
- The average annual churn rate for monthly licenses of WordPress bundles is **9.03%**.

### 6.2. Annual Churn Benchmarks[​](#62-annual-churn-benchmarks "Direct link to 6.2. Annual Churn Benchmarks")

#### SaaS Annual Churn Benchmarks[​](#saas-annual-churn-benchmarks "Direct link to SaaS Annual Churn Benchmarks")

- The average annual churn rate for SaaS businesses is **30-50%**.
- Businesses with strong retention strategies maintain churn rates **below 20%**.
- Enterprise SaaS tends to have lower churn rates, often in the **5-15%** range.

#### WordPress-Specific Annual Churn Benchmarks[​](#wordpress-specific-annual-churn-benchmarks "Direct link to WordPress-Specific Annual Churn Benchmarks")

- The average annual churn rate for annual licenses of WordPress plugins is **29%**.
- The average annual churn rate for annual licenses of WordPress add-ons is **30.2%**.
- The average annual churn rate for annual licenses of WordPress themes is **29.3%**.
- The average annual churn rate for annual licenses of WordPress bundles is **31.1%**.

## Conclusion[​](#conclusion "Direct link to Conclusion")

Churn analysis is an essential metric for understanding user retention and improving your subscription strategy. By regularly analyzing churn rates using Freemius data, you can identify trends, optimize your renewal processes, and improve customer retention.