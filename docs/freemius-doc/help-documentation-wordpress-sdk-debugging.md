---
title: "Debugging"
url: "https://freemius.com/help/documentation/wordpress-sdk/debugging/"
source: "docs"
section: "Docs"
category: "WordPress SDK"
scraped_at: "2026-04-09T19:58:44+06:00"
word_count: 199
---

Freemius has inbuilt options for debugging and logging issues so as to make the integration process easier for developers. Here is how to enable and use these features:

## Access the Freemius Debug Page[​](#access-the-freemius-debug-page "Direct link to Access the Freemius Debug Page")

You can access the **Freemius Debug** page directly via `{domain}/wp-admin/admin.php?page=freemius` to get information about the active SDK, Freemius-powered products on the site, users, and more.

Setting `WP_FS__DEV_MODE` to `true` will enable logging. It will automatically activate the logger that outputs all logs to your browser's debugging console.

## Output Logs to Screen[​](#output-logs-to-screen "Direct link to Output Logs to Screen")

You can output all logs to the screen by adding `&fs_dbg_echo=true` to the query string.

Security Tip

Adding `fs_dbg_echo=true` to the query string will only work when Freemius is set to [development mode](help-documentation-wordpress-sdk-testing.md#setting-freemius-into-development-mode). Therefore, websites using your product are not at risk of exposing the logs unless an administrator sets `WP_FS__DEV_MODE` to `true` or manually toggles on the debugging switch in the *Freemius Debug* page.

## Debug Bar Integration[​](#debug-bar-integration "Direct link to Debug Bar Integration")

Additionally, if you are using [Debug Bar](https://wordpress.org/plugins/debug-bar/), Freemius SDK logging is fully integrated with it to make debugging even easier with its UI.