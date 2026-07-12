We’re always exploring new ways to enhance the software-selling experience for makers and their users. These new Freemius release notes mark an exciting milestone as we begin expanding our support beyond plugins and themes, bringing new and advanced capabilities for SaaS and other software types.

With a strong focus on developer experience (DX), we’ve rolled out updates that make integration easier, workflows smoother, and scaling more accessible.

These features and improvements highlight how we’re making Freemius even better for **all** software makers, starting with:

## Helping Users Blaze (a Clear Paper) Trail by Automatically CC’ing Billing Addresses

We’ve made it simple for buyers to automatically CC payment-related emails — like subscriptions, payments, refunds, and cancellations — to a billing-specific email address.

![User billing on the Freemius User Dashboard](https://freemius.com/blog/wp-content/uploads/2024/10/user-billing-on-the-freemius-user-dashboard.png)

Customers no longer have to deep-dive into their inboxes to manually forward emails to accountants/bookkeepers or set up rules that often pose security concerns for larger companies (and are usually not allowed).

They can now simply add a billing email from the [Customer Portal](wordpress-user-dashboard.md) to avoid the hassle of lost or forgotten invoices, end-of-year scrambling, and tedious forwarding.

Here’s who wins:

- Users in larger organizations where the purchaser is often not responsible for the finances
- Freelancers or small businesses who work with external accountants or bookkeepers
- Any software maker tired of manually forwarding payment-related emails

Best of all? Not many alternative solutions offer this feature, so you get an edge over competitors while delivering a great user experience that builds confidence and loyalty.

[More info here](blog-changelog-ccing-payment-emails-to-user-billing-address.md).

## “One Click” Payments and Subscriptions Data Export

Even though we offer some of the most advanced and granular analytics available, we don’t cover or surface every possible metric “out of the box” as it’s not part of our core business.

Until recently, software makers who needed data not shown in our dashboard had to export it using the API. This was a challenge for those without technical skills or the time to write the necessary code.

Good news — the next evolution of our [Data Liberation Project](blog-changelog-enhancements-to-the-users-export-from-the-developer-dashboard.md) will satisfy the number crunchers out there. With the click of a button, software makers can now easily export [payments](blog-changelog-introducing-new-feature-to-export-payments.md) and [subscriptions](blog-changelog-data-export-now-available-for-subscriptions.md) data as CSV files for custom analyses that reveal deeper insights into product performance, user behavior, and financial metrics. Did we mention there’s no coding required?

![Freemius subscriptions data one-click export](https://freemius.com/blog/wp-content/uploads/2024/10/freemius-subscriptions-data-one-click-export.png)

![Freemius payments data one-click export](https://freemius.com/blog/wp-content/uploads/2024/10/freemius-payments-data-one-click-export.png)

More good news: Our “one-click” feature has other benefits that go beyond granular data details:

**Business sales and acquisitions:** Freemius offers a wide range of analytics that cover most of the day-to-day needs of software makers. However, there are times when additional data is needed, like when trying to sell your business.

Potential acquirers may request specific metrics not directly available from our dashboards. As these data points can directly impact the final purchase price, it’s crucial for makers to deep-dive into their data to unearth the requested metrics.

**Migration:** In cases where makers decide that Freemius isn’t the right fit, or if they sell their business to a new entity with its own processes and systems, the ability to easily export all essential data — like users, websites, licenses, and payments — is key to simplifying the migration process.

You may be wondering why we’re promoting a feature that makes it easier to migrate away from Freemius…

We believe in giving makers the freedom to choose our platform because they see the value in what we offer — not because they feel locked in. If a maker decides to leave, or if they sell their business and the new owner prefers a different platform, we want the transition to be as smooth as possible.

Returning to our Data Liberation Project — the effort is ongoing and software makers will soon be able to export licenses, sites, and affiliate lists.

## WordPress SDK 2.8.0 Enhancements

Two significant updates improve the overall performance of the Freemius SDK.

**PHP 8.2 compatibility:** We addressed deprecation warnings by cleaning up outdated function calls that surfaced when running PHP 8.2. Our SDK now runs more smoothly with the latest version of PHP, offering more stability for makers’ products and a better experience for users.

**Automatic debug mode shutdown:** The Freemius SDK has a built-in debugger that, when enabled, stores logs in the WordPress database.

The problem? Sometimes, turning debug mode off is forgotten. When this happens, logs are still stored for every request in the background, increasing the size of the database pretty quickly — especially on active, high-traffic websites.

A month can go by, and then another, and suddenly the database has bloated so badly it’s causing performance issues.

Those prone to memory lapses need no longer worry. We’ve introduced a mechanism that automatically turns off debug mode after 24 hours, ensuring databases don’t balloon in the background.

**Please note:** This feature will only function if the WordPress instance has cron jobs enabled.

Other SDK bug fixes and improvements are noted [here](https://github.com/Freemius/wordpress-sdk/releases/tag/2.8.0).

## New “Vanilla” JavaScript SDK for the Freemius Checkout

For years, jQuery was the go-to JavaScript library. But as browsers and JavaScript evolved, it became unnecessary baggage in modern web development.

We started using jQuery because it was widely used in WordPress and worked well across different browsers. But as WordPress moved away from it and we now focus on more tech-driven SaaS ecosystems where faster, better tools are expected, jQuery feels outdated.

**Goodbye jQuery:** We’ve removed jQuery dependency in favor of vanilla JavaScript, which doesn’t rely on third-party libraries and comes built into the browser, making the SDK lighter, faster, and more modern.

**Faster load times:** The modal checkout script loads 60% faster, shaving off one second on average from pricing page load times, letting makers strike while the iron’s hot to increase conversion rates.

Plus, the checkout itself, modal or full page, loads 40% faster! This makes the purchase process significantly quicker once customers click “Buy”, reducing friction and ensuring transactions can be completed quickly, without losing momentum by unnecessary delays.

The JS SDK is in beta, and we’re [looking for testers](blog-changelog-new-javascript-sdk-for-freemius-checkout-calling-for-testers.md) to help identify issues, share feedback, and ensure we deliver the best possible version.

## Webhooks Authentication Support

Webhook listeners are typically publicly accessible, and someone with the URL— like an attacker with malicious intent — could send fake data that appears to be from Freemius. These harmful payloads could break or manipulate software makers’ systems by mimicking legitimate webhook events.

Previously, we asked to verify the webhook event sent by Freemius by calling the Freemius API again. While this worked, it slowed down the webhook listener unnecessarily.

From now on, and to simplify things, each event will carry an `HTTP_X_SIGNATURE` header, which you can use to validate the request without any extra API call.

The `HTTP_X_SIGNATURE` relies on the product’s secret key, which you can obtain from the “Settings” page from the Developer Dashboard.

![Getting secret key on the Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2024/10/getting-secret-key-on-the-freemius-developer-dashboard.png)

Now, verifying the authenticity of the incoming webhook is as easy as:

```
<?php

   // Retrieve the request's body payload.
   $input = @file_get_contents("php://input");
   $hash = hash_hmac('sha256', $input, '<PRODUCT_SECRET_KEY>');
   $signature = $_SERVER['HTTP_X_SIGNATURE'] ?? '';

   if ( ! hash_equals($hash, $signature))
   {
      // Invalid signature, don't expose any data to attackers.
      http_response_code(200);
      exit;
   }

   $event_json = json_decode($input);
   // Handle the event JSON as needed
```

Furthermore, the `$event_json->object` will contain most of the resources you need for your webhook listener. So you can implement the listener logic without using any SDK, relying only on the native language of your server.

This makes webhook listener implementations faster, easier, and accessible in any programming language — perfect for SaaS makers using non-PHP backends.

## Checkout Read-Only User Mode

Software makers now have the option to preload and lock the Checkout’s email field.

![Non-editable user field on the Freemius checkout](https://freemius.com/blog/wp-content/uploads/2024/10/non-editable-user-field-on-the-freemius-checkout.png)

Why is this important? Two scenarios:

**Account upgrades or payment plan changes**: Unlike downloadable software, license keys are usually not in play in SaaS, so if a user upgrades or wants to change plans, the system uses webhooks to apply the changes. If the email address used to buy doesn’t match the one used to log in or register, there could be issues with the updates and it becomes the software maker’s problem to follow up and sort things out.

**Login-based purchases**: Most SaaS and similar software have a user registration system to access the app. This means users have to log in to buy. If a user inputs a different email than the one they registered with, it can mess with post-purchase processes like account recognition, feature unlocks, or service access.

The new [Read-Only User Mode](blog-changelog-new-checkout-feature-for-saas-readonly-user-mode-bug-fix.md) forces users to complete the order using the same email tied to their account, solving both scenarios in one SaaS-friendly swoop.

## Simplified API Authentication

No matter the language, no matter the tool, we want all developers to be able to call our API with no hassle.

Up until now, makers using our official [PHP](https://github.com/Freemius/php-sdk) or [WordPress](https://github.com/Freemius/wordpress-sdk) SDKs have been enjoying this “zero fuss” experience and haven’t even had to consider generating tokens for secure communications.

Not so much for those using languages other than PHP 😔 This has led some makers to log support requests because of the tricky nuances of generating authorization signatures in other coding languages.

Obviously, we’d rather have software makers build awesome things than waste time with API payload issues, which is why we now offer:

- **Bearer authentication:** A standard method in the SaaS world, [Bearer Authentication Tokens](https://datatracker.ietf.org/doc/html/rfc6750#section-6.1.1) allow secure API calls from any programming language without relying on our SDKs or implementing complex AUTH signatures

![Freemius API Bearer token](https://freemius.com/blog/wp-content/uploads/2024/10/freemius-api-bearer-token.png)

For more info + how to put the Bearer Auth protocol into action, read our [changelog](blog-changelog-easier-api-authentication-with-bearer-auth-protocol.md).

## New Integration Guides for SaaS and License-Based Software

Not new features per se, but cool and helpful nonetheless.

We’ve added two new step-by-step guides to our knowledge base: one for integrating Freemius with SaaS products, and another for any software requiring license keys (beyond just plugins and themes).

The guides expand Freemius’ usability to almost any software, providing product makers with the tools they need to sell more effectively. They’re also key resources for new product makers looking to get started on their software-making journeys, and we’re excited to share them here:

- [**SaaS integration guide**](help-documentation-selling-with-freemius-saas-integration.md)
- [**License key activation integration guide**](help-documentation-selling-with-freemius-integrating-license-key-activation.md)

## Finland EU VAT Updates

As of September, Finland has increased its [VAT rate from 24% to 25.5%](https://freemius.com/blog/changelog/eu-finland-vat-updates/), and since we handle VAT and sales tax for software makers, we’ve updated the system to reflect the change. All subscriptions and renewals will automatically use the correct tax rate moving forward, so there’s nothing for software makers to worry about or configure.

![Finland VAT on the Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2024/10/finland-vat-on-the-freemius-checkout.png)

![Freemius Checkout Finland VAT exemption](https://freemius.com/blog/wp-content/uploads/2024/10/freemius-checkout-finland-vat-exemption.png)

This is a perfect example of the benefits of having a [Merchant of Record handle your tax burden](blog-sales-tax-on-software.md) — we’ve got your back so you can focus on your business. Keep sipping on your coffee or tea and building incredible things!

## October Release Notes: Elevating the Developer Experience and Expanding Horizons to Empower More Makers

This release marks an exciting expansion for Freemius as [we broaden our support to SaaS and other types of software beyond WordPress plugins and themes](blog-freemius-ten-year-retrospective-future-plans.md). With developer experience (DX) at the forefront, we’ve simplified key processes, making it easier than ever for makers to integrate, sell, and scale their products.

These improvements highlight our commitment to supporting a growing, more diverse ecosystem. We’re really thrilled about this evolution and look forward to empowering more makers to pursue their software passions.

If you’re interested in learning more about our new features or would like to explore a partnership with Freemius, [reach out here](https://freemius.com/cdn-cgi/l/email-protection#1e7d71706a7f7d6a5e786c7b7b73776b6d307d7173).