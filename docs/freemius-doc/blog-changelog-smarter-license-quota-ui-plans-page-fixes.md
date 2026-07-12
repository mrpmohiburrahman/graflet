[Changelog](https://freemius.com/changelog/) / Smarter License Quota UI & Plans & Affiliate Page Fixes

This week we are releasing the following quality-of-life improvements to the Developer Dashboard.

### The License Quota UI Got Smarter

[![License Quota UI enhancement](https://freemius.com/blog/wp-content/uploads/2025/11/license-quota-ui-1024x643.png)](https://freemius.com/blog/wp-content/uploads/2025/11/license-quota-ui.png)

We noticed that many makers needed a simpler way to manage unlimited licenses. The UI now accepts a `0` value and automatically converts it to an [unlimited quota](help-documentation-wordpress-license-utilization.md), making large-scale license updates more intuitive and consistent.

### Bug Fix in the Plans Page

[![Plan page copy feature](https://freemius.com/blog/wp-content/uploads/2025/11/plan-page-copy-feature-1024x844.png)](https://freemius.com/blog/wp-content/uploads/2025/11/plan-page-copy-feature.png)

We also identified an issue where non-admin team members couldn’t use the Checkout Link or the copy-to-clipboard feature in the [plan page](help-documentation-saas-saas-plans-pricing.md#setting-up-plans). This has now been fixed.

### Fix Deployed for Affiliate Settings Save Issue

We identified an issue in the [Affiliate Settings UI](help-documentation-affiliate-platform-affiliate-program-activation.md) where, in certain edge cases, updates were not being properly saved through the API.

[![Freemius Affiliate UI](https://freemius.com/blog/wp-content/uploads/2025/11/freemius-affiliate-settings-ui-1024x799.png)](https://freemius.com/blog/wp-content/uploads/2025/11/freemius-affiliate-settings-ui.png)

After tracing the root cause, we’ve deployed a fix to ensure all changes are consistently saved moving forward.