---
title: "Showing Annual, Lifetime, and Unlimited Upsell Toggles in the Checkout"
url: "https://freemius.com/help/documentation/checkout/features/upsell-toggles/"
source: "docs"
section: "Docs"
category: "Checkout"
scraped_at: "2026-04-09T19:58:37+06:00"
word_count: 282
---

Based on the [automatic discounts](help-documentation-checkout-features-automatic-discounts-in-checkout.md), the Freemius Checkout automatically displays relevant upsells to customers.

These upsells are strategically positioned to gently nudge customers to upgrade to a higher plan, helping maximize conversion.

tip

If you want a dedicated UI for changing the billing cycle, use the [Billing Cycle Selector UI](help-documentation-checkout-features-billing-cycle-selector-ui.md).

## Annual Upsell[​](#annual-upsell "Direct link to Annual Upsell")

The annual upsell is displayed when a customer selects a monthly billing cycle and an annual billing cycle is available that offers a discount compared to the monthly plan.

Read about setting up [annual discounts](help-documentation-checkout-features-automatic-discounts-in-checkout.md#annual-discount).

The upsell is shown unless you specifically load the Checkout with a `lifetime` billing cycle.

If your pricing does not have any discount for the annual price, then the Checkout will not show the upsell toggle. In such cases, the Checkout will fallback to showing the [billing cycle selector](help-documentation-checkout-features-billing-cycle-selector-ui.md#rendering-a-dropdown-ui) in `dropdown` mode. This is intentional so that your buyers can still change the billing cycle from the Checkout interface.

You can also control this behavior using the [`show_monthly`](help-documentation-checkout-integration-freemius-checkout-buy-button.md#show_monthly) setting.

## One-off or Lifetime Upsell[​](#one-off-or-lifetime-upsell "Direct link to One-off or Lifetime Upsell")

This upsell requires lifetime pricing to be configured for your product. The toggle is shown only when the lifetime billing cycle price is higher than the current billing cycle price.

## Unlimited Upsell[​](#unlimited-upsell "Direct link to Unlimited Upsell")

The Unlimited Unit upsell is shown only when the unlimited unit price exceeds the price of the currently selected unit.

## How to Disable Upsells[​](#how-to-disable-upsells "Direct link to How to Disable Upsells")

To disable all upsells, use the [`show_upsells`](help-documentation-checkout-integration-freemius-checkout-buy-button.md#show_upsells) setting. This global setting applies to both unlimited and lifetime upsells.

To disable the annual upsell only, use the [`annual_discount`](help-documentation-checkout-integration-freemius-checkout-buy-button.md#annual_discount) setting.