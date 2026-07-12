---
title: "Selling Bundles & Memberships"
url: "https://freemius.com/help/documentation/wordpress/selling-bundles-and-memberships/"
source: "docs"
section: "Docs"
category: "Setup for WordPress"
scraped_at: "2026-04-09T19:58:45+06:00"
word_count: 708
---

## Bundle vs Membership: What is the difference?[​](#bundle-vs-membership-what-is-the-difference "Direct link to Bundle vs Membership: What is the difference?")

A **bundle** license grants access only to the specific products that were included in the bundle at the time of purchase. If the product maker adds new products to the bundle later, the original license will not cover those additions.

While a **membership** license is more dynamic and allows ongoing access. If the maker adds new products to the membership, existing licenses automatically gain access to these products. This model supports a continuously evolving product offering under a single license.

## Create a bundle “product” on Freemius[​](#create-a-bundle-product-on-freemius "Direct link to Create a bundle “product” on Freemius")

To showcase how you can start selling bundles, let’s assume that you have:

A freemium Core Plugin called **Freemius Starter Bundle** with 2 paid plans (Starter: $100 per year; Professional: $150 per year), and two add-ons:

- **Catwalk Addon 1** - a freemium add-on with one Pro plan for $50 per year.
- **Catwalk Addon 2** - a premium only add-on for $50 per year.

For a customer to access **Freemius Starter Bundle** Starter plan with the 2 paid add-on versions, the total annual price would be $200 per year. However, we can create a bundle of all the products together for $150 (a $50 / 25% discount).

### The process[​](#the-process "Direct link to The process")

Click the **Add product / bundle** button in the top left section under ***Products***:

Switch the product type to **Bundle**

Enter your bundle’s title (e.g. *Starter Bundle*), optionally upload a featured icon and hit the **Get Started** button:

You’ll be automatically redirected to the bundle Product’s page.

Click the **Go to Products** button or click the ***Products*** button on the left hand menu section.

Click the **Add Product** button and choose the addon products to add to the bundle:

Your browser does not support the video tag.

tip

Every bundle can have multiple plans and can include a subset of products.

Once all the products are added, the ***Products*** page should look like this:

Next, go to the ***Plans*** page to set the bundle's plans and prices (just like you would for a plugin or a theme):

The next step would be choosing which products and their plans to include in the bundle’s plan:

Finally, let’s set the plan’s price to $200 per year, as we originally intended:

That’s it! The bundle is ready for sale. Set up a [checkout link](help-documentation-getting-started-making-your-first-sale.md#hosted-checkout) any website or use the [Buy Button JavaScript API](help-documentation-checkout-integration-freemius-checkout-buy-button.md).

## Configuring a Membership[​](#configuring-a-membership "Direct link to Configuring a Membership")

As explained in the [first part](#bundle-vs-membership-what-is-the-difference) of this documentation, you can include future software products in your bundle. Any existing subscriptions or licenses will automatically gain access to these products, regardless of when they were purchased.

This configuration is applied per plan within your bundle, offering greater flexibility in how you structure plans and pricing.

To enable this, go to the desired plan and select the **Membership** option:

## Selling Bundles from the WP Admin Dashboard[​](#selling-bundles-from-the-wp-admin-dashboard "Direct link to Selling Bundles from the WP Admin Dashboard")

Integrating with [Freemius WordPress SDK](help-documentation-wordpress-sdk-integrating-freemius-sdk.md) will automatically include a pricing page within the WP Admin of your users. By default, the rendered pricing page is associated with the plugin or theme the SDK integrated with.

Suppose you're using the add-ons architecture and selling bundles/memberships to your add-ons collection. In that case, it's highly recommended to configure the SDK to render the pricing of your bundle/membership.

You can easily achieve that by setting the `'bundle_id'` and `'bundle_public_key'` arguments in the SDK integration snippet. You can learn more about these parameters and `'bundle_license_auto_activation'` [here](help-documentation-wordpress-sdk-integrating-freemius-sdk.md).

When a bundle is configured, it replaces the upgrade pricing view with the bundle pricing. You can either show the premium core product pricing options or bundles, but not both at the same time.

If your core plugin/theme is free, make sure to add the core free product in the bundle's *Products* section and update the SDK integration snippet by setting the value of `'has_paid_plans'` to `true` for the pricing page to show up.

tip

You can save customers the hassle of manually activating a bundle license for every add-on by adding `'bundle_license_auto_activation' => true,` to your SDK integration snippet.