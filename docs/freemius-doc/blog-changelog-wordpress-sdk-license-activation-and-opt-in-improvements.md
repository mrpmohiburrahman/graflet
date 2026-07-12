[Changelog](https://freemius.com/changelog/) / WordPress SDK: License Activation and Opt-In Improvements

We’re introducing changes to our backend to enhance the experience of using the [WordPress SDK](https://github.com/Freemius/wordpress-sdk).

### Activating licenses for deleted plans

Previously, we added a temporary restriction to prevent makers from deleting plans with active, non-expired licenses. This measure was put in place to avoid scenarios where buyers couldn’t activate licenses tied to a deleted plan.

However, we aim to offer makers the flexibility to delete plans (e.g., to deprecate them) while still enabling buyers to activate their valid licenses.

In this update, we’re rolling out the following improvements:

1. **Plan Deletion Flexibility:** Makers can now delete plans even if active licenses are associated with them.
2. **License Activation Support:** The SDK now fully supports activating licenses linked to deleted plans.

If you’re already using [version 2.9.0](https://github.com/Freemius/wordpress-sdk/releases/tag/2.9.0) of the WordPress SDK, no further updates are required on your end.

### Preventing free plan opt-ins for premium-only products

We identified an edge case where users with malicious intent could modify the SDK integration code within a WordPress plugin or theme to attempt opting into a product’s free plan.

Although this did not pose any security risk, it led to the creation of unnecessary sites, even when the product did not offer a free plan.

With this deployment, we’ve implemented measures to actively detect and block such requests.

### Improved staging site support

Freemius provides out-of-the-box [license utilization](https://freemius.com/help/documentation/selling-with-freemius/license-utilization/#using_one_license_for_live_production_staging_dev_and_localhost_sites) for staging and development sites. We’ve enhanced our system to include support for additional well-known staging providers, making it even easier to manage licenses during development.