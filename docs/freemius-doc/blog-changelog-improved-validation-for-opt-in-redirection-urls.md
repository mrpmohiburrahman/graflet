[Changelog](https://freemius.com/changelog/) / Improved Validation for Opt-In Redirection URLs

Our [SDK Integration page](help-documentation-wordpress-sdk-integrating-freemius-sdk.md) from the [Developer Dashboard](https://dashboard.freemius.com) allows you to configure various settings to tailor the [Opt-In experience](help-documentation-wordpress-sdk-opt-in-message.md) as per the behavior of your plugin.

One such option is to enter a *redirection* path that triggers after the plugin activation. When enabled, the SDK ensures the user is redirected to the specified URL after the Opt-In is completed.

However, we noticed a bug where makers could mistakenly enter the redirection URL in absolute form instead of relative form. This often happened when the full URL was copy-pasted directly from the browser without stripping the unnecessary parts. As a result, the SDK integration and Opt-In flow could break.

[![Freemius WP SDK activation redirection option](https://freemius.com/blog/wp-content/uploads/2025/08/sdk-redirection-url-1024x456.png)](https://freemius.com/blog/wp-content/uploads/2025/08/sdk-redirection-url.png)

To fix this, we’ve now updated our UI to strictly accept only relative URLs for Opt-In redirection. This ensures consistency and prevents accidental misconfigurations.