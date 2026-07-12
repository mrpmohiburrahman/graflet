In 2017, [WooCommerce dropped its 50% Renewals Discount](https://wptavern.com/woocommerce-drops-50-renewal-discount-on-subscriptions) and got some backfire from the community due to how it was rolled out. This inspired me to shed some light on the topic of discounting renewals.

Renewals Discount is an important topic that hasn’t been covered in depth. I personally have had conversations about whether WordPress plugin and theme developers should be discounting renewals in just about every WordPress event I’ve attended in recent years (PressNomics, [PrestigeConf](https://freemius.com/blog/wordpress-plugin-developers-attend-business-conferences/), LoopConf, and [WordCamps](https://freemius.com/blog/wordcamp-europe-2017/)).

When I try to understand the reasoning behind the discount, the common and not surprising answer is: “Others do it, so we decided to follow the trend”. In most cases, I encourage developers to ditch the Renewals Discount for various reasons I’ll cover in this article.

## Was The WooCommerce Renewals Discount Removal Justified?

Let’s start by addressing the elephant in the room.

I *do* think that removing the Renewals Discount was a smart business decision for the company, and I’m certain it won’t have any effect whatsoever on WooCommerce’s checkout funnel conversion rate.

Having said that, much like many other members of the community, I think the transition was handled poorly. If I were a plugin or a theme developer [selling with WooCommerce](freemius-vs-woocommerce.md), it would definitely raise a red flag and hurt my trust in the company. Especially because it’s not the first time WooCommerce made such drastic changes to their licenses, without respecting the terms of the purchase agreement for existing customers — the previous one was [dropping their Unlimited pricing](https://wptavern.com/major-pricing-changes-at-woothemes) and changing the lifetime license terms to annual updates and support.

The proper way was to announce it publicly and explain the reasoning behind the decision, not try to sneak it via the renewal reminder emails, which most users don’t read anyway. Why would someone suspect a price change without any notice, right?

I also think they should have grandfathered the subscriptions for existing customers and applied the change to new customers only.

Now, when that’s out of the way – let’s get down to the details and explain why it was a smart move, and why, in most cases, you should likely do the same.

## Why Did Renewals Discount For WordPress Products Make Sense Five Years Ago?

Let’s start with some history of the WordPress business ecosystem.

We have been witnessing the WordPress products ecosystem mature with our own eyes.

If we rewind 10 years, charging money for WordPress plugins was practically a crime, while charging for a theme was OK, but still left a bad taste. Fast forward to five years ago, ThemeForest and CodeCanyon proved that selling premium plugins and themes was a big business. Many developers rode that success wave and started to [monetize their products](blog-how-wordpress-plugin-developers-make-money.md).

In fact, that was the “golden age” for WordPress themes. The themes market wasn’t yet saturated like it is today, and practically every person building themes was making solid money.

![wordpress plugins or themes](https://freemius.com/blog/wp-content/uploads/2017/06/wordpress-plugins-or-themes.jpeg)

All of this sounds great besides the fact that everyone was selling [lifetime licenses](blog-lifetime-license-for-wordpress-plugins-the-right-way.md)— many were even selling lifetime unlimited licenses.

In the next few years, more players got into the WordPress product “gold rush”, which effectively increased the competition and product supply. Changes in Google’s algorithms hit the ThemeForest and CodeCanyon traffic badly (rumors mention a 30%-50% traffic drop), and inevitably, monthly new sales dropped for many sellers.

What didn’t drop was the number of accumulated customers over all those years. If a developer offered Unlimited site licenses, the cost of providing support for an agency that paid $69 years ago was just growing over time in correlation with the growth of the agency’s clientele. That was a problem — a HUGE one. Many developers and product shops, like WooThemes, were drowning in managing customer support while their monthly income was going down.

The WordPress plugins and themes business model has naturally shifted from one-time payments to a one-time payment restricted to 1 year of support and updates. This move was the life jacket to get rid of the heavy support burden.

Unfortunately, this led to customers not renewing their licenses. If you think about it from the customer’s perspective, why should they? A manual renewal is a painful process. Let me walk you through the user experience flow of manual license renewal, assuming the renewal email was successfully delivered and got past the spam filter:

Ok, I need to login to the site.

Wait, I don’t remember my password, oh no… Now I need to go through a password recovery process. Ok, where’s that link… Oh, found it – “Forgot your password?”.

Do I really need the new version? Let’s give it a try…

Oh, they ask for my Credit Card again??

I should probably ask Ashley from the billing department to do it with the company’s Credit Card, I’ll call her next week to do it.

But do I really want to go through the whole process just for updates and support? We don’t have any issues with the plugin/theme right now, so we don’t need any support.

Do we really need the updates? I mean, it’s working fine as is…

Sounds familiar? How many people do you think bother completing this exhausting funnel? You guessed right — not many 🙂

![It's too much gif](https://freemius.com/blog/wp-content/uploads/2017/06/word-image.gif)

That’s when Renewal Discounts came to save the day— or at least developers hoped they would. Developers had to come up with a strong incentive to encourage customers to go through this tedious manual renewal process by offering aggressive discounts, just like WooCommerce did with their 50% Renewals Discount.

My friend, Mario Peshev, summarized it on his well-thought [post on the topic](http://devwp.eu/woocommerce-pricing-updates-and-community-backlash/):

The 50% renewal rate became a “de facto standard” among a good percentage of the WordPress plugin shops and businesses selling plugins and extensions. Some shops and developers keep charging the full price, others don’t bill for renewals at all, and there are various cases of 30-70% charged on an annual basis.

Moving forward to 2015. The renewal rates remained very low, ranging from 3% to 20% in the best-case scenarios. While it doesn’t cost money to accumulate customers that do not renew, it means that businesses need to sustain the same amount of new sales, month over month, just to get to the same numbers.

But what if Google changes its algorithm again (which happens all the time)? What if [WordPress.org updates its search algorithm](blog-seo-on-new-plugin-repository.md) (happened recently)? Or what if Envato decides to change its guidelines and removes your plugin or theme from its marketplace?

Every major fluctuation in your main distribution channels can have a major impact on your sales. In extreme cases even wipe out your business entirely.

If you think I’m exaggerating, just read [ThemeIsle’s story of Zerif Lite](https://wptavern.com/zerif-lite-returns-to-wordpress-org-after-5-month-suspension-and-63-decline-in-revenue). Their business took a major hit due to a suspension from WordPress.org, losing $75k every month (more than 60% of their business).

Long story short, developers started to acknowledge that, if they want to build a sustainable business and grow without living in constant fear of market shifts, they have to [start thinking more like SaaS companies](blog-why-wordpress-plugin-developers-have-to-start-thinking-saas.md) (Software as a Service): level up with the subscriptions economy and offer recurring payments with automatic renewals.

Over the past few years, there was a significant shift towards a subscription-like model with automatic renewals. Only now, we are starting to see the [buds of this subscriptions movement](http://mastermind.fm/episode-61-automatic-renewals-write-content/) and its enormous business benefits on the bottom line. Instead of an Avg. 10% renewals rate, developers are reporting 60%, 70%, and even 80% renewals rate. While there’s nothing new here and all these numbers have been publicly available for years, it’s a big mindset shift for the WordPress products ecosystem.

Automatic payment renewals are becoming the new market standard, but due to legacy reasons, developers are still offering a Renewals Discount without rethinking it, just because they offered them before.

## Should You Offer Renewal Discounts For Your WordPress Plugin Or Theme?

Before you get rid of your Renewals Discount, there are certain types of plugins and themes for which a Renewals Discount actually makes a lot of sense, even if the billing has automatic renewals in place.

In any case, you won’t be able to avoid Renewals Discount unless you set up your [sales platform to support recurring payments with automatic renewals](wordpress-checkout.md).

How will you determine whether you should keep (or start offering) the Renewals Discount?

If your product:

- Doesn’t bring more value to the customer over time
- Is easy to switch from to a competing product
- Is typically used for short-term periods

Then, you should probably keep the Renewals Discount or consider adding it, simply because you’re going to need to incentivize your customers to keep paying.

Let’s look at a few examples.

### Renewals Discount For WordPress Plugins

About a year and a half ago, we sponsored PressNomics and decided to give away a ticket to the conference as a lead generation mechanism to our marketing funnel.

To save time, we purchased a nifty plugin called KingSumo Giveaways. It served our needs for the giveaway, and I have nothing bad to say about it, but we haven’t run any giveaways since then, so we had no reason to renew the license.

If KingSumo had offered a 50% Renewals Discount, I would definitely have considered renewing the subscription, just in case we needed to run another giveaway in the future. But otherwise, why would I renew? I’ll just pay for a license again if and when we need it.

As a side note, the guys at KingSumo, the company behind the plugin, realized that and have since changed their model to a lifetime license for a higher price. Smart!

On the other hand, many plugins are way harder to ditch since they become even more valuable for the user over time.

Let’s examine Easy Digital Downloads as an example. [Last December, EDD increased all of their extensions’ prices by 50%-250%](https://pippinsplugins.com/reflection-on-a-price-increase/). While they grandfathered the Renewals Discount for customers that had an active recurring payments profile, one that automatically renews, legacy customers with old licenses that require manual renewals had to take a major price increase. For “heavy” customers paying for multiple extensions, that’s a few extra thousands of dollars a year.

Whether you agree with this move or not, what do you think those existing customers of EDD could do?

Yes, they could complain, express their anger on social media, or submit a 1-star review to show their frustration, but the hard truth is that heavy users whose whole eCommerce business [relies on EDD](freemius-vs-edd.md) will most likely continue paying for the renewals, even without the Renewals Discount because they are so vested. Unless, of course, they choose to completely switch to a competing solution, which is too complicated to do without a streamlined migration process, [like the one we offer at Freemius](help-documentation-migration-migrating-from-edd-to-freemius.md).

### Renewals Discount For WordPress Themes

Most themes are becoming harder to switch over time. Not necessarily because they bring more value to the customer, but mainly because the website owner had already spent time tweaking the settings, customizing with a page builder, using the theme’s widgets, adding custom CSS, and so on.

Switching a theme is a major time sink, so unless the customer wants to revamp the whole site, there’s little chance they will switch a theme after it’s all set up and running. Especially if it’s a multipurpose theme like Avada that enfolds dozens of plugins inside it.

When the website is mission-critical and used as the business’s online presence, customers prefer to have peace of mind by getting the latest security updates, and in the case that something bad happens to their site, they want the insurance of having an available support rep to help them. Having said that, I would encourage developers of lean themes, that are relatively low touch in terms of maintenance, to offer a Renewals Discount to increase the chances for renewals.

Themes used for short periods should probably offer a Renewals Discount to try and get at least some renewals. An extreme example of such a product would be a Coming Soon theme. Unless your customer is part of an agency that constantly develops new sites, they will only need to use a ‘coming soon’ theme for a very short period, and probably only once.

I’m not sure if any renewals would work in that case, but an aggressive Renewals Discount (probably 80% and higher) at least gives some chance for renewal.

The bottom line is:

If your product is usually used for a long period, is becoming more valuable over time, and it’s hard to switch to a competing one, once you have automatic payment renewals in place, there’s no need to incentivize your customers to renew the license by offering them a Renewal Discount.

The extra 20%, 40%, or 50% Renewal Discount, is not what’s going to change most customers’ minds if they don’t need your product updates or support. If your product fits that category and you do offer a Renewals Discount, then you’re simply leaving money on the table.

This is obviously a generalization, but it’s based on rock-solid renewals rate data.

## Grab a free copy of our Cheat Sheet for Selling Plugins and Themes

A growth roadmap with concise, actionable tips for every milestone of WordPress product development.

![blue book with the title “Cheat Sheet for Selling Themes and Plugins by Freemius” written on it](https://freemius.com/blog/wp-content/plugins/fsblog-utilities/assets/img/svg/cheat-sheet-ebook.svg)

## Discount The Initial Payment, Not The Renewals

If your premium WordPress plugin or theme **does** fall into one of the categories I mentioned above, once you have recurring payments with automatic renewals in place, instead of offering a Renewals Discount, start thinking like a subscription-based business and consider discounting the initial payment and [offering trials](blog-trials-premium-wordpress-plugins-themes.md).

Assuming you are billing annually, after running subscriptions for a year you should be able to calculate your renewals rate. Once you have that number, you can run experiments to increase your revenues.

Let’s play with some numbers…

Assuming your product’s annual price is $100, and the renewal rate is 50%, we can extrapolate that your customer LTV (lifetime value), is at least $150 (it’s more than that, but let’s go with the conservative calculation).

Let’s also assume that your conversion rate to a paying customer is 2% (a typical conversion rate for WordPress plugins and themes) which represents 30 new customers every month (one sale per day).

If you offered a 30% discount on the initial payment and increased your conversion to 3% by occasional promotions, coupons via an exit intent pop-up, email marketing, and other techniques — you could potentially increase your sales to 45 licenses per month but instead of generating $150 per customer, you’d only get $120.

Assuming that the renewal rate doesn’t change and that your acquisition funnel remains the same, the offering with the discounted initial payment will outperform the one without the discount.

Here’s what the monthly gross revenue will look like for the next five years:

![Monthly gross revenue projection graph](https://freemius.com/blog/wp-content/uploads/2017/06/monthly-gross-revenue-projection-graph-1.png)

I created a simulator so you can play with the numbers yourself, but please kindly make a copy of the spreadsheet before changing the numbers:

[Get the revenue projection simulator spreadsheet](https://goo.gl/tZeuVM)

Examining the most popular subscription-based businesses on the market, only a few offer Renewal Discounts, while the vast majority offers trials and discounts on the initial payment to lure users to become customers.

GoDaddy is a great example of that. They push hard on $1.99 domains for new customers for the 1st year, most likely losing money on new clients. But since they know that most of their customers will renew the domain for $15 / year, and probably buy more products over the years, the acquisition cost is worth their investment.

GoDaddy is very consistent about that —if you Google for GoDaddy coupons, you’ll find thousands of results, but good luck finding any discounts for renewals. All you’ll find are coupons for new customers.

Some people don’t like to discount their products because they think it will hurt their brand. But if you use [strategic discounts](https://hollerwp.com/discount-without-hurting-your-brand/) and don’t overuse them, you can increase revenue. There’s a good reason why GoDaddy and others do it, and we should learn from them.

## How To Transition From Offering Renewal Discounts To Not?

Once you’re ready to remove the Renewals Discount, successful execution of that transition mainly depends on well-thought-out communication with your existing users and respecting the terms of the license with your existing customers.

Unless you’ve been offering some crazy 80% Renewals Discount and the only way to save your business is by removing the discount for everyone, you should always strive to grandfather the license terms of all existing customers. If you don’t, your loyal customers will get upset, and for a good reason.

Basically, whoever created a recurring payments profile with a Renewals Discount before will continue getting the discount. Only new subscriptions will be affected.

The next step would be to publish a blog post announcement, at least 30 days before the change, to publicly let your followers and customers know about the upcoming update to the license renewal terms. Explain why you are changing the terms while focusing on how this change would benefit all of your customers (e.g. more resources to allocate for better support and development of new features).

Then, email all your customers and users ([in the case of a freemium product](https://freemius.com/blog/capture-user-email/)), letting them know that all new purchases will not be qualified for a Renewals Discount. Link to the announcement post and give them a time window to buy more licenses while still using the previous terms. Not only it is an excellent way to be transparent and fair, but also an opportunity to boost your sales among your existing user-base before the change takes place.

You may get a few angry people, but since you’ll be giving a “grace period”, you can simply send them a link to subscribe before the change. That’s fair, transparent, and respectful.

## Food For Thought – How Renewals Pricing Could Look Like In The Future?

In theory, if we could align the renewals’ price to the cost of maintaining each customer, that would be perfect.

Car insurance is a great example of an industry that uses this business model. If you don’t get into any accidents during the 1st year, when you get to renew your insurance, you’ll usually get a Renewal Discount, since statistically there’s a lower chance that an accident will occur during the next year. On the other hand, if you do get into an accident your insurance policy price will go up.

Emulating this model in the WordPress plugins and themes ecosystem would be great for the customers and the businesses. If a customer didn’t ask for any support during the first year, we could offer them a substantial Renewal Discount for their next payment. While a “problematic” customer who had utilized 10 hours of the support team’s time will pay a full price.

Unfortunately, this model isn’t feasible for software today.

First of all, not like WordPress themes and plugins, car insurance is mandatory, so people have to renew (or at least shop for an alternative insurance company). Second, insurance renewal is a manual process. Building a robust solution to sustain that software model is extremely hard, and most of the current payment gateways aren’t flexible enough to fulfill such a complex subscriptions model.

Finally, and the most important factor is people’s habits. While people are accepting this model in the car insurance industry since that’s the way this industry has operated for decades, I’m sure that plugin and theme customers would get upset if you “fined” them for opening too many support tickets 🙂

Now, you may think: “Why can’t you just charge per support hours?” The challenge with software is that in addition to support, as a plugin or theme developer, you have to continue developing, maintaining the existing functionality, adding more features, and improving the product — it requires ongoing work for as long as the product exists. It’s a topic for a blog post on its own, but monetizing based on support consumption is not a sustainable model for a software company.

## The Future Of WordPress Product Business Models

The WordPress products ecosystem has become truly mature.

Recurring payments with automatic renewals without a Renewals Discount have gradually become the market standard. Plugin and theme developers can now build sustainable businesses — which is great for the whole ecosystem.

If I had to guess the next shift in the WordPress premium plugins and themes space I’d definitely put my money on [monthly subscriptions](blog-wordpress-plugin-monthly-pricing-experiment.md), something that I’ve been personally cheering for in the last couple of years. We’ve been encouraging many of the [Freemius](index.md) sellers to include monthly pricing in parallel to their annual, and it’s been working great for them and for their customers (I’ll cover that in a future post with numbers to back up my thoughts).

I’d love to hear your thoughts on Renewals Discount, and if you are thinking about dropping them with your premium WordPress theme or plugin. If you need any additional advice regarding whether or not it’s the right move [get in touch with our team](https://freemius.com/cdn-cgi/l/email-protection#e89b9d9898879a9ca88e9a8d8d85819d9bc68b8785) or explore [more on our blog](blog.md) about [how to improve your subscriptions renewal rate](blog-reduce-customer-churn-increase-subscriptions-renewal-rate.md).