[Changelog](https://freemius.com/changelog/) / Freemius Checkout Improvements with a New Version of the JS SDK

This week, we’re rolling out a few minor improvements to **Freemius Checkout**.

### New Version of the JS SDK

Version **1.1.1** of the [Checkout JS SDK](https://github.com/Freemius/freemius-checkout-js/releases/tag/1.1.1) is now available!

[![Freemius Checkout JS SDK Developer Experience Improvement with improved types](https://freemius.com/blog/wp-content/uploads/2025/03/checkout-js-sdk-dx-improvements-1024x571.png)](https://freemius.com/blog/wp-content/uploads/2025/03/checkout-js-sdk-dx-improvements.png)

This release focuses exclusively on documentation and developer experience improvements. The Checkout JS SDK is used to embed the Checkout inside your website. Please read our [documentation](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md) to get started.

### Improved Coupon Error Handling

We noticed that in some edge cases, our Checkout could silently reject a coupon, which might cause confusion for buyers.

[![Freemius Checkout improved coupon error handling](https://freemius.com/blog/wp-content/uploads/2025/03/checkout-error-coupon-1024x501.png)](https://freemius.com/blog/wp-content/uploads/2025/03/checkout-error-coupon.png)

We’ve implemented a fix to ensure that if a coupon cannot be applied, an error message is now clearly visible in the UI. Additionally, we’ve improved the UX to make it clear that buyers can simply press a button to continue the purchase without the coupon.

### Clearer Error Messages for Checkout Setup

Previously, when passing incorrect configuration parameters (such as an invalid Product ID or Plan ID), Checkout would fail and display only a single-line error message.

[![Freemius Checkout Loading Error UI](https://freemius.com/blog/wp-content/uploads/2025/03/checkout-error-ui-improvement-1024x529.png)](https://freemius.com/blog/wp-content/uploads/2025/03/checkout-error-ui-improvement.png)

We’ve made some UI improvements to enhance the experience:

1. If Checkout is loaded in sandbox mode, it will now display a clearer message to assist makers in setting it up correctly.
2. If Checkout is loaded via the JS SDK, a close button will now appear, allowing users to return to the website easily.