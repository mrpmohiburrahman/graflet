[Changelog](https://freemius.com/changelog/) / API & Backend Stability Improvements

This week we are rolling out a couple of small bug fixes and quality-of-life improvements across our API and backend systems.

- We identified an issue where removing all products from a [bundle](help-documentation-wordpress-selling-bundles-and-memberships.md) could, in some cases, break the [Customer Portal](help-documentation-users-account-management.md). The underlying issue has been addressed and fixed.
- The `license.created` [event](help-documentation-saas-events-webhooks.md#license-created) was not being triggered when licenses were created manually. This has now been corrected, ensuring consistent webhook behavior.