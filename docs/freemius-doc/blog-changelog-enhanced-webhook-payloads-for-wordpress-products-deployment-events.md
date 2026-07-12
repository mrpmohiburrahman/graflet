[Changelog](https://freemius.com/changelog/) / Enhanced Webhook Payloads for WordPress Products Deployment Events

Freemius offers a powerful webhook and events system to support your custom integrations. For example, when a new version is deployed, a `plugin.version.deployed` event is triggered, which your webhook can use to perform automations, such as notifying customers via email.

Based on requests from our maker community, we’ve enhanced the payloads of the following events:

- `plugin.version.deployed` & `plugin.version.updated` — now include `file`, `version`, and `release_mode` fields.
- `plugin.version.deleted` — now includes the `version` field.

[![Freemius Webhook Event Payload](https://freemius.com/blog/wp-content/uploads/2025/07/freemius-product-deployed-event-1024x647.png)](https://freemius.com/blog/wp-content/uploads/2025/07/freemius-product-deployed-event.png)

These enriched payloads should give you more actionable data to build powerful automations.

As a reminder, all `plugin.version.*` events include a `tag` field that holds the deployment ID. You can use that ID to retrieve full deployment details via a single [API call](https://docs.freemius.com/api/deployments) if additional data is needed.