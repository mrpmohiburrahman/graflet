# Refund Payment

This document outlines the various refund options and procedures available to software makers using Freemius.

We empower software makers to issue refunds for product purchases and subscriptions, offering the following options:

* Full refunds
* Partial refunds
* [VAT refunds](#how-to-refund-vat)
* [US sales tax refunds](#how-to-refund-us-sales-tax)

Additionally, full refunds can be processed, excluding fees, helping makers avoid losses on refunded payments.

## How to process a refund[​](#how-to-process-a-refund "Direct link to How to process a refund")

1. As a software maker, log in to the Developer Dashboard.

2. Choose the relevant product.

3. Navigate to the ***Payments*** section.

4. Locate the relevant payment and click the **Refund** button under the `Action` column.
   <!-- -->
   ![Freemius developer dashboard - Refund button on payments page](/help/assets/ideal-img/freemius-developer-dashboard-tax-refund-on-payments.69ae41c.480.png)

5. Select the preferred refund option. This could be partial or full.
   <!-- -->
   ![Freemius developer dashboard payments refund popup dialog box](/help/assets/ideal-img/freemius-developer-dashboard-refund-payments-popup.1a68f11.480.png)

6. You can optionally modify the behavior of the license post-processing the refund.
   <!-- -->
   ![Freemius developer dashboard refunds popup associated license options](/help/assets/ideal-img/freemius-developer-dashboard-refund-payments-popup-associated-license-options.90a2cc9.480.png)

7. Proceed with making a refund note.

   <!-- -->

   ![Freemius developer dashboard refunds popup - add refund note](/help/assets/ideal-img/freemius-developer-dashboard-refund-payments-popup-note.559fabd.480.png)

   note

   All team members, except the product owner, **must** provide a reason for the refund. This note adds context to the refund, ensuring relevant team members are informed. However, this step is optional for the product owner.

8. Next, click the “Yes - Refund & Cancel” button to initiate the refund.

## Tax Refunds[​](#tax-refunds "Direct link to Tax Refunds")

Our system also enables makers to provide VAT and sales tax refunds while retaining the rest of the payment. I.e, a maker can make a refund on only the tax and keep the rest of the payment.

note

The tax refund option ONLY appears for payments with tax.

note

Upon tax refunds of subscription payments, the subscription will be automatically updated to exempt VAT/Sales tax for future renewals.

### How to refund VAT[​](#how-to-refund-vat "Direct link to How to refund VAT")

This pertains to instances where customers did not provide their VAT number in the designated tax field during checkout.

1. Start with steps 1-4 in [how to process a refund](#how-to-process-a-refund) above.

2. Select the **Tax refund** option.

3. Insert the business’ valid VAT number in the appropriate field.

   ![Freemius developer dashboard EU UK VAT tax refund popup](/help/assets/ideal-img/freemius-developer-dashboard-eu-uk-vat-refund-on-payments-popup.b43b92a.480.png)

4. Click the **“Yes - Refund”** button to initiate the refund.

   <!-- -->

   note

   Our system will process a full refund of the original payment and create a new payment, excluding VAT charges. The new reverse charge invoice can be sent to the customer for accounting purposes.

### How to refund US Sales Tax[​](#how-to-refund-us-sales-tax "Direct link to How to refund US Sales Tax")

Currently, our checkout does not support submitting an exemption certification number for tax-exempt entities. To receive an exemption, the purchase must first be made with tax applied, after which the product’s team can issue a refund via the Developer Dashboard.

1. Start with steps 1-4 in [how to process a refund](#how-to-process-a-refund) above.
2. Select the **"Tax refund"** option.
3. Insert the tax exemption certificate number.

   ![Freemius developer dashboard US sales-tax refund payments popup](/help/assets/ideal-img/freemius-developer-dashboard-us-sales-tax-refund-payments-popup.53f17a3.480.png)
4. Read and acknowledge the certificate disclaimer.
5. Click **“Yes - Refund”** to initiate the refund process.

## Refund Processing Timeline[​](#refund-processing-timeline "Direct link to Refund Processing Timeline")

* PayPal refunds are processed immediately.
* A credit card refund may take 5-10 business days to reflect in the buyer’s account.

## Difference in Amount of Partial Refunds[​](#difference-in-amount-of-partial-refunds "Direct link to Difference in Amount of Partial Refunds")

For **full refunds**, the buyer is reimbursed the exact amount paid and in the same currency, regardless of any subsequent currency fluctuations.

**Partial refunds** are handled differently. When a buyer makes a purchase using a credit card or a PayPal account that involves currency conversion, exchange rate fluctuations may affect the refunded amount.

For example, if a German buyer with a settlement currency of EUR purchases a $20 product at a conversion rate of 0.9 EUR per 1 USD, the amount charged in EUR is 18 EUR. Later, if a partial refund of $10 is issued when the conversion rate has shifted to 0.85 EUR per 1 USD, the refund will amount to 8.5 EUR. This results in a discrepancy of 0.5 EUR due to the change in the exchange rate.

## General Refund Policies[​](#general-refund-policies "Direct link to General Refund Policies")

* Once a partial refund is processed, there’s no way to process another one for the same payment.
* PayPal payments can be refunded for up to 180 days.
* Credit card payments can be refunded for up to 365 days.
