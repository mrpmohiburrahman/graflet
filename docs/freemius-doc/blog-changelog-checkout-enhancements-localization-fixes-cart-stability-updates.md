[Changelog](https://freemius.com/changelog/) / Checkout Enhancements: Localization Fixes & Cart Stability Updates

This week we are bringing some small enhancements to our Checkout.

### Fixed Coupon Discount Label Bug

We noticed an issue in the coupon discount label where absolute-value coupons would sometimes display an incorrect amount when the selected currency wasn’t USD. Since many of our makers operate in multiple currencies, this inconsistency created confusion during checkout.

In addition, the label wasn’t properly applying translation and number localization, which made the UI feel inconsistent for non-English locales.

[![Freemius Coupon Discount](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-checkout-coupon-discount-1024x398.png)](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-checkout-coupon-discount.png)

With today’s deployment, both issues have been fixed so that currency handling and localized formatting work as expected.

### Fixed Race Condition Bug in the Cart UI

In some rare cases, a race condition between parallel API calls caused the cart functionality to break—either failing to save or unintentionally disabling the cart when users interacted with the toggle.

[![Freemius Checkout cart toggle button](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-cart-toggle-button-checkout-1024x431.png)](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-cart-toggle-button-checkout.png)

We’ve resolved this race condition to ensure the cart state always updates reliably.