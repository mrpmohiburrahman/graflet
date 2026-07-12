[Changelog](https://freemius.com/changelog/) / Bug Fix in License Table Showing Duplicate Subscriptions

We noticed a bug in our License table where, in some cases, duplicate rows were being rendered. This happened when a license had multiple canceled or inactive subscriptions from the past. With Freemius, it’s possible for a license to go through multiple subscriptions during its lifecycle—for example, when customers [upgrade plans](help-documentation-saas-app-integration.md#handling-license-upgrades) or [change payment methods](help-documentation-marketing-automation-dunning-failed-payments.md).

[![License table in Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2025/09/freemius-license-table-developer-dashboard-1024x517.png)](https://freemius.com/blog/wp-content/uploads/2025/09/freemius-license-table-developer-dashboard.png)

However, showing duplicate licenses created confusion for makers. We’ve rolled out a fix: the table will now display each license only once and correctly associate it with the latest subscription.