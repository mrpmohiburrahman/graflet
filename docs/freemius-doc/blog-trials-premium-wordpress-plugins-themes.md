Trials for software products and SaaS (Software as a Service) has been a standard practice for years and is considered as an excellent way to get a higher reach and improved conversion rates. That said, only a small fraction of the premium WordPress plugins and themes on the market offer Trials. The main reason is that monetization platforms like EDD and WooCommerce, and marketplaces such as ThemeForest and CodeCanyon, don’t offer out-of-the-box solutions to fulfill the technological needs of trials while protecting developers from piracy and trials abuse.

After gathering lots of data on trials conversion rates among dozens of plugin and theme developers who are leveraging [Freemius](index.md)’ trial mechanism, I decided to share some of the aggregated numbers and best practices to encourage more developers in the WordPress ecosystem to consider adding a trial option to their premium product version.

Before I dive into the numbers, it’s important to learn about the different types of Trials so we can all be on the same page:

## What Types of Trials Can You Offer?

There are three well-known trial offerings that are currently popular on the market:

- A free trial without a payment method
- A free trial with a payment method (e.g. credit card, PayPal)
- A paid trial with a significant discount during the trial period

### Free Trials Without A Payment Method

Free Trials without a payment method is a simple way to let a prospect try your premium product in exchange for an email address. This is the safest and easiest trial for consumers since they don’t need to provide their payment information.

**PRO TIP:**

For a higher conversion rate, make sure you make it super clear that the Free Trial is risk-free, here’s how we do it across our site:

![a risk-free Free Trial](https://freemius.com/blog/wp-content/uploads/2017/07/image2.png)

### Free Trials With A Payment Method

Another popular Trial variation is asking the user to provide their payment method along with their email address, without charging their Credit Card or PayPal, until the trial period expires. This Trial is less converting since the user needs to have some trust in your business and feel confident that you won’t scam or charge them unexpectedly. It also adds a hassle since they need to remember to cancel the Trial in case they’re not interested in continuing to use the product. Having said that, that’s how Netflix, Hulu, Amazon Prime, and many other subscription-based businesses have built their empires.

The benefit of a Free Trial with a payment is that users who go through that funnel are more “serious”, or more likely to stick with your service since they made the hardest step – providing you with their credit card. You’ll see how this plays in terms of conversion when I get to the actual numbers part.

### Paid Trials With A Discount

Paid Trials is a common practice in the Enterprise Software world where monthly payments are starting from hundreds of dollars and can go up to millions. This structure usually comes with a pilot period where the prospect wants to evaluate the product and validate that the numbers are aligned with whatever is the promise before they go all in.

Getting back to WordPress products sphere, Paid Trials are usually camouflaged as coupons for the first payment. So for example, when Sven introduced a Black Friday 40% discount coupon with Freemius for [BuddyForms](https://themekraft.com/buddyforms/), the discount was only applicable for the first month’s payment (the Trial period). This way customers can try the product for a much lower price, before actually committing to the full amount.

In this article I’m not going to share numbers about Paid Trials with discounts since we don’t have a statistically sufficient amount of data about this use-case and most of our partners are using it only for periodic promotions (e.g. Black Friday) that come with a marketing boost, so the numbers will probably be skewed.

**Now that we are all on the same page and know the different trial types, let’s examine the numbers…**

## What Are The Main Benefits of Offering a Trial for A Premium WordPress Theme Or A Plugin?

### Higher Conversion Rates

The average conversion rate from a Free Trial without a payment method to a paying customer is 18.78%. This means that almost every 5th user that starts a trial will become a paying customer!

Impressive, right?

Examining the conversion from a Free Trial with a payment method to a paying customer reveals a crazy rate of 69.66%. 7 out of 10 users who start a Trial with a payment method will become customers!

Just to give you some perspective, the average conversion rate from *free*‘ to *paid*‘ of the same group of premium WordPress themes and plugins that offer Free Trials is 1.51%. Meaning, every time you manage to push a user into your Free Trial funnel, you increase the chance that this user will become a paying customer by over 1,243%. And if you also require a payment method, this chance is increased by a staggering 4,613%.

While these numbers are amazing, you have to remember that when you offer a Free Trial, your bottom line conversion rate also depends on the number of users that will actually start a Trial. Here’s what the equation looks like:

`New customers = [# all users] x ([% users that start a Trial] x [% start a Trial & convert to paid] + [% users that convert from free to paid ])`

Once you understand all the variables of the equation, you can start testing different approaches to optimize your bottom line.

For example, you might consider only offering Paid Trials with a payment method, and remove the option to become a direct customer. In that case, the parameters will look like:

`[% users that start a Trial] = 100%`

`[% users that convert from free to paid ] = 0`

`[% start a Trial & convert to paid] = 69.66%` (based on the average.)

So your ‘new customers’ equation in that case is:

`New customers = [# all users] x 69.66%`

While you are going to have an amazing conversion rate, `[# all users]` will probably significantly go down. It’s all about iterations and knowing your numbers. In fact, this is the exact strategy used by Netflix. If you go to their homepage you’ll notice that there’s no way to become a customer without going through a month of a Free Trial funnel:

![The Netflix trial funnel](https://freemius.com/blog/wp-content/uploads/2017/07/image9.png)

### Lead Generation

One of the great benefits of a trial is the ability to ask something back in return for it. The most common thing to ask is their email, but you can ask for additional things too. For example, you can require the user to “give you” their Twitter handler and ask them to follow you on Twitter. That way, you can verify the follow via Twitter’s API and only enable the download button after the verification.

Once you have the verified user’s email you can add them to your Trial marketing funnel. The obvious one is email marketing, but you can also retarget them with ads on social media platforms like Facebook and Twitter by adding them to a Custom Audience or retargeting them with AdWords. All of these efforts will help you to bump the conversion rate of Trial to Paid, which, in turn, will increase the chances the user will become a paying customer.

If the user won’t convert to a customer, since you have already got their email, you can push them to an educational Drip campaign to slowly and safely win their trust. Then, either try to convert them again for the same product or promote a different CTA (Call to Action) which could be an upsell of a different product, asking them to follow your blog, etc.

## Why Is Offering a Trial Mechanism For A WordPress Plugin Or Theme So Hard?

The primary challenge with Trials is how to give access to your premium open-source plugin or theme without risking abuse by the user (get access to your premium code and use it without ever paying). For SaaS (Software as a Service), that’s pretty simple; you just block access to your service upon Trial expiry. But with open-source GPL code, things are way more complex 🙂

The first thing that you have to acknowledge when offering Trials is that if you want to protect your code from Trial abuse you’ll have to add a licensing engine that is connected to an external licensing service and actually block the features, or maybe the whole product when the Trial expires or is canceled. To clarify, GPL doesn’t prohibit licensing and features management – this is absolutely legal and compliant with the GPL license.

And yes – since WordPress products have to comply with the GPL license (at least the PHP code), a tech-savvy user can potentially strip/null your plugin or theme from the licensing logic. But don’t worry too much about that, those users would probably never pay you anyway. Also, if they choose to redistribute your premium product, there are ways to protect yourself against copyright infringement, you can learn more about it in [this article](blog-selling-wordpress-plugins-gpl.md) I wrote with the help of two Intellectual Property attorneys.

Secondly, users who start a Trial understand that they can use the premium plugin or theme only for a temporary period unless they start paying. We’ve facilitated thousands of Trials with Freemius across dozens of plugins and themes, and have never heard anyone complaining about losing access to the paid features after their Trial expiration (or cancellation).

Getting back to the technical part, if you want to offer Trials you’ll have to address the Trial use-case differently than you would a regular license expiration. So for example, if your purchase terms are qualifying customers to get product updates and support for as long as the license is valid, and you still allow users to keep using the premium product after license expiration, you’ll have to implement some custom logic to act differently for Trials and block access for that case. Making this happen requires some license-related logic within your plugin or theme, and also requires your licensing service to support it.

As a “real-world” example – the [‘FooBox Image Lightbox’](https://fooplugins.com/foobox-image-lightbox/) plugin supports product trials (via Freemius), so if a user starts a trial but does not upgrade to the premium version before the trial period ends – the plugin will automatically fall back to its free version.

Examining the market’s most popular solutions and marketplaces, [the only platform that comes with complete Trials support is Freemius](wordpress-features-comparison.md). Let’s look at those different solutions one by one:

### CodeCanyon and ThemeForest

If you are selling premium WordPress plugins on CodeCanyon or themes on ThemeForest, Envato doesn’t offer any Trials for buyers. The reason they don’t is that Envato is a very low-touch marketplace in terms of how they integrate with their products inventory. In fact, you can sell plugins or themes without any integration with Envato. As described before, to offer Trial capabilities they will have to find a way to enforce sellers to integrate some licensing logic that would communicate with Envato’s licensing engine. Since CodeCanyon and ThemeForest aren’t fully focused on the WordPress market (you can sell scripts and other platform templates there), and since Envato has to maintain 5 additional marketplaces that don’t include software at all, it’s simply not their focus.

### Easy Digital Downloads

EDD doesn’t offer an out-of-the-box solution for Free Trials without a payment method because, by default, the Software Licensing extension generates license keys only after a purchase or a subscription is complete.

The good news is that if you want to offer Trials with a payment method, last October [EDD introduced exactly that](https://easydigitaldownloads.com/blog/free-trial-support-added-recurring-payments/) via their [Recurring Payments extension](https://easydigitaldownloads.com/downloads/recurring-payments/). While this is better than nothing, from what I’ve seen and learned from other sellers that have been using the platform, the Trials mechanism isn’t integrated with the Software Licensing extension. This means, that there’s no easy way to write a custom logic to address a Trial period within the plugin or theme. So for example, if a user cancels the Trial and you want to block their access to some (probably all) of the paid features – with the current extensions you’ll only be able to “know” that the license had expired, but you can’t be certain if it’s really the Trial that is over or if the license expiration was triggered due to a different action.

### WooCommerce

Much like EDD’s Recurring Payments extension, WooCommerce offers a [Subscriptions extension](https://woocommerce.com/products/woocommerce-subscriptions/) that supports Trials with a payment method, but there’s no support for Free Trials without asking for a credit card. There’s actually [a 3 years old thread on the WooCommerce Ideas Board](http://ideas.woocommerce.com/forums/133476-woocommerce/suggestions/5748332-subscription-free-trail-without-cc-needed-ask-fo) asking for that exact functionality with more than 230 upvotes. In addition, the current Subscriptions extension isn’t working with coupons, so you won’t be able to offer a Trial along with a promotional coupon.

### Freemius

As our team’s background is SaaS and we know how Trials can be a huge benefit to product sellers, we designed our licensing engine to support trials from day one. Freemius supports Free Trials, with or without a payment method, with coupons and discount codes, and all the bells and whistles that you can think of. And after having numbers collected for more than a year, now we know for sure (backed by data) that it was a smart decision, which helps our sellers to increase their bottom line, outperforming their potential sales on the competing alternatives.

We made it super-easy for developers to implement: all developers have to do are two simple things:

1. In the plan’s configuration, choose the Trial period’s length and decide whether the trial should require a payment method:  
   ![Choosing Trial period length](https://freemius.com/blog/wp-content/uploads/2017/07/image6.png)
2. Add our [GPL Compliant WordPress SDK](https://github.com/freemius/wordpress-sdk) and wrap the paid logic with the following simple license-related logic:

```
if ( my_fs()->can_use_premium_code() ) {

// ... premium only logic ...

}
```

Once a user signs up for a Trial, Freemius will generate a Blocking License. This means that if a Free Trial without a payment method expires or is canceled, `can_use_premium_code()` will return false and the logic won’t be executed. If a Free Trial with a payment method is canceled before the 1st payment goes through, the same thing will happen and again – the logic won’t be executed. On the other hand, once a payment goes through, or a user becomes a paying customer, the method will return true, as long as the license is valid, and when the license expires the method will return true or false based on the plan’s configuration:

![Choosing to keep or block features after trial expiry](https://freemius.com/blog/wp-content/uploads/2017/07/image11.png)

So you can choose to keep the features and only block updates and support or block the features after the license expiration (again, this is compliant with the GPL license).

Another thing to keep in mind is that if you offer Trials for a freemium plugin or theme, the Trial expiration shouldn’t block all the features and the expected behavior is a fallback to the free version:

- In the case of paid add-ons and free core products, blocking or deactivating the add-on is the way to go.
- In the case of plans, you’ll either have to include all the free features as part of the paid version code base or provide your paid version as an additional plugin installation (or a child theme) that needs to run in parallel with your free product.

## Grab a free copy of our Cheat Sheet for Selling Plugins and Themes

A growth roadmap with concise, actionable tips for every milestone of WordPress product development.

![blue book with the title “Cheat Sheet for Selling Themes and Plugins by Freemius” written on it](https://freemius.com/blog/wp-content/plugins/fsblog-utilities/assets/img/svg/cheat-sheet-ebook.svg)

## Should You Offer A Trial For Your WordPress Plugin or Theme?

Before you rush into a Trials mechanism implementation you need to ask yourself three questions:

1. Is your product mainly used for the short or long term?
2. Does your product provide more value over time, like good wine?
3. Is it becoming harder for a user to switch to a competing product over time?

If your WordPress theme or plugin is mainly used for a short period, it doesn’t become more valuable over time, and it’s easy to switch to a competing product, you should probably not offer Free Trials (in 99% of the cases).

And I’ll explain.

Some products offer more value over time, which means that the longer the user will use them, the more vested they become in the product. A great example for such a WordPress plugin would be a reviews plugin. Assuming the user’s site has traffic, as time passes by they are expected to capture more reviews. Switching to an alternative plugin will cost losing the accumulated reviews – and that’s painful.

If we look at themes, most WordPress themes are harder to switch over time. Not necessarily because they bring more value to the user, but mainly because the website owner had already spent time tweaking the settings, customizing the theme’s widgets, uploading images, and maybe even adding some custom CSS. Switching to a different theme is a hassle and can even be expensive since it requires time to adjust the new theme’s look and feel again, and we all know that time equals money.

In both of the above-mentioned cases, it makes total sense to offer a Trial, luring a user to give it a try, while you know that once they try out your product the chances of them switching is just getting lower over time.

On the other hand, products like ‘data export’ plugins or ‘coming soon’ themes are bad candidates for Free Trials. Think about it: if you offer a 30-day Free Trial for a coming soon page there’s a high chance that your premium theme will be needed for less than that until the site owner launches their site. Same thing with data export plugins, which many site owners use only rarely, for migration reasons. Both of these use-cases showcase products that are usually used for very short periods, could be easily switched, and do not provide more value over time.

## What Is The Best Free Trial Length?

The most popular Trial lengths in the market are a 7-day Trial, a 14-day Trial, and a 30-day Trial. But, there’s no magic number here because every premium plugin or theme is different. What you do have to make sure is that your trial is long enough for your prospects to be able to adequately evaluate your offering, and hopefully, get “hooked”.

Another thing to keep in mind is that even if your product is becoming more “addicting” over time, offering very long Trial periods can eliminate the urgency of actually trying out your product. So try avoiding the “I’ll just sign up for the trial and keep it in the email for later” syndrome.

As a rule of thumb, I would recommend starting with a 14-day Trial to give enough time to try the product and get hooked, and then A/B test it with a 7-day Trial and see which one performs better. In my opinion, offering Trials longer than 14-day for premium WordPress themes and plugins doesn’t make sense. Users have a really short time span and patience and the usual flow for choosing a product in the WordPress sphere is installing a bunch of products in parallel on a test environment, and selecting the first one that fulfills all their requirements. But again, every product is different, and maybe for some products, a longer Trial period would make sense.

## Should You Offer Support During A Free Trial Period?

You have to! When a prospect is testing your premium plugin or theme they are not only evaluating your product features and capabilities but also your support quality and response rate. Not only should you offer support during a Trial, but I would also boldly say that you should prioritize your Trial users and support them even before all of your other customers (obviously don’t neglect your clients and make sure you respond in a timely manner).

When a user contacts your support during a Trial period, it confirms that they are in the middle of an ongoing evaluation process and swift support could be the one thing that seals the deal. It shows the prospect that there’s a responsive team behind the product that cares about their customers, and this is the kind of vendors people like to “work” with. If you take longer than 24 hours to answer there’s a high chance that the prospect had already passed on your product and moved on to the next.

## How to Encourage Your WordPress Theme Or Plugin Users To Start a Trial?

As you’ve seen earlier, Trials have a tremendous potential to increase the bottom line. To do so, you’ll have to work on your Trial funnel, and actually get users to start a Trial which could be a challenge of its own. Here are five popular techniques you can use to start adding users to your Trial funnel.

### Exit Intent Pop-up

Many things have been said about exit-intent pop-ups. Whether you like them or not, the fact is that they are working, and with the right promotion they work great! Instead of offering eBooks and promises for great content in exchange for an email, add an exit intent pop-up to your product’s page so when a visitor is about to abandon the page you’ll offer them to try your premium plugin or theme via a Free Trial.

There are many advanced services and plugins for exit intent pop-ups, but if you want to just get a “quick & dirty” solution I’d recommend trying [Ouibounce](https://github.com/carlsednaoui/ouibounce), a lightweight JavaScript library for exit intent identification. Even though it’s pretty limited, it does the job (we use it on our blog).

### Cart Abandonment Recovery Email

Out of the context of this post though very relevant for Free Trials, on average, only 1 out of 5 people who start a checkout process will complete it and become a customer. It means that you are losing grip on 80% of the prospects who show interest in buying your product. If they typed their email address, the best practice is to add them to a cart recovery emails campaign. The typical recovery campaign will send 1-3 emails to remind and encourage the user to complete the checkout. If you offer a Free Trial, you can make this campaign more effective. Instead of sending the 2nd or 3rd email with a discount coupon, devaluing your product, and reducing your potential income, email the prospect a link to try the product via a Trial. Here’s how the 2nd cart recovery email looks like when offering trials with Freemius:

![Freemius Cart Recovery Trial Promotion](https://freemius.com/blog/wp-content/uploads/2017/07/freemius-cart-recovery-trial-promotion.png)

### Checkout Abandonment

Adding on top of the previous section, if the user doesn’t provide their email address, there’s no way for you to start a recovery emails campaign. Instead, you can identify a cart abandonment action:

1. If the user navigates to another page on your site by clicking an internal link, you can use JavaScript to trigger a modal dialog right on the checkout page and offer a Trial, very similar to what Facebook does when you try to navigate away in the middle of a status update:  
   ![trigger a modal dialog right on the checkout page and offer a Trial](https://freemius.com/blog/wp-content/uploads/2017/07/image1.png)
2. Don’t trigger an exit-intent Trial promotion on a checkout page, there’s a good chance the user is moving the mouse to a different browser tab to do some additional research before completing the transaction. You don’t want to offer a Trial when the user has the intent to buy 🙂 But, if the user does navigate away from the checkout page to another page on your site using the browser’s navigation buttons, you can identify that and then trigger the same Trial pop-up when it’s loaded. There are quite advanced techniques for how you can do it with JavaScript, and I think it’s way easier to leverage cookies. Simply store a session cookie with the latest page URL, so once the user navigates away from the checkout, you can inspect that cookie and trigger the pop-up based on the stored value.

### Trials Only

I already mentioned it before – an easy way to pump up your Trial funnel is simply not offering an option to upgrade/subscribe/purchase without going through a Trial. If you want to get the paid version, you have to go through a Trial. It might sound extreme but it’s working for many companies outside the WordPress bubble, and my gut says it can also work well for some premium WordPress plugins and themes.

### WP Admin Dashboard Notification

If you are selling a freemium WordPress theme or plugin, and the free version is hosted on WordPress.org, one great technique that we’ve incorporated into Freemius is showing a promotional admin notice after 24-hours, encouraging the user to switch from the free funnel to the Trial funnel so they can try the fully featured premium offering. Here’s what it looks like:

![encouraging users to switch from the free funnel to the Trial funnel through WP admin dashboard notifications](https://freemius.com/blog/wp-content/uploads/2017/07/image7.png)

It’s friendly, non-intrusive, and dismissible. Also, since we show it only 24-hours after the activation there’s a high chance that the user will have already tested a bunch of other alternatives, and that’s the one they’ve decided to use.

## How To Protect Your WordPress Theme Or Plugin From A Trial Abuse?

### Don’t Give Access to Your Premium Code Right Away

If you choose to offer a Free Trial without a payment method, don’t just reveal the link to the premium product after the user starts the trial, instead, send it to their email. That way, you’ll avoid giving your product to trolls who use fake emails just to get access to your code.

**PRO TIP:**

For the same reason, when the user downloads the product via the link in the email, create special links with unique query-string secure params to set the user’s email as Verified on whatever system you store your emails. Otherwise, you’ll end up with a mailing list that has a high percentage of dummy addresses.

### One Trial Per Site And Email Address

When you offer a Free Trial from your website you can’t know the domain of the site the user intends to install your premium plugin or theme. Therefore, the protection is to check if a user with the same email address had already signed up for a trial before. This can’t guarantee that the user didn’t sign up for a Trial before if they have more than one email address, but it’s better than nothing.

When you offer a Free Trial via an upsell from within the dashboard, you can leverage the $\_SERVER\[“HTTP\_REFERER”] variable to verify, through your licensing engine, that there was never a Trial that was utilized by the same website address.

### Charge A Symbolic Amount

One good practice for Free Trials with a payment method is charging a small amount (e.g. $1) and then refunding it right after it was successfully processed. This tactic assures that the payer’s account is actually chargeable and at least has some funds and that it’s not just a PayPal account that was registered a minute before subscribing to your trial. The downside of this approach is that Credit Card refunds can take between 5 to 14 business days until they show up in the statement. So even if it’s just a symbolic transaction, it may upset some users if they check their statement before the refund processing is completed by the bank.

### Auto Charge After Trial Expiration

When offering a Free Trial with a payment method, make sure that you actually generate a deferred subscription that will automatically start charging the user after the Paid Trial expires. If you don’t do that, all your Trial efforts and conversion to Paid will go down the drain.

## How to Avoid Chargebacks And Disputes When Offering a Trial For Your WordPress Theme Or Plugin?

### Clear Messaging

First of all – be super clear with your messaging! Don’t try to trick users with a misleading copy or let them guess things. It will bite you back. Be very specific about the Trial start date, expiration date, the amount of the initial payment, and renewals.

Here’s what it looks like in the checkout of products using [Freemius](index.md):

1. Even though the “Today’s total” is free ($0.00), the Trial start and expiration dates, and the charge amount are all explicitly specified:  
   ![Today’s total](https://freemius.com/blog/wp-content/uploads/2017/07/image8.png)
2. Explain to the user why do you collect their payment method for a Free Trial, and use that opportunity to set up expectations by telling them there will be an automatic renewal.  
   ![set up expectations by telling them there will be an automatic renewal](https://freemius.com/blog/wp-content/uploads/2017/07/image4.png)
3. Confirm the Trial terms by showing a summary of the details before they subscribe to the Trial:  
   ![showing a summary of the details](https://freemius.com/blog/wp-content/uploads/2017/07/image10.png)

### Trial Expiration Email Reminders

When you offer a Free Trial that requires a payment method, there’s a chance that the user will forget about the Trial. Don’t let their Credit Card statement be their reminder that the Trial is over. Seeing an unexpected transaction from your company is a terrible user experience, even if you process a refund. It’s bad for your brand and a waste of time for your team and your Trial prospect. Therefore, make sure you send an expiration email notice a few days prior to the Trial expiry with instructions on what they need to do to cancel the trial so they can avoid the upcoming charge.

Here’s the email we are sending with Freemius 2 days prior to a trial with a payment method expiration:

![email 2 days prior to a Trial with a payment method expiration](https://freemius.com/blog/wp-content/uploads/2017/07/image5.png)

If you read the email you’ll notice that we are intentionally not giving a one-click cancellation option. This tactic forces users to contact the support and gives the seller an opportunity to learn about the reason for the trial cancellation. Potentially even saving the deal and avoiding cancellation (btw the user can cancel the Trial from their account page, so they do have an option to handle it themselves without any support).

For Free Trials without a payment method, you’ll need to write a copy that is good enough to convince the user to take the final step and become a customer, since you still haven’t captured their payment. A good practice is to highlight all the awesome features that the customer will lose if they cancel the Trial. Here’s the template we use with Freemius:  
![Email template for Free Trials without a payment method](https://freemius.com/blog/wp-content/uploads/2017/07/image3.png)

**PRO TIP:**

If you collect data using a tool like [Freemius Insights](wordpress-insights.md) and track the features the user interacted with during the Trial period, make the expiration email dynamic and highlight those specific features in your email to make it even more compelling.

## How to Offer Trials For A Freemium Plugin Or Theme While Keeping It Compliant With The WordPress.org Guidelines?

Offering a Trial with your free WordPress.org plugin or theme could be slightly challenging. If you check [the WordPress.org guidelines](https://developer.wordpress.org/plugins/wordpress-org/detailed-plugin-guidelines/) you’ll find the following two bullets:

- *“Plugins may not contain functionality that is crippled or locked, only to be unlockable by payment or upgrade. Paid functionality must be part of an externally hosted service or a separate plugin, that is not hosted on wordpress.org.”*
- *“Plugins may not disable included functionality after a trial period or quota.”*

In other words, all features of a plugin/theme that are hosted on WP.org should be accessible to the users, all the time. Therefore, if you do offer a Trial, you’ll have to serve the premium version for the Trial from an external, secure repository, just like you have to do when selling a premium version.

If you use WooCommerce or EDD, you’ll be delivering the downloadable premium version from your server – the one that is running your WordPress site. The benefit of using a service like Freemius or marketplaces in the current context is that the secure repository, the deliverability, and the fulfillment of the downloadable file are all offloaded to an external service which keeps your server happy 🙂

## Moneyback Guarantee VS. Trials With A Payment Method

A “Trial” has a very clear meaning – you get to try something for a limited period. This means that the expectation of consumers is aligned – they understand that after the trial is over if they don’t subscribe or purchase, they won’t be able to use the plugin or the theme anymore. On the other hand, A Moneyback Guarantee is a loose term and open for different interpretations when not reading the fine print. Many consumers assume that a Moneyback Guarantee means that you can buy the product, and if you don’t feel like it, you can get your money back – no questions asked. And since we are in the scope of digital products, there’s no actual need to “return the product”, which means that there’s nothing that should stop them from continue using it.

While some [Moneyback Guarantee types](help-documentation-selling-with-freemius-refund-policy.md) are “no question asked”, if you carefully inspect the refund policies of many popular premium WordPress themes and plugins, you’ll find that most of them offer refunds only when there was an actual issue with the product and the support didn’t manage to resolve the problem. In those cases, when a user just wants to give the product a try, one of the followings can happen:

- If such a user will read the policy and understand they can’t get a refund without a real excuse, they will simply move on to test the next product.
- If that user will upgrade without reading the policy and will decide to bail, they will get upset when your support rep tells them that they aren’t eligible for a refund even though they aren’t interested in continuing using the product. In fact, if you won’t refund them, you risk exposing yourself to rants on social media and bad reviews: things that are bad for your business and reputation.

So if you do want to offer some Moneyback Guarantee, make sure the policy terms are not hidden and super clear to the user.

My bottom line here is that Trials and Money back Guarantees are two different things, and have very different psychological messages for the potential subscriber.

Another quite important reason is that Trials tend to yield better results. You can read [this interesting experiment ran by Neil Patel](http://this%20interesting%20experiment%20ran%20by%20Neil%20Patel) where a Free Trial with a credit card upfront generated 16.4% more revenue than a Moneyback Guarantee offer. Here’s one of the highlights:

> The difference between a money back guarantee and a free trial was huge. Literally, double the amount of people would signup for a 7-day free trial that required a credit card upfront versus a money back guarantee offer.  
> ~ Neil Patel

I’m going to cover moneyback guarantees more in-depth in a future article.

## Summary + Next Steps

While most product ecosystems flourish by offering Trials for decades, Free Trials are highly underestimated and underused in the WordPress products ecosystem, mainly due to technical reasons and the fear of Trial abuse (an open-source code).

Offering Trials with your premium WordPress theme or plugin has huge potential and many marketing benefits. While Trials aren’t a good fit for all plugins and themes, when they are, it can have a meaningful impact on your business’s bottom line.

I’m proud that our team has managed to solve all of those challenges with [Freemius](wordpress-features-comparison.md) and level up our sellers’ capabilities with the top market standards while keeping everything compliant with the GPL license and the WordPress.org guidelines.

So whatever eCommerce solution you are using to sell your WordPress products I encourage you to evaluate your offerings and start incorporating Trial mechanics into your system. It may seem odd today, but so did automatic renewals 5 years ago and now it’s becoming the market’s standard.

Be ahead of your competition – lead the market instead of following it!