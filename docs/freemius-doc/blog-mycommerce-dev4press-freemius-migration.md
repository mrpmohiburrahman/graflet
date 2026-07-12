Last week, software makers worldwide faced a crisis: MyCommerce, a long-standing payment and eCommerce solution owned by [Digital River](https://www.digitalriver.com/), abruptly [shut down and filed for insolvency](blog-digital-river-mycommerce-shutdown-guide.md). For many, this is more than an inconvenience — it’s a financial disaster. Subscriptions have suddenly been canceled, payouts are frozen, and businesses are scrambling for alternatives.

[Milan Petrovic](https://www.linkedin.com/in/milan-petrovic-dev4press/), founder of [Dev4Press](https://www.dev4press.com/) — a company specializing in advanced WordPress plugins — is among those hit hardest by the collapse. After 16 years of relying on MyCommerce, he now faces a race to migrate his sales infrastructure before it’s too late.

In this exclusive interview, Milan shares his first-hand experience of the MyCommerce shutdown, the repercussions of a stable revenue stream running dry, and how he’s successfully transitioning to Freemius.

Before diving into the challenges he faced, let’s first take a closer look at Dev4Press and the plugins Milan has built over the years.

## Hey Milan 👋 Can you tell us about the types of plugins you create?

Our [bbPress](https://bbpress.org/) plugin suite is our biggest success, transforming simple forums into powerful communities that rival platforms like [XenForo](https://xenforo.com/), [vBulletin](https://www.vbulletin.com/), and [Discourse](https://www.discourse.org/). Our flagship product, [GD bbPress Toolbox Pro](https://www.dev4press.com/plugins/gd-bbpress-toolbox/), has been a game-changer since its launch in 2012, hitting its stride in 2015-2016. By mid-2024, it was powering over **15k** websites, accounting for nearly half of all Dev4Press plugin sales.

Since tracking downloads in 2015, we’ve seen over **250k** downloads from paying customers, with our pro plugins now active on nearly **25k** websites.

Meanwhile, [SweepPress](https://www.dev4press.com/plugins/sweeppress/) — our first plugin integrated with Freemius — is rapidly gaining traction, proving that innovation continues to drive our growth.

![dev4press sweeppress plugin](https://freemius.com/blog/wp-content/uploads/2025/02/dev4press-sweeppress-plugin.png)

## Impressive! On a less pleasant note — MyCommerce was a key part of your business for years. What happened when it suddenly shut down? Were any of your plugins directly dependent on it?

Not directly, no. MyCommerce handled the sales, but the plugins themselves were independent. That said, the shutdown still caused a huge disruption.

> Around 900 active automatic subscriptions were affected, and they were essentially canceled when MyCommerce collapsed.

Luckily, we also have a lot of lifetime license holders who weren’t impacted, but for everyone else — it’s a different story. Customers with annual licenses are currently unable to renew. The same goes for subscriptions set to auto-renew. Every affected customer will need to manually repurchase their license through Freemius. This has created a major challenge in terms of both revenue recovery and customer communication.

## That’s awful. How much revenue did you have stuck in MyCommerce when they shut down?

By the latest estimate, around $5,000. Unfortunately, I haven’t been able to recover any funds because I no longer have access to the MyCommerce platform.

[![mycommerce login error message](https://freemius.com/blog/wp-content/uploads/2025/02/mycommerce-login-error-message.png)](https://freemius.com/blog/wp-content/uploads/2025/02/mycommerce-login-error-message.png)

The error message Milan received when trying to log into MyCommerce

I was lucky enough to get regular payments from MyCommerce through December 2024, while many other companies were hit with much larger losses throughout the year.

## You should always count your blessings, I suppose. What were the immediate consequences of MyCommerce’s shutdown for your business?

Originally, I planned to make the switch to Freemius gradually throughout 2025. After MyCommerce’s implosion, I’ve had to accelerate the transition to March. Naturally, this presents a major challenge: finding the time to tackle all this extra work and putting other tasks on hold until the migration is completed.

## That sounds like a massive project. You started migrating your plugins to Freemius before the shutdown. What led to that decision?

Sales had been declining throughout 2024, and [a lot of extra fees](blog-digital-river-mycommerce-shutdown-guide.md#:~:text=This%20collapse%20didn%E2%80%99t%20happen%20overnight.%20Here%E2%80%99s%20how%20events%20unfolded%3A) were added in September 2024:

- A new $100 monthly platform fee
- $185/hour client support fees
- $20 charge per chargeback
- Various undisclosed “miscellaneous” fees

MyCommerce’s support became slow and expensive, and many of my customers had bad experiences with their payment method updates for subscriptions. All of that made me realize it was time to make a change.

## Did you have to update or modify your plugins for the migration?

Yes. Since I was switching to Freemius, I had to integrate their licensing and payment system into my plugins. Given that Dev4Press offers multiple plugins with free and pro versions, maintaining backward compatibility with existing customers while transitioning new ones to Freemius required a lot of testing and development work.

> It was worth it to get everything running smoothly on a more modern and flexible system.

## Even the smoothest transitions have hiccups — what have been the biggest challenges moving to Freemius?

So far, 8 plugins are fully integrated with Freemius, 3 more are in progress, and 5 still to go. The biggest challenge has been finding the time to upgrade the plugins while maintaining the old licensing system.

Each plugin took a few days to integrate with Freemius — not just adding the SDK, but also updating them to the latest version of a shared library that handles plugin structure and interface. On top of that, everything has to be tested with our legacy licensing system, plugin update system, and more.

> Interestingly, adding the Freemius SDK was the easiest part — the real challenge was ensuring everything else was updated and worked seamlessly together.

[![dev4press plugins freemius developer dashboard](https://freemius.com/blog/wp-content/uploads/2025/02/dev4press-plugins-freemius-developer-dashboard.png)](https://freemius.com/blog/wp-content/uploads/2025/02/dev4press-plugins-freemius-developer-dashboard.png)

Milan’s plugins in the Freemius Developer Dashboard

## How has Freemius supported you during the migration process?

I didn’t need much assistance with the process itself. I chatted with Freemius founder and CEO [Vova Feldman](https://x.com/vovafeldman) beforehand to get a clearer idea of what to expect. Once I started, the integration was straightforward.

## What key advantages does Freemius offer over MyCommerce?

One of Freemius’ biggest strengths is its [analytics and insights](https://freemius.com/help/documentation/analytics-insights/), especially for free-to-pro plugins. It shows how users interact with the free version, which is key for understanding the upgrade process. Plus, communication via newsletters and detailed stats about plugin [activation and usage](wordpress-insights.md) is incredibly helpful.

> And, Freemius takes care of everything related to [licensing](help-documentation-wordpress-sdk-software-licensing.md) and [updates](wordpress-automatic-software-updates.md), which means I’ll eventually be able to spend less time managing admin and focus on development.

## Let’s talk about your customers. How are you handling communication?

I’m currently preparing comms. All users will be notified, especially those with active subscriptions, as these won’t be able to continue. For those switching to the Freemius version, I plan to [offer a](blog-freemius-release-notes-december.md#enhancements_for_migrated_products:~:text=drive%20revenue%20growth.-,Targeted%20Coupons%20for%20Migrated%20Customers,-Transitioning%20to%20Freemius) [discount coupon as an incentive](blog-freemius-release-notes-december.md#enhancements_for_migrated_products:~:text=drive%20revenue%20growth.-,Targeted%20Coupons%20for%20Migrated%20Customers,-Transitioning%20to%20Freemius).

## Have you noticed any differences in customer experience since switching?

Since I’ve only been using Freemius for about four months (with a limited number of plugins), I haven’t done any detailed analysis yet. However, this is the first time I’ve had visibility into how potential paying customers interact with free versions of the plugins, especially those from WordPress.org. This data will be incredibly valuable moving forward.

> With Freemius, I anticipate much better conversion rates of free users to paid versions.

## What steps have you taken to minimize subscription cancellations and revenue loss?

I was caught off guard when I received the email about MyCommerce’s service suspension and lost access to my account. My immediate response was to update the plugin pricing pages with notices about the disruption and start preparing for delays in plugin updates and operations. I quickly published a [blog announcement](https://www.dev4press.com/blog/announcements/2025/mycommerce-payment-processor-suspended-operations/) and am in the process of reaching out to all customers. I didn’t have time to panic — staying focused and taking action was a priority.

![milan petrovic mycommerce shutdown announcement on dev4press blog](https://freemius.com/blog/wp-content/uploads/2025/02/milan-petrovic-mycommerce-shutdown-announcement-on-dev4press-blog.png)

Milan’s announcement on Dev4Press’ blog

> This is not the time to panic. Find a replacement service and start migrating any data you can. MyCommerce’s shutdown was a shock, but it underscored the importance of having a backup plan and transitioning smoothly to a new platform.

## Wise words. Have your conversion rates or renewal rates changed since the migration?

I’m **very satisfied** with the current sales, even with the limited data I have from the ongoing migration process.

## Wrapping up with some good advice and looking towards the future – if someone is currently stuck on MyCommerce, what’s the first thing they should do today?

Gather all your MyCommerce data and start exploring other platforms! It’s crucial to find one that not only has the features you need but also allows for a smooth migration. This will save you time and headaches down the road.

Also — if you’re considering moving to Freemius, don’t hesitate to reach out to their support. It’s better to ask for help than waste your time waiting.

## How do you plan to protect your business from surprises like this in the future?

You can’t prevent every risk, especially when it’s out of your hands, but you can be prepared. Keeping up-to-date sales and customer records is key — if something goes wrong, you’ll need to act fast. The goal is to stay flexible and ready to pivot if/when needed.

## What would you say to software makers who are sticking with MyCommerce?

Honestly?

> Staying with MyCommerce at this point is a gamble. Even if they get back on track, the trust is already broken.

Waiting too long to move could mean losing customers and revenue. It’s better to take control now and switch to a platform that won’t leave you stranded.

**\[Editor’s Note:** For a comprehensive guide on making the switch ASAP, check out [How to Migrate from MyCommerce to Freemius in a Weekend](blog-how-to-migrate-from-mycommerce-to-freemius.md).**]**

## Once the migration is fully wrapped up, what’s next for Dev4Press? Any exciting plans?

Absolutely! I have a few new plugins in the works that I can’t wait to launch. But first, I need to focus on getting everything back on track — reconnecting with customers, handling lost subscriptions, and making sure my plugins are running smoothly again. Once that’s settled, I’ll be full steam ahead on new projects!

## Thanks for sharing your insights, Milan! We wish you all the best with the migration in the coming months. Where can readers follow your journey and stay updated on your work?

For updates on my projects, you can follow me on [WordPress.org](https://profiles.wordpress.org/gdragon/) and [GitHub](https://github.com/dev4press), where I share plugin releases, contributions, and open-source work. I’m also active on [X/Twitter](https://x.com/milangd), where I post about my work and the industry. On [LinkedIn](https://www.linkedin.com/in/milan-petrovic-dev4press/), I share professional updates, industry news, and connect with other makers. For more personal content, you can find me on [Facebook](https://www.facebook.com/millanp).