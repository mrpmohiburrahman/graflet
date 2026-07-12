[Changelog](https://freemius.com/changelog/) / Checkout UI/UX Improvements

This week, we’re rolling out some minor UI/UX improvements to our Checkout.

### Smarter License Selector for SaaS & Apps

By default, our Checkout shows the license selector UI so that your buyers can easily choose the license/quota they want.

[![Freemius Checkout showing the license selector UI in the header](https://freemius.com/blog/wp-content/uploads/2025/04/freemius-checkout-license-selector-ui-1024x702.png)](https://freemius.com/blog/wp-content/uploads/2025/04/freemius-checkout-license-selector-ui.png)

Previously, this UI would appear even when there was only one license quota available for the plan. While this made sense for WordPress products, it’s unnecessary for SaaS and Apps.

Starting today, the license selector UI will only be shown if your plan has more than one license quota available.

[![Freemius Checkout without the license selector UI in the header](https://freemius.com/blog/wp-content/uploads/2025/04/freemius-checkout-no-license-selector-ui-1024x657.png)](https://freemius.com/blog/wp-content/uploads/2025/04/freemius-checkout-no-license-selector-ui.png)

Note: You can still use the `hide_licenses` option to hide the selector for other product types or even when your plan has multiple license options.

### Updated Loading Spinner

Since the release of our new Checkout JS SDK, we’ve supported custom spinners that appear while the Checkout loads.

[![The updated spinner for the Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2025/04/checkout-spinner-1024x720.png)](https://freemius.com/blog/wp-content/uploads/2025/04/checkout-spinner.png)

However, we realized that the default spinner hadn’t been rebranded. That’s now fixed. Starting this week, once a buyer clicks the buy button on your website/app, the updated spinner shown above will appear.