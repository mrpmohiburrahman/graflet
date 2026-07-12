---
title: "Embed the Freemius Customer Portal into your website"
url: "https://freemius.com/help/documentation/users-account-management/embedding-customer-portal/"
source: "docs"
section: "Docs"
category: "Customer Portal"
scraped_at: "2026-04-09T19:58:44+06:00"
word_count: 740
---

You can provide your customers with easy access to their accounts by either adding a direct link to the Customer Portal on your website or embedding it directly into your site.

## Adding a Link on Your Store[​](#adding-a-link-on-your-store "Direct link to Adding a Link on Your Store")

If you have a website, we recommend adding a direct link to the portal to make it easier for your customers to access their account. The Customer Portal URL takes the structure below:

```text
https://customers.freemius.com/store/<storeID>
```

Where `<storeID>` is your unique store identifier. Here are the steps to find your **Store ID** in the [Store's settings](#find-store-id--public-key).

## Embedding the Customer Portal in Your Store[​](#embedding-the-customer-portal-in-your-store "Direct link to Embedding the Customer Portal in Your Store")

Alternatively, you can embed the portal directly on your site. The customer portal has been designed to work for this exact use case, keeping users on your store and making the portal feel native to your site.

### Find Store ID & Public Key[​](#find-store-id--public-key "Direct link to Find Store ID & Public Key")

You will need your store ID and public key to embed the portal.

1. Log into your [Freemius Developer dashboard](https://dashboard.freemius.com/).
2. Navigate to your store by clicking **Stores** in the top-left panel under the Freemius logo.
3. Select your store by name.
4. Scroll down the menu and select the **Settings** page.
5. Under the **API & Keys** sub-page, you will find your store ID and public key.

### Embedding Into a WordPress Website[​](#embedding-into-a-wordpress-website "Direct link to Embedding Into a WordPress Website")

1. Install and activate [Freemius Customer Portal WordPress Plugin](https://github.com/Freemius/freemius-users-dashboard/).
2. Create a new page on your website. We recommend using one of the following slugs: `users`, `account`, `members`. Save the page's link to be used in step 4.
3. In your [Freemius Developer account](https://dashboard.freemius.com/), navigate to your store by clicking **Stores** in the top-left panel under the Freemius logo.
4. Select your store by name.
5. Scroll down the menu and select the **Settings** page.
6. Under the Customer Portal sub-page, scroll to the **Embed on your Website** section.
7. In the *Customer Portal URL* setting field, paste the URL address of the page created (in step 2). Make sure the protocol (HTTP or HTTPS) is accurate, otherwise, the portal will not load.
8. Add this shortcode to the page you created:
   
   ```text
   [fs_members store_id="<storeID>" public_key="<storePublicKey>" position="fixed" left="0" right="0" top="<headerHeight>px" bottom="0"]
   ```
9. Replace the following placeholders in the shortcode with your information that we obtained in the [previous steps](#find-store-id--public-key):
   
   - `<storeID>` - with your store ID.
   - `<storePublicKey>` - with your store's public key.
   - `<headerHeight>` - with your site's header height.

Responsive Header Height

If your site’s header height is responsive, you can customize the dashboard’s position with media queries by styling the iframe’s `<div id="fs_dashboard_container">` container as follows:

```css
#fs_dashboard_container {
   top: {headerDesktopHeight}px;
}

@media screen and(max-width: 600px) {
   #fs_dashboard_container {
      top: {headerMobileHeight}px;
   }
}
```

### Disabling Redirect to WordPress Login Page[​](#disabling-redirect-to-wordpress-login-page "Direct link to Disabling Redirect to WordPress Login Page")

Users might be redirected to the default WordPress login page when they log out of the embedded Customer Portal. To disable this behavior, add the following code snippet to the bottom of your active theme's `functions.php` file:

```php
function my_fs_members_dashboard_config( $config ) {
    $config = str_replace( 'window.location.href', '// window.location.href', $config );
    return $config;
}

add_filter( 'fs_members_dashboard', 'my_fs_members_dashboard_config' );
```

### Support For Multiple Domains[​](#support-for-multiple-domains "Direct link to Support For Multiple Domains")

For security purposes, the portal will not load unless it is embedded on the domain specified in the Freemius Developer Dashboard.

However, there are cases where you may want to allow the portal to be embedded on multiple domains, for example, if you have a staging environment or a local development environment.

To set up, follow these steps:

1. Log into your [Freemius Developer dashboard](https://dashboard.freemius.com/).
2. Navigate to your store by clicking **Stores** in the top-left panel under the Freemius logo.
3. Select your store by name.
4. Scroll down the menu and select the **Settings** page.
5. Under the Customer Portal sub-page, scroll to the **Embed on your Website** section.
6. Add your additional domains in the **Additional Whitelisted Domains** configuration.
7. Click the **Add** button to save the additional domain.

## Customizing the Customer Portal Appearance[​](#customizing-the-customer-portal-appearance "Direct link to Customizing the Customer Portal Appearance")

For the Customer Portal to match your website and brand look, find up-to-date instructions on [customizing the Customer Portal appearance with CSS](help-documentation-users-account-management-applying-css-customization.md).