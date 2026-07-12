It’s official! [WordPress SDK 2.5.0](https://github.com/Freemius/wordpress-sdk/releases/tag/2.5.0-rc.1) [RC1](https://github.com/Freemius/wordpress-sdk/releases/tag/2.5.0-rc.1) is now available with awesome (and relevant) enhancements that tackle what we’ve identified as your topmost common and time-consuming issues to date.

Our goal with this version is to help you reduce support load so that you can allocate more of your time towards deliverables and other more productive activities.

Before we dive into the features, we need your help 🙌

## Call for Testers

Even though we ran thorough testing of all kinds (automated, manual, and regression tests), and while we feel pretty confident in the stability of 2.5.0, due to the complexity and amount of code changes & use-cases involved in this version, we decided to push it as a release candidate first.

### “I want to be involved in testing – how can I help?”

Want to help us in testing? That’s great and appreciated!

- If you are running a beta program, simply update the SDK to this RC and push a new version as a *beta*.
- If you are *not* running a beta program and know that some of your customers running cloned environments like staging to production, or using your plugin/theme with WaaS plugins like WP Ultimo, when they contact your support due to SDK issues you can send them a special version of your product with this SDK as it should solve their problems.

Regardless, if you try out the RC, whether you experience issues or, on the contrary, if it resolves the SDK problems your users were facing before, please let us know! Simply contact us via [\[email protected\]](https://freemius.com/cdn-cgi/l/email-protection), open a GitHub issue, or use any other communication channel that is easiest for you – we want your feedback 🙂

Let’s get down to the features.

## Duplicate Websites and Clone Resolution

With the growing popularity of WaaS (WordPress as a Service) networks and hosting companies that provide 1-click staging to production deployment workflows, you’ve probably already dealt with customers complaining about unexpected issues when site duplication is involved.

In short, a clone is a website (or a subsite) that has a unique ID and pair of public/secret keys that were assigned by Freemius and are identical to the ID and keys of another website. You can learn more about clones, how they are typically created, and when, in [this doc](help-documentation-wordpress-sdk-safe-mode-clone-resolution-duplicate-website.md).

Inspired by Jetpack’s UI, I’m excited to share that this SDK release comes with a fully-featured clone identification, management, and resolution mechanism. It’s a capability that’s been on the back-burner for quite some time, and I highly encourage you to familiarize yourself with the [clone websites problem and how the WordPress SDK handles it](help-documentation-wordpress-sdk-safe-mode-clone-resolution-duplicate-website.md) to get the most out of the enhancement:

![Freemius SDK Manual Clone Resolution Notice](https://freemius.com/blog/wp-content/uploads/2022/01/freemius-sdk-manual-clone-resolution-notice-1.png)

### Snoozing for Troubleshooters

While our deactivation feedback form offers a unique opportunity for users to provide feedback to product owners before they abandon, over the years we’ve heard complaints that users really hate the feature. After analyzing the feedback, we managed to attribute this sentiment specifically to the ‘troubleshooters’ segment.

Plugin updates are a common task that website maintainers have to deal with on a daily basis. Sometimes a plugin/theme update can go wrong due to conflicts, bugs, and incompatibilities, causing issues and unexpected errors on a site. Maintainers usually don’t dive into the code level, so the common troubleshooting process is to identify the cause of the problem with plugin deactivations and reactivations, followed by theme switching. Meaning, you need to deactivate the plugins one by one until the problem is resolved, then reactivate them individually and in the same order that they were deactivated. In theory, this should help isolate the ‘problematic’ plugin, but if it doesn’t uncover the issue then the next attempt should be a ‘theme switch’.

As the ‘footprint’ of themes and plugins that use our WordPress SDK grows, the deactivation feedback form adds an additional click to each deactivation. From there, reactivating a Freemius-powered plugin automatically redirects to the opt-in screen or to the plugin main settings page (based on the opt-in state), which adds another click to navigate back to the plugins page.

This means that just 5 plugins using Freemius on a site can potentially add 10 extra clicks — something that’s understandably annoying for troubleshooters. And when managing 20 sites, as an example, all those clicks accumulate over time, which explains why some maintainers really dislike the WordPress SDK.

Having understood the reasons behind the ‘hate’, we came up with a simple solution to relieve the ‘pain’ for troubleshooters and, hopefully, win some of their trust back.

The *Feedback Form* already displays an option that indicates a deactivation is temporary for troubleshooting. So, instead of just sending that feedback our way…

1. We now show an option to snooze the panel from one hour to 30 days.
2. Because we realize it doesn’t add any value to product owners, choosing to snooze skips sending feedback to Freemius altogether.
3. Finally, if the admin snoozes the form, the redirection will be off for the snoozed period.

![Freemius WordPress SDK Feedback Form Snoozing](https://freemius.com/blog/wp-content/uploads/2022/01/freemius-wordpress-sdk-feedback-form-snoozing-1.gif)

**Snoozing will only impact the current logged-in admin and will work across all Freemius powered plugins and themes installed on that website.**

This improved UX can potentially save tons of clicks for ‘heavy’ troubleshooters, and we are excited to see the difference it will make.

### Enable Deactivation with Empty ‘Other’ Feedback

To encourage users to submit feedback you can act upon, previously, when a user selected the ‘Other’ option in the deactivation feedback form, the ‘Submit & Deactivate’ button’s state was changed to disabled until the user entered some input to explain the ‘other’ reason.

It was brought to our attention that this UX was problematic because users read from top-left and some choose that option because they simply don’t want to provide any feedback. I.E., if they choose that option before noticing there’s an option to ‘Skip & Deactivate’, it gives the impression that it’s impossible to deactivate the product without providing any feedback.

Now, when the ‘Other’ option is selected and the explanation box is empty, the button is enabled and labeled as ‘Deactivate’:

![Freemius WordPress SDK Feedback Form Reason Other](https://freemius.com/blog/wp-content/uploads/2022/01/freemius-wordpress-sdk-feedback-form-reason-other-1.png)

And, obviously, no data will be sent to our end because empty ‘Other’ feedback is useless.

### Anonymous Feedback Default Checkbox State

If a user skipped the opt-in and chose to provide feedback using the deactivation feedback form, by default the feedback was not anonymous to allow you to contact the user if needed. This version of the SDK introduces a new filter so that you can control the default submission mode of the feedback form and change it to anonymous feedback by default, using the following:

`my_fs()->add_filter( 'default_to_anonymous_feedback', '__return_true' );`

## User Assets Ownership Mix-Up — Gone!

A healthy percentage of WordPress plugin and theme purchases are made by ‘builders’, where eventually the project is handed over to their client. To facilitate the relationship, we offer a good amount of flexibility to allow changing ownership of account assets from one person to another.

Without diving into the technicalities, with the many millions of websites running our SDK, we stumbled upon several edge cases that unexpectedly mixed up assets between accounts. While these issues were infrequent, it’s painful for the customer, for you, and for us to fix.

If there was a contest for the most annoying and time-consuming issues, this one is the undisputed winner of 2020–2021 🏆 It’s also a good example of where giving too much flexibility without trying to foresee all of the use cases (and you never will) can cause more damage than good.

Not only did we add some restrictions in the backend to reduce the instances of the issue, but the new WordPress SDK release also enhances the Account’s email update experience with additional input from the user, and handles each case slightly differently:

![Freemius WordPress SDK Email Address Update](https://freemius.com/blog/wp-content/uploads/2022/01/freemius-wordpress-sdk-email-address-update-1.gif)

## Fix of HTTP 404 Not Found (AKA ‘No Updates’)

Some of you may have received support tickets where customers complained that the SDK is throwing errors and slowing the system down, typically with a complementary screenshot of an error from Debug Log (or other debugging plugins).

![Query Monitor Plugin Update Freemius API 404 Not Found](https://freemius.com/blog/wp-content/uploads/2022/01/query-monitor-plugin-update-freemius-api-404-not-found-1.png)

The HTTP errors were returned when there were no newer releases, which is the expected behavior of a proper RESTful API implementation when a resource doesn’t exist.

Since it’s not trivial to understand that this behavior is expected until contacting us, and it generated unnecessary support tickets for you (and us), we have modified the HTTP response code to 200 to eliminate this confusion once and for all. This API change was already deployed several weeks ago, so there’s a good chance you’ve noticed this type of complaint has disappeared.

Looking back, we now acknowledge we should have made that change much earlier. It’s just that sometimes the ‘right’ technical thing isn’t ‘right’ for the end-user.

## Fault Tolerance to Background Connectivity Issues

A few weeks ago AWS had a temporary downtime. As we host our servers on Amazon, naturally, the downtime caused connectivity issues to our API server. The websites that their Freemius sync cron was executed during that period were added with a dismissible notice about the connectivity issue, causing a bunch of support inquiries from concerned users. The purpose of the notice is to highlight *ongoing* connectivity issues due to firewalls, ISP blockages, etc. It’s not made for temporary connectivity issues. Therefore, we improved the logic by putting a fault tolerance mechanism in place, so the notice will only be added after 3 consecutive failed connectivity attempts (typically 3 days).

## Resolution of Deprecated Multisite Network Functions

`wpmu_new_blog()` and `deleted_blog()` were deprecated in WP 5.1, which was throwing a notice when running in debug mode. We updated the multisite integration to instead use `wp_insert_site()` and `wp_delete_site()` correspondingly when running on new WordPress releases. Thanks [Dario Curvino](https://github.com/Dudo1985) for your contribution 🙌

## New Filters

We introduced a new `hide_freemius_powered_by` filter to allow you to hide the *Powered by Freemius* tab from the pages generated by the SDK:

`my_fs()->add_filter( 'hide_freemius_powered_by', ‘__return_false’ );`

And another filter named `hide_billing_and_payments_info` to hide the billing and payments history shown by default to customers in the Account page:

`my_fs()->add_filter( hide_billing_and_payments_info’, ‘__return_true’ );`

## ‘Anonymous’ License Activation — We Hear You!

As a startup or any type of business, you have limited resources in the beginning. The Number One focus is getting to product/market-fit, which naturally forces you to prioritize and make sacrifices. When we started Freemius, our analysis of the WordPress market was that DIYers represent the largest percentage of users in the ecosystem. Therefore, some of the practices and UX were designed for that segment. As we mature, in the last two years we’ve made a tremendous effort to apply feedback collected over the years to better accommodate the needs of maintainers and builders. While this is a much smaller percentage of WordPress users, it’s an extremely passionate and important one!

At this stage, the vast majority of the behavioral feedback received over the years was already incorporated into the WordPress SDK. But there’s still one repetitive request that usually comes from tech-savvy users with higher privacy sensitivity: *“Why do I need to opt-in when activating a license key?”*

While we only collect a few basic metrics that benefit users and product makers upon license activation — such as the WordPress version, PHP version, and website locale (the complete info is documented in our new [Data Practices](privacy-data-practices.md) page) — it’s a fair concern that we wanted to address so that users can enjoy your products with confidence.

So, in the next release, we plan to introduce a new option for license activation without sharing data that is not essential for license activation and updates delivery. Instead of re-working the data architecture, we’ll mask the data with dummy values to offer maximum privacy. Keep in mind that we would still have to collect the website URL and IP, SDK version, and whether the product is active or inactive. But that’s it!

## Until Next Time

Have feedback for the upcoming ‘anonymous’ license activation? Got any features in mind that you’d like us to consider? Feel free to add them to our [Trello board](https://trello.com/b/I6o3BZOo/freemius-features-requests), and in the meantime, happy selling!