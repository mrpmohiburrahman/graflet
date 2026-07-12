---
title: "Software Updates and Distribution"
url: "https://freemius.com/help/documentation/wordpress/software-updates-distribution/"
source: "docs"
section: "Docs"
category: "Setup for WordPress"
scraped_at: "2026-04-09T19:58:46+06:00"
word_count: 334
---

The [WordPress SDK](help-documentation-wordpress-sdk.md) includes a complete software updates mechanism out-of-the-box, and is integrated with the [Software Licensing](help-documentation-wordpress-sdk-software-licensing.md) engine, and the rest of Freemius suite of products.

warning

The software updates mechanism is only included for paid plugins and themes. Freemius doesn't support free products distribution, for now.

The auto updates mechanism is seamlessly integrated with the WP Core updates mechanism, but can only work when the product, plugin or theme, is actually active (otherwise, the custom code can't be executed).

## Who Is Eligible for Software Updates?[​](#who-is-eligible-for-software-updates "Direct link to Who Is Eligible for Software Updates?")

Only users who are within a trial period, or customers holding a valid (and non-expired) license, activated on the WordPress site in context, will get access to premium software updates.

## Software Updates in a Multisite Network Environment[​](#software-updates-in-a-multisite-network-environment "Direct link to Software Updates in a Multisite Network Environment")

Since the updates mechanism only works when the product is active - if the plugin or theme is active on a single site in a multisite network - only that site can execute the updates logic. However, since the updates mechanism is in a network environment, it's only triggered in the network admin scope. The updates mechanism will not work just by checking for updates in the network admin.

So, to get updates on that specific use-case, you must follow these steps:

1. Open the WP Admin of the site where the product is active.
2. Navigate to the product's *Account* page.
3. If you're eligible for updates and there's a pending update, you will see the `Install Update Now [<version>]` button. You can click that button to perform an immediate update.
   
   note
   
   Only a super-admin can update plugins and themes in a network environment.
4. After visiting the *Account* page, the network updates transient/cache will be updated with the required data for the product's update.
5. At this point, if you visit **WP Network Admin → Dashboard → Updates**, or the network plugins page, the update should be available.