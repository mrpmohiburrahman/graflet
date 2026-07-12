[Changelog](https://freemius.com/changelog/) / Improved Trial Emails and Backend Fixes

We’ve rolled out the following small improvements and bug fixes in our backend.

## Improved Trial Emails

We’ve reviewed all emails our system sends during the lifecycle of a trial and updated them to look consistent with the new style.

[![Updated trial email design](https://freemius.com/blog/wp-content/uploads/2026/06/trial-email-freemius-1024x929.png)](https://freemius.com/blog/wp-content/uploads/2026/06/trial-email-freemius.png)

Freemius trials are a great marketing tool to boost sales by giving potential customers a risk-free way to experience your product before committing to a purchase. You can read more about it in our [documentation](help-documentation-selling-with-freemius-set-up-trials.md).

## API and Webhook Fixes

- We noticed a minor regression where, in some cases, deleting a license from the Developer Dashboard resulted in an error. We identified the root cause and deployed a fix.
- We identified a rare edge case where [webhooks](help-documentation-saas-events-webhooks.md) would not fire for some [cart-related events](help-documentation-saas-events-webhooks.md#cart). This has been fixed.