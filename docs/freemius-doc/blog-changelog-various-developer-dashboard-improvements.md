[Changelog](https://freemius.com/changelog/) / Various Developer Dashboard improvements

This week, we’re deploying some minor improvements to our Developer Dashboard. Please find the details below.

### Fixed regression in the secret key UI component

[![](https://freemius.com/blog/wp-content/uploads/2025/01/developer-dashboard-secret-key-ui.png)](https://freemius.com/blog/wp-content/uploads/2025/01/developer-dashboard-secret-key-ui.png)

We identified a regression where the copy button for the secret key component on the [profile page](https://dashboard.freemius.com/#!/profile/) wasn’t functioning. This has now been fixed.

Please note that since we do not load the Developer’s secret key (not even in memory), you will need to click the “Reveal” button before the copy button is displayed.

### Other fixes

- We addressed console errors caused by incorrect interpolation of SVG icons.
- We also fixed an issue where the feature ordering wasn’t working correctly for certain products.