---
title: "Single Sign-On for WordPress"
url: "https://freemius.com/help/documentation/users-account-management/sso-single-sign-on-wordpress/"
source: "docs"
section: "Docs"
category: "Customer Portal"
scraped_at: "2026-04-09T19:58:44+06:00"
word_count: 481
---

If you are using WordPress to power your website and like to allow users and customers to login to your WordPress with their Freemius credentials, you can use our official [Single Sign-On WordPress Plugin](https://github.com/Freemius/freemius-wordpress-sso).

This plugin bridges the gap between WordPress and the Freemius API. When a user logs in with their Freemius credentials and there is no matching user in WordPress, a new user with the same email address and password will be created in WordPress.

When [embedding the Customer Portal](help-documentation-users-account-management.md) on your site using our [Customer Portal WordPress plugin](https://github.com/Freemius/freemius-users-dashboard), a logged-in user will be automatically logged into their Freemius Customer Portal without the need to log in again. This structure offers a much better user experience to your users.

## Enabling SSO for WordPress[​](#enabling-sso-for-wordpress "Direct link to Enabling SSO for WordPress")

1. Download the plugin from [GitHub](https://github.com/Freemius/freemius-wordpress-sso/archive/refs/heads/master.zip).
2. Open your WordPress installation's `wp-config.php` file and add the following lines at the end, replacing the placeholders with your actual credentials:
   
   ```php
   define( 'FREEMIUS_STORE_ID', '<STORE_ID>' );
   define( 'FREEMIUS_DEVELOPER_ID', '<DEVELOPER_ID>' );
   define( 'FREEMIUS_SECRET_KEY', '<DEVELOPER_SECRET_KEY>' );
   ```
   
   Access the required credentials
   
   Via the [Freemius Developer Dashboard](https://dashboard.freemius.com/), under the:
   
   - **My Profile** page, get your `developer ID` and `secret key`.
   - **Store** → **Settings** page, get your `store ID`.
3. Upload and activate the plugin.
4. Done! Users will be able to login with their Freemius credentials and your local WP users will be automatically logged in to Freemius without needing to log in again.

## How to restrict content from non-paying customers?[​](#how-to-restrict-content-from-non-paying-customers "Direct link to How to restrict content from non-paying customers?")

The SSO (Single Sign-On) plugin comes with several handy methods to easily allow you control the logic according to the user's state on Freemius.

For example, if you have a contact form page or a forum, which you wish to restrict from users but show it to your customers, you can create a [page template](https://developer.wordpress.org/themes/template-files-section/page-template-files/) that will render different content according to the user's licenses on Freemius as follows:

```php
<?php
/**
 * Template Name: Support Page Template
 */
$is_logged_in           = false;
$has_any_license        = false;
$has_any_active_license = false;

if ( is_user_logged_in() ) {
    // User currently logged in.
    $is_logged_in = true;

    if ( class_exists( 'FS_SSO' ) ) {
        // Freemius SSO plugin is installed and running.
        $sso = FS_SSO::instance();

        $has_any_license  = $sso->get_freemius_has_any_license();

        $has_any_active_license  = $sso->get_freemius_has_any_active_license();
    }
} ?>

<?php get_header(); ?>

<?php if ( ! $is_logged_in ) : ?>
    <p>Whatever you want to show when the user is not logged in.</p>
<?php elseif ( $has_any_license ) : ?>
    <p>User logged in and has at least one license on Freemius.</p>
<?php elseif ( $has_any_active_license ) : ?>
    <p>User logged in and has at least one ACTIVE license on Freemius.</p>
<?php else : ?>
    <p>Whatever you want to show when the user is logged in but does not have any licenses for your product on Freemius.</p>
<?php endif; ?>

<?php get_footer(); ?>
```