Release Notes is our monthly update that highlights the recent product improvements we’ve made, so you can easily stay up to date on what’s new. Here’s what we launched in March.

This product cycle was focused on three main objectives:  
1\. Increasing payments renewal rates  
2\. UX Improvements  
3\. Technical debt – making development on our end more efficient so we can move quicker

## Dunning & Retention

As you already know, we are [big believers in recurring revenues](https://freemius.com/blog/wordpress-agency-subscription-based-income/ "This WordPress Agency Turns Its Custom Plugins/Themes to A Recurring Income") with automatic payment renewals. Hence, the monthly and annual plans developers can use are automatically renewed. Having said that, the fact that the next payment should be automatically billed doesn’t guarantee that the charge will not fail.

There are many reasons for failed payments, the most common ones are credit card expiration, lack of sufficient funds, and credit card reported as stolen.

If you live in the US, I’m sure you have already experienced a stolen credit card. Since I moved to NYC in 2014, I replaced four cards (that’s more than a card a year!). If that’s the common case and you only offer annual plans, there’s a high chance that the annual plan renewal will fail.

### What is Dunning?

Dunning is an intelligent mechanism that emails the customer upon failed payments, with tips on how to fix the problem to recover the failed payments (lost revenue).

### How does Freemius’ Dunning mechanism work?

We’ve implemented a [sequence of 4 emails](https://freemius.com/help/documentation/selling-with-freemius/dunning-failed-payments/) that will notify the customer about the failures in the following schedule:

**1st failed attempt:**  
\* Send a failure email to the customer.  
\* Retry one day after the 1st failed attempt.

**2nd failed attempt:**  
\* Send a failure email to the customer.  
\* Retry three days after the previous failed attempt.

**3rd failed attempt:**  
\* Send a failure email to the customer.  
\* Retry five days after the previous failed attempt.

**4th failed attempt and final:**  
\* Cancel subscription.  
\* Cancel associated license.  
\* Send cancellation email to the customer.

#### Credit Card Subscriptions

If it’s a credit card subscription, the sent emails will contain a direct link to a secure form to update the card:

![Credit Card Subscriptions](https://freemius.com/blog/wp-content/uploads/2017/03/Credit-Card-Subscriptions.png)

Upon credit card update, Freemius will immediately attempt to process the outstanding payment, and will only update the card on success. If it fails, a corresponding error message will be shown to the customer.

#### PayPal Recurring Profiles

Since PayPal’s errors mechanism isn’t as good as Stripe’s, PayPal doesn’t provide an accurate indicator for the failed payment. Therefore, the emails we send to PayPal customers are the same and include instructions on how to fix the common failure issues + how to contact PayPal’s support for a resolution.

At the moment this process runs in the background. We plan to add some metrics to the dashboard so you can get some data about the recovered payments.

### How much does it cost?

Nothing! Dunning is *just* another capability we empower our developers with. As we always say – your success is our success, and that’s inherent in our business model when you monetize with Freemius. So that you know – Dunning services usually start from $50 / mo and can grow to thousands of dollars a year, if you are processing many payments.

## Manual License Renewal for Migrated Plugins & Themes

Last year we introduced a [migration tool from Easy Digital Downloads to Freemius](help-documentation-migration-migrating-from-edd-to-freemius.md), and after working with the [Pootlepress](http://www.pootlepress.com/) team, we also extended the plugin for [migrating from WooCommerce to Freemius](https://github.com/Freemius/edd-migration/tree/feature/woocommerce). Since the release, many of the developers who migrated to Freemius didn’t have automatic renewals in place. So we spent some time thinking how to address those migrated accounts so customers can easily renew their license without a hassle.

Our decision was to extend the checkout logic for license renewals (something we didn’t support before), and also adding a license renewals reminders mechanism that works according to the following schedule:

- 30-days prior to license expiration
- 7-days prior to license expiration
- 48-hours prior to license expiration
- 1-day after license expiration

The sent emails showcase the benefits of the renewal and provide a direct link to secure checkout form. Here’s one of the initial drafts:

![email explaining the benefits of the renewal](https://freemius.com/blog/wp-content/uploads/2017/03/email-explaining-the-benefits-of-the-renewal.png)

## Developers Dashboard:

1. **Performance Optimization:** We made heavy performance optimization so that most dashboard pages will be now loading quicker.
2. **License Sites:** Added the option to show all the sites that are currently utilizing a specific license. Simply click the link under the license’ *Activations* field, and you’ll get a filtered view of all the sites that are using that license:[![filtered view](https://freemius.com/blog/wp-content/uploads/2017/03/filtered-view-1024x40.png)](https://freemius.com/blog/wp-content/uploads/2017/03/filtered-view.png)
3. **Monthly Effective Growth chart:**  
   ![Monthly Effective Growth chart](https://freemius.com/blog/wp-content/uploads/2017/03/Monthly-Effective-Growth-chart-1024x464.png)  
   This is a great indicator to measure the success of your product iterations. Your goal is to make the line go up all the time. If you release a version that triggers a drop, that’s a sign that something isn’t working as expected and you should dive into the uninstallation feedback from data for further investigation.  
   At the moment this feature is not available to developers who are only using the Freemius Insights free tier.
4. **MRR (Monthly Recurring Revenues) Growth** chart:  
   ![Monthly Recurring Revenues Growth chart](https://freemius.com/blog/wp-content/uploads/2017/03/Monthly-Recurring-Revenues-Growth-chart-1024x464.png)  
   MRR is one of the most important bottom line metrics for subscription businesses. Freemius’ MRR analytics will give you a clear view of the composition of MRR movements, providing insights into the health of your business – past, present, and future.  
   Your Net MRR Growth is derived from:  
   **New Business MRR:** New paid conversions  
   **Churn MRR:** Paying customers that have canceled or downgraded to a free plan  
   You want to make sure that your Net MRR (the line chart), is always in the positive section, which means that you added more value in subscriptions than what you’ve lost (churn).
5. **Plugin Icons:** Plugins that have a free version on WordPress.org will now show the plugin icon:  
   ![Plugin Icons](https://freemius.com/blog/wp-content/uploads/2017/03/Plugin-Icons.png)  
   Besides the fact that it’s cool, for developers that are using Freemius on multiple plugins, it makes the experience slightly better when you can identify the plugin without even looking at the title.
6. **Contextual Integration Snippet Updates**: When you now make changes within the dashboard that require changes in the integration code, a window will pop-up with the new code ready for your copy-paste 🙂  
   ![Contextual Integration Snippet Updates](https://freemius.com/blog/wp-content/uploads/2017/03/Contextual-Integration-Snippet-Updates.png)
7. **Automatic Updates Bug Fix:** After receiving a few complaints about customers that were not getting the latest release of the product, we investigated the updates mechanism and found out that the versions ordering mechanism was using “string type sort” which was causing versions like to`1.1.8` be a newer version than `1.1.10`. We fixed that!

## Offering Trials Directly from Your Site

We now officially support trials with a payment method via Freemius Checkout. This means that you can offer an option to try your plugin or theme directly from your site while capturing the user as a lead, as well as their billing information. We chose to invest in trials since we noticed that developers are getting a much higher conversion rate when offering them.

Unlike with an in-dashboard trial, since we can’t know where this trial is going to be utilized, the decision whether to allow the user a trial or not is based on the customer’s email. If the user had already utilized a trial for a certain plugin/theme using the same email, the trial won’t work. If the user tries to use a fake email address just to access the trial, since we only expose the download link and license in the *after upgrade email*, they won’t be able to abuse the trial.

**Fix:** A fix related to trials and the checkout, we now ignore trials when the user types in a 100% discount coupon code.

## WordPress SDK – v.1.2.1.6

The new WordPress SDK introduces new in-dashboard checkout, an optimized localization system, and improved logging. It is available for download here:  
[https://github.com/Freemius/wordpress-sdk/tree/1.2.1.6.1](https://github.com/Freemius/wordpress-sdk/tree/1.2.1.6.1)

### New In-Dashboard Checkout

We have finally deprecated the current in-dashboard checkout and replaced it with the new checkout we use for Freemius Checkout. It will help us to be even agile when it comes to changes and maintenance of the checkout form (only one code base). Plus, the new checkout is written in angular, which makes it more sustainable for the long run.

![New In-Dashboard Checkout](https://freemius.com/blog/wp-content/uploads/2017/03/New-In-Dashboard-Checkout.png)

This also means that the new in-dashboard checkout is now fully responsive! With an optimized mobile UX enabling easy purchase experience from any mobile device.

![optimized mobile UX](https://freemius.com/blog/wp-content/uploads/2017/03/optimized-mobile-UX.png)

Some of you customized the checkout page with custom CSS stylesheet. Before you update to the latest SDK, make sure to adjust the CSS rules to work with the new checkout.

The “legacy” checkout will continue to be fully functional for backward compatibility, but we won’t be extending its functionality anymore, nor fixing any future revealed bugs.

### Security Fixes

1. We discovered that many sites have an exposed filesystem structure when someone types a direct path to a folder without an `index.php` file. Besides the fact that it’s insecure to expose your files/folders structure, search engine crawlers are indexing those pages. Therefore, we’ve added empty `index.php` files to all of the SDK folders.
2. XSS fix. We received a report from a fellow developer ([Marcus Skies](https://twitter.com/marcussykes) from Events Manager plugin) about an unescaped string in the SDK. Indeed, we forgot to escape an optional error message on failed opt-in. The reason we didn’t contact anyone is that the opt-in page is only available to users who have permissions to the WP Admin settings page. So if the user already had login access to that admin page, they are able execute any JavaScript code anyway.

### Translations

1. The SDK is now *almost* fully localized to **Japanese**!!! Many thanks to [Takayuki Miyauchi](https://github.com/miya0001), [@8bitOdyssey](https://github.com/8bitOdyssey), [Hidetaka Okamoto](https://github.com/hideokamoto), [Tomohyco Tsunoda](https://github.com/plastikdreams). The SDK was actually fully localized, but we kept adding more features to the current version which came with additional strings.  
   If you speak another language besides English, be awesome and help us translate the SDK to more languages:  
   [https://www.transifex.com/freemius/wordpress-sdk/dashboard/](https://www.transifex.com/freemius/wordpress-sdk/dashboard/)
2. The WP.org translations mechanism doesn’t support more than one text-domain. I won’t dive deep into the reason why we think it could be improved by supporting more than one, but what this means in practice is that even if you had only a few localized strings in your plugin or theme, by adding the Freemius SDK, the translations mechanism would automatically add hundreds of strings to your product.  
   Since the translation of strings is made per product, they all would have to get translated (even if they were already fully translated on a different plugin or theme, ignoring the translations that the SDK came with).  
   [Joachim Jensen](https://github.com/intoxstudio) helped us solve that problem by wrapping all of the methods in new ones and enriching the Gulp script that extracts the text domain related strings. So from now on, the Freemius SDK strings won’t be extracted by WordPress.org and won’t affect your translations efforts. Thank you @intoxstudio!

### Logging

Due to the complexity of the WordPress SDK that combines synchronous execution, WP-Cron, and AJAX calls. Inline logging is not enough to resolve edge cases. As we grow, the SDK is becoming more and more stable, having said that, we still see issues related to corruption in the Freemius data records. Those edge cases usually require production debugging from our end (WP Admin + FTP Access). We want to reduce those and have investigated more issues on our end. Therefore, we enriched our logger for multi-session persistent DB logging with export capabilities. In plain words, when you **turn on** the debugging mode, the SDK will create a custom logging table and will start storing everything that happens with the SDK (whether it’s synchronous or asynchronous requests). Then, you can download a CSV dump of those logs and send it to us for further investigation. Turning off the debug mode will drop the custom logging table (don’t forget to turn it off!).

![debug mode](https://freemius.com/blog/wp-content/uploads/2017/03/debug-mode-1024x380.png)

#### How to access the debug page?

To access Freemius debug page, go to `https://path.to/site/wp-admin/admin.php?page=freemius`

#### How to turn the debug mode on?

Click the **Debugging** switch:

![the Debugging switch](https://freemius.com/blog/wp-content/uploads/2017/03/the-Debugging-switch.png)

### SDK Misc

### SDK Version Contributors

[Leo Fajardo](https://github.com/fajardoleo)  
[Vova Feldman](https://github.com/vovafeldman)  
[Joachim Jensen](https://github.com/intoxstudio)  
[Rami Yushuvaev](https://github.com/ramiy)