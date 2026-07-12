I’m glad to share these Release Notes including some unique upgrades to the Developer Dashboard – most of which are a response to community requests. The revamped Earnings page lets you better forecast the amount of your next payouts; there’s now a centralized Email Notifications Center; and you can now easily promote your positive reviews with nicely designed shareable review cards. That’s not all though – keep reading for more surprises 🎁

Here’s a shoutout to our partner [Luke Seager](https://www.linkedin.com/in/lukeseager/) for proposing great UI suggestions that we implemented on the earnings page, which you can find below.

Besides updating the layout, the earnings page now fully supports multi-currency and we added an estimated balance that is calculated daily in order for developers to gauge how much they’ll be making each month.

![Freemius Developer Dashboard Revamped Earnings Page](https://freemius.com/blog/wp-content/uploads/2021/01/freemius-developer-dashboard-revamped-earnings-page.png)

Since the initial update, we’ve improved the estimated balance calculation even further to make it more precise for developers who are still under the $5,000 threshold in lifetime sales because the estimated balance now takes into account unpaid gross.

## Email Notifications Center

After many requests from partners to have more control over the different types of emails Freemius sends, we organized all of the emails into the Emails Notification Center. Any time we add a new automated email to the platform, we’ll add it in here. Keep in mind that some transactional emails, like payment notifications, are required and cannot be disabled.

![Freemius Developer Dashboard Email Notification Center](https://freemius.com/blog/wp-content/uploads/2021/01/freemius-dashboard-notifications-management.gif)

The goal is to finally have one place where you can see all the emails we are sending and achieve centralized notification management.

## Shareable Review Cards

Each time your product gets a review from a paying customer, we automatically send an email with the review content.

We started to notice that developers were taking screenshots of the review emails in order to share them on social media or for other marketing purposes. To improve the “hacky” approach of taking a screenshot from the email, we created something easier to use, more visually appealing, and more professional: You can now click “Get Shareable Card” in the automated email:

![Freemius New Review Notification Email with Shareable Cards](https://freemius.com/blog/wp-content/uploads/2021/01/freemius-new-review-notification-email-with-shareable-cards.png)

And you’ll get this nicely designed (dynamically generated) review card to share wherever you’d like:

![Freemius Shareable Review Cards](https://freemius.com/blog/wp-content/uploads/2021/01/freemius-shareable-review-cards.png)

All your current reviews also have Shareable Cards now available in the Reviews section:

![Freemius Developer Dashboard Link to Shareable Review Cards](https://freemius.com/blog/wp-content/uploads/2021/01/freemius-developer-dashboard-link-to-shareable-review-cards.png)

## Site Plugins & Themes Data

Plugin and theme data is now finally exposed so you can see what plugins and themes are installed on your users sites (those who permitted it), and the latest [WordPress SDK 2.4.1 fixed the bug](blog-release-notes-wordpress-sdk-2-4-1-deployment-composer-dkim-login-as-user-security.md#improved_plugin_theme_data_collection) that showed all plugins as “inactive” for all sites.

![Freemius Developer Dashboard Sites Plugins and Themes Data](https://freemius.com/blog/wp-content/uploads/2021/01/freemius-developer-dashboard-sites-plugins-and-themes-data.gif)

## Coupon Enhancements

We received several useful requests to enhance our coupon capabilities for [Black Friday + Cyber Monday 2020](blog-bfcm-2020-wordpress-plugins-themes.md), so we implemented as many as we could:

### Coupons Timezone Selection

Previously, the coupons promotional date range selection was limited to the GMT timezone. If you know that most of your customers are concentrated in specific markets, like the US, the GMT timezone is actually not a very good option, so you can now specify the coupons effective timezone as you wish.

### Coupons for New vs Existing Customers

One of the main reasons to offer aggressive discounts on holidays like BFCM is to win new customers.

The problem with most coupon engines is that you either offer a discount to everyone or to nobody. However, there’s no way to segment your offers based on whether the customer is new or current.

I’m pumped to share that you can now target your coupons according to different segments of your users. This new option allows you to create a single coupon code that, for example, will provide a 50% discount to new customers and a 30% discount to existing customers. That way, you can lure more new customers while still appreciating your existing ones.

### Coupons Search

Because we’ve observed the volume of coupons increasing over the years as more and more developers run seasonal promotions more frequently, we’ve added a search mechanism that lets you search based on ID or the coupon code.

### Coupons for Migrated Subscription Licenses

We now support the ability to apply coupons to migrated subscription licenses, something that previously was only supported when migrating the payments data as well.

### New Flags for Preventing Purchase of Non-discounted Packages

To avoid distractions and potential mistakes of buying a non-discounted package when running special deals that are only applicable for a specific billing cycle and/or license-level, we added two new flags to the Checkout API: `hide_billing_cycles` and `disable_licenses_selector`. The new params can be found [here](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md).

### Coupon Notes

You can now add notes to coupons to remind you about special use-cases or linking to your support history. The data stored here is not searchable (yet).

![Freemius Developer Dashboard Coupon Notes](https://freemius.com/blog/wp-content/uploads/2021/01/freemius-developer-dashboard-coupon-notes.png)

## User Notes

We’ve also added the ability to include internal notes about your customers to help document the relationship, like support tickets, reminders about who they are, etc. This data is also not yet searchable, but it is easily accessed just by navigating to a User’s profile.

![Freemius Developer Dashboard User Notes](https://freemius.com/blog/wp-content/uploads/2021/01/freemius-developer-dashboard-user-notes.gif)

## Webhooks failures mechanism enhancement

If you’re using [webhooks to automate your marketing](help-documentation-marketing-automation-events-webhooks.md) and the webhooks are failing for any reason, we’ll now notify you every 20th failure, and then automatically disable the webhook on the 100th failure. Previously, we would only notify developers at the 100th failure and simultaneously disable the webhook, so now there’s more awareness of what might be happening in the background, giving you enough time to address the issue before the webhook is auto-disabled.

## We’re Working Hard for YOU!

As your trusted monetization team, we’re constantly looking for ways to optimize the platform so you can easily monetize your plugins or themes and sustainably grow your sales revenue. If you’re interested to keep up to date about our platform, subscribe to our blog and get future Release Notes in your inbox.