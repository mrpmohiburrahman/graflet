[Changelog](https://freemius.com/changelog/) / API Fix: Resolved 504 Errors and Significantly Improved Sites Version Filter Performance

We noticed an intermittent issue where querying Sites by version number was returning a `504` server error from the API. This typically surfaced when makers clicked the **Downloaded** link from the [Deployment page](help-documentation-wordpress-deployment-process.md).

[![Downloaded Link from the Deployment Page](https://freemius.com/blog/wp-content/uploads/2025/12/querying-sites-by-version-1024x457.png)](https://freemius.com/blog/wp-content/uploads/2025/12/querying-sites-by-version.png)

After investigating, we identified the root cause and deployed a fix. Alongside this, we substantially optimized the underlying API request, resulting in a much faster experience. The Sites page now loads instantly when filtering by version, instead of occasionally timing out.