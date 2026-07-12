[Changelog](https://freemius.com/changelog/) / Better Events Filtering and Mobile UI for the Developer Dashboard

We are releasing a few minor yet impactful enhancements to our Developer Dashboard this week.

### Events Table Filtering

Freemius [events and webhooks](help-documentation-marketing-automation-events-webhooks.md) are a powerful way to build seamless [SaaS integrations](help-documentation-selling-with-freemius-saas-integration.md) — for example, listening to the `license.created` event and responding to it within your app.

[![Filtering event logs from the Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2025/06/events-table-filter-by-status-1024x557.png)](https://freemius.com/blog/wp-content/uploads/2025/06/events-table-filter-by-status.png)

The Developer Dashboard already includes a UI to view these events and even resend them for testing or debugging. However, we found a bug that prevented filtering events by webhook status. This has now been fixed, and the status filter works as expected.

### Responsiveness improvements

Some pages — such as the [**Earnings**](https://dashboard.freemius.com/#!/earnings/) page — weren’t fully optimized for mobile viewing.

[![Freemius Earnings page, as viewed from mobile devices](https://freemius.com/blog/wp-content/uploads/2025/06/earnings-page-responsiveness-1024x686.png)](https://freemius.com/blog/wp-content/uploads/2025/06/earnings-page-responsiveness.png)

We’ve addressed this, ensuring those pages are now responsive and easier to use on-the-go.

### Other Bug Fixes and Improvements

- Fixed an edge case in the **License Creation** UI where associated sites were not displayed correctly.
- Fixed an issue where a newly created **Plan** for a new product wouldn’t immediately show up in the UI.