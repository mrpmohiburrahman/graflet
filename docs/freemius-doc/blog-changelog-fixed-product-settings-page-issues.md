[Changelog](https://freemius.com/changelog/) / Fixed Product Settings Page Issues

This week, we are rolling out a few bug fixes around the [Settings page](help-documentation-getting-started-explore-the-developer-dashboard.md#:~:text=Settings%20%2D%20Update%20product%20settings%20such%20as%20title%2C%20slug%2C%20icon%2C%20team%20members%20etc.) of a product.

[![Freemius Developer Dashboard Settings page for a product](https://freemius.com/blog/wp-content/uploads/2026/05/product-settings-page-1024x603.png)](https://freemius.com/blog/wp-content/uploads/2026/05/product-settings-page.png)

- Newly created products did not show the [bearer token](https://docs.freemius.com/api/section/bearer-token-auth) on the Settings page immediately. It would only appear after a full page refresh. This has been fixed.
- We noticed that adding or deleting plans for a product could, in some edge case scenarios, break the settings form. We found the root cause and have deployed a fix.