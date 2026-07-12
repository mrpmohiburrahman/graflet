[Changelog](https://freemius.com/changelog/) / Fixed Missing Payload in Checkout Redirection for Free Trials

We noticed a regression where, when the [Checkout](help-documentation-checkout.md) was used under [Free Trial mode](help-documentation-wordpress-free-trials.md), the redirected page did not receive all of the expected payloads — for example, the license ID created for the trial, its expiration date, and other related information.

[![Freemius Checkout in Free Trial Mode](https://freemius.com/blog/wp-content/uploads/2025/10/freemius-checkout-free-trial-1024x976.png)](https://freemius.com/blog/wp-content/uploads/2025/10/freemius-checkout-free-trial.png)

We have now deployed a fix for this issue. If you’re using the Checkout Redirection feature, you can now correctly access license information even for free trial flows. Please refer to our [documentation](https://freemius.com/help/documentation/checkout/hosted-checkout/#redirection-after-a-successful-purchase) to learn how to set up checkout redirection after a successful purchase.