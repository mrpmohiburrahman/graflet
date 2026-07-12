[Changelog](https://freemius.com/changelog/) / Fixed plugin/theme update issue with the Staged Rollouts feature

Freemius supports the Staged Rollouts feature, which allows you to gradually send your product updates to users. You can read more about it [here](help-documentation-release-management-staged-rollouts.md).

We noticed in an edge case that if a site had already received a notification for an update — but the site admin didn’t choose to update immediately — the updates could fail later on because the “staged rollout” might have been completed since then.

In this iteration, we fixed these edge-case scenarios. The update will now fall back to the last stable release if such a case is encountered. We fixed this from our API layer. No changes to the WordPress SDK were necessary.