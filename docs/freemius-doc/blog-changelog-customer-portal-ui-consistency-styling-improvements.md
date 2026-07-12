[Changelog](https://freemius.com/changelog/) / Customer Portal UI Consistency & Styling Improvements

This week we are rolling out follow-ups addressing several UI glitches and styling enhancements in the [Customer Portal](help-documentation-users-account-management.md).

[![Customer Portal - Freemius](https://freemius.com/blog/wp-content/uploads/2026/02/customer-portal-1024x529.png)](https://freemius.com/blog/wp-content/uploads/2026/02/customer-portal.png)

These changes are primarily at the infrastructure level and touch many UI components across the portal. As a result, you should now experience better visual consistency, especially when applying custom themes using [CSS variables](help-documentation-users-account-management-applying-css-customization.md). Below are the notable improvements:

1. All icons are now rendered as inline SVGs, allowing your custom CSS to style them more reliably.
2. Several minor alignment issues have been resolved based on feedback from our makers.
3. We audited and replaced all remaining hard-coded color values with CSS variables to ensure custom styling works more predictably.

In addition to the UI fixed, we also fixed an issue where the portal could remain on a stale page after login. For example, if a store sells only SaaS products (and has no Websites page), users will now be correctly redirected to the Licenses page.