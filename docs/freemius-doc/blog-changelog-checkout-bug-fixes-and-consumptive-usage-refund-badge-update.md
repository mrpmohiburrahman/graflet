[Changelog](https://freemius.com/changelog/) / Checkout Bug Fixes and Consumptive Usage Refund Badge Update

We have released the following bug fixes and minor improvements to our Checkout and related systems.

## Upsell UI Bug Fix

Freemius Checkout supports strategically placed [upsell interfaces](help-documentation-checkout-features-upsell-toggles.md) to help boost your conversion rate. For example, right before the CTA, we show two upsells to buy an unlimited or lifetime license.

[![Checkout upsell UI before the CTA](https://freemius.com/blog/wp-content/uploads/2026/06/freemius-checkout-upsell-ui-bug-fix-1024x704.png)](https://freemius.com/blog/wp-content/uploads/2026/06/freemius-checkout-upsell-ui-bug-fix.png)

It came to our attention that, in some cases, the upsell UI could disappear when changing the buyer country. We identified the root cause and deployed a fix.

## Updated Refund Badge for Consumptive Usage

We recently introduced the concept of [consumptive usage](help-documentation-selling-with-freemius-refund-policy.md#consumptive-usage). When enabled, Freemius updates the generated refund policy to clarify that any consumed credits will not be refunded.

[![Consumptive usage refund policy configuration](https://freemius.com/blog/wp-content/uploads/2026/06/consumptive-usage-flag-1024x752.png)](https://freemius.com/blog/wp-content/uploads/2026/06/consumptive-usage-flag.png)

With today’s deployment, we are bringing this information to the [money-back guarantee badge](help-documentation-checkout-features-social-proofing-ui.md#displaying-the-money-back-guarantee) in the Checkout as well.

[![Checkout money-back guarantee badge mentioning consumed credits](https://freemius.com/blog/wp-content/uploads/2026/06/checkout-consumptive-usage-disclaimer-1024x509.png)](https://freemius.com/blog/wp-content/uploads/2026/06/checkout-consumptive-usage-disclaimer.png)

## Fixed Duplicate Payment Failed Emails

The Freemius [dunning mechanism](help-documentation-marketing-automation-dunning-failed-payments.md) kicks in when there is an issue collecting payments from active subscriptions, helping recover revenue from potentially lost customers. We noticed that, in some extremely rare edge cases, our system could accidentally send multiple emails to the same customer on the same day.

[![Payment failed email preview](https://freemius.com/blog/wp-content/uploads/2026/06/failed-payment-email-dunning-991x1024.png)](https://freemius.com/blog/wp-content/uploads/2026/06/failed-payment-email-dunning.png)

We were able to identify the root cause and have deployed a fix.