[Changelog](https://freemius.com/changelog/) / New Checkout Events for Tracking Coupon Interactions

Our Freemius Checkout supports tracking several events across the buyer journey — from when the checkout is loaded, to when billing information is entered, or when a plan is changed.

Today, we’re rolling out a few new events focused on tracking interactions with [coupons](help-documentation-selling-with-freemius-coupon-discount.md).

[![Freemius Checkout coupon code](https://freemius.com/blog/wp-content/uploads/2026/02/freemius-checkout-coupon-code-1024x452.png)](https://freemius.com/blog/wp-content/uploads/2026/02/freemius-checkout-coupon-code.png)

- `coupon-added`: Triggered when a new coupon is applied through the checkout UI.
- `coupon-removed`: Triggered when a coupon is removed, either explicitly from the UI or when the coupon is [no longer valid](help-documentation-selling-with-freemius-coupon-discount.md#creating-same-coupon-with-discounts-for-different-plans) for the selected quota/licenses or billing cycle.
- `coupon-updated`: Triggered when a coupon’s discount value changes due to an update in quota/licenses or billing cycle.

These events make it easier to understand how buyers interact with coupons during checkout and which discounts are ultimately applied based on the selected configuration.

[![Sample tracking of coupon events](https://freemius.com/blog/wp-content/uploads/2026/02/checkout-coupon-tracking-1024x554.png)](https://freemius.com/blog/wp-content/uploads/2026/02/checkout-coupon-tracking.png)

You can read more about this in our [documentation](help-documentation-checkout-features-tracking-analytics.md#advanced-event-tracking).