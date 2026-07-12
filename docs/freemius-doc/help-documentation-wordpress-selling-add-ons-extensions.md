---
title: "Selling Add-Ons / Extensions"
url: "https://freemius.com/help/documentation/wordpress/selling-add-ons-extensions/"
source: "docs"
section: "Docs"
category: "Setup for WordPress"
scraped_at: "2026-04-09T19:58:45+06:00"
word_count: 926
---

Historically, many WordPress developers chose to monetize with the add-ons/extensions freemium business model, trying to replicate the success of popular products like WooCommerce.

In most cases, the add-ons model is actually not a good fit and we are seeing a market shift towards plans and add-on bundles (similar to plans). Therefore, if you are just starting out, don’t rush into add-ons only because you see others doing it. Be certain it makes sense for your product first.

tip

We wrote an in-depth article "[Premium vs. Add-ons - Which is the best monetization model for your plugin?](blog-premium-vs-add-ons-which-is-the-best-monetization-model-for-your-wordpress-plugin.md)" that will give you a solid insight before you make your decision. If you’d like to see an example of a plugin that sells add-ons, check out [RatingWidget](https://wordpress.org/plugins/rating-widget/).

## How to Sell Add-Ons with Freemius?[​](#how-to-sell-add-ons-with-freemius "Direct link to How to Sell Add-Ons with Freemius?")

Freemius fully supports the add-ons business model, and the integration only takes a few minutes. You can sell add-ons for plugins and themes.

tip

Freemius also supports [selling bundles](help-documentation-wordpress-selling-bundles-and-memberships.md) which is particularly useful when selling add-ons.

1. Login to your [Freemius dashboard](https://dashboard.freemius.com/).
2. If you already created your “parent” product on Freemius, skip to #4. If not, create your “parent” plugin or theme by clicking the **Add product / bundle** button on the left side nav:
3. Follow the instructions to complete the “parent” product creation. (We will integrate the SDK later).
4. In the “parent” product menu, click on the ***Add Ons*** menu item:
5. Click the **Create Add-On** button and fill in all the required details
6. Click the **Get Started** button. This will create the add-on product.
7. Unlike in your parent product, you’ll need to add some marketing material like: description, selling points, screenshots, and visual banners. These can be added via the ***Settings*** of the add-on product.
8. After you fill up the marketing related material, head over to the add-on ***Plans*** and create your plans, pricing, and features list:
   
   You can price your plans based on monthly, annual, as well as lifetime prices (we recommend using all of them). Here are some well researched and helpful articles if you’re not experienced with pricing:
   
   - [Careful! This Simple Pricing Experiment Cost Us $2,000 in Revenue](blog-wordpress-plugin-monthly-pricing-experiment.md)
   - [Lifetime license for WordPress plugins – the right way!](blog-lifetime-license-for-wordpress-plugins-the-right-way.md)
   
   You can also leverage our [trials functionality](help-documentation-wordpress-free-trials.md) to offer potential customers to try out your add-on before committing.

## Preparing the Add-On for Sale[​](#preparing-the-add-on-for-sale "Direct link to Preparing the Add-On for Sale")

To ensure your add-on is ready for sale in production, verify the following:

1. Under the **Plans** page of the add-on, the "Release plans to users" toggle is turned on.
2. Under the **Settings** page of the add-on, the "Show add-on in the WP Admin Add-Ons marketplace" toggle is turned on.

While you're developing and testing the add-on, you can keep these toggles off and put the SDK in [testing mode](help-documentation-wordpress-sdk-testing.md) until you are ready to go live.

tip

If your "parent" product is already in the wild, we recommend disabling the add-on until the code has been deployed and you are ready to sell the product. For this you can just turn off the "Show add-on in the WP Admin Add-Ons marketplace" toggle in the add-on settings.

## Selling Add-Ons from Your Website[​](#selling-add-ons-from-your-website "Direct link to Selling Add-Ons from Your Website")

Selling the add-on from your site is a piece of cake.

- Go back to the ***Plans*** page, and click on **Get Checkout Code** the button to get the checkout JavaScript snippet:
- Copy the code and paste it into the add-on’s marketing page source on your site, and you are pretty much ready to go.

## Selling Add-Ons from within the WP Admin Dashboard[​](#selling-add-ons-from-within-the-wp-admin-dashboard "Direct link to Selling Add-Ons from within the WP Admin Dashboard")

Now it’s time to integrate!

1. Switch back to your parent product’s context, and go to the ***SDK Integration*** section:
2. Follow the [SDK integration](help-documentation-wordpress-integration-with-sdk.md) process carefully, step by step. If you already integrated Freemius into the parent product, you’ll need to update the generated SDK snippet (you'll notice a new flag named `has_addons` added). Copy the new snippet and replace the one you’ve integrated previously.
3. To verify the new snippet, install the plugin or theme on your development environment, and check if a new submenu item is added under your product’s menu item:
4. Clicking on the “Add Ons” menu item in your testing environment should show a mini-marketplace with all the product’s add-ons and you should already be able to test the purchase process
5. After validating the parent’s product integration, it’s time to integrate the SDK with your add-on. Switch the context to the add-on by clicking on the **Products** tab under the Freemius logo and select the add-on by name. Then, go to the ***SDK Integration***, and follow the integration steps.
6. When your add-on is ready for production, deploy it via the ***Deployment*** section.
7. And when you are ready to show the add-ons marketplace to your users simply release a new version of the plugin/theme with the updated SDK integration snippet.

tip

Whenever you want to release a new add-on just create it in the dashboard as described and it will appear automatically in the add-ons marketplace inside the admin dashboard. There is no need to update the parent product to make changes in the add-ons collection.

note

The in-dashboard add-ons marketplace has a 24-hours caching while running in production. Therefore, if you release a new add-on, it may take up to 24-hours until your users see it live.