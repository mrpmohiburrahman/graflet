---
title: "Known License Activation Issues"
url: "https://freemius.com/help/documentation/wordpress-sdk/license-activation-issues/"
source: "docs"
section: "Docs"
category: "WordPress SDK"
scraped_at: "2026-04-09T19:58:44+06:00"
word_count: 769
---

In some cases, a license activation can fail unexpectedly without showing any errors.

Typical symptoms:

- The license activation page refreshes without anything happening.
- The *Activate* button gets "stuck," and nothing happens.
- The license remains activated on a site that is no longer accessible, and the activations limit is reached.

Here are the most common cases in which this happens, including how to work around the issues:

## 1. License Activations Limit Reached[​](#1-license-activations-limit-reached "Direct link to 1. License Activations Limit Reached")

The issue typically arises when a website instance is deleted or becomes inaccessible without the license being deactivated through the standard process, or when the license is already activated on another site.

### Solution[​](#solution "Direct link to Solution")

#### Have WordPress Site Access[​](#have-wordpress-site-access "Direct link to Have WordPress Site Access")

If you have access to the WordPress site’s `Account` page for the relevant plugin/theme, navigate to it and click the `Deactivate License` link. After that, you can activate the license on another site.

Give Your Customers More Control

Additionally, you can ask your customers to restrict the sites that have access to the license by whitelisting those from the self-service [Customer Portal](help-documentation-users-account-management-license-security.md#url-whitelisting-aka-license-firewall).

#### No WordPress Site Access (Single-Site License)[​](#no-wordpress-site-access-single-site-license "Direct link to No WordPress Site Access (Single-Site License)")

If you no longer have access to the WordPress site and your license is for a single site, follow these steps:

- Log in to the [Customer Portal](https://customers.freemius.com/).
- Navigate to the `Licenses` section (beneath the `Websites` menu item).
- Click the `Deactivate` button.

#### No WordPress Site Access (Multi-Site License)[​](#no-wordpress-site-access-multi-site-license "Direct link to No WordPress Site Access (Multi-Site License)")

If you no longer have access to the WordPress site and your license supports multiple site activations, follow these steps:

- Log in to the [Customer Portal](https://customers.freemius.com/).
- Navigate to the `Websites` section.
- Find the relevant site (you can check the domain).
- Click on it to open its details panel.
- Scroll down to find the license section and click the `Deactivate` button.

## 2. ISP Blockage[​](#2-isp-blockage "Direct link to 2. ISP Blockage")

We noticed that some ISPs, especially in Turkey and Russia, are often blocking websites that utilize Cloudflare, which can block connectivity to our API servers.

### Solution[​](#solution-1 "Direct link to Solution")

You can activate the license using a proxy by following these simple steps:

1. Go to [us-proxy.org](https://www.us-proxy.org/)
2. Get the 1st proxy details available and add the following code to the `functions.php` of the currently active theme:

```php
add_action('http_api_curl', function( $handle ){
    curl_setopt($handle, CURLOPT_PROXY, "REPLACE_ME_WITH_PROXY_IP");
    curl_setopt($handle, CURLOPT_PROXYPORT, REPLACE_ME_WITH_PROXY_PORT);
}, 10);
```

3. After a successful license-activation, comment out the newly added lines of code to avoid running future cURL requests through a proxy.

## 3. Caching Layer Issue[​](#3-caching-layer-issue "Direct link to 3. Caching Layer Issue")

For performance reasons, many in-memory caching solutions like Memcached or Redis require setting a Byte-limit to the values they store, and to optimize performance, all Freemius settings are stored in a single record in the `wp_options` table, which means that if the length of the settings is greater than the configured limit, it may cause one of the following unexpected behaviors:

- The settings won't be stored at all
- The settings will fail to properly load
- The settings will be stored incompletely, causing data corruption

This will prevent the settings from properly propagating to (or from) the Database.

### Solution[​](#solution-2 "Direct link to Solution")

Try to temporarily disable the caching layer just for the license activation process.

## 4. Database Encoding Issue[​](#4-database-encoding-issue "Direct link to 4. Database Encoding Issue")

In some cases, we noticed that misconfigured encoding of the `option_value` column in the `wp_options` table could fail to store the required data after license activation. E.g. - Even though the license gets properly activated, WordPress may not “remember” it. Typically this happens when there are any UTF-8 or UTF-16 characters in the license owner's name or address.

### Solution[​](#solution-3 "Direct link to Solution")

Try changing the encoding of the `option_value` column in the `wp_options` table to UTF-8 (or UTF-16) and then try activating the license again.

## 5. Security Layer Blockage[​](#5-security-layer-blockage "Direct link to 5. Security Layer Blockage")

Freemius’ license key generator randomly creates 32-char keys using alphanumeric characters and some special characters for enhanced security. We noticed that some security plugins/layers/modules (e.g., ModSecurity) might block a license activation process if the combination of the license’s special characters “look” suspicious.

### Solution[​](#solution-4 "Direct link to Solution")

Try to temporarily disable any security plugins/layers/modules you have just for the license activation process. After the license is activated, make sure to reactivate the security components you disabled.