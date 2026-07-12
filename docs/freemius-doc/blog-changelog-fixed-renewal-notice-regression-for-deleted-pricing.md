[Changelog](https://freemius.com/changelog/) / Fixed Renewal Notice Regression for Deleted Pricing

Our [Checkout](help-documentation-checkout.md) supports [license renewals](help-documentation-checkout-integration-generate-renewal-payment-method-update-link.md) even when the original pricing (quota) has been deleted. In such cases, the Checkout intelligently selects the closest pricing the license can be migrated to, based on its quota and activation count. When this happens, the Checkout also shows a notice to the buyer explaining the change.

[![License renewal with deleted pricing notice](https://freemius.com/blog/wp-content/uploads/2026/04/checkout-license-pricing-missing-notice-1024x556.png)](https://freemius.com/blog/wp-content/uploads/2026/04/checkout-license-pricing-missing-notice.png)

However, we identified a regression in this flow where the notice could appear in unintended cases, especially for licenses whose quota had been changed from the Developer Dashboard. We found the root cause and deployed a fix. In addition, we improved the UX of the notice so it is clearer for buyers.