[Changelog](https://freemius.com/changelog/) / Deployment Endpoints Bug Resolved

We noticed two bugs in our deployment-related endpoints. When generating the download links for the latest [deployment](https://docs.freemius.com/api/deployments) (or “tag” as we call them internally), we found that in some cases, the links were not properly signed and were getting blocked by our authentication layer.

1. [Get latest deployment for a product](https://docs.freemius.com/api/deployments/get-latest)
2. [Retrieve latest update for an install](https://docs.freemius.com/api/installations/retrieve-latest-update)

We’ve identified the root cause and rolled out a fix. If you’re using these endpoints for a custom integration, you should no longer encounter any issues.

**Note**: Our [WP SDK](help-documentation-wordpress-sdk.md) was not affected by this bug and its auto-update functionality remained fully operational.