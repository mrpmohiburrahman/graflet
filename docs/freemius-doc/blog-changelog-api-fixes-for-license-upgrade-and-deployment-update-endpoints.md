[Changelog](https://freemius.com/changelog/) / API Fixes for License Upgrade and Deployment Update Endpoints

### Bug Fix for Checkout Upgrade Link Generation API

We’ve rolled out updates to the recently released API endpoint for [generating upgrade links for licenses](blog-changelog-new-api-endpoint-to-generate-license-upgrade-links.md).

- The links now use time-limited authorized tokens instead of license keys, improving both security and alignment with best practices.

<!--THE END-->

- We also removed the `currency` parameter from the payload documentation. This was mistakenly included earlier — Freemius does not support changing currency through the license renewal or upgrade flow.

Upgrade links provide a great UX for your buyers to manage their subscriptions. You can find the detailed documentation [here](https://docs.freemius.com/api/licenses/generate-upgrade-link).

### Bug Fix for Deployment Update API Endpoint

We noticed an issue in the [deployment update API endpoint](https://docs.freemius.com/api/deployments/update) where the `limit` value was incorrectly accepting negative integers and converting them to `0`.

The `limit` value is used for [staged rollouts](help-documentation-release-management-staged-rollouts.md) — a great way to gradually release deployments, helping to catch bugs earlier within a tighter feedback loop. However, due to this bug, an incorrect value would essentially disable staged rollout altogether.

[![Staged rollout UI update for rejecting negative value - Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2025/05/freemius-release-management-staged-rollout-1024x1003.png)](https://freemius.com/blog/wp-content/uploads/2025/05/freemius-release-management-staged-rollout.png)

This bug has now been fixed. Additionally, we’ve updated the UI to prevent negative values from being submitted.