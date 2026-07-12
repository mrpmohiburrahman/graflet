[Changelog](https://freemius.com/changelog/) / Misc enhancements and various bug fixes

This week we are also deploying some enhancements and bug fixes for the [Developer Dashboard](https://dashboard.freemius.com/).

## Improved “Custom localhost URLs” UI from store

When [viewing a user](https://freemius.com/help/documentation/analytics-insights/user-data/#your_users) from a Store, we have improved the **“[Custom localhost URLs](https://freemius.com/help/documentation/selling-with-freemius/license-utilization/#custom_staging_development_testing_localhost_patterns)“** section to include instructions on how to change it from the relevant product.

[![Freemius stores page "Custom localhost URLs" section](https://freemius.com/blog/wp-content/uploads/2024/07/freemius-store-page-custom-localhost-urls-1024x346.png)](https://freemius.com/blog/wp-content/uploads/2024/07/freemius-store-page-custom-localhost-urls.png)

Previously we allowed changing it directly for the product associated with the latest license of the user. Since a user can have licenses for multiple products from a store, it created some confusion. To avoid such confusion, we have improved the UI to tell explicitly what action needs to be taken and for what product.

## Bug fix for the new product form

We noticed a bug in the “[New Product Form](https://dashboard.freemius.com/#!/live/new-product/)” when it was loaded directly due to some race condition. We have deployed a fix for the same.

## Analytics bug fix

We noticed that for some makers, the store-level analytics were generating some API errors. We identified the root cause and have deployed a fix.

## Minor Checkout enhancement

We noticed some redundant API requests being made from our Checkout when calculating taxes. We have pushed a fix to make the system more efficient while making network requests.