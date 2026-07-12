[Changelog](https://freemius.com/changelog/) / Fix for License Expiration Not Updating After Initial PayPal Payment

A bug was reported where, for some customers, the [license](help-documentation-saas-integrating-license-key-activation.md) was not being extended correctly after receiving the first [subscription](subscriptions.md) payment through PayPal.

This was caused by a rare edge case: customers could cancel their subscription during the window between subscription creation and the first payment being charged. With PayPal, this window can last up to 48 hours, making the issue more likely to surface for a small subset of users.

After a thorough investigation, we identified the root cause and deployed a fix. Our system will now correctly log incoming subscription payments and extend the associated license’s expiration, regardless of the subscription’s interim status.