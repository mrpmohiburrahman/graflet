---
title: "Setting up Coupon Discounts with Configurable Segments, Types & Plans"
url: "https://freemius.com/help/documentation/selling-with-freemius/coupon-discount/"
source: "docs"
section: "Docs"
category: "Selling with Freemius"
scraped_at: "2026-04-09T19:58:43+06:00"
word_count: 933
---

Coupons are a powerful marketing tool that allow you to offer discounts to customers, incentivizing them to make a purchase or renew their subscription.

## How to create a discount coupon[​](#how-to-create-a-discount-coupon "Direct link to How to create a discount coupon")

A coupon can be created at both the **store** and **product** levels. If a coupon is created at the store level, it can be applied to any product within that store. If a coupon is created at the product level, it will only be applicable to that specific product.

Follow these steps to create a new coupon:

1. Log in to your [Freemius Developer Dashboard](https://dashboard.freemius.com/).
2. Select the store or product where you want to create the coupon.
3. Navigate to the **Coupons** page in the Developer Dashboard.
4. Select the **Coupons** tab.
5. Click the **Add Coupon** button.
6. A settings panel will open with options such as the coupon name, [lifespan](#lifespan), [discount type](#discount-type), [number of redemptions](#redemptions), [who can redeem the coupon](#who-can-redeem-the-coupon), and [where to apply it](#where-to-apply-the-coupon).
7. After configuring the coupon, scroll to the bottom of the panel and click **Create**. The new coupon will then appear in the coupons table.

note

You can also duplicate or delete existing coupons from the coupons table by clicking the **Duplicate** or **Delete** buttons next to each coupon. To edit a coupon, click the item in the table and the settings panel will open for editing.

## Customizing coupons[​](#customizing-coupons "Direct link to Customizing coupons")

You can create multiple coupons with different settings to cater to various marketing strategies and customer segments. The different settings include:

### Lifespan[​](#lifespan "Direct link to Lifespan")

When creating a coupon, set the period during which it will be active by selecting the start and (optionally) end dates in the **Effective date range** section.

For ongoing (forever, until deleted) coupons, leave the end date empty. You can also activate or deactivate the coupon using the toggle button.

### Discount Type[​](#discount-type "Direct link to Discount Type")

You can configure the type of discount the coupon will provide. There are two main categories:

#### Renewal cycle:[​](#renewal-cycle "Direct link to Renewal cycle:")

- **First payment only**: The coupon will apply only to the initial payment.
- **First payment and renewals**: The coupon will apply to the initial payment and all future renewals.

#### Value:[​](#value "Direct link to Value:")

- **Percentage**: The coupon will apply a percentage discount to the payment amount.
- **Fixed amount**: The coupon will apply a fixed monetary discount to the payment amount.

### Redemptions[​](#redemptions "Direct link to Redemptions")

You can limit the number of times a coupon can be redeemed. This is useful for creating exclusive offers or managing overall usage. Limits can be set per user or as a total number of redemptions across all users.

### Who Can Redeem the Coupon[​](#who-can-redeem-the-coupon "Direct link to Who Can Redeem the Coupon")

You can specify which group of users is eligible to redeem the coupon. This allows you to target specific customer segments with tailored discounts.

Coupons can be applied to:

- All users: Everyone can use the coupon.
- New customers only: Only users who have never made a purchase can use the coupon.
- Previous customers only: Only users who have made a purchase in the past can use the coupon.
- Current customers only: Only users with an active subscription can use the coupon.
- Current and previous customers only: Only users who have made a purchase in the past or have an active subscription can use the coupon.
- Migrated customers only: Only users who have been migrated from another platform and have not yet made a purchase through Freemius can use the coupon.

### Where to Apply the Coupon[​](#where-to-apply-the-coupon "Direct link to Where to Apply the Coupon")

You can choose to apply the coupon to specific plans/tiers and billing cycles. This allows you to create targeted discounts for particular offerings (e.g., monthly or yearly subscriptions or one-off purchases).

## Configuring Store-level Coupons[​](#configuring-store-level-coupons "Direct link to Configuring Store-level Coupons")

Store-level coupons require you to select the specific products within the store where the coupon will be applicable, or you can select all products.

You can configure the same options as for product-level coupons, including lifespan, discount type, redemptions, who can redeem the coupon, and where to apply it.

note

Go to the **Store** → **Coupons** page in the Freemius Developer Dashboard to create and manage store-level coupons.

## Creating Same Coupon with Discounts for Different Plans[​](#creating-same-coupon-with-discounts-for-different-plans "Direct link to Creating Same Coupon with Discounts for Different Plans")

Freemius allows you to create coupons with the same code but different settings. This is useful for running multiple promotions simultaneously or targeting different plan and pricing segments with tailored discounts.

For example, you might want to create two coupons with the same code that give:

- A 20% discount for the Professional plan.
- A 10% discount for other plans.

To do this, create two coupons with the same code but select different plans options for each under "Where to apply the coupon."

warning

This type of advanced coupon setup is only available for plans, licenses, and billing cycles. You cannot create different coupons for different types of users.

## Applying Coupons in the Checkout[​](#applying-coupons-in-the-checkout "Direct link to Applying Coupons in the Checkout")

Freemius Checkout provides multiple ways to apply coupons, enabling you to offer discounts for general promotional campaigns, [Special Coupons & Discounts](help-documentation-marketing-automation-special-coupons-discounts.md) as well as [Assigning Affiliate Coupons](help-documentation-affiliate-platform-affiliate-coupon.md) for your affiliate program.

For additional guidance on selecting the approach that best aligns with your marketing strategy and customer engagement objectives, refer to the [coupon usage guide](help-documentation-checkout-features-coupons.md).