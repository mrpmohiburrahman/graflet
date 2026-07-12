---
title: "Setup Product, Plans & Pricing"
url: "https://freemius.com/help/documentation/selling-templates/templates-plans-pricing/"
source: "docs"
section: "Docs"
category: "Setup for Templates"
scraped_at: "2026-04-09T19:58:42+06:00"
word_count: 619
---

Here is how to set up your product, plans, billing cycles, prices and currencies for your templates and kits.

## Add the product[​](#add-the-product "Direct link to Add the product")

To create your product;

1. Log in to the [Developer Dashboard](https://dashboard.freemius.com).
2. Click the "**+**" in the top right corner next to the profile picture and click "New Product".
3. Add the required details for your product, which include:
   
   1. A store name,
   2. Title e.g., 'My Template'
   3. And the downloadable file name. This is a unique name for your product e.g. `my-template`.
   4. Upload the product icon to match your brand.
4. Click the "Get Started" button to create your product.

## Add plans[​](#add-plans "Direct link to Add plans")

Creating a new product comes with a default "Pro" plan. You can edit this plan or create more plans for your product. Each plan can have different pricing, billing cycles and settings.

To create your a plan:

1. Under the ***Plans*** page, click the **Add Plan** button to create a new plan.
2. Then insert a title and unique name e.g., 'Pro' and 'pro' respectively.
3. Click the "**Create New**" button to complete the plan setup.

note

- You can create pricing options for plans that offer more than 1 site usage by clicking **Add Bulk** and select the number of units, then enter the relevant pricing options.
- Similarly, you can add pricing in [other currencies](help-documentation-selling-with-freemius-multi-currency.md) by clicking **Add Currency** and select the number of units, then enter the relevant pricing options.

Set up One-Time Fee

To sell templates and kits that don't require recurring payments, you can create a plan with a one-time/lifetime purchase product by adding a price to the Lifetime input field only. This can also be setup for bulk and multiple currencies as in the note above.

The pricing plans will be displayed in the [Freemius Checkout](help-documentation-checkout-integration-freemius-checkout-buy-button.md) when customers purchase your product, as seen here:

## Plans Customization[​](#plans-customization "Direct link to Plans Customization")

To customize the different settings for a specific plan under the ***Plans*** page.

1. Click the respective settings tab.
2. Change the settings as needed.

Here are the settings you can customize for each plan:

### Refund Policy[​](#refund-policy "Direct link to Refund Policy")

By default, the product has a "No Refunds" policy, which means that all sales are final.

This is the recommended option because refunds are only expected if the buyer has not downloaded or accessed the software. Once downloaded, refund requests can be declined unless you choose otherwise. This helps reduce abuse for easily copyable or one-time-use software. However, this can be changed.

To learn more about the available refund policy options visit our [Refund Policy Guide](help-documentation-selling-with-freemius-refund-policy.md).

### Prorated Discount Period[​](#prorated-discount-period "Direct link to Prorated Discount Period")

Freemius supports [proration](help-documentation-selling-with-freemius.md) out of the box, giving incentive to your buyers to upgrade to a higher plan or pricing. While subscriptions are automatically prorated based on the remaining time in the billing cycle, lifetime licenses proration period is set to 30 days by default. You can customize this period.

### Payment Recovery Flow[​](#payment-recovery-flow "Direct link to Payment Recovery Flow")

Freemius [sends recovery emails](help-documentation-marketing-automation-dunning-failed-payments.md). to customers when a payment fails. By default, these link to our Checkout app at `checkout.freemius.com`.

Some buyers may find it confusing to receive an email from your brand/website but be redirected to a third-party domain, which could be mistaken for phishing.

Here you can set a custom recovery URL on your own website for customers.

### Renewals Discount[​](#renewals-discount "Direct link to Renewals Discount")

For products with recurring billing, you can set up a discount for customers who renew their subscription. This is a great way to incentivize customers to continue using your product and reward their loyalty.