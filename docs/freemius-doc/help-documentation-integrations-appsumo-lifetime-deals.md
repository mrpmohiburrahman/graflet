---
title: "AppSumo & Lifetime Deals"
url: "https://freemius.com/help/documentation/integrations/appsumo-lifetime-deals/"
source: "docs"
section: "Docs"
category: "3rd Party Integrations"
scraped_at: "2026-04-09T19:58:38+06:00"
word_count: 676
---

Before you get started with AppSumo or any similar LTD (Lifetime Deal) partners, we highly recommend reading [this in-depth article](https://freemius.com/blog/appsumo-lifetime-deals-selling-plugins/index.md). It will guide you through the pros and cons of running an LTD, as well as the nitty-gritty unit economics shared by Puneet on his experience running a deal with AppSumo. If you are considering selling on the *AppSumo Marketplace*, [check out Nicole's experience](blog-appsumo-marketplace-plugin-developers.md) with her plugin, Studiocart.

## Do I need to share any revenue with Freemius when running a LTD through AppSumo?[​](#do-i-need-to-share-any-revenue-with-freemius-when-running-a-ltd-through-appsumo "Direct link to Do I need to share any revenue with Freemius when running a LTD through AppSumo?")

First, it's important to understand that whether a transaction is processed through Freemius or not, the product licenses still need to be managed for activations, deactivations, etc. If you for example sell 10,000-lifetime licenses, we'll need to support 10,000 customers of yours forever both on the resource side of things and support when necessary.

Since we don't have usage-based pricing yet and need to cover our expenses, a 7% revenue share applies to your gross sales after deducting the LTD partner commission.

For example, if you sell a redemption code for $30 and AppSumo takes a 70% commission, your gross revenue is $9, and our revenue share would be $0.63.

Considering that these deals are already heavily discounted and structured for lifetime commitments, we typically lose rather than make money in these cases. With the context of the $30 license example, even if we end up with one support ticket per ~60 licenses you sell, we still lose money on support resources (not even counting the computing, storage, and bandwidth costs).

The only reason we handle LTDs not transacted through Freemius is their potential value for your business growth and reputation. As your monetization partner, we want to support this need.

## How to run an LTD while selling through Freemius?[​](#how-to-run-an-ltd-while-selling-through-freemius "Direct link to How to run an LTD while selling through Freemius?")

Most LTD-focused websites will require you to send them a list of “Redemption codes”. When a customer purchases from AppSumo, they actually buy a redemption code they can use in order to get access to the paid plugin or theme and premium license key.

There are several approaches to handling this with Freemius.

Our first recommendation is to generate bulk license keys using our [PHP SDK](https://github.com/Freemius/freemius-php-sdk) then send these to your LTD partner as redemption codes.

note

The benefit of this approach over using coupons is that it avoids storing multiple unnecessary coupon records, since licenses will be needed eventually.

Your API permissions need to be elevated to generate bulk licenses and your IP needs to be whitelisted to avoid any unexpected rate-limit restrictions. After you agree to our terms of sale, we will manually adjust the settings on our end and send you a PHP snippet to generate bulk licenses.

In order for buyers to redeem their codes, you'll need to create a redemption page on your website. You need to collect their name, email, and redemption code (license key) and optionally collect the user's consent for promotional offers. If you do, we recommend adding a an opt-in checkbox with the following label: **"Send me security & feature updates, educational content and offers."**

Here's a short snippet that showcases the backend implementation of a license redemption using the API:

```php
<?php
    $license = $api->Api("/plugins/{$plugin_id}/licenses.json", 'PUT', array(
        'license_key'          => urlencode($license_key),
        'email'                => $email,
        'name'                 => $name
        'is_marketing_allowed' => $is_marketing_allowed,
    ));

    if (is_object($license) && !empty($license->user_id) && is_numeric($license->user_id)) {
        // Successful activation, email sent. Redirect the user to the success page or show some message.
    } else if (!empty($license->error)) {
        $error = $license->error->message;
    } else {
        // Unexpected message.
    }
```

tip

If you prefer to use a ready-made solution, our awesome partners at [Stackable](https://wpstackable.com/) created [this nifty little plugin](https://github.com/gambitph/Freemius-x-AppSumo-Redemption-Page) that adds a complete redemption page for AppSumo Codes for Freemius.

[](https://github.com/gambitph/Freemius-x-AppSumo-Redemption-Page)

Upon successful redemption, the redeemed license is associated with the buyer's details, and the buyer will receive an email message with their secure download link, license key, and account login information: