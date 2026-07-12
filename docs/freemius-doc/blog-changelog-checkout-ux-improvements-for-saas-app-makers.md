[Changelog](https://freemius.com/changelog/) / Checkout UX Improvements for SaaS & App Makers

This week we are rolling out some small but important enhancements to our [Checkout](help-documentation-checkout.md), aimed at delivering a better experience to your buyers, especially for SaaS and App makers.

### Better Title for Plan Update

Our Checkout previously showed the title “License Update” when buyers tried to [upgrade or downgrade their subscription](help-documentation-checkout-integration-generate-renewal-payment-method-update-link.md). While this makes sense for WordPress products, we understood that for SaaS & App products it could be confusing. To make the flow more intuitive, we now identify such cases and display the title “Plan update” instead.

[![Checkout showing plan update](https://freemius.com/blog/wp-content/uploads/2026/02/checkout-showing-plan-update-1024x762.png)](https://freemius.com/blog/wp-content/uploads/2026/02/checkout-showing-plan-update.png)

Similarly, for manual renewals the Checkout will now display “Subscription renewal” instead of “License renewal”, aligning the terminology with how SaaS and App makers typically position their offerings.

[![Manual subscription renewal through Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2026/02/checkout-showing-subscription-renewal-1024x517.png)](https://freemius.com/blog/wp-content/uploads/2026/02/checkout-showing-subscription-renewal.png)

### Back Button Hides Automatically

To further streamline the Checkout experience, when buyers reach the Review step (and about to pay), the [back button](help-documentation-checkout-integration-hosted-checkout.md#configuring-the-back-button) will no longer be shown.

[![Freemius Checkout in Review state](https://freemius.com/blog/wp-content/uploads/2026/02/checkout-review-state-1024x785.png)](https://freemius.com/blog/wp-content/uploads/2026/02/checkout-review-state.png)

This reduces confusion where two left arrows were previously visible on the left side of the screen—one to return to the billing form and another to navigate back to the product’s website.

### Better Fallback for the Billing Cycle Selector

Recently, we [published an update](blog-changelog-smarter-billing-cycle-selection-and-coupon-fixes-in-checkout.md#smarter_billing_cycle_selector_ui) where our Checkout automatically detects if there is no annual discount and, in such cases, falls back to displaying the [billing cycle selector](help-documentation-checkout-features-billing-cycle-selector-ui.md) instead of the upsell UI. At that time, the billing cycle selector defaulted to `responsive_list` mode.

[![Checkout billing cycle selector](https://freemius.com/blog/wp-content/uploads/2026/02/checkout-billing-selector-dropdown-1024x838.png)](https://freemius.com/blog/wp-content/uploads/2026/02/checkout-billing-selector-dropdown.png)

After reviewing feedback from makers with all three billing cycles configured, we are now defaulting the selector to `dropdown` mode, as it consumes less vertical space and keeps the layout more compact.

### Cleaner Purchase Email for Licenses

We received feedback that the information shown in [purchase emails](help-documentation-marketing-automation-transactional-emails.md) about [multi-unit licenses](help-documentation-saas-customize-license-unit-label.md) could be confusing for buyers. For example, if someone purchased a 5-Device license, the email previously displayed this as “Activations: 0 out of 5 devices”. This terminology is not always familiar outside the WordPress ecosystem. Additionally, in many SaaS and App scenarios, license usage is managed directly by the product, so Freemius may not have visibility into actual usage.

[![License information in Freemius Transactional Emails](https://freemius.com/blog/wp-content/uploads/2026/02/license-information-purchase-email-1024x527.png)](https://freemius.com/blog/wp-content/uploads/2026/02/license-information-purchase-email.png)

To make this clearer and more universally applicable, the email will now display a simplified label such as “License Type: 5 devices”, which better aligns with different product types and usage models.