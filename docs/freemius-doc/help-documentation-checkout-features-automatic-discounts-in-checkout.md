---
title: "How Automatic Discounts Work in the Checkout"
url: "https://freemius.com/help/documentation/checkout/features/automatic-discounts-in-checkout/"
source: "docs"
section: "Docs"
category: "Checkout"
scraped_at: "2026-04-09T19:58:37+06:00"
word_count: 916
---

Freemius Checkout is highly optimized for upsells. For example, if you're selling both monthly and annual subscriptions, our Checkout will automatically upsell the annual pricing to your customers.

The checkout performs the upsell by automatically calculating the discounts when upgrading from a single unit monthly pricing and displaying the discount in the UI. Below is an example of how the checkout will display both annual discount and multi-site discount.

These discounts are calculated automatically; no additional setup is required from your side. Understanding how these discounts are calculated can help you better price your products and explain value to users.

There are three main types of automatic discounts:

- Annual Discount
- Multi-unit Discount
- Bundle Discount

note

A unit is the measure of primary entitlement of licenses you sell through Freemius. For SaaS, it could be credits; for Apps, it could be activations; for WordPress products, it is a Site. Freemius allows you to [customize the unit label in the product settings](help-documentation-saas-customize-license-unit-label.md).

## Annual Discount[​](#annual-discount "Direct link to Annual Discount")

This discount applies when your product is available in both monthly and annual billing cycles.

If your product has a monthly price set, Freemius multiplies that monthly price by 12 (to represent a full year). Then, it compares that amount to your actual annual price. If the annual price is lower, the difference is shown to the customer as a discount.

```text
 Annual Discount = (Single Unit Monthly Price × 12 - Single Unit Annual Price) × Number of Licenses
```

### Example[​](#example "Direct link to Example")

Let's say a product has the following pricing:

UnitsMonthly PriceAnnual Price1$10$1003$25$2505$40$400

The table below shows the annual discount for different numbers of licenses.

Number of Units (Licenses)CalculationAnnual Discount1(10 × 12 − 100)$203(10 × 12 − 100) × 3$60

note

Notice that when purchasing multiple units (licenses), we do not take the monthly and annual price of that pricing into account. This allows us to show multi-unit discounts separately.

### Disabling the Annual Discount[​](#disabling-the-annual-discount "Direct link to Disabling the Annual Discount")

- You can set the `annual_discount` setting to `false` in the [JS SDK](help-documentation-checkout-integration-freemius-checkout-buy-button.md#annual_discount) to disable the annual discount.
- If you're using the [Hosted Checkout](help-documentation-checkout-integration-hosted-checkout.md), simply pass `annual_discount=0` to the checkout URL as a query parameter.

## Multi-unit Discount[​](#multi-unit-discount "Direct link to Multi-unit Discount")

This applies when a customer selects more than one license unit, e.g., a 5-unit license (excluding unlimited licenses). Freemius calculates what the total would cost if each license was priced individually (based on the current billing cycle), and then compares that to the actual price shown for the multi-license purchase.

```text
 Multi-unit Discount = (Single License Price × Number of Licenses) - Current Price
```

### Example[​](#example-1 "Direct link to Example")

For the same pricing configuration as above, the table below shows the multi-unit discount for different numbers of licenses.

Billing CycleNumber of LicensesCalculationMulti-unit DiscountMonthly3(10 × 3) − 25$5Annual3(100 × 3) − 250$50Monthly5(10 × 5) − 40$10Annual5(100 × 5) − 400$100

### Disabling the Multi-unit Discount[​](#disabling-the-multi-unit-discount "Direct link to Disabling the Multi-unit Discount")

- You can set the `multisite_discount` setting to `false` in the [JS SDK](help-documentation-checkout-integration-freemius-checkout-buy-button.md#multisite_discount) to disable the multi-unit discount.
- If you're using the [Hosted Checkout](help-documentation-checkout-integration-hosted-checkout.md), simply pass `multisite_discount=0` to the checkout URL as a query parameter.

note

When the annual discount is disabled, the multi-unit discount is calculated based on the current billing cycle price and not the monthly price.

## Bundle Discount[​](#bundle-discount "Direct link to Bundle Discount")

This applies when your product is part of a bundle of multiple products like plugins, themes, or add-ons.

- We calculate the sum of individual prices of all child products in the bundle. Let's call this the *base price*.
- The annual and multi-unit discounts are calculated based on the bundle's pricing.
- The remaining discount, after deducting the annual and multi-unit discounts, is attributed to the bundle discount.

### Base Price Calculation Modes[​](#base-price-calculation-modes "Direct link to Base Price Calculation Modes")

The base price (undiscounted price) is calculated based on the [`bundle_discount`](help-documentation-checkout-integration-freemius-checkout-buy-button.md#bundle_discount) setting.

`bundle_discount`What Freemius Uses`maximize` (default)Single Unit Monthly Price of each child × current months × license count`true`Current Unit and Current Billing Cycle Price of each child

#### Example[​](#example-2 "Direct link to Example")

Let's say we have two plugins, A and B, with the following pricing:

Plugin APlugin BMonthly price$10$20Annual price$100$200

In such a scenario, the bundle discount will be calculated as follows:

#### With `bundle_discount` set to `maximize`[​](#with-bundle_discount-set-to-maximize "Direct link to with-bundle_discount-set-to-maximize")

- Child sum = (10 + 20) × 12 = $360
- Bundle price = $260
- Bundle discount = $360 − $260 = $100

#### With `bundle_discount` set to `true`[​](#with-bundle_discount-set-to-true "Direct link to with-bundle_discount-set-to-true")

- Child sum (annual) = 100 + 200 = $300
- Bundle price = $260
- Bundle discount = $300 − $260 = $40

note

When `bundle_discount` is not set to `maximize`, we intentionally do not show the Annual Discount percentage in the UI, because the breakdown price of the individual product changes based on the billing cycle itself.

### Disabling the Bundle Discount[​](#disabling-the-bundle-discount "Direct link to Disabling the Bundle Discount")

- You can set the `bundle_discount` setting to `false` in the [JS SDK](help-documentation-checkout-integration-freemius-checkout-buy-button.md#bundle_discount) to disable the bundle discount.
- If you're using the [Hosted Checkout](help-documentation-checkout-integration-hosted-checkout.md), simply pass `bundle_discount=0` to the checkout URL as a query parameter.

That covers everything about automatic discounts in Freemius Checkout. Based on these discounts, Freemius Checkout will automatically display various upsells to customers.

Let us know if you have questions or would like to optimize your pricing setup!