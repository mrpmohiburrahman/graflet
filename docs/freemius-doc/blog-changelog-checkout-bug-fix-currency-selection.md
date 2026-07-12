[Changelog](https://freemius.com/changelog/) / Checkout Bug Fix: Currency Selection

We identified an issue where the requested currency was not being honored during Checkout if the `plan_id` parameter was missing.

Historically, we recommend including the `plan_id` parameter when using our [Checkout](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md#arguments). When it is not provided, the system defaults to loading the cheapest visible plan.

However, in such cases, the currency parameter was not being applied correctly, even when specified.

[![](https://freemius.com/blog/wp-content/uploads/2024/12/freemius-checkout-currency-1024x774.png)](https://freemius.com/blog/wp-content/uploads/2024/12/freemius-checkout-currency.png)

This issue has now been resolved, and the requested currency will be respected as intended.