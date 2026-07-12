[Changelog](https://freemius.com/changelog/) / Fix for Rare License Migration Edge Case in the WP SDK

Our WP SDK includes a built-in mechanism to detect when a site is being cloned or moved to a new URL. When that happens, it presents [several options](help-documentation-wordpress-sdk-safe-mode-clone-resolution-duplicate-website.md) to help users properly handle the migration — for example, marking the site as a staging copy or fully migrating it to the new domain.

[![Freemius WP SDK Clone Resolution Notice](https://freemius.com/blog/wp-content/uploads/2025/12/wp-sdk-clone-resolution-1024x269.png)](https://freemius.com/blog/wp-content/uploads/2025/12/wp-sdk-clone-resolution.png)

We identified an edge case in the “[Migrate License](help-documentation-wordpress-sdk-safe-mode-clone-resolution-duplicate-website.md#license-migration)” flow where, in very rare situations, the system migrated a license without running all the expected validation checks. This included skipping [quota validation](help-documentation-wordpress-license-utilization.md) or overlooking URL restrictions enforced by the [license firewall](help-documentation-users-account-management-license-security.md#url-whitelisting-aka-license-firewall).

The issue has now been fully resolved on our infrastructure side, ensuring all migrations go through the correct validation path. No update to the WP SDK is required on your end.