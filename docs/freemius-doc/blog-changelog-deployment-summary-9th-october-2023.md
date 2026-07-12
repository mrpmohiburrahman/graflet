[Changelog](https://freemius.com/changelog/) / Deployment summary 9th October, 2023

### Backend Fixes

- We found an edge-case scenario where a product’s payment could not be refunded. We have found the issue and have pushed a fix.
- We noticed a regression in our last [major update](blog-changelog-improvements-to-the-analytics-date-selection-logic-and-ui-additional-fixes.md) on the analytics system. The `MRR` and `Active Subscription` metrics were incorrect, including sandbox subscriptions. We have pushed a fix for this.
- We noticed and fixed a small typo on the EULA page of Freemius products.

### Developer Dashboard Enhancements

#### Coupons Settings UI Enhancement

We have deployed a bunch of enhancements to the coupon settings UI.

[![Freemius Coupons Settings UI](https://freemius.com/blog/wp-content/uploads/2023/10/freemius-coupons-settings-ui.jpg)](https://freemius.com/blog/wp-content/uploads/2023/10/freemius-coupons-settings-ui.jpg)

1. The coupon code will now always be visible inside the sticky header.
2. The `Is Active` toggle is also now a part of the sticky header, located beside the close button.
3. We have also fixed some layout issues along the way.

#### PayPal account types

We have renamed the PayPal account types in the “Payouts” section of the profile page to better reflect their meaning.

[![Freemius Payouts Settings](https://freemius.com/blog/wp-content/uploads/2023/10/freemius-payouts-paypal-account-type.jpg)](https://freemius.com/blog/wp-content/uploads/2023/10/freemius-payouts-paypal-account-type.jpg)

You will now get a clear indication to understand what the different types of accounts mean.