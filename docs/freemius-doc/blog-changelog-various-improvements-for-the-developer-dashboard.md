[Changelog](https://freemius.com/changelog/) / Various Improvements for the Developer Dashboard

This week, we’re deploying several updates to the [Developer Dashboard](https://dashboard.freemius.com/), including improvements and bug fixes

### Improvements to Product Ownership Transfer

Freemius has long supported [ownership transfers](help-documentation-security-team-member-role-management.md#assigning_a_new_owner), which is especially useful if you’re [selling your business](https://freemius.com/blog/selling-wordpress-product-business/).

[![](https://freemius.com/blog/wp-content/uploads/2024/12/change-product-owner-fs-developer-dashboard-1024x552.png)](https://freemius.com/blog/wp-content/uploads/2024/12/change-product-owner-fs-developer-dashboard.png)

We identified and fixed a glitch in the system where ownership transfers could be blocked in certain cases due to recent enhancements to the API system.

While addressing this issue, we also discovered and resolved a couple of edge-case bugs. The entire transfer system, including the team member UI, should now work flawlessly.

### Better Filtering for the Custom Webhook Integration

With Freemius, you can add [webhook listeners](help-documentation-marketing-automation-events-webhooks.md) for custom integrations. Freemius logs numerous events throughout a product’s lifecycle, such as when a new subscription is created or canceled.

As a product owner, you can use these events to trigger responses in your own system.

[![](https://freemius.com/blog/wp-content/uploads/2024/12/webhooks-events-list-ui-773x1024.png)](https://freemius.com/blog/wp-content/uploads/2024/12/webhooks-events-list-ui.png)

We discovered that the UI for filtering events was incorrectly displaying events not scoped to the selected product. This issue has been resolved, and we’ve also made performance improvements for a smoother experience.

### Other Enhancements and Bug Fixes

- Fixed an issue where adding a new whitelisted site could cause errors.
- Resolved a bug where some URLs incorrectly triggered the product code change pop-up.
- Added toast notifications to confirm successful operations when reordering or toggling features on the **Plan** page.