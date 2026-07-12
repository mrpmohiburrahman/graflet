---
title: "Migrating from ThemeForest to Freemius"
url: "https://freemius.com/help/documentation/migration/migrating-from-themeforest-to-freemius/"
source: "docs"
section: "Docs"
category: "Migration"
scraped_at: "2026-04-09T19:58:39+06:00"
word_count: 350
---

With the help of our partners who migrated from ThemeForest to Freemius, we managed to develop a very simple and proven migration process that anyone can follow.

## Step I - Start to sell with Freemius[​](#step-i---start-to-sell-with-freemius "Direct link to Step I - Start to sell with Freemius")

Follow the [getting started guide](help-documentation-getting-started.md) to...

- [Create an account](help-documentation-getting-started-creating-an-account.md)
- [Create the theme on Freemius](help-documentation-getting-started-integrating-your-first-product.md#add-a-new-product)
- [Configure its plans and prices](help-documentation-wordpress-setup-product-pricing-plans-refunds.md)
- [Integrate the theme with our SDK](help-documentation-wordpress-integration-with-sdk.md)
- [Update your site’s buy buttons to trigger the Freemius checkout](help-documentation-getting-started-making-your-first-sale.md#hosted-checkout)

## Step II - Migrating ThemeForest customers to Freemius[​](#step-ii---migrating-themeforest-customers-to-freemius "Direct link to Step II - Migrating ThemeForest customers to Freemius")

If you want to migrate your ThemeForest customers, you’ll need to take the following steps:

- Choose a transition date
- Using [this WordPress plugin](https://github.com/Freemius/codecanyon-to-freemius-license-converter/tree/develop) in order to create a page on your WP site where a customer can enter their Envato purchase code & email address to receive a Freemius license key. We recommend setting the license expiration with an additional 3 months and allowing customers whose license key has expired to get a Freemius key that expires in 3 months. The benefits are that you give a grace period to existing customers and also move non-paying customers to Freemius, which comes with a bunch of marketing automations that can help you convert them back to a paid subscription.

warning

Creating users via the API is disabled by default. Therefore, for the WordPress plugin to work properly, please get in touch with our team via [\[email protected\]](/cdn-cgi/l/email-protection#a3d0d6d3d3ccd1d7e3c5d1c6c6cecad6d08dc0ccce) with your theme details and ask to elevate your account's permissions for the migration.

- Add an admin notice to the theme hosted on ThemeForest notifying your users about the upcoming transition with a link to the page where they can convert their license to a Freemius license.
- Push an update to the theme to notify customers about the upcoming change.
- Integrate the Freemius SDK into the ThemeForest theme and remove any previous updates & licensing mechanisms.
- Customers that will upgrade will be prompted to activate their Freemius license key.
- Done!