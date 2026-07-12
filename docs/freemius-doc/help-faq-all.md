---
title: "All"
url: "https://freemius.com/help/faq/all/"
source: "docs"
section: "FAQ"
category: "All"
scraped_at: "2026-04-09T19:58:46+06:00"
word_count: 3181
---

## Is Freemius a WordPress.org Compliant?[​](#is-freemius-a-wordpressorg-compliant "Direct link to Is Freemius a WordPress.org Compliant?")

Mos-def! If you are familiar with the [guidelines](https://wordpress.org/plugins/about/guidelines/), you already know that “phoning home” is not allowed without the user’s consent. Therefore, we don’t capture any information without user opt-in. We probably have the most strict opt-in form in the wp.org repo.

## What makes Freemius WordPress.org compliant?[​](#what-makes-freemius-wordpressorg-compliant "Direct link to What makes Freemius WordPress.org compliant?")

We’ve built a special PHP preprocessor that looks into your project’s PHP files and uses the SDK calls in your code as annotations to understand what parts of it should be excluded from the free product version. Then, the preprocessor automatically generates a free version of your plugin by striping away all of its premium code. The free version is the version that should be uploaded to WordPress.org, in order to comply with the [WordPress.org guidelines](https://developer.wordpress.org/plugins/wordpress-org/detailed-plugin-guidelines/).

## Can I use Freemius Insights with EDD or WooCommerce?[​](#can-i-use-freemius-insights-with-edd-or-woocommerce "Direct link to Can I use Freemius Insights with EDD or WooCommerce?")

Absolutely YES! There’s no collision nor interaction between [Freemius Insights](wordpress-insights.md) and other eCommerce solutions. [Freemius Insights](wordpress-insights.md) does not depend on on our monetization solutions. You can add [Freemius Insights](wordpress-insights.md) to both your free and premium plugin versions.

## Can I use Freemius Insights on CodeCanyon and ThemeForest?[​](#can-i-use-freemius-insights-on-codecanyon-and-themeforest "Direct link to Can I use Freemius Insights on CodeCanyon and ThemeForest?")

Yes! It’s compliant with the marketplace rules. In fact, a similar analytics product, called *PressTrends*, was widely adapted by *ThemeForest* and *CodeCanyon* developers in early 2014.

## Can I use Insights in my Premium only plugin or theme?[​](#can-i-use-insights-in-my-premium-only-plugin-or-theme "Direct link to Can I use Insights in my Premium only plugin or theme?")

Yes, you can! In addition, since you are not obligated to any guidelines, you can capture all the information and skip the opt-in screen. If you do so, you would need to explicitly mention that part in your privacy and terms of use. Having said that, since no one actually reads the privacy and terms, we recommend using the opt-in screen as an ethical transparency act.

## Can I use Freemius with my theme?[​](#can-i-use-freemius-with-my-theme "Direct link to Can I use Freemius with my theme?")

Yes! *Freemius* is now fully integrated with themes!

## Will you share the captured emails with someone else?[​](#will-you-share-the-captured-emails-with-someone-else "Direct link to Will you share the captured emails with someone else?")

Your data is safe and sound. We will never-ever, never-ever share your captured user emails with any 3rd party.

## What payment methods can I accept with Freemius?[​](#what-payment-methods-can-i-accept-with-freemius "Direct link to What payment methods can I accept with Freemius?")

We use iDeal (Netherlands), Stripe and PayPal, and therefore accept all major credit cards and PayPal payments. See the list of [supported countries](help-documentation-selling-with-freemius-supported-countries.md).

## Can I customize the opt-in screen?[​](#can-i-customize-the-opt-in-screen "Direct link to Can I customize the opt-in screen?")

We have crafted special filters to customize the messaging and buttons of the opt-in screen. You can also completely edit the PHP template file in the SDK. Make sure you keep it clear about what information is being captured and that it’s sent to *Freemius*. Otherwise, it won’t be compliant with the [WordPress.org guidelines](https://wordpress.org/plugins/about/guidelines/).

## Do I need to set up a gateway to sell with Freemius?[​](#do-i-need-to-set-up-a-gateway-to-sell-with-freemius "Direct link to Do I need to set up a gateway to sell with Freemius?")

Nope. No need for that because Freemius serves as your reseller.

## What currencies do you support?[​](#what-currencies-do-you-support "Direct link to What currencies do you support?")

With Freemius you can sell and receive payments in USD (US dollars), GBP (British pounds), and EUR (Euros). See the list of [supported countries](help-documentation-selling-with-freemius-supported-countries.md).

## Does Freemius store customer credit card numbers on Freemius servers?[​](#does-freemius-store-customer-credit-card-numbers-on-freemius-servers "Direct link to Does Freemius store customer credit card numbers on Freemius servers?")

We aren’t crazy 🙂 Credit Cards do not even “touch” our servers and “speak” directly to Stripe, a well trusted and secure gateway.

## Is Freemius Checkout PCI compliant?[​](#is-freemius-checkout-pci-compliant "Direct link to Is Freemius Checkout PCI compliant?")

Yes, we are PCI compliant; we use PayPal Express Checkout and Stripe.js, and our checkout is secured with an HTTPS protocol.

## Is Freemius In-App/Dashboard checkout PCI compliant?[​](#is-freemius-in-appdashboard-checkout-pci-compliant "Direct link to Is Freemius In-App/Dashboard checkout PCI compliant?")

Yes. Whether the housing site runs securely over HTTPS or not, our In-Dashbord Checkout is loaded securely via a PCI compliant HTTPS iframe.

## Can I customize the in-dashboard pricing and checkout pages?[​](#can-i-customize-the-in-dashboard-pricing-and-checkout-pages "Direct link to Can I customize the in-dashboard pricing and checkout pages?")

The pricing page is automatically generated and styled by Freemius, following WordPress admin dashboard design practices. We make sure it looks natural and optimized for best conversation results.

We have years of experience optimizing conversion, and we use data to continuously improve on the pricing page.

We do provide an option to add custom CSS stylesheets to enable personalization.

You can add those stylesheets in ***Plans*** -&gt; **Customization**:

> Note: For now, we do not recommend using custom CSS since changes in the page HTML structure might break your styles. We’ll try to communicate any changes in the HTML DOM. Having said that, and for the sake of agile development, we do not guarantee notifying you about any changes – it’s up to you to monitor changes.

## Do you support coupons?[​](#do-you-support-coupons "Direct link to Do you support coupons?")

Yes – we support absolute amounts and percentage based [coupons](help-documentation-marketing-automation-special-coupons-discounts.md). You can set up the effective date range of a coupon’s validity, whether the discount should apply for all payments or only for the initial payment, and multiple customization options.

## Does Freemius support EU VAT?[​](#does-freemius-support-eu-vat "Direct link to Does Freemius support EU VAT?")

Yes. Avoid the hassles of EU VAT compliance by having Freemius handle VAT collection, compliance and payments. Utilize support for real-time VAT ID validation and exemption when selling to businesses.

## How much do I have to generate in order volume using Freemius before I can get paid?[​](#how-much-do-i-have-to-generate-in-order-volume-using-freemius-before-i-can-get-paid "Direct link to How much do I have to generate in order volume using Freemius before I can get paid?")

The minimum account balance required for payment is $100.00.

## Can I refund my customers?[​](#can-i-refund-my-customers "Direct link to Can I refund my customers?")

You can refund transactions up to 30 days after the transaction was successfully processed and payment was created. We currently only offer full refunds (no partial refunds). If you’d like to refund a customer after the 30 days refund window is over, we recommend resolving the refund request with your own payment services.

## Do you offer automated recurring/subscription-based billing?[​](#do-you-offer-automated-recurringsubscription-based-billing "Direct link to Do you offer automated recurring/subscription-based billing?")

We support automatic renewals, and encourage software makers to sell subscriptions to build long term sustainable businesses. It increases renewal rate, removes the hassle of payment renewal and increases your bottom line. Freemius monthly and annual plans are both automatically renewed.

## How long will it take until the customer sees the refund?[​](#how-long-will-it-take-until-the-customer-sees-the-refund "Direct link to How long will it take until the customer sees the refund?")

While some refunds may be instantaneous, credit refunds can take 5–10 business days to show up in their customer’s credit card statement.

## What happens if a customer disputes a payment / chargeback?[​](#what-happens-if-a-customer-disputes-a-payment--chargeback "Direct link to What happens if a customer disputes a payment / chargeback?")

The payment amount will be temporarily be held and we’ll contact you ASAP, giving you the chance to resolve the dispute directly with the customer.

If the dispute isn’t resolved, we’ll step inup and handle each case individually.

- If the dispute is resolved in your favor, you are all good.
- If the dispute is resolved in favor of the customer, the held amount will be refunded to the customer.
- If it was a bank dispute (via Stripe), chargebacks incur a fee of $15 which will be deducted from your balance.

## Do you offer specialized pricing for micro-transactions like on Apple’s App Store or Google’s Android Market?[​](#do-you-offer-specialized-pricing-for-micro-transactions-like-on-apples-app-store-or-googles-android-market "Direct link to Do you offer specialized pricing for micro-transactions like on Apple’s App Store or Google’s Android Market?")

The recommended minimum price per transaction is $3.99. Otherwise, your processing fee will be as high as 30%-50% due to the minimum per transaction rates charged by Stripe and PayPal. [Email us](https://freemius.com/cdn-cgi/l/email-protection#4c3f393c3c233e380c2a3e29292125393f622f2321) to discuss your specific situation.

## How do you handle downloads and file hosting?[​](#how-do-you-handle-downloads-and-file-hosting "Direct link to How do you handle downloads and file hosting?")

We securely deliver reliable downloads to valid license holders through our API, utilizing S3 hosting on AWS.

## What provision is there for users to export their data if they wanted to leave the platform?[​](#what-provision-is-there-for-users-to-export-their-data-if-they-wanted-to-leave-the-platform "Direct link to What provision is there for users to export their data if they wanted to leave the platform?")

Many marketplaces choose to hide their customers’ data from developers and “lock them” inside the platform.

We believe that the data belongs to the developers. If a developer decides to leave the platform for any reason whatsoever, he/she can easily download their user-list from our dashboard with one click, and they can access all of their data by leveraging our RESTful API for migration purposes.

## Can I customize the ‘From’ addresses of the email messages sent by Freemius?[​](#can-i-customize-the-from-addresses-of-the-email-messages-sent-by-freemius "Direct link to Can I customize the ‘From’ addresses of the email messages sent by Freemius?")

Yep – you can do that in the ‘Email Addresses’ section.

## Do you support affiliates?[​](#do-you-support-affiliates "Direct link to Do you support affiliates?")

Yes we do! Freemius comes with a fully-featured [Affiliation Platform](help-documentation-affiliate-platform.md) which you can utilize to onboard and manage affiliates.

## What does the license renewal process look like for customers?[​](#what-does-the-license-renewal-process-look-like-for-customers "Direct link to What does the license renewal process look like for customers?")

All plans (besides lifetime / one-time plan) are automatically renewed. For annual plans, the customer will receive a friendly reminder email a month prior to the renewal date, giving them enough time to cancel the subscription, if they wish to do so.

## How can I send emails to my users and customers?[​](#how-can-i-send-emails-to-my-users-and-customers "Direct link to How can I send emails to my users and customers?")

We don’t provide a custom emailing mechanism. We might offer this option in the future as an additional paid package.

For now, the best way is to either download the ‘users list’ file from the ***Users*** section in the dashboard,

or leverage our [webhooks mechanism](help-documentation-marketing-automation-events-webhooks.md) by pushing users’ details, including emails addresses, to mailing platforms such as MailChimp or Customer.io.

## Does Freemius support prorating?[​](#does-freemius-support-prorating "Direct link to Does Freemius support prorating?")

Proration handles the increase or decrease to the subscription price when a price changes during any period of a subscription. By default, [Freemius prorates plan updates](help-documentation-selling-with-freemius-proration.md) (upgrades or downgrades).

## Can I offer a free trial to my users?[​](#can-i-offer-a-free-trial-to-my-users "Direct link to Can I offer a free trial to my users?")

Yes. You can set a [trial period](help-documentation-selling-with-freemius-free-trials.md) in your plan settings. Just make sure to turn the “Require Credit Card or PayPal” option off.

## How do trials work if I have a free version on WordPress.org?[​](#how-do-trials-work-if-i-have-a-free-version-on-wordpressorg "Direct link to How do trials work if I have a free version on WordPress.org?")

If you have a free version, after 24 hours, a dismissable admin notice with a trial offer will automatically appear in the WP admin dashboard.

Clicking on the “Start free trial” button will redirect the user to the plugin’s in-dashboard pricing page with the option to start a trial with any of the plans. Once the user selects a plan and starts the trial, the premium version is securely accessible through a download link which will appear in an admin notice and in an automated email.

## Can I offer a paid trial to my users?[​](#can-i-offer-a-paid-trial-to-my-users "Direct link to Can I offer a paid trial to my users?")

Yes. You can offer a [Free Trial with a required payment method](help-documentation-selling-with-freemius-free-trials.md) by setting a trial period in your plan settings and then turning on the “Require Credit Card or PayPal” option.

## Is your SDK RTL compliant?[​](#is-your-sdk-rtl-compliant "Direct link to Is your SDK RTL compliant?")

Yes, it is.

## Under the “Sites” menu, what is the difference between “Plan” and “Is Premium”?[​](#under-the-sites-menu-what-is-the-difference-between-plan-and-is-premium "Direct link to Under the “Sites” menu, what is the difference between “Plan” and “Is Premium”?")

If you name your paid plan as **“Premium”** you might get a little confused with the terminology. The data under the plan column shows the current plan of the install. **“Is Premium”** tells if that site is running the *free* or the *premium* code version of your module.

## Will selecting “deactivate license” under user account in WordPress cancel the billing / subscription?[​](#will-selecting-deactivate-license-under-user-account-in-wordpress-cancel-the-billing--subscription "Direct link to Will selecting “deactivate license” under user account in WordPress cancel the billing / subscription?")

Deactivating the license will not cancel the subscription. It’s there for cases in which the customer wants to migrate a license to a different installation (for example, when migrating to a different host or domain).

## What languages is your WordPress SDK translated to?[​](#what-languages-is-your-wordpress-sdk-translated-to "Direct link to What languages is your WordPress SDK translated to?")

You can check out all of the supported languages and help us translate the SDK (we know you want to be on our hall of fame 😉 ) on our [Transifex translations manager](https://www.transifex.com/freemius/wordpress-sdk/).

## How to switch the language on the pricing and checkout pages in the dashboard?[​](#how-to-switch-the-language-on-the-pricing-and-checkout-pages-in-the-dashboard "Direct link to How to switch the language on the pricing and checkout pages in the dashboard?")

This is a work in progress. Currently, the pricing and checkout pages are only in English. Making them translatable is part of our roadmap.

## Can I protect my premium offering if the user cancels the trial or if the trial is over and the user didn’t upgrade?[​](#can-i-protect-my-premium-offering-if-the-user-cancels-the-trial-or-if-the-trial-is-over-and-the-user-didnt-upgrade "Direct link to Can I protect my premium offering if the user cancels the trial or if the trial is over and the user didn’t upgrade?")

If a user got your premium code via a trial but never paid for a license, you can block the premium logic and protect yourself from trial abuse by using the following code:

```php
If ( my_fs()->can_use_premium_code() ) {
    // … premium code ...
}
```

By default, all trials are “blocking” to prevent trial abusement. So if the trial is over/expired and the user didn’t upgrade (or canceled the trial), the premium features will be blocked even if you set your plan to keep the features and only block updates and support:

## Can I offer a discount on license renewals?[​](#can-i-offer-a-discount-on-license-renewals "Direct link to Can I offer a discount on license renewals?")

Yes, you can. Keep in mind though, that our annual and monthly plans renew automatically. This means that customers don’t have to take any proactive action to renew the license. In other words, you don’t need to convince the customer to renew. The decision is whether to cancel the license or continue. Unless a customer is unhappy with your plugin or has stopped using it, a renewal discount has no significant effect on that decision.

Therefore, as a rule of thumb, we do not recommend setting a discount for renewals unless your plugin does not provide a continued value (e.g. a migration plugin, or any one-time action plugin). In that case, maybe it is worth setting up a [lifetime price](blog-lifetime-license-for-wordpress-plugins-the-right-way.md).

## Can I upsell multi-site licenses?[​](#can-i-upsell-multi-site-licenses "Direct link to Can I upsell multi-site licenses?")

Yes. You can set up custom *monthly*, *annual* and *lifetime* pricing for any amount of licenses.

## Are there any additional fees for receiving payments through PayPal?[​](#are-there-any-additional-fees-for-receiving-payments-through-paypal "Direct link to Are there any additional fees for receiving payments through PayPal?")

PayPal payment transfers to U.S.-based accounts are free. For payment transfers to non-U.S. accounts, PayPal incorporates a 2% fee (maximum of $20 USD).

## What will my customers see on their Credit-Card and PayPal statement?[​](#what-will-my-customers-see-on-their-credit-card-and-paypal-statement "Direct link to What will my customers see on their Credit-Card and PayPal statement?")

Customers who purchase your product through Freemius will receive a credit card statement showing your product’s name.

For PayPal transactions, the store name will appear as your product’s name. However, PayPal email notifications will state Freemius and include your product description in the plan details. Unfortunately, PayPal does not offer a way to customize this further.

## I received a subscription notification without a payment notification, what’s going on?[​](#i-received-a-subscription-notification-without-a-payment-notification-whats-going-on "Direct link to I received a subscription notification without a payment notification, what’s going on?")

Due to the way PayPal’s recurring profiles mechanism works, it can take up to 24 hours until Freemius receives the approval notification for the subscriptions’ initial payment. To keep a smooth purchase experience for customers, Freemius will email the license key and the download link to the paid product – right away.

To mitigate potential abuse, when a customer subscribes to your product the system will issue a 24-hour blocking license. Once we receive the payment notification from PayPal, the license will be extended based on the subscription billing cycle, and the blocking state of the license will be auto-adjusted based on the plan’s configuration.

We could have designed the upgrade process slightly differently, emailing the downloadable product only after the payment approval, but we decided that we aren’t going to “break” a proper subscription UX just because of a small group of trolls that can abuse this PayPal flaw.

## How can I get paid? How do I get my earnings?[​](#how-can-i-get-paid-how-do-i-get-my-earnings "Direct link to How can I get paid? How do I get my earnings?")

There are currently four payment methods available for you to collect your earnings from Freemius:

1. PayPal (default payment method, using PayPal MassPay)
2. Payoneer
3. Wire transfer (international and domestic / IBAN / SWIFT)
4. Wise (formerly TransferWise)

International wires can be converted to your local currency. Due to our high volumes we’ve managed to negotiate great terms with our bank for currency conversion-rates and a complete fee waiver on foreign-currency international wire.

## Why is the active installs metric on WordPress.org different than the one on Freemius?[​](#why-is-the-active-installs-metric-on-wordpressorg-different-than-the-one-on-freemius "Direct link to Why is the active installs metric on WordPress.org different than the one on Freemius?")

There’s a fundamental difference in the way WordPress.org and Freemius count active installs.

Based on publicly available responses from key people in the WordPress meta team, the WordPress.org active installs counter relies on the WordPress.org updates mechanism, which is sampled on a weekly basis. Updates are triggered only when there’s traffic to the site, so if a site installed your plugin or theme and did not get any traffic during that sampling period OR, if the updates mechanism is blocked (or turned off), this site will not get counted. Also, we suspect that the WordPress.org sampling relies on domains and not on IPs. In that case, for example, all of the VVV installs that installed your product will only be counted as a single site.

On the other hand, Freemius uses real actions such as an explicit opt-in or deactivation/uninstall events. One fallback of that tracking methodology is if a user hard-deletes the product from the filesystem, using FTP/SSH, it is still considered active.