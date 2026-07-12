[Changelog](https://freemius.com/changelog/) / Optimizing Webhook Payloads: Removal of Developer Data

Freemius provides a [webhook mechanism](help-documentation-marketing-automation-events-webhooks.md) for seamless integration with your software. We recently discovered that some webhook payloads were unintentionally including developer data. To optimize network payloads, we will no longer be sending this data. All other entities and payloads will remain unchanged. For example, the `license.created` webhook will continue to receive the license object as expected.

This inclusion of developer data was an oversight on our part, and since it was never documented, we have no reason to believe it was actively used. However, if you were relying on it, you have two options:

1. Retrieve the developer data directly via the API when needed.
2. **Recommended:** Store the developer data in an environment variable or cache it within your system. Since this data rarely changes, frequent API calls or webhook-based retrieval are unnecessary.