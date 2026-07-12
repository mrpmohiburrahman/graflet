[Changelog](https://freemius.com/changelog/) / Enhanced Checkout Accessibility, Billing Selector Logic, and iDEAL Flow Fixes

This week we are releasing a few UI/UX improvements to the Checkout, aimed at enhancing accessibility and fixing a bug related to the newly introduced iDEAL flow.

### Improved Accessibility of Dropdowns

We’ve enhanced the [license](help-documentation-getting-started-setup-product-pricing-plans-refunds.md) and [billing cycle selector](blog-changelog-new-feature-billing-selector-ui-for-checkout.md) dropdowns to be fully accessible for keyboard users. The dropdowns now behave just like native elements — users can tab into them, navigate using arrow keys, and select using space or enter. The Escape key also closes the dropdown.

This marks an important step in our ongoing push toward improved accessibility, aligning with — and aiming to exceed — the new standards set by the EU Accessibility Act.

### Improved Behavior of Monthly Billing Cycle Selector

Our Checkout offers two UI approaches for the billing cycle:

**Upsells** – the recommended and default way to show billing cycle options as toggleable upsells:

[![Freemius Checkout Upsells with togglable switch](https://freemius.com/blog/wp-content/uploads/2025/05/checkout-upsell-ui-monthly-switch-1024x437.png)](https://freemius.com/blog/wp-content/uploads/2025/05/checkout-upsell-ui-monthly-switch.png)

[**Billing Cycle Selector UI**](blog-changelog-new-feature-billing-selector-ui-for-checkout.md) – a dedicated UI for billing cycle selection:

[![Freemius Checkout billing cycle selector UI](https://freemius.com/blog/wp-content/uploads/2025/05/freemius-checkout-billing-cycle-dropdown-ui-1024x801.png)](https://freemius.com/blog/wp-content/uploads/2025/05/freemius-checkout-billing-cycle-dropdown-ui.png)

Previously, both interfaces would only display the monthly billing cycle if:

- The `show_monthly_switch` flag was explicitly set, or
- The Checkout was loaded with the monthly billing cycle.

Following feedback from our makers, we’ve updated this behavior. Now, the monthly billing cycle will show by default if no billing cycle is explicitly passed when loading the Checkout.

To streamline configuration, we’ve introduced a new `show_monthly` flag for use with the [Checkout JS SDK](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md) and [Hosted Checkout](help-documentation-selling-with-freemius-hosted-checkout.md). The older, more verbose `show_monthly_switch` parameter is now deprecated. With the updated billing cycle UI, the `_switch` suffix no longer aligns with the current design.

### Fixed VAT Number Validation Issue with iDEAL Checkout Flow

We recently introduced the new [iDEAL payment](blog-changelog-new-payment-method-in-freemius-checkout-ideal-for-netherlands.md) flow in our Hosted Checkout:

[![Freemius Checkout VAT Number UI with iDEAL payment method](https://freemius.com/blog/wp-content/uploads/2025/05/checkout-ideal-flow-vat-number-1024x610.png)](https://freemius.com/blog/wp-content/uploads/2025/05/checkout-ideal-flow-vat-number.png)

This week, we fixed an edge case where the VAT number would occasionally be lost after the redirect step in the iDEAL flow. This issue did not impact any completed transactions — we had already patched the affected cases retroactively.