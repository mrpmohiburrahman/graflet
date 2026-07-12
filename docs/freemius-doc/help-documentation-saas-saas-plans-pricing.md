---
title: "SaaS and Apps Plans & Pricing"
url: "https://freemius.com/help/documentation/saas/saas-plans-pricing/"
source: "docs"
section: "Docs"
category: "Setup for SaaS & Apps"
scraped_at: "2026-04-09T19:58:42+06:00"
word_count: 501
---

In this guide we will learn how to configure pricing plans for your users, each with distinct billing cycles, prices, number of units (e.g., seats, devices, credits), currencies and feature sets.

## Setting up plans[​](#setting-up-plans "Direct link to Setting up plans")

To create your first plan:

1. Log in to the [Developer Dashboard](https://dashboard.freemius.com).
2. Navigate to the ***Plans*** page.
3. Click the **Add Plan** button to create a new plan.
4. Then insert a specify a title and unique name e.g., 'Pro' and 'pro'.
5. Enter information about the plan such as pricing for the **Single Unit** option.

tip

- You can create pricing options for plans that offer more than 1 unit. To do this click **Add Bulk** and select the number of units, then enter the relevant pricing options.
- Similarly, you can add pricing in other currencies. This is done by clicking **Add Currency** and select the number of units, then enter the relevant pricing options.

The pricing plans will be displayed in the [Freemius Checkout](help-documentation-checkout-integration-freemius-checkout-buy-button.md) when customers purchase your product, as seen here:

## Plans Customization[​](#plans-customization "Direct link to Plans Customization")

There are other settings you can fill out to customize your plans, such as:

- [Additional currencies](help-documentation-selling-with-freemius-multi-currency.md)
- [Free and Paid Trials](#free-and-paid-trials)
- [Features](#configure-a-plans-features)
- [Refund Policy](help-documentation-saas-setup-refund-policy.md)
- [Checkout Confirmation Dialog](#checkout-confirmation-dialog)
- [Checkout Success Redirection](#checkout-success-redirection)
- [Customize License Unit Label](help-documentation-saas-customize-license-unit-label.md)
- [Checkout CSS](help-documentation-checkout-customization-applying-css-customization.md)

### Free and Paid Trials[​](#free-and-paid-trials "Direct link to Free and Paid Trials")

Freemius enables you to easily offer free trials for your users, with or without requiring a payment method. Offering a free trial may help you increase your product’s distribution and sales. See the [supported trial types](help-documentation-wordpress-free-trials.md).

### Configure a Plan's Features[​](#configure-a-plans-features "Direct link to Configure a Plan's Features")

You can set up the features for each plan.

These can be set up by:

1. Navigating to ***Plans*** page.
2. Click the relevant plan to edit its details.
3. Scroll down to the **Features** section.
4. Add the respective feature details. Type the name of the feature and click the “+” button or press enter to add it to the plan. Repeat this step until you've added all the required features.

tip

These features can be accessed later using the [Features API endpoint](https://docs.freemius.com/api/products/list-features).

### Checkout Confirmation Dialog[​](#checkout-confirmation-dialog "Direct link to Checkout Confirmation Dialog")

After purchasing, customers will see a confirmation dialog that includes a thank-you message and a close button. The custom dialog allows the title, message and button to be configured. It is accessible via the **Customization** tab, under the **Plans** page. [Learn more](help-documentation-checkout-customization-customizing-confirmation-dialog.md).

### Checkout Success Redirection[​](#checkout-success-redirection "Direct link to Checkout Success Redirection")

Under the **Plans** page, via the **Customization** tab, you can set a redirection URL where the Checkout will take the customer after a successful purchase. It will work only for Checkouts opened in page mode and will not show the confirmation dialog (even if customized). The URL will be automatically populated with purchase data. [Learn more](help-documentation-checkout-integration-hosted-checkout.md#redirection-after-a-successful-purchase).

note

Click [here](help-documentation-wordpress-setup-product-pricing-plans-refunds.md) to set up WordPress and other products pricing.