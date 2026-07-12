---
title: "Advanced Topics"
url: "https://freemius.com/help/documentation/getting-started/advanced-topics/"
source: "docs"
section: "Docs"
category: "Getting Started"
scraped_at: "2026-04-09T19:58:38+06:00"
word_count: 566
---

Once you've completed the integration process, you'll no doubt want to find out more about the advanced features available with Freemius.

This section covers some common advanced topics likely to be of interest.

## Updating the WordPress SDK[​](#updating-the-wordpress-sdk "Direct link to Updating the WordPress SDK")

Freemius is continuously (and rapidly) evolving with new features being added all the time. Just take a look at the WordPress SDK [release archive](https://github.com/Freemius/wordpress-sdk/releases) to see how much has been added in recent versions.

However, this means that the core Freemius WordPress SDK included with your plugin or theme will be out of date when new versions get released.

It's not always critical that you update immediately, but it's good practice to keep an eye on the release schedule and update as necessary. If there are urgent security upgrades or bug fixes, we will usually send an email suggesting you to update your product as soon as possible. You’ll want to maintain your product with the latest WordPress SDK to ensure that you and your users can take advantage of all the new features that become available.

When a new SDK version is released, you can easily update your WordPress product by swapping out the **freemius** folder with the [latest version](https://github.com/Freemius/wordpress-sdk/releases) that is always available on GitHub.

## Debugging[​](#debugging "Direct link to Debugging")

[Debugging](help-documentation-wordpress-sdk-debugging.md) is an essential part of any project, and Freemius makes it as easy as possible to identify integration issues.

To enable debugging, simply add a new constant to your WordPress config file:

`define( 'WP_FS__DEV_MODE', true );`

This adds a new **Freemius Debug** admin menu item located directly underneath the **Settings** menu in the WP Admin. Click this to go to the Freemius debug page to discover any issues going on with the SDK and/or your integration

Sometimes, issues can be solved just by clearing the Freemius API cache, which you can do via the debug page.

If you don't have debugging enabled, then you can reach this page by manually navigating to:

```text
/wp-admin/admin.php?page=freemius
```

## Freemius API[​](#freemius-api "Direct link to Freemius API")

The Developer Dashboard provides you with a comprehensive product, license, and customer management interface. However, there are still times when you might need to interact with the powerful Freemius API directly.

We've developed two dedicated SDKs to help you interact with the API more easily. You can check them out here:

- [**PHP SDK**](https://github.com/Freemius/freemius-php-sdk) - For interacting with the Freemius API via PHP.
- **[Node SDK](https://github.com/Freemius/freemius-node-sdk) (in beta)** - For interacting with the Freemius API via JavaScript / Node.

## Selling Add-ons & Extensions[​](#selling-add-ons--extensions "Direct link to Selling Add-ons & Extensions")

Freemius fully supports the selling of add-ons or extensions for core products. Please review our documentation about [Selling Add-ons / Extensions](help-documentation-wordpress-selling-add-ons-extensions.md) for details.

## Affiliate Platform[​](#affiliate-platform "Direct link to Affiliate Platform")

Setting up an [Affiliate program](https://freemius.com/blog/affiliate-program-wordpress-plugins-themes/index.md) is a great way to boost sales for your WordPress products. Freemius includes a fully featured [Affiliate Platform](help-documentation-affiliate-platform.md) out-of-the-box. There are no setup fees whatsoever, as it's all included in the Freemius revenue share [pricing](help-documentation-getting-started-our-pricing.md).

## 3rd Party Integrations[​](#3rd-party-integrations "Direct link to 3rd Party Integrations")

Freemius offers out-of-the-box [3rd party integrations](help-documentation-integrations.md) with some very useful tools such as Help Scout and Mailchimp. Other 3rd party integrations can be easily set up using Custom Webhooks with platforms like Zapier, HubSpot, customer.io, segment.io, and many other solutions.

Integrating these platforms can help take your business to the next level!