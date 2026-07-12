[Changelog](https://freemius.com/changelog/) / Smarter SaaS-Friendly Discount Calculation, Renewals UI, and Other Checkout Improvements

This week we’re rolling out several SaaS-friendly improvements to our Checkout.

### Smarter Discount Calculation

Previously, our discount calculation was limited to 2 or 3 decimal places — sufficient for the WordPress ecosystem but limiting for SaaS products where pricing often involves high precision (e.g., [bulk credit purchases](help-documentation-selling-with-freemius-customize-license-unit-label.md) where each unit costs less than `0.0001`).

[![Freemius Checkout smarter unit price calculation showing 0.0001 unit price](https://freemius.com/blog/wp-content/uploads/2025/05/freemius-checkout-unit-price-calculation-1024x550.png)](https://freemius.com/blog/wp-content/uploads/2025/05/freemius-checkout-unit-price-calculation.png)

Our Checkout is now smart enough to detect such cases and display the correct level of precision. Additionally, large numbers in the license unit section are now formatted for better readability.

### Improved Line Item to Show Renewal Price

Based on feedback from our maker community, we’ve added more clarity to the renewal pricing. Specifically, when there’s a discount involved (e.g., annual or volume-based discounts), the Checkout will now display a “**Renews**” line item just after “**Today’s total**”.

[![Renewals price UI in Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2025/05/freemius-renewal-price-line-item-1024x735.png)](https://freemius.com/blog/wp-content/uploads/2025/05/freemius-renewal-price-line-item.png)

You can also force this line item to always appear — even when there’s no discount — by enabling the `always_show_renewals_amount` [configuration](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md#arguments).

### Responsiveness Improvements in Hosted Checkout

We’ve made layout improvements to enhance the responsiveness of the [Hosted Checkout](help-documentation-selling-with-freemius-hosted-checkout.md).

[![Freemius Hosted Checkout](https://freemius.com/blog/wp-content/uploads/2025/05/freemius-hosted-checkout-responsiveness-1024x717.png)](https://freemius.com/blog/wp-content/uploads/2025/05/freemius-hosted-checkout-responsiveness.png)

The Checkout now adjusts more gracefully to both vertical and horizontal screen sizes, offering a smoother and more optimized buying experience across devices.