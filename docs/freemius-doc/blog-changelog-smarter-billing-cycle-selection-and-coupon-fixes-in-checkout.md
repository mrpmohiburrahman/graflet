[Changelog](https://freemius.com/changelog/) / Smarter Billing Cycle Selection and Coupon Fixes in Checkout

This week we have updated the Checkout with the following improvements and bug fixes:

### Smarter Billing Cycle Selector UI

Our Checkout uses a set of [Upsell UI](help-documentation-checkout-features-upsell-toggles.md) components by default. One of them automatically shows up whenever there are billing-cycle-related discounts, such as annual-over-monthly pricing. The same UI is also used by your customers to toggle between billing cycles.

[![Checkout monthly switch UI](https://freemius.com/blog/wp-content/uploads/2026/02/checkout-monthly-switch-upsell-1024x493.png)](https://freemius.com/blog/wp-content/uploads/2026/02/checkout-monthly-switch-upsell.png)

However, when there are no such discounts, we recommend using the explicit [billing cycle selector UI](help-documentation-checkout-features-billing-cycle-selector-ui.md) by configuring it through the [Checkout Config](help-documentation-checkout-integration-freemius-checkout-buy-button.md). While this works as expected, we understand that this behavior can be a bit confusing for new makers joining the platform—especially those selling [SaaS & Apps](help-documentation-saas.md), where billing-cycle discounts are not very common. In such cases, makers testing the Checkout would see the annual plan auto-selected, without a clear way to switch to a monthly billing cycle.

To address this, we’ve made the Checkout smarter by automatically detecting these scenarios and switching to the billing cycle selector UI when appropriate.

[![Checkout Billing Cycle Selector UI](https://freemius.com/blog/wp-content/uploads/2026/02/checkout-billing-cycle-selector-ui-1024x593.png)](https://freemius.com/blog/wp-content/uploads/2026/02/checkout-billing-cycle-selector-ui.png)

Please note that in sandbox mode, a hint will also pop up to guide makers toward configuring discounts if they prefer to use the upsell UI instead. All other behaviors remain unchanged. For example, if you explicitly load the Checkout with an [annual billing cycle](help-documentation-checkout-integration-freemius-checkout-buy-button.md#billing_cycle), the option to switch to monthly will not be shown, preventing buyers from changing the intended configuration.

### Fixed Non-USD Flat Discount Coupon

We identified a recent regression where applying a [non-USD flat discount coupon](help-documentation-selling-with-freemius-coupon-discount.md#discount-type) did not work correctly in certain edge cases, particularly in some PayPal flows.

[![Checkout Coupon UI](https://freemius.com/blog/wp-content/uploads/2026/02/checkout-coupon-ui-1024x473.png)](https://freemius.com/blog/wp-content/uploads/2026/02/checkout-coupon-ui.png)

This issue has been identified and fixed.