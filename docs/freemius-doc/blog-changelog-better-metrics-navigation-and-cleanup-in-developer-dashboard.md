[Changelog](https://freemius.com/changelog/) / Better Metrics, Navigation, and Cleanup in Developer Dashboard

This week we’re rolling out various quality of life improvements to the Developer Dashboard.

### Corrected Metric Badge Indicators

We identified an issue where some metric badges on the [Analytics Dashboard](help-documentation-analytics.md) page (for WordPress products) were showing incorrect comparisons. For example, a decrease in trial cancellation count was still marked in red with a downward arrow, indicating a negative change, whereas it is conceptually positive. This has now been corrected across relevant metrics.

[![Metric comparison badge update](https://freemius.com/blog/wp-content/uploads/2026/03/updated-metric-comparison-badge-1024x646.png)](https://freemius.com/blog/wp-content/uploads/2026/03/updated-metric-comparison-badge.png)

### Shareable Links for Plans Tabs

All individual tabs in the Plans page now have unique URLs. This makes it easier to share direct links within teams and allows our support team to point to specific settings when needed.

[![Plans page tab has links](https://freemius.com/blog/wp-content/uploads/2026/03/plans-page-tab-link-1024x483.png)](https://freemius.com/blog/wp-content/uploads/2026/03/plans-page-tab-link.png)

### Improved App & SaaS Context by Removing “Sites” References

We identified some references to “Sites” that are not relevant for App & SaaS products. These have now been removed (especially inside individual user information and also from tables like Events, as well as Subscriptions), making the experience more consistent across product types.

[![Removed irrelevant Site and Localhost info from user page for App & SaaS](https://freemius.com/blog/wp-content/uploads/2026/03/updated-user-info-1024x650.png)](https://freemius.com/blog/wp-content/uploads/2026/03/updated-user-info.png)

### Other Fixes

- The sidebar and detail panels of the Licenses and Subscriptions pages had some minor UI glitches. These have now been fixed.
- We noticed a regression where the “Join Freemius Slack” item in the Setup Checklist could not be marked as completed. This has been fixed.