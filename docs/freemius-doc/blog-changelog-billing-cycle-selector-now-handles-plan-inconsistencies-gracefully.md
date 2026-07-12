[Changelog](https://freemius.com/changelog/) / Billing Cycle Selector Now Handles Plan Inconsistencies Gracefully

We discovered a bug in the newly introduced [billing cycle selector UI](blog-changelog-new-feature-billing-selector-ui-for-checkout.md) of our Checkout. In cases where a plan’s pricing options had inconsistent billing cycles, the selector could still render an invalid option.

[![Freemius Checkout Billing Cycle Selector UI](https://freemius.com/blog/wp-content/uploads/2025/07/freemius-checkout-billing-cycle-selector-ui-1024x613.png)](https://freemius.com/blog/wp-content/uploads/2025/07/freemius-checkout-billing-cycle-selector-ui.png)

While this was an edge case, we prioritized the fix. The UI will now behave correctly regardless of how your plans are configured.

**Reminder**: The billing cycle selector is **not** shown by default. To enable it, you must opt in by adding the [`billing_cycle_selector`](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md#billing_cycle_selector) option in your Checkout config.

We recommend using the billing cycle selector UI *only if you don’t have a pricing page* where buyers can pre-select their billing cycles. By default, [Freemius’ upsell UI](blog-changelog-beta-release-dual-column-checkout-with-upsells-and-social-proofing.md#various_upsells) is optimized for conversion and offers the best purchase flow.