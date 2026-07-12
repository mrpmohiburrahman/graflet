[Changelog](https://freemius.com/changelog/) / Fix for Payment Method Recovery Flow in Checkout JS SDK 1.4.1

This week we are releasing version **1.4.1** of the [Checkout JS SDK](https://github.com/Freemius/freemius-checkout-js).

This update addresses an issue in the [automatic dunning recovery flow](help-documentation-marketing-automation-dunning-failed-payments.md#customizing-payment-method-update-links), where in certain cases the library failed to correctly restore the payment-method update experience.

Since this flow is critical for recovering failed subscriptions, we prioritized fixing it to keep the recovery process as seamless as possible for both you and your customers.

[![Demo payment recovery flow in Freemius](https://freemius.com/blog/wp-content/uploads/2025/11/payment-recovery-flow-1006x1024.png)](https://freemius.com/blog/wp-content/uploads/2025/11/payment-recovery-flow.png)

If you’re using the [CDN version](https://freemius.com/help/documentation/checkout/freemius-checkout-buy-button/), nothing needs to be changed on your end. For NPM package users, please update with the following command:

```
npm install @freemius/checkout@latest
```