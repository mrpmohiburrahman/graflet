[Changelog](https://freemius.com/changelog/) / Miscellaneous Changes – November 4, 2024

This week, we deployed the following updates:

- **API Documentation Enhancements**: We’ve expanded our [API documentation](https://freemius.com/help/documentation/api/) with additional endpoints to improve your development experience.
- **Webhook Fix for `user.email_status.bounced`** : We resolved an issue where this [webhook](help-documentation-marketing-automation-events-webhooks.md) could incorrectly trigger irrelevant events.
- **Deployment Mechanism Bug Fix**: An edge case bug was identified and fixed where the [deployment process](https://freemius.com/help/documentation/selling-with-freemius/deployment/) could break when changing a product from a “static” type (e.g., templates, widgets) to a “dynamic” type (e.g., WordPress plugins or themes).
- **Simplified Checkout Links**: We are now generating short links for checkouts from the Developer Dashboard. Instead of using links like `https://checkout.freemius.com/mode/dialog/<productType>/<productID>/`, you’ll see the cleaner format `https://checkout.freemius.com/<productType>/<productID>`. The old links will still work, but the new format is more visually appealing, and the `mode/dialog` part is no longer necessary for modern usage.