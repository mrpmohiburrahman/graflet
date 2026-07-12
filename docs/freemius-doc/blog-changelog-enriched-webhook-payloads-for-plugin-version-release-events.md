[Changelog](https://freemius.com/changelog/) / Enriched Webhook Payloads for Plugin Version Release Events

Responding to a feature request from one of our makers, we’ve enriched the `plugin.version.released`, `plugin.version.beta.released`, and `plugin.version.release.suspended` [events](help-documentation-saas-events-webhooks.md#types-of-events) to include more detailed information about the tag and deployment.

Previously, the payload only included a reference like `tag: <ID>`. From now on, the webhook payload will include richer data, for example:

```
{"tag": "1234", "version": "3.0.1", "release_mode": "released"}
```

This makes [webhook automation](help-documentation-saas-events-webhooks.md) simpler and more self-contained, especially for workflows like notifying buyers after a new version is released. Earlier, this required an additional API call to fetch deployment details; the webhook payload now includes everything you need upfront.