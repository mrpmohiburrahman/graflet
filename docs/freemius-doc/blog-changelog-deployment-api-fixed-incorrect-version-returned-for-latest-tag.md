[Changelog](https://freemius.com/changelog/) / Deployment API: Fixed Incorrect Version Returned for Latest Tag

We discovered a bug in some of our API endpoints responsible for fetching the latest deployment of a WordPress product — for example, `products/{product_id}/tags/latest.json`.

Instead of returning information about the most recent deployed version, these endpoints were incorrectly returning the latest [incremental release](help-documentation-release-management-incremental-update.md). We’ve identified the root cause, and a fix has been deployed.

This bug did **not** affect the update flow of our WordPress SDK. The SDK has always expected and correctly received updates based on the incremental versioning and other [release mechanisms](help-documentation-release-management.md) that Freemius offers.