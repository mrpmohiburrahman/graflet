[Changelog](https://freemius.com/changelog/) / Checkout Improvements: GDPR Opt-In Control, Localization, and UX Fixes

This week we’re rolling out several improvements and bug fixes to our Checkout. Here’s what’s new.

### New Feature to Control Marketing Opt-In UI

Freemius Checkout has several built-in features to make it fully compliant with GDPR and other privacy-related regulations, while providing the best possible UX for your buyers. One such feature is the Marketing Opt-In UI.

[![Freemius Checkout Marketing Opt-In UI](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-checkout-marketing-opt-in-ui-1024x513.png)](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-checkout-marketing-opt-in-ui.png)

Until now, the UI would show up where relevant per regulation, and buyers had to explicitly choose whether they wanted to opt in to marketing or not. There wasn’t a way to configure this behavior.

We’ve now introduced a new configuration parameter, `gdpr`, to better customize this flow based on your own preferences.

- `default` – This is the current default behavior, where the UI will show up if the buyer has not previously opted in the past.
- `opt_out` – Use this to have the UI pre-select the “No” option by default, saving a click before purchase at the expense of fewer marketing opt-ins.
- `hidden` – Completely hides the UI from the Checkout. Use this if you don’t want Freemius to manage the opt-in consent and already have your own system in place.

You can read more about it in our [documentation](https://freemius.com/help/documentation/checkout/gdpr/#marketing-consent-ui).

### All Dates in the Checkout Are Now Localized

Freemius Checkout supports [various languages](https://freemius.com/help/documentation/checkout/freemius-checkout-buy-button/#language%20%7C%20locale) out of the box.

[![Freemius Checkout localized date](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-checkout-date-localized-1024x463.png)](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-checkout-date-localized.png)

We’ve now extended this capability to also translate and localize the dynamic dates shown in the UI based on the selected language.

### Coupon UI Now Has Better Resilience Against Errors

We noticed a UI glitch in the Checkout when a [coupon](help-documentation-selling-with-freemius-coupon-discount.md) could not be validated due to network or similar transient issues.

[![Coupon Error UI in the Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-checkout-coupon-error-ui-1024x734.png)](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-checkout-coupon-error-ui.png)

We identified the root cause and made the UI and UX more resilient to such errors, helping keep the checkout experience as smooth as possible.

### Better License Upgrade Flow

Last week, we saw a regression in the [license upgrade flow](https://freemius.com/help/documentation/checkout/freemius-checkout-buy-button/#license_key) where the flow was broken in some cases. We identified and hot-fixed it immediately.

[![Number of Sites in license upgrade flow in Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-checkout-license-quota-1024x832.png)](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-checkout-license-quota.png)

As a follow-up, we also addressed additional edge cases, such as licenses that were manually upgraded to a higher quota by the maker. The Checkout will now always select the correct minimum pricing or quota when upgrading a license, whether the upgrade is within the same plan or across different plans.

### Fix in the Review Avatar

Freemius Checkout can show [reviews as a social proofing interface](https://freemius.com/help/documentation/checkout/social-proofing-ui/#displaying-reviews-or-testimonials) to help boost your sales.

[![Freemius Checkout Review UI avatar fix](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-checkout-review-ui-1024x558.png)](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-checkout-review-ui.png)

We noticed a small UI bug where the fallback avatar was not being generated correctly in some cases. We’ve deployed a fix to ensure avatars are now rendered consistently across all scenarios.