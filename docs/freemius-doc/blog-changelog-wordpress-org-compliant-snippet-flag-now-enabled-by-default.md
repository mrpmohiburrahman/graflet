[Changelog](https://freemius.com/changelog/) / WordPress.org Compliant Snippet Flag Now Enabled by Default

As per the updated guidelines from the wordpress.org review team, we are updating the [integration snippet](help-documentation-wordpress-integration-with-sdk.md#insert-the-auto-generated-sdk-integration-snippet) our system generates for the [Freemius WP SDK](help-documentation-wordpress-sdk.md). Previously, the [`is_org_compliant`](help-documentation-wordpress-sdk-integrating-freemius-sdk.md#is_org_compliant) flag was only present in the snippet if it was explicitly set to `false`. Our SDK always treats the integration as WordPress.org compliant.

With the latest compliance update, the flag is now always present, defaulting to `true`.

[![Freemius WP SDK Integration Snippet](https://freemius.com/blog/wp-content/uploads/2026/02/freemius-wp-sdk-integration-code-1024x797.png)](https://freemius.com/blog/wp-content/uploads/2026/02/freemius-wp-sdk-integration-code.png)

For new products, this change ensures your first submission won’t get rejected due to a missing compliance flag. For existing products, we recommend making this manual change in your integration snippet. We will also follow up soon with an update to our [deployment mechanism](help-documentation-wordpress-deployment-process.md) so the flag is automatically added to your integration snippet in [newly generated versions](help-documentation-release-management-deployment.md#free-version-auto-generation--paid-logic-stripping--php-preprocessor).