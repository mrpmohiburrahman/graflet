This release is packed full of great updates, including Advanced Checkout Tracking to give you the ability to track many aspects of the checkout (like time to complete, coupon usage, and more); events have been added to our newly improved subscription and license management tools, and we’ve added a psychological tactic in our Automated Emails “Fear of Losing Out” to inform users they may miss out on their current pricing if they fail to add an updated payment method. Much more inside, so let’s jump in.

### Advanced Checkout Tracking

We enriched the Checkout’s JS API so you can tap into [different actions](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md#advanced_event_tracking_new) taken by the user while they are checking out. The new `track( event, data )` callback handler allows you to do advanced event tracking for all kinds of cool things.

Here’s an example of how you might use the events: When a user gets to the review order section (after filling up their payment method and just before completing the purchase), the checkout will trigger a `review-order` event. You can “listen” to this event, and if the user doesn’t complete the purchase within 30 sec, you can trigger a chat notification with a “How can I help?” message to help seal the deal.

If you end up using checkout events (or just have ideas), please tell us about it so we can inspire other community members about interesting use-cases/practices.

### After Checkout Redirect

Some developers are selling from their websites by linking directly to the checkout page as opposed to using our [JS API](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md) to open the checkout in a dialog box embedded on their site.

After receiving some feedback about the checkout process (which showed an empty page to buyers that confirms they received the after-purchase confirmation email), we’ve now set it to redirect back to the referrer by default. So, customers who complete checkout will now be directed back to your site automatically.

### Secure Checkout Badge

At the top of the Checkout, we’ve added a Secure Checkout Badge, which is in addition to those from 3rd parties that appear at the bottom of the checkout form (SSL, etc).

This was another update requested from the community to increase potential buyers confidence to complete a purchase by making it clear, right on top, that the checkout is secure.

![Freemius Secure Checkout Badge](https://freemius.com/blog/wp-content/uploads/2021/01/freemius-secure-checkout-badge.png)

### Preventing Duplicate Purchases

We introduced a mechanism to block duplicate purchases by validating there’s no other purchase that was processed by the same buyer in the last 60 sec. If we do find another purchase a corresponding error will be shown:

![Notice About Preventing Duplicate Purchases on the Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2021/01/notice-about-preventing-duplicate-purchases-on-the-freemius-checkout.png)

## Events Added for Trials & Subscription Cancellations

When users cancel their trials or subscriptions via the User Dashboard, they’re requested to leave a reason for doing so.

While this data isn’t stored anywhere, if you are using our [webhooks mechanism](help-documentation-marketing-automation-events-webhooks.md), you can now take advantage of the reasons reported in your marketing automations with the `install.trial.cancelled` and `subscription.cancelled` [events](https://gist.github.com/vovafeldman/e27df1fd6d5785f980e4cc5765496e38).

One example use case here is to send a coupon to users who cancel, incentivizing them to continue with their signup after the free trial or the subscription renewal. Keep in mind that if you’ve set up [Special Coupons](blog-release-notes-special-coupons.md), Freemius can automatically send a subscription recovery email that includes a coupon 30 days before a cancelled renewal was supposed to take place, however, this event lets you take care of that use-case yourself, in addition to many others.

This is another “hidden”, yet super-powerful way to automate your marketing and minimize churn, and we’re constantly looking for these opportunities 💰

## Optionally Extend a Subscription when Extending a License

Previously, extending a license that is associated with an active subscription didn’t adjust the next billing date of the subscription, leading to users getting billed earlier than expected when their license had previously been extended.

These extra options will now display if there is an active subscription when extending a license:

![Freemius Developer Dashboard Extend License and Update Subscription Renewal Date](https://freemius.com/blog/wp-content/uploads/2021/01/freemius-developer-dashboard-extend-license-and-update-subscription-renewal-date.png)

There are many reasons why a developer may need to extend a license, such as when a user requests an extension to their trial period, and it’s logical that the associated subscription next billing date should be updated in some situations, so you can now optionally postpone the next billing date when extending a license expiration date for a free trial or active subscription.

![Freemius Developer Dashboard Extend Trial License and Update 1st Payment Date](https://freemius.com/blog/wp-content/uploads/2021/01/freemius-developer-dashboard-extend-trial-license-and-update-1st-payment-date.png)

It should be noted that you can’t “advance” a subscription renewal when advancing a license expiration, which is an intentional restriction because there is little to no reason why this would be needed, and it may open up risk for charging customers too early.

If we’ll see there is a need to support the option to advance renewal payments, we’ll look into a more structured and secure way to make this happen.

Extending a license to lifetime will automatically cancel the subscription:

![Freemius Developer Dashboard Extend License to Lifetime and Cancel Subscription](https://freemius.com/blog/wp-content/uploads/2021/01/freemius-developer-dashboard-extend-license-to-lifetime-and-cancel-subscription.png)

### The PayPal Exception

Unfortunately, PayPal doesn’t support updates to subscription renewal schedules after the first payment for that subscription has been processed.

That being said, our current PayPal integration charges the 1st payment as a “setup fee”, so if you are selling annual/monthly subscriptions, you’ll still be able to postpone the renewal during the first year/month of the subscription (assuming the subscription didn’t have a trial period, in which case the trial period is the “setup” period, and the fee at the end of the trial is the first subscription payment).

And don’t worry, you don’t need to check the subscription before attempting to update its next billing date, we’ll show you an error when the update is not supported right in the dialog box.

## FOLO Warning about Possible Price Increases on Subscription Renewal Failure

We now include a FOLO (Fear of Losing Out) message about potential price increases if a subscription renewal fails, which should encourage more people to fix their payment details to avoid the cancellation of their subscription and keep their current pricing.

Furthermore, to make it even easier to identify the problem card and to reduce suspicion of a fraudulent phishing attack, the card type and last 4 digits are included in the Failed Payment Notice sent to customers:

![Freemius Failed Payment Notice including payment details and fear of losing out on current pricing notice](https://freemius.com/blog/wp-content/uploads/2021/01/freemius-failed-payment-notice-including-payment-details-and-fear-of-losing-out-on-current-pricing-n.png)

## Dispute Email Notifications to Keep you Up to Date

We introduced a set of notifications to keep you in the loop about everything going on with your disputed payments, so expect to receive notifications when:

- A charge is disputed by a customer
- A dispute is canceled by a customer
- A dispute is lost (ruled in favor of the customer)
- A dispute is won (ruled in our favor)

All of these emails can be enabled/disabled in the new [Email Notification Center](blog-release-notes-developer-dashboard-email-notification-center-shareable-reviews.md).

Please note that you may encounter cases where you receive a ruling about a dispute without ever receiving any prior notifications about the disputed payment. We’ve seen this happening mostly with PayPal as their IPN (webhooks) mechanism is unreliable, and sometimes they simply don’t send us the dispute opening event.

## Filter Payments by Disputes & Chargebacks

You can now easily filter to see the disputed payments and chargebacks that were created due to lost and won disputes that were ruled in your favor, which makes the dispute process more transparent.

Eventually, we hope to automate evidence submission from developers and streamline the entire dispute resolution process even further to minimize lost disputes as much as possible while maximizing your control over the process.

![Payments Filter for Disputes, Chargebacks, and Won Disputes](https://freemius.com/blog/wp-content/uploads/2021/01/payments-filter-for-disputes-chargebacks-and-won-disputes.gif)

We also introduced a little icon as an indicator to indicate the type of the payment:

![Freemius Developer Dashboard Payments Type Icon Indicator](https://freemius.com/blog/wp-content/uploads/2021/01/freemius-developer-dashboard-payments-type-icon-indicator.png)

Up until now, we attributed disputed payments to your earnings balance and deducted those only when they turned into chargebacks after receiving the official ruling from the bank; which sometimes can take 2-3 months. But recently we identified an attacker who abused that mechanism by committing dispute fraud. Therefore, we are already updating the logic to be consistent with the disputes logic of payment gateways – a payment will get deducted from your balance once it’s disputed, and it will get credited back after the dispute is resolved in your/our favor.

## Invoices Now Clearly Marked as Paid + Include Payment Deets

Invoices are now enriched with the payment method details + a PAID label to make it clear that the invoice was already paid. Some customers (perhaps with separate accounting or billing departments) were getting confused as to which invoices had been paid or not, and some were even sending checks to our US address to invoices that were already paid. This added transparency helps to prevent confusion and will save time for you and your customers.

![Freemius Invoices Marked as Paid and including Payment Method Details](https://freemius.com/blog/wp-content/uploads/2021/01/freemius-invoices-marked-as-paid-and-including-payment-method-details.png)

## PayPal Paid Trials Fix

We received some reports about PayPal trials converting to subscriptions hours prior to their expected time. After thorough investigation and several exchanges with PayPal’s support, it appears that there’s no guarantee about the hour PayPal will process the 1st payment of a trial, as they are running those in batches.

To mitigate the issue, we are now creating all PayPal trials with an extra day until their 1st payment, as well as extending the initial blocking license by a day.

We now have to “force” the trial period to include an extra day to prevent customers from potentially being charged too early by PayPal. The point is that we now 100% avoid charging customers before they expect it, and the downside is they may get up to an extra 24 hours on their trial if they signed up for a trial with PayPal. Unfortunately, our hands are tied on this one and limited by PayPal’s batch mechanism.

Regardless, the Freemius automated email is sent on time, so customers shouldn’t have confusion about the fact that they will be charged imminently if they have not already by the time they receive that email.

## Germans can Now Checkout with Subscriptions on PayPal

Due to regulatory reasons, PayPal didn’t support recurring profiles (subscriptions) for German accounts for years. Therefore, we were hiding the option to checkout with PayPal for Germans to avoid unexpected issues.

However, recently [@Sanjip Shah](https://twitter.com/sanjipshah) pinged us on Slack saying he spotted two German customers that managed to “trick” the checkout by switching the billing cycle to lifetime and then back to annual, allowing them to subscribe.

We immediately contacted our account manager at PayPal, who, unsurprisingly, wasn’t even aware of the issue. She helped us get an official answer from PayPal’s engineering team, and apparently the restriction was removed somewhere in early 2019.

No one updated the merchants 🤦

There’s no public evidence of this change. Nothing. Moreover, our dev team spent over a month of work on adjusting our infrastructure for supporting “manual subscriptions” (where a customer needs to manually renew every billing cycle), which is still in an ongoing code-review.

To make a long story short, [@Patrick Posner](https://twitter.com/patrickposner_), a partner from Germany with a German PP account, helped us test and verify that things work as expected, and we already pushed the update.

So, effective immediately, PayPal works for Germans. This is AMAZING news because PayPal is way more popular in Germany than credit cards, so expect your German subscriptions to go up.

## EU VAT Rate Changes

On July 1st, [Germany reduced their VAT rate from 19% to 16% for COVID relief](https://freemius.com/blog/eu-vat-rate-change-covid-19-digital-product-sellers/). This impacted subscriptions that were created prior to the change, and also some payments that were processed during July and August, since we only discovered the change in mid-Aug.

After a bunch of research and scripting, I’m happy to share that all subscriptions that were created prior to the VAT rate change have been updated to use the new rate. Also, we partially refunded the VAT difference for payments that were processed with the wrong VAT rate. And since the VAT relief period was over this month, subscriptions created during the relief period were also updated to incorporate a 19% rate instead of 16%.

Ireland is the 2nd EU country to follow, on September 1st they reduced their VAT rate from 23% to 21%, which will stick for the next 6 months.

## Stay in the Know!

We regularly share release notes covering our latest platform updates, so subscribe to our blog to stay up to date and get these updates in your inbox.