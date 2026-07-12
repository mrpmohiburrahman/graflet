[Changelog](https://freemius.com/changelog/) / Various improvements to our Checkout

We’re excited to share the latest UI/UX improvements we’ve made to our Checkout application! At Freemius, we deeply value conversion optimization—because your success is our success. Here’s a look at what’s new.

### Mobile UI/UX improvements

[![](https://freemius.com/blog/wp-content/uploads/2025/01/checkout-mobile-label-fix-1024x377.png)](https://freemius.com/blog/wp-content/uploads/2025/01/checkout-mobile-label-fix.png)

We’ve resolved form label alignment issues on mobile and small-screen devices for certain languages. Long labels are now truncated instead of overflowing or wrapping to the next line, with a tooltip added to display the full text. This update ensures the billing form maintains a clean and consistent visual hierarchy.

[![](https://freemius.com/blog/wp-content/uploads/2025/01/checkout-language-selector.png)](https://freemius.com/blog/wp-content/uploads/2025/01/checkout-language-selector.png)

We also identified a glitch in the [language selector UI](blog-changelog-enhanced-language-support-and-ui-updates-for-freemius-checkout-translation.md) on mobile devices where the flag failed to render, displaying a placeholder text like ‘flag-us’ instead. To simplify the user experience, we’ve opted to remove the flag on mobile and display only the language label. On desktop devices the UI still renders with flags as before.

[![](https://freemius.com/blog/wp-content/uploads/2025/01/checkout-upsell-component-1024x603.png)](https://freemius.com/blog/wp-content/uploads/2025/01/checkout-upsell-component.png)

Lastly, we addressed a visual glitch in the [upsell component](blog-new-freemius-checkout-drive-conversions-increase-sales-price.md#introducing_the_dual_column_checkout_beta). The switch was not rendering correctly, either appearing shrunken or overflowing onto two lines. This issue has now been resolved.

### Improved asset loading

We noticed that the Checkout was incorrectly making network calls for certain assets, resulting in 404 errors and increased loading times. We’ve identified the root cause and resolved the issue.

[![](https://freemius.com/blog/wp-content/uploads/2025/01/checkout-freemius-logo-update-1024x663.png)](https://freemius.com/blog/wp-content/uploads/2025/01/checkout-freemius-logo-update.png)

We’ve also updated the Freemius logo to align with our recent [rebranding](blog-changelog-a-fresh-new-design-for-the-developer-dashboard-with-performance-improvements.md).

### Improved Credit card 3DS flow

[![](https://freemius.com/blog/wp-content/uploads/2025/01/checkout-3ds-error-handling-1024x413.png)](https://freemius.com/blog/wp-content/uploads/2025/01/checkout-3ds-error-handling.png)

We’ve improved error detection for credit card payments when the issuer requires 2FA authentication. Our Checkout now handles edge-case errors more effectively, ensuring a smoother experience for buyers in these scenarios.

### Fixed discount for lifetime trials

[![](https://freemius.com/blog/wp-content/uploads/2025/01/checkout-coupon-discount-with-lifetime-trial-1024x769.png)](https://freemius.com/blog/wp-content/uploads/2025/01/checkout-coupon-discount-with-lifetime-trial.png)

We identified an edge case where coupon discounts were not properly applied to [lifetime](blog-lifetime-license-for-wordpress-plugins-the-right-way.md) [trials](help-documentation-selling-with-freemius-free-trials.md). The root cause has been resolved, and a fix has been deployed.

### Fixed issue with the coupon UI

[![](https://freemius.com/blog/wp-content/uploads/2025/01/checkout-coupon-ui-migrated-license.gif)](https://freemius.com/blog/wp-content/uploads/2025/01/checkout-coupon-ui-migrated-license.gif)

We also discovered an edge case where the coupon UI wasn’t updating correctly after entering a license, particularly during renewals of migrated licenses. This issue occurred when the [pro-rated discount](help-documentation-selling-with-freemius-proration.md) and the product’s [renewal discount](https://freemius.com/help/faqs/#can_i_offer_a_discount_on_license_renewals) exceeded the coupon value. Given the various configurations a coupon can have during a license renewal or update, we’ve carefully addressed the root cause and deployed a fix.