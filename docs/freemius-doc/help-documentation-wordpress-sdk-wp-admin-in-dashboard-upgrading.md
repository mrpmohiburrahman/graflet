---
title: "In-dashboard Upgrading in WP Admin"
url: "https://freemius.com/help/documentation/wordpress-sdk/wp-admin-in-dashboard-upgrading/"
source: "docs"
section: "Docs"
category: "WordPress SDK"
scraped_at: "2026-04-09T19:58:45+06:00"
word_count: 260
---

When you [integrate Freemius’ WordPress SDK](help-documentation-wordpress-integration-with-sdk.md) into your plugin or theme, the free version automatically includes a pricing table and a purchase button, enabling customers to purchase directly from their WP Admin dashboard. We call this *In-Dashboard Upgrading*.

The pricing and features on this table automatically sync with what you’ve configured in the **Plans** section of your Developer Dashboard, keeping everything up-to-date and consistent.

## Customizing the Pricing Table[​](#customizing-the-pricing-table "Direct link to Customizing the Pricing Table")

If you’d like to hide a plan from the WP Admin pricing table, you can do so by toggling the **Is Hidden** switch in the **Plans** section.

## Customizing the Pricing Page[​](#customizing-the-pricing-page "Direct link to Customizing the Pricing Page")

You can customize the appearance of the pricing table displayed in the WP Admin dashboard by modifying the CSS styles. This allows you to match the look and feel of your plugin or theme.

Alternatively, you can create a completely custom pricing page by following the steps outlined in our [Custom Pricing Page](https://github.com/Freemius/pricing-page#how-to-create-my-own-pricing-app-version) public repo.

## Customizing with Hooks[​](#customizing-with-hooks "Direct link to Customizing with Hooks")

The WordPress SDK provides several hooks that allow you to customize the pricing table and purchase process. You can use these hooks to modify the content, appearance, and behavior of the pricing table to better suit your needs.

- Show pricing besides [default monthly setting](help-documentation-wordpress-sdk-filters-actions-hooks.md#pricingshow_annual_in_monthly).
- Override the default Freemius WordPress SDK [pricing page url](help-documentation-wordpress-sdk-filters-actions-hooks.md#pricing_url)
- Controls the [visibility of the pricing link for the product](help-documentation-wordpress-sdk-filters-actions-hooks.md#is_pricing_page_visible)

More hooks and filters can be found under the [Filters & Actions Hooks](help-documentation-wordpress-sdk-filters-actions-hooks.md) section.