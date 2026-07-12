Release Notes is our monthly update that highlights the recent product improvements we’ve made, so you can easily stay up to date on what’s new. Here’s what we launched in May.

This product cycle was focused on three main objectives:

1. Integration with 3rd party email marketing services
2. Improving the in-dashboard upgrade process for freemium products
3. User-friendly usage tracking terms

Since our early days, we released a webhooks mechanism, because we know it’s impossible to develop every feature in-house and address every use-case. A solid webhooks mechanism makes Freemius more powerful and extensible and allows developers to integrate the platform with practically any 3rd party service.

Over the past year, we learned that the #1 (by far) usage of the webhooks mechanism was for integrating Freemius with MailChimp, powering up the email marketing efforts with our high converting opt-in. At first, we created an example of a [vanilla PHP Webhook integration](https://github.com/Freemius/php-webhook-example). Though some WordPress developers in our community had a lack of sysadmin knowledge for taking and deploying it to their WordPress powered site. A collaboration between two of our developers (Bruno Carreço and Rob Marlbrough) yielded this [lovely WordPress plugin](https://github.com/sebet/freemius-webhook-listener), which does the trick. That was great, but we felt it wasn’t enough since we have developers who are monetizing with Freemius and are using a freemium model to sell their paid version from within the dashboard, without even having a website.

So, I’m super excited to announce that we’ve just launched our MailChimp integration, making it easy to sync emails from Freemius to MailChimp. All you need to do is connect your MailChimp to Freemius:

![Freemius MailChimp Connect](https://freemius.com/blog/wp-content/uploads/2017/05/freemius-mailchimp-connect.png)

Then, create a set of rules to sync the emails when certain events are triggered on the Freemius end:

[![Freemius MailChimp Integration Dashboard](https://freemius.com/blog/wp-content/uploads/2017/05/mailchimp-integration.jpg)](https://freemius.com/blog/wp-content/uploads/2017/05/mailchimp-integration.jpg)

No need to create any webhooks or touch your server – it’s that simple!

## The Webhooks Mechanism Got Stronger!

Speaking of webhooks, you can now pick exactly which events are sent to your endpoint:

![Freemius Webhooks Event Selection](https://freemius.com/blog/wp-content/uploads/2017/05/webhooks-event-selection.png)

This makes the webhook mechanism even more powerful and will significantly reduce the load on your servers when you only need to consume few events.

## Help Scout Integration

The [Freemius’ Help Scout integration](help-documentation-integrations-help-scout.md) is actually not new, but it was quite hidden (unintentionally) in the dashboard. We moved it from the SETTINGS section into a separate menu item under the new INTEGRATIONS menu to increase the awareness, since we know that most WordPress plugin & theme shops are running their support on the platform.

## The Most Seamless and Customer Friendly Upgrade Process for Freemium Plugins

If you have a plugin or a theme listed on WordPress.org and you follow the repo’s announcements on make.wordpress.org, you’ve probably already heard there was a [clarification thread by Mika regarding guideline #8](https://make.wordpress.org/plugins/2017/03/16/clarification-of-guideline-8-executable-code-and-installs/) concerning [Jetpack’s recent announcement](https://jetpack.com/2017/03/16/165-beautiful-free-themes/) on installing non-wp.org themes via the plugin. Prior to that clarification, the consensus in the WordPress community was that developers are not allowed to list plugins or themes on WordPress.org if they programmatically install executables (e.g. plugins and themes) which are hosted outside of the official repository. This means that freemium plugins/themes on WordPress.org had to ask their customers to do a LOT of work just to start using the premium version. Here’s how the process looked like for the customer, in the past:

1. Complete the checkout
2. Download the premium code version
3. Upload the premium plugin/theme
4. Deactivate the free version of the plugin/theme (in some cases this step isn’t required)
5. Activate the premium version
6. Activate the license key

*Note: This process isn’t the case for Serviceware plugins, i.e., services which are basically wrapped into a plugin.*

Moreover, some hosting companies require SSL or FTP authentication just to upload the premium version, which means that non-tech-savvy customers had to contact the developer’s support just to have the product installed. Isn’t that crazy? Are you familiar with any other paid product that requires so many steps just to get started?

But yes – that’s how it works, and the community had to learn to live with it.

Luckily, with the new clarification and some creative thinking, we managed to reinvent the whole upgrade mechanism for freemium WordPress.org products by building the BEST and most seamless upgrade process that WordPress had ever seen!

### How does it work?

During the checkout process we’ve added a checkbox, right before the final upgrade button, where the user can choose to automatically install the product after the upgrade:

[![Freemius Auto-Install Opt-in Checkbox](https://freemius.com/blog/wp-content/uploads/2017/05/freemius-auto-install-opt-in.png)](https://freemius.com/blog/wp-content/uploads/2017/05/freemius-auto-install-opt-in.png)

If the customer checks that box, all the steps mentioned above will occur automatically, in the following order:

1. The premium version will automatically be uploaded to the site
2. The free version will be deactivated
3. The premium version will be activated
4. The license key will be automatically applied
5. Premium product ready for use!

It’s that easy!

And btw – if the file system permissions require FTP or SSL authentication, the new SDK version will prompt the user for those, integrating with WordPress core file system permissions request native mechanism.

Here’s a 50-sec recording showing the whole upgrade process for an opted-in user showcasing FooBox Image Lightbox, one of Freemius’ makers:

Yes, excluding the time it takes to type the credit card, the whole upgrade process takes less than 50-sec!

### Why is it compliant with the WordPress.org guidelines?

1. The premium version will only be installed upon explicit opt-in consent of the user, it will never happen automatically.
2. The opt-in checkbox is running on our checkout as a service, not as part of the plugin code that is hosted on wp.org.
3. Even if the user mistakenly checks the auto installation box, they still get a 30-sec “grace period”, during which the process can be canceled.
4. All of the messaging is super-clear to the user, including the fact that the premium plugin version will be installed from the Freemius repo and not from WordPress.org repo. No hidden footprints, everything is straightforward.

## License and Download Recovery (semi-Members Area)

As you already know, the “Members Area”, which we currently offer with Freemius is part of the SDK and is available under the Account section within the WP admin dashboard when the plugin or theme is installed. This means that if a customer purchases a product via Freemius, and for some reason deletes the after-upgrade-email, they won’t have a way to recover the download link and license key for the premium product without installing the free version on their site. However, if the product is premium-only and the customer doesn’t have the download link, it practically means that they have to contact the support to get the downloadable. Being that our goal is to maximize our makers’ revenues, and since we know that more support means more costs – we developed a cool temporary workaround that addresses it. You can now provide a link on your site and documentation to where customers will be able to type the email they’ve used for the upgrade and get the download of the premium code with the license key, directly to their email.

Here’s what it looks like:

![Freemius Customers License Recovery](https://freemius.com/blog/wp-content/uploads/2017/05/license-recovery.png)

The link structure is as follows: https://dashboard.freemius.com/license-recovery/{id}/{slug}/

## Beautiful and User-Friendly Usage-Tracking Terms Page

If you’ve been using our default opt-in messaging you probably noticed that we mention that the usage-tracking is handled by [freemius.com](index.md) with a link to our insights marketing page. The link was an important temporary placeholder to show users what is Freemius all about and how it works. But, it was targeted at developers, not users. Our new WordPress SDK is now pointing to a new dynamic, auto-generated, terms page that was built to explain the value of usage-tracking to the users, and to let them know what exact data is being collected. In other words, it’s a user-friendly terms page.

Here’s an example:

![Freemius' Users Usage-Tracking Terms](https://freemius.com/blog/wp-content/uploads/2017/05/freemius-usage-tracking-terms.png)

[https://freemius.com/wordpress/usage-tracking/56/rating-widget/](https://freemius.com/wordpress/usage-tracking/56/rating-widget/)

As you can see, the page is personalized by pulling your product’s name and featured icon from WordPress.org.

> If you’ve already customized or plan to customize the opt-in message, make sure you keep the default link for legal reasons.

## Subscription Renewal Emails

We’ve added some new informative columns to the subscription renewal emails to show the total gross of the subscription and the number of successful renewals:

![Freemius Subscription Renewal Email](https://freemius.com/blog/wp-content/uploads/2017/05/subscription-renewal-email.png)

## WordPress SDK – v.1.2.1.7

We released a [new version of our WordPress SDK](https://github.com/Freemius/wordpress-sdk/releases/tag/1.2.1.7.1 "Freemius WordPress SDK"). The major update includes a secure logic to facilitate the new auto-installation process. In addition, we’ve fixed a bunch of bugs and added a lot of improvements, including optimization for environments with symlinks.

### Bug Fixes

- Fixed the method that downloads the plugin’s featured icon from WordPress.org when running on localhost (while the icon’s URL is over HTTPS).
- Fixed the “Upgrade” label arrow direction for RTL ([Closed #155](https://github.com/Freemius/wordpress-sdk/issues/155)).
- Apparently, some shared hosting providers are disabling `get_current_user()` which we were using for logging, so now, before calling the method we check if it’s not disabled ([Close #158](https://github.com/Freemius/wordpress-sdk/issues/158)).
- Added a missing email address sanitization when the user tries to recover their license key(s) ([Closed #154](https://github.com/Freemius/wordpress-sdk/issues/154)).
- Prior to version 1.2.1.6, we didn’t trigger the deactivation feedback form upon free product version deactivation if the user had an active license. That was assuming that the customer’s intent was to deactivate the free version before activating the premium product. In the previous release, we introduced a new mechanism that automatically deactivates the free version when activating the premium one. Thus, we modified the code to trigger the feedback form on every deactivation. While running tests for the new release, we noticed that we forgot to modify some of that logic, which caused the form not to show up in some use-cases.
- There are more and more [1-click staging environment services](https://instawp.com/set-up-wordpress-staging-site/) out there. Usually, those services are cloning the whole WordPress environment, including the Database, and only making some small Database changes to update the domain references to the staging site. Due to the complexity of some of our newest SDK identification, we use the DB to store references to the plugins and theme paths that are running the Freemius SDK. After several bug reports, we managed to reproduce the problem and now the SDK will purge the cache for those cases in addition to FTP deletions and/or folder renaming.

### Symlinks

After investigating a few bug reports, we found out that the SDK special logic that handles the automatic identification of the newest SDK was failing on some edge cases for test environments with [symlinks](https://en.wikipedia.org/wiki/Symbolic_link), usually related to [VVV (Varying Vagrant Vagrants)](https://varyingvagrantvagrants.org/). This version fixes those issues.

### Optimization

- We improved the logic that identifies the associated plugin’s basename for edge cases when an add-on is including the parent plugin as part of the execution.
- Optimized API connectivity error handling when specified cURL methods are disabled using the `disable_functions` directive in `php.ini`.
- Optimized the Account page for premium only modules without a free version (e.g. showing “Cancel Subscription” instead of “Downgrade”, hiding “Change Plan” button).

### Development Mode / Debugging

We’ve added buttons to get and set DB options from the Freemius Debug page:

![Freemius WordPress SDK Debug Page Actions](https://freemius.com/blog/wp-content/uploads/2017/05/wordpress-sdk-debug-page-actions.png)

This is particularly useful for developers who migrated from EDD or WooCommerce and would like to investigate a failed license migration of a customer by first verifying that the customer really has a license key stored in the Database. You can do so by heading over to `/wp-admin/admin.php?page=freemius`, clicking on the *Load DB Option* button and entering the option name that should store the license key.

## What’s coming up?

### SDK Memory Consumption Optimization

Due to legacy reasons and a decision taken when we initially designed the WordPress SDK, all the SDK’s translatable strings are located in a single file (`i18n.php`) and one huge global array. While this design is pretty convenient and organized, it also means that all those strings are loaded into the memory every time the SDK is included. The whole file is 44Kb, but we received a few complaints from site owners on low-memory in shared hosting, that got a PHP memory exhausting exception after installing a Freemius powered plugin or theme. We decided to prioritize that issue and the next SDK release will incorporate a major change to our localization logic infrastructure, turning it to lazy load which will significantly reduce the SDKs memory consumption.

### Affiliation Platform

Freemius’ mission is to help open-source developers build prosperous, subscription based, sustainable businesses. As we are dealing with digital products, one of the most effective ways to promote your products online is using affiliate marketing. As a temporary workaround, we encouraged developers to reach out to affiliates and track the sales they made for them by creating custom coupons. This was a nice temporary alternative, but it’s about time we offer a real solution. I’m happy to announce that we’ve officially started to work on a fully-featured affiliation platform. The first release will be minimalistic and will incorporate just the basics to start working with affiliates. The end goal is to have a fully automated affiliation platform, which will include automated payouts to affiliates and more. All I can say is – stay tuned!