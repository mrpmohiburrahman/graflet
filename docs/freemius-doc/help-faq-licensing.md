---
title: "Licensing"
url: "https://freemius.com/help/faq/licensing/"
source: "docs"
section: "FAQ"
category: "Licensing"
scraped_at: "2026-04-09T19:58:46+06:00"
word_count: 973
---

## Can I upsell multi-site licenses?[​](#can-i-upsell-multi-site-licenses "Direct link to Can I upsell multi-site licenses?")

Yes. You can set up custom *monthly*, *annual* and *lifetime* pricing for any amount of licenses.

## Can I offer a discount on license renewals?[​](#can-i-offer-a-discount-on-license-renewals "Direct link to Can I offer a discount on license renewals?")

Yes, you can. Keep in mind though, that our annual and monthly plans renew automatically. This means that customers don’t have to take any proactive action to renew the license. In other words, you don’t need to convince the customer to renew. The decision is whether to cancel the license or continue. Unless a customer is unhappy with your plugin or has stopped using it, a renewal discount has no significant effect on that decision.

Therefore, as a rule of thumb, we do not recommend setting a discount for renewals unless your plugin does not provide a continued value (e.g. a migration plugin, or any one-time action plugin). In that case, maybe it is worth setting up a [lifetime price](blog-lifetime-license-for-wordpress-plugins-the-right-way.md).

## Will selecting “deactivate license” under user account in WordPress cancel the billing / subscription?[​](#will-selecting-deactivate-license-under-user-account-in-wordpress-cancel-the-billing--subscription "Direct link to Will selecting “deactivate license” under user account in WordPress cancel the billing / subscription?")

Deactivating the license will not cancel the subscription.

It’s there for cases in which the customer wants to migrate a license to a different installation (for example, when migrating to a different host or domain).

## Can I offer a paid trial to my users?[​](#can-i-offer-a-paid-trial-to-my-users "Direct link to Can I offer a paid trial to my users?")

Yes. You can offer a [Free Trial with a required payment method](help-documentation-selling-with-freemius-free-trials.md) by setting a trial period in your plan settings and then turning on the “Require Credit Card or PayPal” option.

## Can I offer a free trial to my users?[​](#can-i-offer-a-free-trial-to-my-users "Direct link to Can I offer a free trial to my users?")

Yes. You can set a [trial period](help-documentation-selling-with-freemius-free-trials.md) in your plan settings. Just make sure to turn the “Require Credit Card or PayPal” option off.

## Does Freemius support prorating?[​](#does-freemius-support-prorating "Direct link to Does Freemius support prorating?")

Proration handles the increase or decrease to the subscription price when a price changes during any period of a subscription. By default, [Freemius prorates plan updates](help-documentation-selling-with-freemius-proration.md) (upgrades or downgrades).

## What does the license renewal process look like for customers?[​](#what-does-the-license-renewal-process-look-like-for-customers "Direct link to What does the license renewal process look like for customers?")

All plans (besides lifetime / one-time plan) are automatically renewed. For annual plans, the customer will receive a friendly reminder email a month prior to the renewal date, giving them enough time to cancel the subscription, if they wish to do so.

## Can I protect my premium offering if the user cancels the trial or if the trial is over and the user didn’t upgrade?[​](#can-i-protect-my-premium-offering-if-the-user-cancels-the-trial-or-if-the-trial-is-over-and-the-user-didnt-upgrade "Direct link to Can I protect my premium offering if the user cancels the trial or if the trial is over and the user didn’t upgrade?")

If a user got your premium code via a trial but never paid for a license, you can block the premium logic and protect yourself from trial abuse by using the following code:

```php
If ( my_fs()->can_use_premium_code() ) {
    // … premium code ...
}

```

By default, all trials are “blocking” to prevent trial abusement. So if the trial is over/expired and the user didn’t upgrade (or canceled the trial), the premium features will be blocked even if you set your plan to keep the features and only block updates and support:

## How do trials work if I have a free version on WordPress.org?[​](#how-do-trials-work-if-i-have-a-free-version-on-wordpressorg "Direct link to How do trials work if I have a free version on WordPress.org?")

If you have a free version, after 24 hours, a dismissable admin notice with a trial offer will automatically appear in the WP admin dashboard.

Clicking on the “Start free trial” button will redirect the user to the plugin’s in-dashboard pricing page with the option to start a trial with any of the plans. Once the user selects a plan and starts the trial, the premium version is securely accessible through a download link which will appear in an admin notice and in an automated email.

## How do you handle downloads and file hosting?[​](#how-do-you-handle-downloads-and-file-hosting "Direct link to How do you handle downloads and file hosting?")

We securely deliver reliable downloads to valid license holders through our API, utilizing S3 hosting on AWS.

## Do you offer automated recurring/subscription-based billing?[​](#do-you-offer-automated-recurringsubscription-based-billing "Direct link to Do you offer automated recurring/subscription-based billing?")

We support automatic renewals, and encourage software makers to sell subscriptions to build long term sustainable businesses. It increases renewal rate, removes the hassle of payment renewal and increases your bottom line. Freemius monthly and annual plans are both automatically renewed.

## I received a subscription notification without a payment notification, what’s going on?[​](#i-received-a-subscription-notification-without-a-payment-notification-whats-going-on "Direct link to I received a subscription notification without a payment notification, what’s going on?")

Due to the way PayPal’s recurring profiles mechanism works, it can take up to 24 hours until Freemius receives the approval notification for the subscriptions’ initial payment. To keep a smooth purchase experience for customers, Freemius will email the license key and the download link to the paid product – right away.

To mitigate potential abuse, when a customer subscribes to your product the system will issue a 24-hour blocking license. Once we receive the payment notification from PayPal, the license will be extended based on the subscription billing cycle, and the blocking state of the license will be auto-adjusted based on the plan’s configuration.

We could have designed the upgrade process slightly differently, emailing the downloadable product only after the payment approval, but we decided that we aren’t going to “break” a proper subscription UX just because of a small group of trolls that can abuse this PayPal flaw.