[Changelog](https://freemius.com/changelog/) / Developer Dashboard Improvements for Webhooks, Plan Pricing, and License Creation

This week, we’re rolling out several quality-of-life improvements to our [Developer Dashboard](https://dashboard.freemius.com/).

## Developer Role Can Manage Webhooks

We noticed a regression where a [team member](help-documentation-security-team-member-role-management.md) with the **Developer** role could not manage [webhooks](help-documentation-saas-events-webhooks.md). This has been fixed.

[![Manage webhooks in Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2026/06/manage-webhooks-1024x350.png)](https://freemius.com/blog/wp-content/uploads/2026/06/manage-webhooks.png)

## Fixed Various UI Glitches on the Plan Page

We noticed a few bugs on the [Plan page](help-documentation-saas-saas-plans-pricing.md) where, in some cases, adding or removing currencies could break parts of the UI. We also found some edge cases where recommended pricing was not working properly.

We also noticed that there was no clear way to delete single-unit USD pricing. This could be confusing for makers selling in [local markets](help-documentation-checkout-features-local-languages-currencies.md) where USD pricing is not relevant or supported.

Since pricing configuration is one of the more important parts of product setup, we did a thorough investigation and rewrote several sections of the page to make the experience more reliable.

[![Pricing and plan page in Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2026/06/plan-page-1024x503.png)](https://freemius.com/blog/wp-content/uploads/2026/06/plan-page.png)

We hope this fixes the reported bugs and UI glitches. If you notice any issues, please report them to us through support.

## Fixed Unit Label in the License Creation Dialog

We noticed that the license creation dialog was always showing “Site”, even for SaaS and App products with a custom unit label.

[![Create license dialog](https://freemius.com/blog/wp-content/uploads/2026/06/create-license-1024x754.png)](https://freemius.com/blog/wp-content/uploads/2026/06/create-license.png)

This has now been fixed.