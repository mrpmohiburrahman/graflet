---
title: "Testing your product before releasing to production"
url: "https://freemius.com/help/documentation/wordpress-sdk/testing/"
source: "docs"
section: "Docs"
category: "WordPress SDK"
scraped_at: "2026-04-09T19:58:45+06:00"
word_count: 587
---

After integrating the Freemius SDK into your WordPress product, you should test it to ensure everything works properly before releasing a version to production.

Here is what Freemius recommends for testing the functionality and integration:

## Setting Freemius into Development Mode[​](#setting-freemius-into-development-mode "Direct link to Setting Freemius into Development Mode")

During development and testing, add the following constant to your testing environment's `wp-config.php` file to display the **Freemius Debug** menu item.

```php
/* Set Freemius into development mode */
define( 'WP_FS__DEV_MODE', true );
```

tip

These definitions are added under the **WordPress debugging mode** section before the *WordPress Engine* starts, i.e. before `/* That is all, stop editing! Happy blogging. */` comment.

When you refresh the WP Admin, you should notice a new top-level menu item. If you click it, you will be able to see all the Freemius data associated with your local environment.

Important Warning

Activating development mode also sets the SDK for debugging, which, among other things, will turn the SDK's logging system on:

- Logs are stored in the DB, so activating logging on a highly-active production site can quickly fill up the DB storage.
- Logs are also printed out to the console log, so if a highly-active site utilizes a filesystem caching plugin while running in debug mode, the site’s disk may fill up quickly.

Therefore, do not forget to turn development mode off after completing troubleshooting.

## Testing User Opt-in[​](#testing-user-opt-in "Direct link to Testing User Opt-in")

The [opt-in screen](help-documentation-wordpress-sdk-opt-in-message.md) appears only during product activation.

After opting in or skipping the process, the screen will not appear again.

### Reset Opt-in after Opting in[​](#reset-opt-in-after-opting-in "Direct link to Reset Opt-in after Opting in")

To display the opt-in screen after opting in initially, you will need to [delete the installation from Freemius](help-documentation-wordpress-sdk-wp-admin-account.md#deactivate-a-license-from-the-website) under the **Account** submenu item.

### Reset Opt-in after Skipping[​](#reset-opt-in-after-skipping "Direct link to Reset Opt-in after Skipping")

To display the opt-in screen after skipping it initially, follow these steps:

1. Enable the [Freemius debugging](help-documentation-wordpress-sdk-debugging.md) page.
2. Then clear Freemius data in the admin dashboard by selecting the **Delete All Accounts** button.

## Skipping Email Activation[​](#skipping-email-activation "Direct link to Skipping Email Activation")

For security and data integrity reasons, if an already opted-in user attempts to opt in to Freemius again, you will first receive an activation email to complete the process. This helps prevent users from hijacking other user accounts.

However, this step might slow down the development and testing process. To skip it, add the following constant to your testing environment's `wp-config.php` file in addition to the previously added constants:

```php
/* Skip email activation when a user with the same email already opted-in */
define( 'WP_FS__SKIP_EMAIL_ACTIVATION', true );
```

## Sandbox Payments[​](#sandbox-payments "Direct link to Sandbox Payments")

The Freemius WordPress SDK embeds a full checkout system that allows you to monetize your products via the **Upgrade** or pricing page. This checkout process can be fully tested in a sandbox environment before going live.

To set Freemius Checkout to sandbox payment mode, make sure your `wp-config.php` file contains the following constant with your secret key:

```php
/* Set Freemius into development mode */
define( 'WP_FS__DEV_MODE', true );

/*
 * Set your plugin / theme Freemius secret key for super powers!
 *   1. Replace `my-slug` with your product's lowercase slug.
 *   2. Replace `sk_mySecretKey` with your product's secret key.
 */
define( 'WP_FS__my-slug_SECRET_KEY', 'sk_mySecretKey' );
```

With this setup, choose the desired plan from the pricing page. When the Checkout appears, complete the payment using these [credit cards](help-documentation-checkout-integration-testing.md#testing-credit-cards) and [PayPal](help-documentation-checkout-integration-testing.md#testing-paypal-accounts) accounts in sandbox mode.