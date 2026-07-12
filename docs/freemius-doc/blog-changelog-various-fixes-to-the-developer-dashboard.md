[Changelog](https://freemius.com/changelog/) / Various fixes to the Developer Dashboard

This week’s deployment also brings various fixes to the Developer Dashboard.

### Revealing the secret key on the Store Settings page

We had a UI issue on the Store Settings page where the secret key could not be revealed. Not only did we fix this issue, we also improved the UI in general.

[![Secret key UI in the Developer Dashboard - Freemius](https://freemius.com/blog/wp-content/uploads/2023/08/secret-key-ui-freemius-developer-dashboard.jpg)](https://freemius.com/blog/wp-content/uploads/2023/08/secret-key-ui-freemius-developer-dashboard.jpg)

From now on, the secret key will be hidden by default on every page that displays it. You can choose whether to reveal it or to copy it.

### Other fixes/improvements

- The cache busting now works seamlessly when we deploy a new version of the Developer Dashboard app. Previously, some of our partners faced some issues.
- Fixed an edge case issue where the main pricing wouldn’t load properly on the pricing page.
- Fixed an issue where the [earnings page](https://dashboard.freemius.com/#!/earnings/) could not be loaded directly from the bookmark.