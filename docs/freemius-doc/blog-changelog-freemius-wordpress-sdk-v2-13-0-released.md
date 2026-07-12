[Changelog](https://freemius.com/changelog/) / Freemius WordPress SDK v2.13.0 Released

We’ve just released version **2.13.0** of the Freemius WordPress SDK — packed with developer-focused enhancements and improvements to existing integrations. For the complete changelog and implementation details, check out the [GitHub release notes](https://github.com/Freemius/wordpress-sdk/releases/tag/2.13.0). Or read below for a quick summary of what’s new in this release.

### New License Lifecycle Hooks

Two new [hooks](help-documentation-wordpress-sdk-filters-actions-hooks.md) — `after_license_activation` and `after_license_deactivation` — are now available, allowing developers to respond to license status changes more efficiently. This makes it easier to sync external systems or trigger custom workflows when licenses are activated or deactivated.

### Gross Amounts in Payments

To make transaction details clearer for customers, payments in the Accounts page now display the **Gross amount** (including taxes) instead of the Net amount.

[![Payment table in the WordPress SDK](https://freemius.com/blog/wp-content/uploads/2025/11/payment-table-1024x376.png)](https://freemius.com/blog/wp-content/uploads/2025/11/payment-table.png)

### New Filter for Checkout Parameters

We’ve introduced a new filter, `checkout/parameters`, that lets you fine-tune the Checkout experience — such as forcing social proofing UI or billing cycle selectors. This is especially handy for custom pricing pages or dynamic checkout links.

For if you include the following code in your plugin

[![WP SDK checkout customization parameter](https://freemius.com/blog/wp-content/uploads/2025/11/checkout-param-snippet-wp-sdk-1024x494.png)](https://freemius.com/blog/wp-content/uploads/2025/11/checkout-param-snippet-wp-sdk.png)

The SDK will now render the Checkout with the proper UI like below:

[![Freemius Checkout with the customized params](https://freemius.com/blog/wp-content/uploads/2025/11/checkout-customized-1024x696.png)](https://freemius.com/blog/wp-content/uploads/2025/11/checkout-customized.png)

### Updated Pricing Page App

The SDK now includes the latest version **1.3.0** of our Pricing Page App, featuring a fix for annual discount calculations and enhanced security badges.

[![Freemius WP SDK pricing page](https://freemius.com/blog/wp-content/uploads/2025/11/pricing-page-751x1024.png)](https://freemius.com/blog/wp-content/uploads/2025/11/pricing-page.png)

### Improved InstaWP Compatibility

The SDK now fully supports the new **InstaWP staging environment**, automatically switching to safe mode when cloned, ensuring smoother workflows for testing and staging sites.