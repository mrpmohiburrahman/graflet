Unlike previous release notes where we update our selling makers about new features, this release is dedicated to plugin & theme users and covers all recent changes to address feedback and concerns raised in the community.

Many of these concerns are rooted in the fact that Freemius has always been seen as a dev-centric platform. We’re working hard to change this. And one of our main priorities going forward is to pay close attention to the user community’s feedback so that Freemius becomes as amazing for you guys as it is for our software makers.

I want to thank the WordPress community, who hold us accountable and help us improve the platform as we go. I’d like to thank [Chris Wiegman](https://twitter.com/ChrisWiegman) for sharing insightful feedback and actionable tips on how we can improve the license activation experience, as well as several Facebook groups and their community leads who have helped to facilitate feedback collection from their communities:

- [Verdi Heinz](https://twitter.com/HeinzVerdi) and the members of the [Code Snippets Community](https://www.facebook.com/groups/282962095661875)
- [Sergiu](https://twitter.com/sergiuradoo) & Andrei, and the members of the [Blocksy Community](https://www.facebook.com/groups/601810683978727)
- [Benjamin Intal](https://twitter.com/bfintal), and the members of the [Stackable Community](https://www.facebook.com/groups/341991773356009)
- [David McCan](https://twitter.com/webtng) and the members of the [Dynamic WordPress](https://www.facebook.com/groups/700226834266137) group
- [Paul Charlton](https://twitter.com/WPTutz) and the members of the [WP Tuts](https://www.facebook.com/groups/336940873845231) group

For developers reading this: the complete release notes for the new 2.5.1 version of our WordPress SDK can be found [here](https://github.com/Freemius/wordpress-sdk/releases/tag/2.5.1).

Right, let’s get into it:

## Opt-In v.2.0

Following tons of feedback, we are excited to introduce the next generation of our opt-in screen 🎊

![Freemius Opt-In Screen Version 2.0](https://freemius.com/blog/wp-content/uploads/2022/11/freemius-opt-in-screen-version-2-0.png)

In addition to the slicker UI:

- The opt-in copy had a significant overhaul to better communicate its purpose as well as what users can expect when opting in.
- The permissions list was reviewed thoroughly to ensure it covers exactly what’s shared when opting in.
- We updated the permissions’ micro-message to clarify that opting in means sharing the info with the product’s team.
- We improved the copy to clarify how it helps the user who is installing the product, better explaining the benefits of opting in.
- New tooltips were added to most permissions, adding more context to how sharing the info benefits users.

## New Opt-In Info Page & Explainer Video

The “Terms of Service” now links to a brand new page explaining the relationship between Freemius, the product team, and users…

The feedback we received surfaced that some users were confused about how Freemius fits into the product/user relationship, so we’ve shifted the perspective of our messaging to:

- clarify the differences between opting in (and sharing data) and skipping (no data shared).
- maximize transparency by sharing the PHP code snippets behind every collected data point.
- explain the benefits that *users* gain from opting in.

![User-Focused 'Opt In' Explainer Video & Landing Page](https://freemius.com/blog/wp-content/uploads/2022/11/user-focused-opt-in-explainer-video-and-landing-page.png)

Here’s an example of how the page looks for our selling maker, Stackable: [https://freemius.com/product/opt-in/5650/stackable-ultimate-gutenberg-blocks/](https://freemius.com/product/opt-in/5650/stackable-ultimate-gutenberg-blocks/)

Although we have an in-depth page that covers frequently asked questions about the [Freemius opt-in and our data practices](privacy-data-practices.md), we learned that users don’t have the time/energy/will to read long articles. To make the info ‘bite-sized’, the marketing team consolidated all of that info into a short, friendly video and complementary landing page. These dual user-focused assets outline *exactly* what is shared when opting in and unpack the specific benefits that users can expect by doing so.

They also explain what happens when users don’t opt in. Spoiler alert: the product will work just fine! We value your right to choose what info is shared (or not shared).

Opt in, or don’t — Freemius cares about your privacy:

## ‘Anonymous’ License Activation

Like the opt-in, the [license activation](https://freemius.com/product/license-activation/) went through a similar UI and framing refresh. What’s even more exciting is that licenses can now be activated with a minimal data footprint. This means only sharing the essentials needed for Freemius’s license & updates delivery engine:

- Homepage URL
- Product version
- SDK version
- Whether the product is active (or uninstalled)

**That’s it!**

Anyone sensitive about privacy can easily expand the permissions list and toggle off the new *Diagnostic Info* permission. This skips the sharing of WordPress & PHP versions, and site language & title.

![Freemius License Activation Screen & Expanded Permissions List](https://freemius.com/blog/wp-content/uploads/2022/11/freemius-license-activation-screen-and-expanded-permissions-list.png)

Thanks for providing your feedback, Chris Wiegman!

## User IP Sharing — No More!

After our CEO [Vova Feldman](https://twitter.com/vovafeldman) participated in a [live QA about Freemius](https://www.youtube.com/watch?v=eNgNs_3jlPM), a concern was raised about sharing user IPs.

For context, the IP was used to identify user geolocations to help developers recognize which languages & regions their plugin/theme should be translated and tailored to. It can also be used for security purposes to flag suspicious activity and prevent impersonation.

Even though it was only shared with user consent upon opting in, we have re-evaluated the need for this data point and decided to remove it altogether: [https://github.com/Freemius/wordpress-sdk/pull/580/files](https://github.com/Freemius/wordpress-sdk/pull/580/files)

Along with the user IP removal, we’ve also stopped sharing the nickname of the opting-in user — this was used as a placeholder for when the user had an empty first and last name.

Thanks for bringing it to our attention, Sean D.!

## Skip … Is Only for Skipping

When we launched Freemius in 2015, the WordPress.org repository didn’t have the active installs growth chart (which was recently back [in the news](https://wptavern.com/wordpress-org-removes-active-install-growth-data-for-plugins) after [its removal](https://meta.trac.wordpress.org/ticket/6511)). At the time, plugin and theme developers were “thirsty” to understand how efforts to improve their products impacted adoption. To solve this problem and give developers an accurate picture of their product usage, skipping the Freemius opt-in also sent an anonymous ping, which increased the product’s “skips” counter. Along with the [Deactivation Feedback Form](https://freemius.com/help/documentation/analytics-insights/user-feedback/) and some heuristics, we could offer an estimate of the product’s audience size.

Long story short: we’ve realized the skips counter is far from accurate, unreliable, and prone to errors, which is why we’ve removed it from the new dashboard. Combined with the fact that some didn’t like this behavior, the *Skip* button is just for skipping the opt-in now. That’s it.

## Improved Copy for Email Verification

The connection between the SDK and the Freemius API is secured with public/private keys and we manage a single entity per email address. If a person with the same email address has already opted in on another website, we have to make sure they are not impersonating by confirming the ownership of their address before sharing the keys with the website.

Following feedback (thanks, David McCan), we realized the email copy was confusing. We therefore revised the copy to clarify the purpose of the confirmation:

![Freemius Email Verification Confirmation With Revised , Clearer Copy](https://freemius.com/blog/wp-content/uploads/2022/11/freemius-email-verification-confirmation-with-revised-clearer-copy.png)

## Granular Opt-Out Permissions

To make the opt-in permissions more flexible and allow users to pick and choose what they want to share, the team has introduced a brand new permissions management layer for free and paid products.

Clicking the *Opt Out* action link now opens a new dialog box where users can selectively choose which of the permissions they want to opt out from or keep sharing:

![Freemius Opt-Out Screen With Permissions Management Layer For Free Products](https://freemius.com/blog/wp-content/uploads/2022/11/freemius-opt-out-screen-with-permissions-management-layer-for-free-products.png)

The granular permissions now support new states that were not supported before. For example, a user can stay subscribed to receive email updates from the product team while opting out from sharing diagnostic info about their WordPress environment.

And here’s how it looks for paid products:

![Freemius Opt-Out Screen With Permissions Management Layer For Paid Products](https://freemius.com/blog/wp-content/uploads/2022/11/freemius-opt-out-screen-with-permissions-management-layer-for-paid-products.png)

## Deactivation Feedback Form UX Enhancements

### Snoozing for Troubleshooters

While our deactivation feedback form offers a unique opportunity for users to provide feedback to product owners before they abandon, over the years we’ve heard complaints that users really hate the feature. After analyzing the feedback, we managed to attribute this sentiment specifically to the ‘troubleshooters’ segment.

Plugin updates are a common task that website maintainers have to deal with daily. Sometimes a plugin/theme update can go wrong due to conflicts, bugs, and incompatibilities, causing issues and unexpected errors on a site. Maintainers usually don’t dive into the code level, so the common troubleshooting process is to identify the cause of the problem with plugin deactivations and reactivations, followed by theme switching. Meaning, you need to deactivate the plugins one by one until the problem is resolved, then reactivate them individually and in the same order that they were deactivated. In theory, this should help isolate the ‘problematic’ plugin, but if it doesn’t uncover the issue then the next attempt should be a ‘theme switch’.

As the ‘footprint’ of themes and plugins that use our WordPress SDK grows, the deactivation feedback form adds an additional click to each deactivation. From there, reactivating a Freemius-powered plugin automatically redirects to the opt-in screen or to the plugin main settings page (based on the opt-in state), which adds another click to navigate back to the plugins page.

This means that just 5 plugins using Freemius on a site can potentially add 10 extra clicks — something that’s understandably annoying for troubleshooters. And when managing 20 sites, as an example, all those clicks accumulate over time, which explains why some maintainers really dislike the [WordPress SDK](https://freemius.com/blog/changelog_category/wp-sdk/).

Having understood the reasons behind the ‘hate’, we came up with a simple solution to relieve the ‘pain’ for troubleshooters.

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

## WP AJAX Querystring Parameters — De-touched 👋

Since version 2.0.1, the SDK comes with advanced support for multi-site networks. As part of the implementation, we needed a way to identify if an admin notice should be dismissed from the network admin or site-level admin.

Unfortunately, due to WordPress limitations, there’s no way to programmatically know if an AJAX request was initiated from the network or sub-site admin. So, we came up with a simple jQuery snippet that intercepts WP Admin AJAX requests before they are triggered. This enriches them with a querystring flag based on the admin context so that the backend code will have the proper context. We chose this approach because it was the easiest and most efficient code-wise.

Long story short, this implementation raised concerns as it gave the impression that the SDK was monitoring all AJAX requests. While obviously not the case, impressions matter. So, I’m happy to share that we are no longer intercepting admin AJAX requests. The querystring flag is now ***only*** added to AJAX requests triggered by the SDK: [https://github.com/Freemius/wordpress-sdk/pull/578/files](https://github.com/Freemius/wordpress-sdk/pull/578/files)

Thanks Amber C. for continually calling us out on this!

## “Delete” Link to “Disconnect” Update

To reduce confusion, the previously titled *Delete* link shown in the Account page is now titled *Disconnect*:

![Freemius Account Page 'Delete' Link Updated To 'Disconnect'](https://freemius.com/blog/wp-content/uploads/2022/11/freemius-account-page-delete-link-updated-to-disconnect.png)

In addition, the link now shows a confirmation dialog box explaining exactly what the disconnection means:

![Confirmation Dialog Box To Explain What Disconnecting Website Means](https://freemius.com/blog/wp-content/uploads/2022/11/confirmation-dialog-box-to-explain-what-disconnecting-website-means.png)

## What’s Next?

We weren’t able to address all concerns in this iteration, but we are not done and plan to tackle the rest of the items in the next releases 💪

We’re also not done listening and would like to encourage anyone reading this to share any feedback or concerns with us (on any channel). This will help the team address your points and improve the Freemius platform for the entire WordPress community.

We’re available, engaged, and open to great ideas — we look forward to hearing from you.