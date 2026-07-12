[Changelog](https://freemius.com/changelog/) / Bug Fix in Webhooks: License Key Now Included in All License Events

We recently discovered that the license key was unintentionally omitted from all license-related webhook events. This issue has now been resolved. Webhook listeners will now receive the full license object, which includes the `secret_key` property — representing the license key.