[Changelog](https://freemius.com/changelog/) / UX Improvements to Review, License Recovery, and Exports

This week, we released several quality-of-life improvements to our [Developer Dashboard](https://dashboard.freemius.com/), with a focus on exports and the Review & License Recovery apps.

### Improved UX of the Review & License Recovery App

Following our recent rebranding of the [License Recovery](help-documentation-wordpress-license-recovery-tool.md) and [Review app](help-documentation-marketing-automation-reviews.md#reviews-collection), we’re rolling out a set of UX improvements to make these applications more intuitive and resilient.

[![Review App Form Error](https://freemius.com/blog/wp-content/uploads/2026/01/review-app-form-error-1024x815.png)](https://freemius.com/blog/wp-content/uploads/2026/01/review-app-form-error.png)

The forms are now reactive to validation issues upfront, helping users identify and resolve problems earlier in the flow. We also addressed a few layout inconsistencies to ensure a cleaner and more predictable experience.

### Fixes in the Exports

We identified a couple of minor gaps in our [export mechanism](blog-freemius-release-notes-october.md#one_click_payments_and_subscriptions_data_export) that could lead to missing context in exported data.

[![Export licenses from the Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2026/01/licenses-export-1024x358.png)](https://freemius.com/blog/wp-content/uploads/2026/01/licenses-export.png)

- The licenses export was missing the license key
- The affiliates export was missing the user ID

Both issues have been resolved with today’s deployment, ensuring exports now include all the expected fields.

### Fixed License Unit in the Analytics UI

We noticed an issue where the license unit was not correctly reflected in the [Analytics filtering UI](help-documentation-analytics-sales.md#filtering-the-data).

[![Live filtering UI in the Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2026/01/analytics-live-filtering-ui-1024x275.png)](https://freemius.com/blog/wp-content/uploads/2026/01/analytics-live-filtering-ui.png)

This has now been fixed, and the label correctly reflects your [configured license unit](help-documentation-saas-customize-license-unit-label.md).