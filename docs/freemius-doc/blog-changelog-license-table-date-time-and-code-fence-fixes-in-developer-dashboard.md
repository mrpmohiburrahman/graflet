[Changelog](https://freemius.com/changelog/) / License Table, Date-Time, and Code Fence Fixes in Developer Dashboard

This week we are releasing several UI/UX enhancements and bug fixes in our Developer Dashboard. Please find the details below:

### Fixed alignment issue in the license table

We noticed an alignment glitch when bundle license icons were being displayed on the license page. We have fixed this and repositioned the icon after the plan name to ensure a consistent visual layout.

[![Bundle license icon in table](https://freemius.com/blog/wp-content/uploads/2025/08/license-table-alignment-issue-1024x403.png)](https://freemius.com/blog/wp-content/uploads/2025/08/license-table-alignment-issue.png)

This UI provides a quick way to see the licenses generated from the purchase of [bundles](help-documentation-wordpress-selling-bundles-and-memberships.md).

### Fixed date-time values in tables

We noticed that some date-time values in certain tables were incorrectly converted into the wrong time zone before being displayed. This led to confusion when compared with data from the Sales Analytics page.

[![Timezone fix in the Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2025/08/datetime-timezone-fix-1024x645.png)](https://freemius.com/blog/wp-content/uploads/2025/08/datetime-timezone-fix.png)

We have identified and deployed a fix. Now all dates in the Dashboard are consistently displayed in UTC timezone.

### Improved code fences

We noticed a regression in the code fence components, especially in the dark mode theme.

[![Code fences in the Developer Dashboard with copy button](https://freemius.com/blog/wp-content/uploads/2025/08/code-fence-color-improvement-1024x379.png)](https://freemius.com/blog/wp-content/uploads/2025/08/code-fence-color-improvement.png)

This has now been fixed and code fences render properly in all modes. We also did a small triage and ensured that all code fences include a copy button, so you can easily copy-paste snippets.