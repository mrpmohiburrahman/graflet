In the past few months, I’ve stumbled across multiple online discussions among WordPress plugin and theme developers on how hard it is to win Stripe/Credit-Card Disputes. So much so, that many developers gave up on dealing with them entirely, as they feel it isn’t worth their time. We were in the same boat when we just started [Freemius](index.md), averaging at about a 4% success rate. Over the years, we managed to develop various and unique techniques that helped us increase our Credit Card Disputes winning success rate by 740% (from 4% to 29.6%), and almost without losing any PayPal Dispute and recovering most of the Chargeback.

Since I couldn’t find a benchmark for the Avg. success rate of winning CC Disputes (Credit Card Disputes) in the WordPress ecosystem, I conducted a poll on [Selling WordPress Products](https://www.facebook.com/groups/sellingwpproducts/) (a great Facebook group for WordPress product people selling plugins, themes, and SaaS), to gauge the market. Here are the results:

![Poll results on Credit Card Disputes via the "Selling WordPress Products" group](https://freemius.com/blog/wp-content/uploads/2018/09/Poll.png)

Reference: [https://www.facebook.com/groups/sellingwpproducts/permalink/1222125077927552/](https://www.facebook.com/groups/sellingwpproducts/permalink/1222125077927552/)

I got 34 responses from a wide range of sellers from different countries and product types. So it makes for a solid representation of the market:

- 44% indicated that their success rate in winning CC (Credit Card) Disputes is less than 5%
- 26.5%, including the CEOs of [WPML](https://wpml.org) & [ThemeIsle](https://themeisle.com), admitted they ignore CC Disputes entirely because it isn’t worth their time
- 11.7% said their success rate is between 5% to 10%
- 5.8% never won a CC Dispute case
- Nirav, the founder and CEO of [StoreApps](https://www.storeapps.org/) managed to optimize their evidence submission process to yield a success rate of 36%-50% – which is super impressive.
- There were also 3 sellers that claim they manage to win more than 50% of the Credit Card Dispute cases. When I tried to dive in and get an exact number and understand how – I didn’t get clear explanations. While it is possible, I’m a little skeptical. My guess is that they mixed their stats with PayPal Disputes which are much easier to win or maybe based their vote on rough estimation and gut feeling, which we all know can be misleading.

Bottom line, even if we take those 3 votes into account, assuming it’s a solid representation of the ecosystem, we are performing significantly better than most of the WordPress theme shops and plugin businesses, and we are getting better and better at it all the time.

If you follow our content you already know that in the spirit of open-source, we try to share as much of the know-how we gain along the way with the community so we can all get better and build a more sustainable WordPress business ecosystem. So the main goal of this guide is to help you improve at winning CC Disputes for your plugins/theme business by sharing the proven tactics we use to win at 29.6% of the cases at Freemius.

Before we dive into the actionable tactics, it’s important to understand if/why you should care about Disputes, why it’s so damn hard to win them, how Credit Card Disputes differ in the WordPress sphere, and the reasons why handling Disputes is actually important for the long run.

## Should You Care About Credit Card Disputes When Running A WordPress Plugins/Themes Business?

Disputes are inevitable. The more payments you process, the more disputes you get. Based on [Chargebee’s Credit Cards Processing Stats](https://www.chargebee.com/resources/guides/credit-card-processing-statistics/), a CyberSource Fraud Benchmark Study revealed that the average Credit Card Dispute Rate is 0.5-0.8%, with an industry-standard maximum of 1%.

Chargebee’s stats also reference a Consumer Insights Survey from chargeback.com, which shows that 6 out of 10 customers admit that they’re unaware of a store’s return policy at the time of purchase and 8 out of 10 customers admit to filing a chargeback out of convenience.

So even if you process a few payments a month today, if you plan to grow your business you should at least start planning on seeding the fundamental mechanisms, which will eventually save you money and a LOT of time.

In countries like the US, where Credit Card Fraud is an epidemic, submitting Credit Card Disputes is ridiculously easy. Two mouse clicks on the bank’s website and you get the money back, that’s it! No questions asked. The banks and the Credit Card companies optimized the CC Disputes submission process in a way that it’s cheaper to reissue and mail new Credit Cards across the country while transferring the loses to the businesses.

## Why Are Credit Card Disputes Mostly Ruled In Favor Of The Customer?

You may ask yourself why would you ever lose a CC Dispute if you operate legally, follow all the regulations, and only charge customers when they actually buy your plugin/theme or when there’s a subscription renewal, and that’s a totally legitimate question. To answer that question, it is important to understand how Credit Card Disputes and chargebacks work, as well as the dynamics of the figures involved in the process.

When your customers submit a Dispute to their Credit Card company or bank, they are basically claiming that they were wrongfully charged for a specific payment on their statement. The reasons may vary and I’ll cover them further down the article. Their dispute triggers the bank/credit card company to immediately refund the payment, AKA “chargeback”, which will be deducted from your business’ balance, without questioning the customer, and you’ll have a limited time frame (usually 10 business days) for submitting evidence to prove you are “not guilty”. So basically, the burden of proof is on YOU.

[![Freemius credit cards dispute diagram](https://freemius.com/blog/wp-content/uploads/2018/09/freemius-credit-cards-dispute-diagram.jpg)](blog.md)

Remember, the customer’s bank and Credit Card company have (almost) no relationship with you. The risk of upsetting their customer and losing them for a competing bank/credit-card company vs. you stopping to process VISA transactions, for example, is much higher. So by nature, these financial institutions are automatically in favor of THEIR customer, and not your business. Therefore, to win a Credit Card Dispute you’ll have to convince the “jury” (the representative of the financial institution) that it is the customer that is “guilty” without a doubt, and not your business. Even the slightest doubt will cause a ruling in favor of the customer (and against you).

As a customer – that’s exactly what we expect from our Credit Card company. As a business owner – that sucks, but it doesn’t mean you can’t win in “court”.

## Do You Need To Deal With Credit Card Disputes If You Are Only Selling With PayPal?

When it comes to one-time payments, PayPal enables checking out with a Credit Card, without signing up for a PayPal account. This is not the typical PayPal transaction, but it happens every once in a while. When it does, since those customers don’t have a PayPal account, in order to initiate a Dispute it has to go through their Credit Card company, which will immediately trigger a chargeback, just like a Credit Card Dispute will. So, unfortunately, you’ll have to deal with Credit Card Disputes even if you only transact with PayPal 😢

## Why Ignoring Credit Card Disputes Is Bad?

From a financial point of view, handling CC Disputes may seem a waste of time, especially in the WordPress products ecosystem where the average transaction amount ranges from $30 to $150. That said, your payment gateway providers, as well as the banks and the Credit Card companies, are all keeping statistical records on the percentage of your business’ disputed payments, and the number of losses vs. wins. If you ignore a Dispute, just because you don’t think it’s worth your time, not only will you automatically lose it but it also shows the bank that you agree that the Dispute is legitimate, which means that you’ve done something bad as a business. Those negative points add up and elevate the risk of being banned by banks, Credit Card companies, or in extreme cases, [closing your payments gateway account](https://medium.com/@puntofisso/paypal-closed-my-account-with-no-explanation-it-could-happen-to-you-6ff0ba4ea95f), which already happened for plugin and theme devs who have been using PayPal and Stripe before. So even if you think you are going to lose a Dispute, it’s still important to submit your counter-evidence, showing the banks, Credit Card company, and the payment gateways, that from your end, you did everything by the book and that you are not running a “funny business”.

## How Are Disputes Different for WordPress Plugin & Theme Businesses?

Unlike SaaS (Software as a Service) companies, where all the data and tracking is processed directly on the service’s side, the vast majority of WordPress plugins and themes are self-hosted digital goods, which makes things such as determining if a plugin/theme is still in use, where it is being used from (e.g. geolocation, IP), and when was the last time the user downloaded the paid product not trivial – AT ALL. So on the surface, if you are selling a plugins/theme as a pure self-hosted digital product without any connection to a server-side, you won’t be able to know and tell much about your customers, how, where, and when they use your products. All of these data points are essential and even crucial when submitting evidence to win Credit Card Disputes.

Therefore, if you want to have a real chance to get the chargeback reversed, you’ll have to turn your product into a hybrid of a traditional digital good and a service.

## Common Credit Card Dispute Types You Have To Deal With When Selling WordPress Plugins And Themes

### Fraudulent

If you don’t add any fraud-prevention mechanics into your checkout process, “Fraudulent” charge is the most common Dispute reason you are going to encounter. It basically happens when a cardholder claims that they didn’t authorize the payment. This can often happen when the credit card was either lost or stolen and then used to make a fraudulent purchase. It can also happen if the cardholder doesn’t recognize the payment when they see it on the billing statement they receive from their credit card company.

### Duplicate Charge

The customer claims they were charged multiple times for the same product or service. Duplicate charges usually happen when processing of a purchase times out and the customer clicks the buy button again.

### Subscription Cancelled

The cardholder claims they were charged after the subscription had already been canceled. Since payment gateways won’t perform a charge of a subscription renewal unless the subscription is still active, it can happen when:

1. A customer didn’t notice they are purchasing a subscription with automatic renewals, hence didn’t expect to be charged again.
2. The customer did cancel the subscription through your interface, but due to a technical issue, the cancellation didn’t propagate to the payment gateway.
3. The customer uninstalled your plugin/theme and assumed that it will end the billing contract with your company, as well as cancel its recurring payments, which is not the case (uninstallation of a plugin/theme usually does not cancel the subscription).

### Goods Not Delivered

The customer claims they did not receive the purchased plugin/theme/service. The common reasons for the Dispute are:

1. There’s an issue with your repository, the customer didn’t manage to download the product after the purchase.
2. If you deliver the product via email and they didn’t get the after purchase email since it went to spam or due to other email deliverability issues.
3. If you require that the customer logs in to their account to download the product and they didn’t receive their login credentials via email.

### Unrecognizable Charge

The buyer doesn’t recognize the payment appearing on their credit-card statement. Many WordPress businesses have a very different legal entity name than their plugin/theme name or shop. For example, not many people know this, but Rocketgenius, Inc. is the name of the company behind Gravity Forms. For the sake of the example, if a customer buys Gravity Forms and finds “ROCKETGENIUS” on their credit-card statement there’s no chance they will link between the two, especially because there’s almost no mention of the company name on their website. If the customer won’t do the extra mile and investigate the brand name online, there’s a good chance that it will end in a Dispute.

### Product Unacceptable

The plugin/theme was received but found as defective, damaged, or not as described. This one usually happens for plugins and themes when:

1. You mentioned something in your marketing material that was not included in the product.
2. The customer received the product but had issues setting it up/using it.
3. There was a conflict between your plugin/theme with another product that was installed on the customer’s website.
4. The customer assumed that your product would do something when it actually doesn’t.

If you’d like to learn more technical details on Credit Card Disputes handling, check out this great source by Stripe:

[https://stripe.com/docs/disputes/categories](https://stripe.com/docs/disputes/categories)

## What Actions To Take And What Data Points To Collect To Reduce The Number Of CC Disputes And Strengthen Your Credit Card Disputes Evidence Submission?

### Crystal Clear Checkout – Avoid Surprises And Hidden Footnotes

Make sure that the terms of refund, subscription renewals, amounts of charges, any taxes, trial periods, moneyback guarantees, etc. are all crystal clear and stated prior to the purchase button. Avoid surprises, don’t hide things in your Terms Of Use.

Here’s what we show on the Freemius checkout when a user is about to subscribe to an annual plan:

![Freemius checkout subscription terms](https://freemius.com/blog/wp-content/uploads/2018/09/freemius-checkout-subscription-terms.png)

By making things clear to the prospect you automatically reduce the chance for Disputes. Moreover, on some CC Dispute types, you’ll be required to show a screenshot of those terms and how they are presented to the customer as part of the evidence submission process – so the clearer it is, the higher the chance of winning the CC Dispute.

### Avoid Ambiguous Copy – Don’t Let Prospects Guess Or Assume

The best way to explain this is by a real case I dealt with years ago in my side-business, [RatingWidget](https://rating-widget.com). The plugin’s most popular paid feature is the rich-snippets integration. The paid professional and business plans add the required HTML metadata for search engines to show the rating of a product/post/item right in the SERP (search engine results page). While the premium WordPress plugin automatically adds the required metadata, there’s no guarantee that Google or any of the other search engines will actually display it. Understandably, customers that subscribed to the paid offering just to get that feature were pretty upset after they paid money for a certain product capability, but Google’s algorithm “decided” not to show their ratings. They perceived it as a failure/damage in the product because they assumed that if the plugin adds the rich-snippets, stars will show up on Google. Thus, there was a period in which we got a bunch of “Product Unacceptable” Disputes. To solve that, we’ve added a disclaimer on the pages where the feature is mentioned, as well as a new FAQ item that is visible on the pricing page:

**How long does it take until Google will show the ratings?**

It can take up to 4 weeks. We have many customers which have their ratings shown in Google SERP (Search Engine Results Page). We follow Google’s best practices and constantly improve the plugin according to the newest market standards to make sure that your pages will pass Google’s official rich snippets testing tool. But, we can NOT guarantee that Google will show your stars in the search results. Why? Unfortunately, we don’t have access nor control of Google’s algorithm. The algorithm which decides whether to show the stars (or not) is based on the search keywords, page popularity, device type, country, and many more variables. Note – there won’t be any refunds for claims about the Rich-Snippets.

Adding this disclaimer didn’t have any effect on the sales, resolved 100% of those cases, and set the correct expectations with the prospects right from the get-go, even before they became our clients. It also reduced the support load and increased the support reps motivation, because we are no longer getting those angry complaints on that matter.

### Zip Code Verification

Based on this report by CyberSource from 2017, businesses reported that the most effective fraud prevention technique is address verification. Taking that into action, you don’t really have to validate the whole address. Simply validating the zip code associated with the costumer’s card will significantly reduce fraud. If you’re using a payment gateway like Stripe, it comes with a really great ML-based (Machine Learning) fraud detection mechanism called Radar. If you force the zip code validation, you can include it as part of the evidence you submit, which significantly increases your chances of winning Fraud-related Disputes, in which customers claim they didn’t use the card.

### Consider Sharing The Download Link Only Via Email

Send the product via email. Don’t allow downloading it directly after the checkout. There are pros and cons to that methodology:

- The **downside** is that if there’s an email deliverability issue, or if the customer had a typo in their email address, there’s a chance they won’t receive it and will contact support. BUT, you can easily resolve that by allowing them to resend the email if they don’t get it, or modify their email address in case of a typo. If that happens, they will contact your support – just make sure the support email is visible right after the purchase. Worst case, they will start a Dispute, but that’s quite rare if you make the support email visible enough.
- The BIG **upside** of that approach is that if they download the paid product, you can be certain that they are in fact receiving your emails, which is a very strong evidence for most of the CC Dispute types.

### Email Validation

We all know (or should know) that fewer fields in an online form yield a higher completion rate. When it comes to conversion rate optimization of a checkout form, there’s a constant battle between collecting more data vs. minimizing the number of fields a user is required to fill in order to complete a purchase. For that exact reason, when we just started, the Freemius checkout collected the email address without asking for an email address verification. That was working well, but like I mentioned before, in some cases, users had typos in their address and since we are only sharing the digital good with the customer via their email it led to “product not delivered” type of disputes.

To avoid adding another input field and affecting the “first impression”, we found an elegant solution where the email confirmation field is reactively shown **only after** the user had entered their email and first name:

![Freemius checkout email validation](https://freemius.com/blog/wp-content/uploads/2018/09/Freemius-checkout-email-validation.gif)

This approach basically eliminated 95% of those claims.

### Tracking The Download Event

Another great technique to tackle the “Product not received” Disputes is by tracking the download of your paid plugin/theme together with the IP address of the device from which the download is initiated. If you can prove that the customer had downloaded the product, and are able to include details such as when and from which device, then you are most likely going to win that CC Dispute type.

Moreover, the EU introduced a concept called [the 14-day cooling-off period](https://en.wikipedia.org/wiki/Cooling-off_period_%28consumer_rights%29), which you have to respect when selling to EU customers. It basically means that an EU buyer can return the purchased goods which have been supplied, for any reason, and get a refund. When it comes to physical goods, this policy must be respected if the customer didn’t unbox the goods. When digital goods are concerned, the “unboxing” occurs when the customer downloads the paid product. Thus, if you don’t track the download event of the paid product you won’t be able to tell if the customer “unboxed” your product or not. This consequently leads to offering a 14-days “No questions asked” money back guarantee to all EU customers, whether you like it or not.

### Subscription Renewal Reminder Emails With “Open” Event Tracking

If you are selling subscriptions, the “fraudulent” disputes are quite common where the cardholder claims that they didn’t authorize the payment, either because they didn’t permit a subscription or because they thought they had canceled it.

The best technique that we’ve developed which almost always voids these chargebacks is by emailing a subscription renewal reminder enough time in advance (we do it 30 days prior), and tracking the open event either with your own “[tracking pixel](https://en.wikipedia.org/wiki/Web_beacon)” or by leveraging the tracking capabilities of email deliverability services like SendGrid. At Freemius, we implemented our own tracking mechanism to work inline with our event tracking engine. Here’s an example of the events section of a site with an active subscription:

![Freemius dashboard renewal reminder open event](https://freemius.com/blog/wp-content/uploads/2018/09/Freemius-dashboard-renewal-reminder-open-event.png)

As you can see in the screenshot, it clearly shows the subscription renewal reminder was sent (and when), and that it was opened by the customer 2 hours after it was sent. Once we have this tracking in place, we can submit it as part of the counter evidence. So if this customer will start a CC Dispute it’s almost certain that we will win it because we can prove that the customer knew about the upcoming renewal and had enough time to cancel it.

### Collecting Customer IP, Full Name, And Email

If you aren’t collecting the IP address of the customer during the purchase you are most likely going to lose most (probably all) of your CC Disputes. The IP address is, de facto, the shipping tracking code of the digital goods eCommerce world. It’s a mandatory field that you have to fill in when submitting evidence for any type of CC or PayPal Disputes. The IP address helps the bank to validate if there’s a match in the geolocation associated with the IP address and the cardholder’s address and check if the cardholder had ever logged into the bank/credit card’s website from that IP. When there’s a match, obviously it refutes most Fraudulent-type Disputes.

In fact, if you are selling your plugins/themes to customers in Europe (which most of us do), as part of the [EU VAT regulations](https://freemius.com/wordpress/collecting-eu-vat-europe/), you are legally obliged to capture your customers’ IP, geolocation, email, VAT ID (when they provide one), and billing information (country is mandatory).

So, if you don’t yet capture the customer’s IP address, stop everything and prioritize it.

### Ongoing Data + Event Tracking

The more data you can show about your product’s usage by the customer, the better. Things like the URL of the WordPress installation that’s using your premium theme/plugin, what’s the WordPress/PHP version running on that site, etc. All these data points make your evidence stronger, which makes it harder for the Credit Card representative that is reviewing the evidence to deny it. It’s important that this data will be associated with the customer/license. Anonymized data won’t help you here.

Also, while saving static data is a good start, to increase your chances in winning Credit Card Disputes you need to start collecting an events log associated with timestamps. So for example, if a customer claims that they are no longer using the product and that they were fraudulently charged with a renewal – you will be able to show an event log of their WordPress version upgraded yesterday from 4.8 to 4.9 and prove that they’ve updated the premium plugin version after the date of the Dispute initiation. There’s a higher chance of winning that Dispute than if you only know that the user has installed it two years ago.

## Grab a free copy of our Cheat Sheet for Selling Plugins and Themes

A growth roadmap with concise, actionable tips for every milestone of WordPress product development.

![blue book with the title “Cheat Sheet for Selling Themes and Plugins by Freemius” written on it](https://freemius.com/blog/wp-content/plugins/fsblog-utilities/assets/img/svg/cheat-sheet-ebook.svg)

### Suggesting To Cancel A Subscription Upon Deactivation

This is something that we still haven’t had the chance to implement but has been on our TODOs for a while. The idea is very simple: when a customer clicks on your premium plugin’s deactivation button or tries to switch from your premium theme to another, instead of just deactivating your product, check if there’s an active subscription that is associated with the license, and if so, check if the license is associated with any additional websites. If there is an active subscription and this is the only site that is running the product ask the customer if they are interested to cancel the subscription before the deactivation. This will resolve the common confusion that a deactivation of a product also cancels its subscription.

### Use Dynamic Soft Descriptions

Most modern credit-card payment gateways support setting up the [soft-descriptor](https://stripe.com/blog/dynamic-descriptors) of every payment you process, which gives you the ability to control and modify the statement descriptor that will appear on the customer’s credit card statement. If your legal entity’s name is different from your product’s name, we highly recommend leveraging the soft-descriptor and setting it to the name of the product you’re selling. This will significantly reduce the “Unrecognizable Charge” Dispute types by reducing the confusion.

## Credit Card Disputes Handling Automation

Once you start collecting all these data-points and transactional events, you should be able to pull that data programmatically and generate your evidence with a click of a button. In fact, you can almost fully automate the whole process by integrating with your payments gateway webhooks mechanism. Generate the evidence on your end and auto-submit it with the gateway’s API (Stripe and PayPal both support those capabilities).

Here’s an example of real counter-evidence we submitted for a fraudulent Stripe Dispute, following a subscription renewal, which we won:

**Product Description:**

On May 1, 2017, &lt;customerName&gt; used Freemius, a trusted reseller of WordPress products, to purchase an Annual subscription for “Storefront Pro” Pro plan from &lt;customerIP&gt;.

Storefront Pro lets you easily customize the WooThemes Storefront theme. The product is a WordPress plugin (digital good).

The digital product and license were delivered to the customer via their email, and the subscription renews every year for continued customer support and software updates. The purchased subscription costs $75.00 (plus taxes) for each billing period.

**Billing address:** &lt;customerZipcode&gt;

**Customer IP address:** &lt;customerIP&gt;

**Activity logs:**

Our system automatically logs customers via their IP address, to make a record of the actions they take in our system and to provide an added level of verification when processing orders. Here are the actions taken by &lt;customerFirstName&gt; on our system:

On May 1, 2017, the user registered an account &lt;customerEmail&gt; and purchased an annual subscription for “Storefront Pro” Pro plan via Freemius from &lt;customerIP&gt;.

On May 1, 2017, a payment was processed by Freemius. An email receipt was sent to &lt;customerEmail&gt; with the payment’s PDF invoice.

On May 1, 2017, user &lt;customerEmail&gt; downloaded the paid plugin after purchase from &lt;customerIP&gt;.

On May 1, 2017, user &lt;customerEmail&gt; installed and activated the plugin on their site &lt;customerWebsiteUrl&gt; from &lt;customerIP&gt;.

On May 1, 2017, user &lt;customerEmail&gt; activated their Storefront Pro’s license key on their site &lt;customerWebsiteUrl&gt; from &lt;customerIP&gt;. The license key was only sent to &lt;customerEmail&gt;, hence the user can not claim that they are not receiving emails from Freemius.

On Apr 1, 2018, 30 days prior to the renewal, an automated renewal reminder notice was sent to &lt;customerEmail&gt; by Freemius. Giving the customer enough time to cancel the subscription.

On Apr 1, 2018, user &lt;customerEmail&gt; opened the renewal reminder email from &lt;customerIP&gt;.

On May 2, 2018, a subscription renewal payment was processed by Freemius. An email receipt was sent to &lt;customerEmail&gt; with the payment’s PDF invoice.

**Additional information:**

The user agreed to the product’s EULA, which includes the refund and subscription cancellation policies and can be found here: &lt;eulaUrl&gt;. As the product’s refund policy states, due to the nature of digital products, no refunds are issued after downloading the premium plugin.

As you can see in the activity logs, an automated email reminder notice was sent 30 days prior to the subscription renewal, giving the customer enough time to cancel their subscription. The activity logs also prove that the customer had opened the renewal reminder.

As an extra security precaution to reduce fraud we require that users enter their card’s CVC and zip code in the checkout form and only process the transaction when the CVC is cleared and if the zip code that’s returned from the bank matches the credit card holder’s address. When &lt;customerFirstName&gt; upgraded, the CVC check passed and the given zip code (“NNNNN”) perfectly matched the holder’s zip code.

Automating 100% of the process is great because you won’t need to spend any time on Credit Card Disputes. That said, we do recommend making it a semi-automated process, so you can moderate the auto-generated evidence before submission, and in some cases, reach out to the customer, in order to first try to resolve the case directly with them.

### Notice to Freemius Sellers

At the moment, if you’re selling your WordPress plugin or theme with Freemius, you already know that we’re the ones handling all Credit Card Disputes directly, removing this burden from our sellers. That said, since we almost managed to completely automate the evidence submission, we do plan to integrate with Stripe’s and PayPal’s Disputes-APIs and hand that control over to you.

The idea is to offer a simple CC Disputes dashboard, where the evidence will be automatically pre-filled. You, the seller, will be able to optionally enrich it with extra data like direct interactions with the customer and submit the evidence with a click of a button. This will save your and our time, by eliminating us as the “man in the middle”, preserve the high winning rate with all the best-practices I covered, and give you more control.

## A Recap

Credit Card Disputes are inevitable. On average, you’re expected to get 1-2 Disputes for every 200 payments you process. Due to the relatively low prices of WordPress plugins and themes, ignoring CC Disputes may sound like a good idea, however, if you are planning to grow your plugins business or theme shop, ignoring CC Disputes and chargebacks is not a good strategy for the long run, since you elevate the risk of getting your business blacklisted by banks, Credit Card companies, and the payment gateways.

Instead, find a way to implement the proven practices that I’ve demonstrated above. If you are using an existing self-hosted sales platform like EDD or WooCommerce, send them a link to this article and encourage them to go over the list and implement the mentioned practices to help you keep running a “healthy business”. If you are running an in-house/custom-built eCommerce solution, you can implement it yourself. Alternatively, if you don’t have at least one designated team member which is able to solely focus on the eCommerce engine, consider moving to a hosted solution like [Freemius](index.md), or any of the other mentioned self-hosted solutions.

**I’d love to hear how you handle your Credit Card Disputes! Feel free to share your process and any tips and tricks in the comments below. It would be helpful for other plugin and theme developers.**