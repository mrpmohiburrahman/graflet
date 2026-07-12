[Changelog](https://freemius.com/changelog/) / Fixed Loading of Abandoned Licenses in the Developer Dashboard

From the Freemius Developer Dashboard, makers can view and download a list of licenses. The system also allows filtering licenses based on various criteria.

[![Freemius Developer Dashboard - Filter Licenses](https://freemius.com/blog/wp-content/uploads/2025/03/license-filter-ui-freemius-1024x844.png)](https://freemius.com/blog/wp-content/uploads/2025/03/license-filter-ui-freemius.png)

We identified a regression where selecting the Abandoned filter was not working correctly. Abandoned licenses refer to those that have expired or have an expired/canceled subscription. We have now identified the root cause and deployed a fix.