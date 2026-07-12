[Changelog](https://freemius.com/changelog/) / Fixes for Zero-Value Trial Payments and Payment Update Emails

After releasing [invoices for zero-value payments](blog-changelog-subscription-zero-value-invoices-are-now-sent-to-buyers.md), we noticed that the Developer Dashboard was also listing the first zero-value payment for trials. Since this information is internal to our system and does not provide any actionable value to makers, we’ve refined the behavior.

Going forward, the Dashboard (and API) will only surface relevant zero-value payments along with their associated invoices, keeping the UI cleaner and more focused.

In addition, we fixed a regression where a payment-like email was mistakenly sent when users updated their payment method.