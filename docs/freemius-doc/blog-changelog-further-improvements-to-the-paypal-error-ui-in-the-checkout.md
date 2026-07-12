[Changelog](https://freemius.com/changelog/) / Further improvements to the PayPal error UI in the checkout

Continuing our work from the [last deployment](blog-changelog-improved-paypal-subscription-failure-messages-in-the-checkout.md), we’ve further improved some of the error UI shown in the checkout for PayPal, especially when the checkout is loaded from the SDK.

### General PayPal error UI

[![Freemius checkout error UI with general PayPal issue](https://freemius.com/blog/wp-content/uploads/2024/06/paypal-general-error-ui-1024x628.png)](https://freemius.com/blog/wp-content/uploads/2024/06/paypal-general-error-ui.png)

For every other PayPal-related error, we are now including a “retry link” in the message, so that the user can quickly retry without manually refreshing the page.

### When the initial payment fails

[![Freemius Checkout - PayPal initial payment issue](https://freemius.com/blog/wp-content/uploads/2024/06/paypal-initial-payment-fail-error-1024x551.png)](https://freemius.com/blog/wp-content/uploads/2024/06/paypal-initial-payment-fail-error.png)

This can happen for a PayPal account with insufficient balance or credit source. Apart from the inline link in the error UI, the primary button will also reload the checkout so the user can retry with a different PayPal account or a card.

### When the billing agreement was already created

[![Freemius Checkout - PayPal billing agreement issue](https://freemius.com/blog/wp-content/uploads/2024/06/paypal-billing-agreement-error-1024x555.png)](https://freemius.com/blog/wp-content/uploads/2024/06/paypal-billing-agreement-error.png)

In some rare edge cases, it can happen that the billing agreement was already created in PayPal, yet it failed to process the payment. Since we know retrying with the same PayPal billing agreement would not work, we now show a clear message, and the buttons would reload the checkout so that the user can try again with a different payment method.

Please note that these improvements were rolled out to the [beta or the `phase2` version of the checkout](blog-changelog-beta-release-dual-column-checkout-with-upsells-and-social-proofing.md). The behavior of the current checkout has not changed from the last deployment, apart from the improved error messages.