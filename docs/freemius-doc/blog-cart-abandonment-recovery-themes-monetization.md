Release Notes is our monthly update that highlights the recent product improvements we’ve made, so you can easily stay up to date on what’s new. Here’s what we launched between June-August.

This product cycle focused on three main objectives:

1. Conversion Optimization
2. Saving developers time

We are getting many feature requests, so before we dive into the release notes, I’d like to take this opportunity and give you a little insight into our feature prioritization process and road map.

Freemius is fundamentally different than Easy Digital Downloads or WooCommerce. The alternative platforms’ business model is based on maximizing the number of add-ons they sell to their customers, simply because that’s how they make money. Their revenue isn’t dependent on your business’ success, as long as you are still in business. When monetizing with Freemius, developers are treated as our makers, not customers. We intentionally set our business model as a revenue share, inherently aligning our interests with yours – our makers. Our success relies on yours, so we do everything we can to help your business succeed by empowering you with the full suite of our products without asking a dime. This has a direct implication on the way we prioritize our features and set our roadmap.

We have a selfish interest in focusing our roadmap on features and partnerships that will yield more money for our makers. So for example, building an integration with Slack is a super cool feature that is on our TODOs for more than a year. Both EDD and WooCommerce are selling a Slack extension that does exactly that because they can capitalize on that feature. When we evaluate whether we should work on that feature or not, we ask ourselves one simple question – “how much money/time will it add/save for our makers?” the answer in the current case is practically ZERO – it’s a “nice-to-have” feature. Therefore, developing a Slack integration has a very low priority on our TODOs list. This strategy helps us to focus on what helps your business thrive.

Obviously, it’s not all black and white and when there are quick features that we believe can provide value to our developers, we are happy to develop them. In addition, we made sure that any use-case and integration can be implemented keeping things flexible, by developing a powerful webhooks mechanism from day one, making Freemius highly extensible for any scenario.

Now, let’s have a look at the new features we’re introducing today:

After analyzing data across the whole Freemius makers’ community, we found a 65% checkout abandonment rate. This statistic is just one example of the many eye-opening [Ecommerce stats](https://wpastra.com/resources/ecommerce-statistics/) out there that can help inform our decision-making processes. Even though it’s a huge number, we are in great shape compared with [these 37 other companies that average at 69.23%](https://baymard.com/lists/cart-abandonment-rate). At the same time, it still means that on average, of every 100 people that start a checkout only 35 will complete the transaction. That’s a lot of dollars left on the table.

I’m excited to announce that we’ve developed a fully featured cart abandonment recovery solution in an effort to save those abandoned carts. It’s already up and running for about 3 weeks and we’ve already seen an 11.5% recovery rate! This increases the checkout conversion rate from 35% to 42.5% – that’s an increase of 7.5% in revenues, and that’s exactly the type of features we are focused on.

You can now track all of your shoppers’ carts in real-time inside the new CARTS section in the dashboard:

![track all of your shoppers’ carts in real-time](https://freemius.com/blog/wp-content/uploads/2017/08/image1.png)

Those numbers are still fresh and will probably change in the future, but even if we only manage to increase the checkout conversion rate by 5%, it’s still a very meaningful increase.

If you don’t know what is a [cart abandonment recovery](https://freemius.com/blog/wordpress-cart-abandonment/ "A Customer Picks Up Your WordPress Plugin Or Theme & Ditches It: How To Handle Cart Abandonment?"), in a few words, Freemius will automatically capture the user’s email once it’s typed in the checkout (or if the user opted-in to usage-tracking we’ll already have the email loaded into the checkout). If the checkout isn’t completed within an hour after it was initiated, a cart recovery emails campaign will kick in sending a set of 3 emails trying to remind and convince the user to complete the checkout with a direct link to the abandoned checkout page. You can learn more about our implementation [here](help-documentation-marketing-automation-cart-abandonment-recovery.md), and generally about Cart Abandonment here.

Our implementation is in-sync with your refund policy configuration, so if you offer a money back guarantee, it will be highlighted in the cart recovery emails. Similarly, we connected the cart recovery campaign with the trials mechanism, so if you are offering trials, the 2nd and 3rd emails in the sequence will offer an alternative way to complete the checkout with a trial. After the recent [research we conducted on trials](blog-trials-premium-wordpress-plugins-themes.md), it’s better to have a 69.66% of converting that user to paid than none 🙂

Here’s a screenshot of the 2nd email in the cart recovery campaign for a plugin that offers a 14-Day Satisfaction Guarantee policy and also has a 7-Day Free Trial offering:

![email in the cart recovery campaign for a plugin](https://freemius.com/blog/wp-content/uploads/2017/08/image8.png)

We believe that we can increase the conversion even more! A common practice that many eCommerce businesses with a cart recovery solution apply is offering a discount/coupon as part of the cart recovery emails campaign. We still don’t have concrete data on that, but our gut feeling tells us it could increase the conversion rate. Therefore, we plan to add the capability of setting up a special coupon which will be exclusively sent in the 3rd email of the recovery campaign to incentivize those customers that just need a little push. We’ll make sure that this coupon will only work for abandoned carts, eliminating the risk of abuse if someone will publish that coupon code in the wild.

The cheapest Cart Abandonment Recovery service in the market starts with $50 per month and can cost up to thousands of dollars a year, depending on your sales’ volume. Freemius makers get it for free!

## Testimonials + Verified Buyers Reviews

One proven practice to improve the conversion rate is showing user reviews as testimonials to your product’s value for people. Here are a few data points you can find online:

- [According to Google](http://www.powerreviews.com/event/proven-power-of-ratings-and-reviews/), 95% of Americans now say they look at product reviews before making a purchase.
- [A CompUSA and iPerceptions study](http://www.searchenginejournal.com/the-power-of-social%C2%A0proof/21896/) revealed that 63% of consumers indicate that they are more likely to purchase from a site if it contains user-ratings and product reviews.
- [According to a Harvard Business Review research](https://blog.hubspot.com/blog/tabid/6307/bid/27067/Positive-Customer-Reviews-Lead-to-Increases-in-Revenue-New-Research.aspx), a 1-star increase in Yelp rating leads to a 5-9% growth in sales.

Accordingly, I’m excited to announce that we’ve added a new reviews carousel to the in-dashboard pricing page to feature some of your greatest recent reviews, which we automatically import from WordPress.org.

![new reviews carousel](https://freemius.com/blog/wp-content/uploads/2017/08/image13.png)

The reviews import is an automatic process that fetches 5-star reviews based on some pre-defined heuristics.

Also, you can manually add reviews collected from your users and/or customers via other channels, and set them to “featured” in order to feature them on your pricing page.

![manually add reviews collected from your users](https://freemius.com/blog/wp-content/uploads/2017/08/image6.png)

In addition, we deployed a new customer-reviews collection mechanism that automatically helps you get more reviews from your buyers. The mechanism triggers a special MAP email ([Mail After Purchase](https://www.yotpo.com/blog/mail-after-purchase-the-complete-guide/)) to your customers, 7-days after their purchase, asking them to review your plugin or theme. We used a technique that is commonly used among the most popular reviews services like Yotpo and Bazaarvoice, by embedding the review form right in the email. This allows customers to review your plugin/theme without ever leaving their email inbox, which, based on Yotpo, is proven to increase the reviews’ conversion rate by more than 100%.

![review form right in the email](https://freemius.com/blog/wp-content/uploads/2017/08/image21.png)

If the user doesn’t complete the whole review in their email, we’ll try to complete it, using the following form:

![Review form](https://freemius.com/blog/wp-content/uploads/2017/08/image4.png)

You will get notified every time a customer leaves a review, and it will be up to you whether you choose to feature it on your pricing page or not.

This is yet another feature you get absolutely for free! If you shop around, you’ll find that services charge hundreds of dollars a month for it, based on your sales volume.

## Features Description

After receiving several requests, we’ve added the option to add a description to features:

![option to add a description to features](https://freemius.com/blog/wp-content/uploads/2017/08/image9.png)

This allows you to optionally add a paragraph to describe a feature in more length. The feature description will be shown in the pricing page as a tooltip next to the relevant feature:

![feature description will be shown in the pricing page as a tooltip](https://freemius.com/blog/wp-content/uploads/2017/08/image12.jpg)

## Checkout Security Badges / Trust Seals

After doing some research on conversion rate optimization during April, we stumbled across a bunch of articles showing how [trust seals can have a meaningful effect on your conversion rate](https://www.crazyegg.com/blog/trust-seal-ecommerce/). After 3 months and thousands of transactions and A/B testing different combinations of seals on our in-dashboard pricing and checkout pages, we have pushed the winning combo of seals into our checkout page, which had shown an average conversion rate increase of 1.5%. After tracking a decrease in conversion rate from the pricing page to the checkout – we removed the seals from the pricing page. It doesn’t mean that seals are necessarily bad for the pricing page, it just means that our positioning and the combinations we’ve tested had a negative effect on conversion rate. We may give it an additional spin in the future, using different positioning on the page.

## Invoices

Due to security reasons related to our API, we couldn’t include a secure link to the invoices in the emails. Thus, customers that needed an invoice had to contact support to ask for the latest invoice. While our Help Scout integration makes it super easy to access that invoice right from the Help Scout dashboard, not all of our developers are using Help Scout and it still added some extra burden on support.

No more!

We’ve enriched our API and now all payment receipt emails include a direct link to a PDF invoice. That’s one small step for developers, one giant leap for customers 😉

![emails include a direct link to a PDF invoice](https://freemius.com/blog/wp-content/uploads/2017/08/image5.png)

## A Renewal Notice Reminder, Email Opens Tracking & Handling Customer Disputes

When you sell an annual license of your premium WordPress plugin or theme with Freemius, the platform will automatically notify the customers about the upcoming renewal 30 days before the payment goes through, giving the customer enough time to cancel the subscription if they want. With that said, we are still seeing customers that dispute their renewals. To strengthen our evidence during the dispute resolution process, we are now tracking the renewal notice email open event, to increase our chances of winning a possible dispute. You can now see this event in the user’s profile:

![tracking the renewal notice email open event](https://freemius.com/blog/wp-content/uploads/2017/08/image11.png)

Our disputes rate is around 0.4% and while this number may sound fairly small, every dispute that we receive is a huge time sucker because every dispute is slightly different and we still haven’t found an effective way to programmatically automate the evidence submission process. At the moment we don’t charge anything for handling disputes, but if we won’t find a robust way to automate that process we’ll consider adding a dispute handling fee (obviously, we prefer to avoid that).

## Dashboard Licenses

We’ve added a new column to the licenses section to show the associated subscription with a direct link to it. Making it easier to navigate from a license to its subscription.

![associated subscription with a direct link to it](https://freemius.com/blog/wp-content/uploads/2017/08/image3.png)

## Advanced Coupons

Running periodical promotions by leveraging the coupons mechanism is a great way to boost sales. The functionality we supported so far was very extensive, but there were still valid use-cases we didn’t cover. I’m happy to announce that advanced coupons are now up! Not only can you create a coupon for specific site license limits, it’s also possible to specify which billing cycles should be supported by the coupon:

![advanced coupons](https://freemius.com/blog/wp-content/uploads/2017/08/image14.png)

For example, you can now create a coupon specifically for your 5-site lifetime plan. This coupon won’t work for other billing cycles, or for the single-site license.

## WordPress SDK New Mega Version

We released a [new version of our WordPress SDK](https://github.com/Freemius/wordpress-sdk/tree/master). You will notice a huge jump in the versioning from 1.2.1.7 to 1.2.2.8. The reason for that is because we finally merged the themes and plugins SDK together. **This is a HUGE code update and while we are confident that it’s in a good shape after many days of testing, we still ask you to run a sanity check before you deploy it to production. Just to be clear, everything remains backward compatible, and in fact, the theme’s SDK was already running in production among dozens of themes and thousands of websites (we also released it for our plugins a week ago and didn’t get any tickets related to the SDK, so far).** Bringing the SDK versions into a shape which we can merge them into, is something that we’ve been working on for about 6 months. The fundamental difference we had to incorporate in our design is rely on IDs instead of slugs since a plugin and a theme can have the exact same slug, which may cause conflicts. While the scenario of a plugin and a theme with the same slug, both using Freemius and installed on the same site has a very tiny probability of occurring, we are building a solution for the long term and it was important for us to avoid this possible conflict.

### Themes Monetization

After six months of ongoing conversations with the WordPress.org themes review team, we’ve finally sealed all the details and the expected UX, to offer our monetization capabilities within the WP Admin for themes. Not going to dive into the technicalities, but we adjusted the SDK to seamlessly integrate with tabs (instead of menu items) and the customizer, so you can now upsell your premium theme version right from within the WP Admin, without even having a website.

#### Call for Freemium Theme Developers

If you are interested in giving it a spin, we’re currently gathering a closed group of development customers. The benefit of joining as an early adopter is that we’ll help you with the quick integration and make sure it’s all working as expected, and you’ll be able to give us your feedback, which will be taken into account as we finalize the beta version. To apply contact us via [\[email protected\]](https://freemius.com/cdn-cgi/l/email-protection)

### License Update from GPLv2 to GPLv3

Josh Habdas started an [issue on GitHub regarding our SDK’s GPLv2 license](https://github.com/Freemius/wordpress-sdk/issues/166), raising the concern that our licensing isn’t compatible with GPLv3 and AGPL. After doing some research and advising with an attorney, we adjusted the SDK’s license to GPLv3 which actually gives more freedoms to developers.

### Version Updates Population

After receiving a few complaints from developers saying that they have released a new version and their customers can’t see the update, we ran a thorough profiling of the premium updates mechanism. We found that due to a layer of caching on top of our API requests manager, together with WordPress core’s 12 hours updates cache, customers with a valid license had to wait up to 36 hours to see an update in their WP Admin dashboard. Not optimal at all.

Therefore, We reduced the cache expiration for that request to 1-hour, which will reduce the wait time to up to 13 hours. In addition, when forcing an updates check from the Updates page in the WP Admin, we immediately invalidate the relevant cache and pull a fresh result directly from the server. This means that the update will be available immediately after clicking the “Check Again” button:

![wordPress Updates Check Again Button](https://freemius.com/blog/wp-content/uploads/2017/08/image10.png)

### UX

- After several support tickets, we found a repetitive UX issue where customers do not notice the Billing tab when opening their Account page, which means that they don’t know how to update their business information for invoicing. Thus, we moved the billing and invoices section right into the Account page.
- After numerous internal discussions and advising with the WordPress.org Themes Review Team, we eventually decided to add the opt-out option from usage-tracking for themes, right in the theme’s details dialog box:  
  ![opt-out option from usage-tracking for themes](https://freemius.com/blog/wp-content/uploads/2017/08/image7.png)

### Selling Add-Ons

- We made a significant performance optimization to the Add-Ons marketplace when selling add-ons from the WP Admin.
- The SDK now supports a proper upsell for freemium add-ons within the WP Admin. Before, this section only worked properly for free or premium only add-ons.
- Activating a premium add-on that was purchased via Freemius Checkout from the developer’s site now auto redirects to the license activation form. In previous versions, if an add-on was purchased outside the WP Admin, we automatically deactivated a premium only add-on with a corresponding message that it requires a license. Simply because we never implemented that use-case and were relying on an in-dashboard upgrade which automatically fetches the license key via the API.

### Bug Fixes

- The auto-deactivation process of the free version upon activation of the premium one was only working for opted-in users. The problem is that if a user skipped the opt-in, and later purchased a premium version from the developer’s website using Freemius Checkout, when that user would try to activate the premium version, the free version remained activated. This caused unpredicted behavior.
- In the last release, we mistakenly added a bug that caused the opt-in/out functionality in the plugins’ page to fail. This issue is now fixed.
- Fixed a few bugs related to environments with Symlinks.

## Affiliation Platform Update

In our [last release notes update from May](blog-mailchimp-and-seamless-freemium-checkout.md), I’ve announced that we’ve officially started working on an affiliation platform for Freemius developers. The good news is that we are on track! We finished the development, passed two cycles of code review, and hope we can release it in September.

## What’s coming up?

### SDK Memory Consumption Optimization

I mentioned this in our last release notes, we need to redesign our localization mechanism to avoid loading all our translatable strings into the memory. Unfortunately, we didn’t manage to prioritize this.

### Premium Version Folder Name Customization

Currently, when deploying a freemium or premium plugin/theme to Freemius, the engine will generate a premium version that will be named \`{slug}-premium\`. This convention allows us to do a lot of magic in the SDK, such as automatically deactivating a free version upon the premium version activation.

In the last month, we received several requests from different developers, with valid use-cases for which the “-premium” suffix addition doesn’t make sense. For example, when a WordPress.org freemium theme has a “-lite” suffix in its slug, the premium folder name will look like “my-theme-lite-premium”. When the proper naming should probably be “my-theme” without the “-lite” suffix.

Long story short, we plan to add the ability to customize the premium version folder naming by adding it as an additional parameter to the SDK’s init snippet.

### Reducing The Number Of Dummy Emails

After looking at our SendGrid stats (the service that we are using for transactional emails), our bounce rate is ~4%. The reason for that is a decent chunk of the WP admins that install a WordPress site are using a dummy email address, just to complete the installation, without ever updating it to a real address.

A quick solution would be asking the admin for their email address on the opt-in page, though this will decrease the conversion rate to opt-in significantly (we did something similar in our own plugin before), probably more than 4%. So here’s what we are planning to do: we’ll use heuristics to identify if the admin email address is a dummy one, and will also use DNS resolve to check if the domain exists at all. If we identify the address as suspicious, we’ll prompt the admin with a simple input box right after they click the “Approve”. If they cancel the email modification, we’ll opt them in with the potentially dummy address, if they do update – even better! In any case, by using that user-experience, we’ll be able to secure the same opt-in conversion rate.

### Bundles

The ability to sell multiple add-ons, plugins, or themes, or any combination of them, is the last missing piece in what I call the “essential capabilities” Freemius has to support. In a high level, we plan to start working on bundles after we release the affiliation platform, and you’ll be able to sell any combination of your products via bundles – not only add-ons.

So for example, if you are a WooCommerce focused business with multiple products, you’ll be able to sell a WooCommerce theme with a set of plugins as one discounted item. If you are selling bundles or thinking about it, please contact us via [\[email protected\]](https://freemius.com/cdn-cgi/l/email-protection#8bf8fefbfbe4f9ffcbedf9eeeee6e2fef8a5e8e4e6) and tell us how you plan to do it, making sure that once we get to the process of designing the infrastructure, it will be able to handle your use-case.

**That’s it for today’s update, hope you’re excited about the new features as we are – let us know what you think 🙂**