Release Notes is our periodic update that highlights the recent product improvements we’ve made, so you can easily stay up-to-date on what’s new. Here’s what we launched between April 2018 and November 2018.

During the past six months we’ve shipped many powerful new capabilities, including several essential features which many of you have been waiting for:

- Customer Portal
- Premium Changelog and Readme.txt
- Customization of the Premium Slug / Folder-Name
- The ability to offer [Free Trials](blog-trials-premium-wordpress-plugins-themes.md) without a payment method from your site

I’m not going to cover all of it, only the major releases.

We are super proud to announce our fully-featured and reactive *Embeddable Customer Portal*. Just to give you some background, our UX methodology is all about keeping things within the comfort zone of the WP Admin. Up until a few months ago, customers and users could only manage their account within their WP Admin. That was great, as long as they had the plugin or theme installed and activated on their site, but if they had to take actions, like canceling a subscription after the product has already been deactivated, this usually went through the sellers support, which added an avoidable support load. After months of planning and around 6 months of development, we have released the most advanced, reactive, responsive, and user-friendly *Customer Portal* you can find on the market. Here’s how it looks:

![Freemius Users Dashboard Downloads Section](https://freemius.com/blog/wp-content/uploads/2018/11/freemius-users-dashboard-downloads-section.png)

We are already getting an amazing feedback from our community which proves the efforts were worth it.

> The new members area has been a lifesaver in reducing the amount of support we now have to undertake. What’s more, users can self-serve 24/7 and the growing library of FAQ’s within the portal has further reduced repeat questions, so we can concentrate our resources on product development and marketing.
> 
> Jamie Marsland  
> CEO at [Pootlepress](https://pootlepress.com)

Customers and users can now manage *everything* themselves without any intervention from the seller. And when I say *everything* I mean it. They can:

- Update their personal information
- Update their billing, including business Tax/VAT ID
- See all the sites on which they installed the product in one place
- Upgrade/Downgrade their plan
- Cancel/Renew subscriptions
- Update their payment method
- Access their licenses
- See a history of their payments and easily access the invoices
- Get a real-time view of their active subscriptions and manage them
- And much more!

**Technology:** If you’re curious about the frontend technology involved, we decided to go with Angular 5 as the SPA framework, which works with ES6 and TypeScript, as well as Angular’s material design for the UI components and responsive behaviour. I know many of you are Vue.js and React fans, but the reason we decided to go with Angular is because it’s more structured and also a strongly typed framework. Also, many of us have a C# background, and the Angular framework is maintained and supported by Google. If you have experience in Angular 2+ (or C#), have [7+ years of PHP dev experience](https://freemius.com/careers/senior-php-developer/), and are looking for your next remote job opportunity – send us your CV over to [\[email protected\]](https://freemius.com/cdn-cgi/l/email-protection#167c79746556706473737b7f63653875797b). We have an exciting project that will impact the whole WP ecosystem coming up soon, and we are looking for a senior dev to lead it.

We also included an FAQ section covering the most frequent use-cases for the portal. The goal is to keep adding new questions and answers overtime, making it as self-served as possible.

![Freemius Users Dashboard FAQ Section](https://freemius.com/blog/wp-content/uploads/2018/11/freemius-users-dashboard-faq-section.png)

We also addressed two advanced, but quite common use-cases:

1. Developer & Billing Department: Larger organizations usually have a billing department which is responsible for swiping the credit card, rather than the developer who actually installs the product and sets it up.
2. Freelancers/Agency & Client: In many cases when working with agencies, the agency is responsible for maintaining the website, its plugins and themes, while delegating the payment for the premium plugins/themes to its client.

To address those use-cases, we introduced a new *Payer* persona, in addition to the *Customer* persona that we already had. So for example, when an agency needs its client to actually pay for the paid product, they can simply choose to send the upgrade link to the client:

![Freemius Users Dashboard - Send Upgrade Link](https://freemius.com/blog/wp-content/uploads/2018/11/freemius-users-dashboard-send-upgrade-link.png)

The *Payer* persona is restricted to control all the billing aspects, while keeping the ownership of the license and access to support for the agency. Moreover, all the billing related emails will be emailed to the *Payer*, while the technical emails, like how to install the paid product and its license key, will go directly to the agency (the *Customer* persona).

As far as we know, no other eCommerce solution nor marketplace addresses those use-cases for WordPress plugin and theme sellers. So we are proud to be the first and hope others will follow.

The portal can run in 2 modes: Customers can access it directly via [https://users.freemius.com](https://users.freemius.com) and it will show them all the data about all their products that are running Freemius. Alternatively, we created a special embeddable mode in which developers can easily embed the portal right on their site in the context of their store. Here’s an example of how the portal looks like in embedded mode running from [IconicWP](https://iconicwp.com):

![Freemius Users Dashboard - Embedded Mode](https://freemius.com/blog/wp-content/uploads/2018/11/freemius-users-dashboard-embedded-mode.png)

Developers can customize the look & feel by including their own custom CSS stylesheet, optionally making it aligned with your store’s design. Also, we spend quite some time on supporting deep linking, so changes in the view of the portal affect the URL of the browser and vice versa. That way, you can send links to customers which will open a specific view in the Customer Portal. As an example, the following URL links to a specified site details of the customer right in the *Customer Portal*:

`https://your-store.com/account/#!/websites/customer-site.com/(details:installs/123)`

This deep linking allows us to do many magical things 🙂 For example, in the subscription renewal reminder emails we now automatically include a direct link to the relevant subscription options in the *Customer Portal*. If you embedded the portal on your site, it will open that right on your store.

You can learn more about the portal and how to embed it on your store here:

[https://freemius.com/help/documentation/users-account-management/users-dashboard/](https://freemius.com/help/documentation/users-account-management/users-dashboard/)

## Premium Changelog and `readme.txt`

I’m pleased to share that you can now create a custom readme for your paid product version, and the new [WordPress SDK](https://github.com/freemius/wordpress-sdk) will pick that data up from our API. This was on our list for quite a while and we have finally managed to prioritize it. These are great news for premium only product owners: now you can finally show your readme’s content in the WP Admin, including changelog changes.

Like with everything we do, we try to build the best mechanism to save you time and avoid duplicate work. After some brainstorming we decided to follow the same pattern of auto-generating the readme.txt files dynamically, using special Markdown-friendly syntax. If you have a premium-only product, you are all good. Just write your readme.txt as you would. If you have a freemium plugin or theme, you’ll only need to have a single readme.txt file (yep, that’s right!), it will include all of your data. For premium-only content wrap it as follows:

```
[//]: # fs_premium_only_begin

Whatever goes in here will be only in the premium readme

[//]: # fs_premium_only_end
```

For content that should appear only in the free version, wrap it as follows:

```
[//]: # fs_free_only_begin

Whatever goes in here will be only in the free readme

[//]: # fs_free_only_end
```

Content that will not be wrapped in neither of the above will simply appear both in the free and premium readme.txt files.

Please notice that it will only work for new deployments that include the new version of the SDK. You can learn about the version deployment mechanism in general, and the new premium readme.txt support here:

[https://freemius.com/help/documentation/selling-with-freemius/deployment/](https://freemius.com/help/documentation/selling-with-freemius/deployment/)

## Custom Premium Slug / Folder-Name

Due to historical reasons, whether if you have a freemium product or a premium one, our deployment mechanism would automatically add a “-premium” suffix to the product’s folder name. This convention was essential for making the upgrade process of freemium products more user-friendly, so they could install and activate the paid product version without the need to deactivate and uninstall the free one. But this was far from optimal:

1. Premium-only products had to have a redundant “-premium” suffix in their product’s folder name.
2. Over the years, we learned that many freemium themes are using “-lite” as the suffix for their free WordPress.org slug. In those cases, the deployment mechanism would generating awkward theme folder names like “awesome-theme-lite-premium”.

Drums…

You can now fully customize your premium version folder name! And also customize the “(Premium)” suffix that we add to the premium version product’s name. You can do both in the SDK INTEGRATION section in the dashboard:

![Freemius Dashboard - Premium Slug & Suffix Customization](https://freemius.com/blog/wp-content/uploads/2018/11/freemius-dashboard-premium-slug-and-suffix-customization.png)

**IMPORTANT:**  
Please notice that the integration snippet requires an update for the custom premium slug support. Your updated code needs to look like that:

```
&amp;amp;lt;?php
    /**
     * Plugin Name: My Very Awesome Plugin
     * .....
     */

    if ( ! defined( 'ABSPATH' ) ) {
        exit;
    }

    if ( function_exists( 'my_fs' ) ) {
        my_fs()-&amp;amp;gt;set_basename( true, __FILE__ );
    } else {

        // ... Freemius integration snippet ...

        // ... my plugin's code ...

    }
?&amp;amp;gt;
```

It has to be integrated into the plugin’s main file. If you like to include it in a different file, make sure to replace the `__FILE__` with the absolute path to the plugin’s main file.

If you already have customers that are using your paid version and would like to rename it, to avoid any PHP errors during the update process, you’ll have to do it incrementally by releasing 2 new versions:

1. The 1st release should remain with the same default premium slug and will needs to include the newest SDK which comes with a special mechanism that supports folder renaming.
2. Then, customize the premium slug and release the 2nd version (minor version). Our updates mechanism will make sure that the 2nd release will only be available for users that are already using the latest SDK, the one that supports renaming.

## Dashboards Login

As a reseller of your products, in some cases, buyers visit our website and assume that our login button is for them to login to their account management. To avoid the confusion, we now offer one login for developers and another login for users/customers:

![Freemius Website Login Options](https://freemius.com/blog/wp-content/uploads/2018/11/freemius-website-login-options.gif)

## The Freemius Checkout

### Free Trials Without A Payment Method

The checkout is now officially supporting free trials without a payment method outside the WP Admin dashboard, in addition to the in-dashboard ones it supported thus far.

![Freemius Checkout - Free Trial Without Payment Method](https://freemius.com/blog/wp-content/uploads/2018/11/freemius-checkout-free-trial-without-payment-method.png)

If your plan’s configuration is set to support a trial *without* a payment method, you can trigger the checkout in both modes, with or without requiring a payment method, by setting the `trial` param to `'paid'`/`'free'` correspondingly.

If your plan’s configuration is set to only support trials *with* a payment method, you can only open the checkout in that mode.

### Manual Renewal Of An Outdated Plan

When a license is about to expire and its subscription is cancelled, Freemius will trigger a manual renewals email campaign that will include a direct link to the checkout. If the license level is no longer supported the checkout will now suggest to renew to the closest level that is available by also including a warning, letting the customer know about it:

![Freemius Checkout - License Renewal Missing Pricing Notice](https://freemius.com/blog/wp-content/uploads/2018/11/freemius-checkout-license-renewal-missing-pricing-notice.png)

This feature is essential for out methodology encouraging our partners to keep experimenting with pricing and different business models. This addition makes it safer to delete site levels you are no longer interested in supporting.

### Selling Bundles

When selling bundles, the checkout now shows the products included in the bundle: ![Freemius Checkout - Bundle Products Collection List](https://freemius.com/blog/wp-content/uploads/2018/11/freemius-checkout-bundle-products-collection-list.png)

We would like to extend it even more by showing the buyer the cost of every independent product and how much money they save by getting the bundle. Stay tuned! (hope to release before 2019).

### Invalid Zip Code On Credit Card Checkout

As some of you may have already noticed, when a customer enters their credit card information with an invalid zip code, due to the way Stripe’s zip code validation works, the failed payments may temporarily appear as pending on the credit card’s statement. This usually leads customers to panic and immediately contact support (angry) asking why their credit card was charged more than once. To avoid this situation, we now track those failed charges and show a set of corresponding notices in several places, letting the customer know about that in advance, and avoiding the panic and the unnecessary support load.

The immediate error shows after a failed charge due to an invalid zip code:

![Freemius Checkout - Invalid Zip Code Error](https://freemius.com/blog/wp-content/uploads/2018/11/freemius-checkout-invalid-zip-code-error.png)

A notice that is shown in the after purchase screen when there was a single failed purchase due to an invalid zip code:

![Freemius Checkout - Invalid Zip Code After Purchase Notice](https://freemius.com/blog/wp-content/uploads/2018/11/freemius-checkout-invalid-zip-code-after-purchase-notice.png)

And a final notice about the invalid zip code charge in the after purchase email:

![Freemius After Purchase Email - Invalid Zip Code Notice](https://freemius.com/blog/wp-content/uploads/2018/11/freemius-after-purchase-email-invalid-zip-code-notice.png)

### Subtitle Customization

We’ve introduced a new \`subtitle\` parameter to customize the checkout’s subtitle (emojis supported!): ![Freemius Checkout - Custom Subtitle](https://freemius.com/blog/wp-content/uploads/2018/11/freemius-checkout-custom-subtitle.png)

### Lifetime Trials

The checkout now supports lifetime trials which means that a user can be registered for a trial with a payment method, which will automatically be converted into a lifetime purchase by the end of the trial. It saves the hassle for users that don’t wish to subscribe to monthly/annual, but would still like to try the product with a trial first. This is yet another unique functionality which we are proud to be able to say we’re the only solution on the market to support.

## Refunds

As your business grows, many of you will hire a person to handle some of the support load. Since it’s not feasible for you to keep track of every refund and the reasoning behind it, we introduced a new field where you or the person that processes the refund can enter the reason for the refund:

![Freemius Developers Dashboard - Refund Reason Dialog Box](https://freemius.com/blog/wp-content/uploads/2018/11/freemius-developers-dashboard-refund-reason-dialog-box.png)

This field is required for all team members except you, the owner of the product, and will be included with the after-refund notification email which is sent to the product admins:

![Freemius Developers Email - Refund Notification With Reason](https://freemius.com/blog/wp-content/uploads/2018/11/freemius-developers-email-refund-notification-with-reason.png)  
This should make it easier for you to delegate the refunds to your support staff while keeping track of the refund process.

## Developers Dashboard

### SANDBOX Checkout Link

As part of our efforts of simplifying the testing process of sandbox payments, you can now easily access the checkout in a sandbox mode using the CHECKOUT LINK button on the PLANS page:

![Freemius Developers Dashboard - Direct Checkout Links](https://freemius.com/blog/wp-content/uploads/2018/11/freemius-developers-dashboard-direct-checkout-links.gif)

### Setting An Unlimited License Limit

You can now easily set a license limit to *unlimited*. If the license quota is more than 1-site, click on the minus icon to reduce the quote to 1. Then, you’ll notice an infinite icon (∞) will show up. Clicking it will bump the license quota to unlimited:

![Freemius Developers Dashboard - Setting Unlimited License](https://freemius.com/blog/wp-content/uploads/2018/11/freemius-developers-dashboard-setting-unlimited-license.gif)

### Easy Secure Download Link

It’s inevitable that sometimes customers won’t get the after purchase email. When it happens, the best practice is to direct them to the new Customer Portal and guide them to click the *Never received your password?* link to set their password:

![Freemius Users Dashboard - Never Received Your Password Link](https://freemius.com/blog/wp-content/uploads/2018/11/freemius-users-dashboard-never-received-your-password-link.png)

In some cases, you may want to just email them a secure download link. Therefore, we introduced a new button in the LICENSES section to generate a secure download link which will be valid for 48 hours. The button will show up once you hover the relevant license:

![Freemius Developers Dashboard - Generate Secure Download Link](https://freemius.com/blog/wp-content/uploads/2018/11/freemius-developers-dashboard-generate-secure-download-link.jpeg)

## Email

### Emojis

You’ve probably noticed that some emails now include emojis in the subject line 😱 We got inspired by eBay’s after purchase emails, which include the check ✅ emoji. Emojis drive visual attention, making those emails stand-out in the inbox, and increasing the open rate. We also use the emojis to visually help you know what the email is about. So for example, we are adding a sand watch emoji ⏳ in the “trial started” email notification or the recycle emoji 🔄 for subscription related emails.

### Support Contact Email

Following requests from the community, we enriched the email you receive after a user initiates a ticket from the WP Admin contact form. The updated email now contains all the metadata that we have about the site, installation, user, license, and their subscription.

## Add-Ons

You can now control which add-ons will be visible in the in-dashboard *Add-Ons* page in the WP Admin. This functionality was introduced especially for the period in which you develop a new add-on and would probably like to test it before it appears in the WP Admin of your users. You can either control it from the ADD-ONS section of the parent plugin:

![Freemius Developers Dashboard - Add-Ons Release Switch](https://freemius.com/blog/wp-content/uploads/2018/11/freemius-developers-dashboard-add-ons-release-switch.gif)

Or directly inside the SETTINGS page of an add-on:

![Freemius Developers Dashboard - New Add-On Release Checkbox](https://freemius.com/blog/wp-content/uploads/2018/11/freemius-developers-dashboard-new-add-on-release-checkbox.png)

Just don’t forget to hit the *UPDATE* button at the bottom if you set it in the SETTINGS page.

Please notice that when running the new SDK in DEV mode, the marketplace will show all the add-ons, released or not.

## WordPress SDK

### Terms of Service Update

We updated the URL of the “Terms of Service” link shown in the opt-in screen:

![Freemius Opt-In - Terms of Service Link](https://freemius.com/blog/wp-content/uploads/2018/11/freemius-opt-in-terms-of-service-link.png)

Instead of linking it to our general website’s terms, which leads to some confusion among admins, it is now linked to your product’s specific usage tracking “terms” page that detail all the information about the usage-tracking and collected data:

`https://freemius.com/wordpress/usage-tracking/<productID>/<productSlug>/`

When running the premium version, the link label is now changed to “EULA” and its URL refers to the auto-generated EULA for the product:

`https://freemius.com/terms/<productID>/<productSlug>/`

**Note:** We are currently working with a top tier attorney on revamping the EULA to make it more protective for you and for Freemius. So a new EULA is coming up soon!

### Support Forum Link

The optional submenu item that links to the WordPress.org support forum now opens on a new page. This was a repeating request so we finally prioritized it 😉

### Subscription Cancellation

From a consumer point of view, being billed for a subscription renewal unexpectedly is a real pain. Not only is it annoying, it requires the user to “work” to get their money back. Money that, in theory, shouldn’t have been taken from their account in the first place. Moreover, it drives negative emotions like anger and frustration and affecting the way a consumer perceives your business. From the business owner’s point of view, it means dealing with angry customers, which is mentally hard and not the fun part of the business. So you end up wasting time on “refund support”, that could be invested in the actual product or into helping customers that have real problems.

Therefore, we are constantly trying to come up with techniques to eliminate those unexpected charges, saving you, the seller, the time and the emotional hassle of dealing with those issues. As well as making the experience of customers that buy products through Freemius as pleasant as possible.

In the last year, we discovered two use-cases in which some customers assume that the following actions will also cancel all of their future billing:

1. Deactivation and uninstallation of the product
2. Deactivation of a license (without cancelling its subscription)

This assumption actually makes a lot of sense, as this is how things are working with most online services (SaaS). If you deactivate your account, the subscription will (usually) be canceled.

To avoid this confusion, when a user is about to deactivate your plugin/theme and it’s associated with an active subscription with a license that’s only been activated on that website, before showing the deactivation feedback form, the SDK will now prompt the customer and let them cancel the subscription, as part of the product deactivation sequence. This is how it looks like:

![Freemius SDK - After Plugin Deactivation Subscription Cancellation Prompt](https://freemius.com/blog/wp-content/uploads/2018/11/freemius-sdk-after-plugin-deactivation-subscription-cancellation-prompt.gif)

Similarly, when the user clicks on the license deactivation option from their Account page, if the subscription license has only been activated on that site, we ask the customer if they would also like to cancel the subscription, in addition to deactivating the license:

![Freemius SDK - After License Deactivation Subscription Cancellation Prompt](https://freemius.com/blog/wp-content/uploads/2018/11/freemius-sdk-after-license-deactivation-subscription-cancellation-prompt.png)

We are aware that it will most likely increase the subscriptions churn a bit, but it will save you time and hassle, as well as have a positive effect of your brand. If users will feel more confident when buying your products because you are using Freemius, that’s a win-win-win for everyone.

### After Purchase Notice

The after in-dashboard purchase admin notice was enriched. Instead of immediately guiding the customer to download and install the premium code base, the logic now first checks if the premium version is already installed on the site. If it is, instead of guiding the user to download and install, simply suggest to activate it with a single click:

![Freemius SDK - After Upgrade Notice Premium Already Installed](https://freemius.com/blog/wp-content/uploads/2018/11/freemius-sdk-after-upgrade-notice-premium-already-installed.jpeg)

### Translations – Dutch

The SDK was fully translated to Dutch! Huge thanks to [Benny Vluggen](https://www.transifex.com/user/profile/bvl/), [Mike van der Sluis](https://www.transifex.com/user/profile/mikesmth/), and [Patrick Buntsma](https://www.transifex.com/user/profile/Patrick070/). The SDK is now translated to:

- Spanish
- Dutch
- Italian
- Japanese
- Hebrew
- Russian
- Danish

If your native language is not English and you have a high-level of English, please join our translations efforts to help us maintain the current translations and translate it into new languages:

[https://www.transifex.com/freemius/wordpress-sdk/](https://www.transifex.com/freemius/wordpress-sdk/)

### Freemium License Activation & Deactivation

Prior to this SDK release, when a user would upgrade a freemium plugin/theme directly within the WP Admin, our WordPress SDK would automatically take care of the license activation in the background. But, if the user would purchase the paid version from your site (outside the WP Admin) and would have already opted-in/skipped the opt-in in the free version before, they would have to activate the license by clicking on the “Activate License” link, either on their Account page (if they ever opted-in), or on the plugins/themes page. Basically, there was no clear path or instructions for the customer on how to activate the license, which usually generated a support ticket.

So now, after installing and activating a paid version of a freemium product, even if the user had already opted-in/skipped the opt-in on the free version before, the SDK will now automatically prompt the customer with the license activation screen.

Also, if a user deactivates their license they will also be redirected and prompted with the license key screen.When the product is freemium, they do have an option to just continue using the free version without activating a license.

### WooCommerce Extensions Compatibility

WooCommerce has a custom plugin header to confirm compatibility with the latest versions:

![WooCommerce Extension - Plugin Compatibility Header](https://freemius.com/blog/wp-content/uploads/2018/11/woocommerce-extension-plugin-compatibility-header.png)

Due to the execution order of the Freemius WordPress SDK and WP core’s caching, the headers data wasn’t getting retrieved, which resulted the following errors:

![Not tested with active version of WooCommerce](https://freemius.com/blog/wp-content/uploads/2018/11/word-image.png)

This issue is now fixed.

## Misc

### License Renewals

We optimized the manual license renewal/expiry mechanism to avoid emailing to customers who purchased another license. If a customer purchased another license during the past 90 days which is still active and associated with a site that has the same URL -&gt; do not send expiration campaign.

### Webhooks Mechanism

The user’s `is_marketing_allowed` flag is now included in the event data that is sent to the webhooks.

### Bug Fixes

- Fixed a UI layout bug of the in-dashboard contact, pricing, and checkout pages for iPhones.
- Fixed a bug when an add-on’s license was activated before the parent plugin was opted-in/skipped.

## What’s next?

We have a mega list of hundreds of features we can work on, including great suggestions we keep getting from the community on our [public feature requests board](https://trello.com/b/I6o3BZOo/freemius-features-requests). After lots of thinking, during the next months we are going to focus on:

1. Upsells: It’s not a secret that upsells work and can have a meaningful increase of about 10%-30% in the CLTV (customer lifetime value). We already started experimenting with upsells about a year ago, so now it’s time to hit the gas paddle on that, taking your business to the next level. We are still working on the game plan and how to tackle upsells, and there’s a good chance we will start with product2bundle upsells for those of you who offer bundles. In any case, this is a big thing that is going to get our full attention in the upcoming period.
2. Earnings reporting simplification: We keep getting feedback that the earnings page is confusing. Since we 100% agree with that, and believe that you deserve to get a clearer view of your earnings and payouts, we are planning to simplify the UI and make the required backend changes to also show you a more detailed overview of all the moving parts, like the gateway fees, our cut, and your net.