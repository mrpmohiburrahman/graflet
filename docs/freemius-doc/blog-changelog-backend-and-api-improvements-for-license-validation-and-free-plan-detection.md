[Changelog](https://freemius.com/changelog/) / Backend and API Improvements for License Validation and Free Plan Detection

We have made the following updates to our backend and API servers.

### License API Improvements

We have enhanced our [license activation API doc](https://docs.freemius.com/api/licenses/activate) to document the various error codes the endpoint might return and how to handle them. This should make it easier to build more reliable [application license integration](help-documentation-saas-app-integration.md) logic.

[![Freemius License Activation API Doc](https://freemius.com/blog/wp-content/uploads/2026/03/license-activation-api-doc-1024x627.png)](https://docs.freemius.com/api/licenses/activate)

Additionally, all our endpoints now return an `X-API-Server-Time` header to help protect against local time tampering when [validating a license’s expiration](help-documentation-saas-integrating-license-key-activation.md#license-validation) on the client side.

### Fixed Free Plan Identification

We identified an edge-case bug where our system was incorrectly treating some plans as “Free” plans. This led to some unintended side effects. For example, some of the [transactional emails](help-documentation-marketing-automation-transactional-emails.md) were being sent with “Thanks for upgrading” instead of “Thanks for subscribing”, even when no Free offering was involved.

[![Subscription email sent by Freemius](https://freemius.com/blog/wp-content/uploads/2026/03/freemius-subscription-email-1024x314.png)](https://freemius.com/blog/wp-content/uploads/2026/03/freemius-subscription-email.png)

We found the root cause and fixed the issue.