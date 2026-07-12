Do you recall the last time you released a new version of your WordPress plugin or theme to quickly discover that you mistakenly added a new major bug that slipped through your testing sequence cracks?

[Yoast SEO 3.0](https://yoast.com/yoast-seo-3-0-release-a-recap/) broke many websites back in 2015. [Elementor 3.0](https://elementor.com/blog/elementor-3-0-lessons-learned/) did the same this year. And those are just two examples off the top of my head of fantastic companies in our space with 100+ employees and dedicated QA personnel (and no, it’s not related to version 3.0, but maybe it’s a sign to skip that version in your software ;)).

Whether you are a self-taught coder or software engineer, indie-developer, or part of a large plugin/theme shop, we all have to deal with bugs. It is an inevitable part of software development.

No matter what fancy CI/CD/testing automations you put in place – you will never be able to test it all. The number of server configurations (PHP, MySql, caching, web server), WP versions, combinations of plugins and themes… is all endless.

And it’s counterintuitive. The more popular & stable your products get, the higher the chances for a dreaded “Clusterbug” release, which will drain your support, may significantly impact your customers’ trust & loyalty, and potentially harm overall brand reputation.

While you can’t avoid bugs, you can, and most definitely should, mitigate risk as much as you can.

If you have a smartphone, you probably noticed that some of your friends get Android/iOS updates days, weeks, sometimes even months before you get them. That’s not a coincidence, and no, it’s nothing personal against you. It’s an intentional progressive deployment process called Staged Rollouts that helps companies like Apple ship major software updates to over a billion devices.

Yes, a billion!

Can you even comprehend the amount of responsibility a version lead at Apple would have on their shoulders if they had to push a live update to 1.5 billion mobile devices simultaneously? I can’t. I bet that no sane man would agree to carry such a responsibility.

So, how does the Staged Rollouts mechanism work? How can you implement it? And what is WordPress.org waiting for? These are the topics I’m going to cover down below.

## What are Staged Rollouts for WordPress Plugins & Themes?

Staged Rollouts allow you to specify the number (or percentage) of websites that you want to roll out a new version to. A Staged Rollouts mechanism enables you to begin your release cycle with limited exposure and then increase it incrementally while you monitor support & feedback, thereby building confidence in your release for you and your users.

![Freemius Staged Rollouts Mechanism Overview](https://freemius.com/blog/wp-content/uploads/2020/12/freemius-staged-rollouts-mechanism-overview.jpeg)

## What are the Benefits of Staged Rollouts?

Instead of risking your entire install base with the release of potential bugs, conflicts with 3rd party plugins/themes, or even UI/UX issues, you can release versions progressively, minimizing the number of people and websites that will get exposed to unexpected problems. Once you iron-out all the issues and bugs discovered during the rollout process, the vast majority of your users will get exposed to a “mature” and much more stable version.

> We use rolling updates to ensure the quality of our new releases. If there is a problem with a new release, we can identify it quickly, and only a small subset of users would have been affected.
> 
> John Turner, Founder at SeedProd

Using Staged Rollouts is THE best practice for responsibly releasing software – a process that many companies (regardless of size) outside the WP bubble follow.

There is a big opportunity for the WordPress community to take advantage of Staged Rollouts, which I’ll get to in a bit.

## Are Beta Programs Similar to Staged Rollouts?

Setting up a [Beta program for your WordPress product](https://freemius.com/blog/wordpress-plugin-beta-testing/) is a great start, but it is far from being as effective as Staged Rollouts, and it has a fundamentally different purpose & dynamic.

Unless your plugin or theme is extremely popular and has a large community, it’s quite challenging to recruit a statistically sufficient beta-group since only a tiny fraction of users will be interested in joining. Even if you excel in recruiting a decent group of beta-testers, you have to rely on their availability & goodwill to test the product, and then hope they make the extra effort to report the issues they find.

How many people do you think will see through this entire process? Not many.

![Beta Test Meme](https://freemius.com/blog/wp-content/uploads/2020/12/beta-test-meme.png)

Beta testing is a pre-production process in which your support efforts are fully controlled and testers expect to have issues with beta releases. Therefore, testers’ expectations about quality do not represent the general sentiment of your user base.

Moreover, a responsible Beta program will warn its testers to avoid using beta versions in production environments, so beta-testing doesn’t really simulate live production websites.

## How to Manage a Staged Rollout Release for Your WordPress Plugin or Theme?

As part of my research on Staged Rollouts, I had the chance to e-meet Amir Helzer and learn from their 2+ years of experience using [Staged Rollouts with WPML](https://wpml.org/changelog/2019/09/wpml-4-2-8-launched-through-staged-rollout/) and Toolset, plugins running on more than 1,000,000 WordPress websites.

Here’s what Amir shared about their Staged Rollouts implementation:

> When a website installs any of our plugins, we draw a random number between 1 to 100 and store it in the site’s database to remember. This method essentially splits the websites into 100 bins in a random fashion.
> 
> When a release is ready to go live, it will only become incrementally available to a single selected bin. Every day we increase the release’s exposure to an additional 5% of websites in the designated bin. And fix and patch the coming issues as we go.

![WPML Staged Rollouts Mechanism Distributes Updates to Bins of Users](https://freemius.com/blog/wp-content/uploads/2020/12/wpml-staged-rollouts-mechanism-distributes-updates-to-bins-of-users.jpeg)

To diversify the environments using the updated version and avoid having the same early release “victims” repeatedly, Amir confirmed that every new release goes to a different bin of users first.

This approach also means that an average release cycle takes about a month to be available for every user.

> It takes time until people see a new release available in the WP Admin and update their version. And even after they do, it can take days until they discover an issue.
> 
> With our audience size, inevitably, every release has some issues. Our main goal is to make sure we avoid introducing new issues, and if we do, we have a reliable process to solve them.
> 
> The release cycle is indeed long, but even if, in a worst-case scenario, there’s some crazy bug that we missed in testing, 95% of our users are not even aware of all the drama, as they are not exposed to the release until it’s stable.

Amir also emphasized the importance of syncing with the entire team before releases, especially customer support and development. This way, team members can provide extra focus on tickets triggered because of issues related to the ongoing release, with the goal of checking, confirming, and fixing valid issues and releasing patches as quickly as possible.

> We have three support tiers in our team. Tier 1 will look at the issue, validate it is actually an issue related to the plugin’s release by reproducing it. When a case seems related to the new release, it goes to tier 2, which will debug the problem to validate it’s indeed related to the release and locate the relevant parts in the code that triggers the issue. If validated, the developer responsible for that code will get notified immediately to prioritize a fix.

OnTheGoSystems is a large company with almost 100 employees, so it makes sense they perfected their Staged Rollouts process. But, even as a single product developer with one support tier (you & yourself), Amir’s insight can teach us that it’s critical to allocate dedicated resources to releases. It’s a good practice to prioritize support tickets that even “smell” to be related to your fresh release and reduce exposure from new issues as much as possible.

## Why are there (almost) No Plugins or Themes which Support Staged Rollouts?

In preparation for writing this article, I tried to ask the community to see who’s utilizing staged rollouts in order to get feedback about their experience, what they learned, etc.

Unsurprisingly, I found only two WordPress companies in my network that have set up Staged Rollouts as part of their release cycle. Many devs didn’t even know of the concept, and the rest don’t use it since their distribution solution doesn’t support it (or they may have thought about developing it and don’t have the time).

![Facebook Survey by Vova Feldman Majority Do not Use Staged Rollouts ](https://freemius.com/blog/wp-content/uploads/2020/12/facebook-survey-by-vova-feldman-majority-do-not-use-staged-rollouts.png)

Most plugin and theme developers that are not selling through Freemius sell from their website via [EDD or WooCommerce](https://www.codeinwp.com/blog/edd-vs-freemius-vs-gumroad-vs-woocommerce/), which both do not support Staged Rollouts. Those who are selling through marketplaces like [CodeCanyon](blog-codecanyon-sell-premium-plugin.md) and [ThemeForest](blog-themeforest-good-place-sell-premium-wordpress-theme.md) also don’t have an out-of-the-box solution, and most likely will never have.

Even developers who are aware of the concept have no choice but to develop their own mechanism to support Staged Rollouts. This infrastructural development is typically very hard to prioritize within a product company.

## Subscribe and grab a free copy of our WordPress Plugin Business Book

Exactly how to create a prosperous WordPress plugin business in the subscription economy.

![The WordPress Plugin Business Book](https://freemius.com/blog/wp-content/plugins/fsblog-utilities/assets/img/svg/cheat-sheet-ebook.svg)

## How Do Staged Rollouts Give You a Commercial Advantage?

Since almost no one takes advantage of Staged Rollouts at the present moment, if you start utilizing Staged Rollouts and market it properly on your website to let visitors know you have responsible release cycles, it definitely gives you a competitive edge and increases trust in your product/brand!

If you analyze the market from a developer’s perspective, you’ll notice that many developers closely follow their competitors and usually set their prices within the market’s price range in their vertical, which leads to competing WordPress products offering similar features in the same price range.

From the buyer’s perspective, that means it’s often a toss-up about which product to buy because they all have comparable features and pricing. But, when you evaluate several plugins that cost the same and, give or take, have the same features, wouldn’t you be inclined to go with the product that offers Staged Rollouts knowing its production releases should be more stable than competitors?

Staged Rollouts increase the confidence in your product and business. It is an edge that you can capitalize on before Staged Rollouts become standard practice (which I truly hope they do).

## Freemius Now Supports Staged Rollouts for Paid Plugins & Themes

We are excited to pioneer Staged Rollouts in the premium WordPress plugins and themes ecosystem. Our selling makers can now release updates safely, confidently, and reliably, with minimal blowback to their users or support/development resources.

We know how challenging and nerve-racking major releases can be, especially since there’s always the potential risk of negatively impacting your brand following a “Clusterbug” release.

With Staged Rollouts in place, there’s a safety net to our makers’ brand sustainability & defendability, and ease the unnecessary stress associated with releases to a large userbase.

This goes hand to hand as a benefit for our makers’ customers. When users purchase products sold through Freemius, they can now have confidence they are opting into a solution powered by Staged Rollouts and they can expect much more stable releases from premium plugins and themes utilizing the mechanism.

If you are selling with Freemius, [here’s how to properly use our Staged Rollouts mechanism](help-documentation-release-management-staged-rollouts.md#how_to_use_staged_rollouts).

### How Has Freemius Implemented Staged Rollouts?

Every website that activates a license to unlock a premium plugin or theme gets a record in our database. The first thing we’ve done is to introduce a new `last_served_update_version` property to store the latest product version that was made available to a website.

Then, we enriched the table responsible for storing release data with two new properties: `limit`, `uniques`.

When a developer flags a version as released, they will be prompted with the following dialog, allowing them to set up the percentage (or number) of websites that have an active license they want to roll out the paid version to:

![Freemius Staged Rollouts Release Limit by Percentage or Number of Sites](https://freemius.com/blog/wp-content/uploads/2020/12/freemius-staged-rollouts-release-limit-by-percentage-or-number-of-sites.png)

If they set a limited release rollout, the system will count the total active websites with an active license and then set the new `limit` property of the release accordingly.

Finally, we updated the API endpoint called by websites for checking if there’s a new release and introduced the following logic (in pseudo-code):

```
  latest_version = load latest version of product X
  If (website is on latest_version)
  	return “no new version”

  If (last_served_update_version of website same as latest_version)
  	return “no new version”

  If (latest_version is limited)
  	If (latest_version is limited AND uniques >= limit)
  	      return “no new version”

  	previous_version = load the previous version of product X

  	If (previous_version is limited too AND uniques <= previous_version.uniques)
  		If (website not using previous_version AND
  	  	  	last_served_update_version different from previous_version)
  			  	return “no new version”
  	else If (random({true, false}) )
  		return “no new version”

  	Set last_served_update_version of website to latest_version
   	Increment uniques by 1

  return latest_version
  
```

This algorithm ensures that:

- The exposure of the release is limited according to the set percentage of the rollout.
- If the previous version is still staged, i.e., it was never exposed to the entire install base, the websites that received the previous staged release will be exposed to the latest staged release first.

Unlike WPML’s Staged Rollouts architecture that assures each release will go to a different subset of their install base using logical bins, our implementation relies on randomness. So, a website may get two early-stage releases in two consecutive release cycles. However, this approach’s benefit is that we were able to ship Staged Rollouts to all our makers’ customers without the need to push an SDK update, which can take many months, even years, to propagate to all the customers.

## Why are Staged Rollouts Essential for The Future of WordPress?

When I asked Amir what was their trigger to develop Staged Rollouts for WPML release cycles, this is what he told me:

> 3 years ago, at WordCamp Europe, I spent time chatting with WPML customers to collect all kinds of feedback about their overall experience. The #1 frustration I found was that our customers were afraid to update the plugin as it can unexpectedly break their site.
> 
> Amir Helzer,
> 
> Founder of OnTheGoSystems (WPML, Toolset)

**I absolutely relate to that.**

Our internal policy at Freemius when it comes to updating plugins & themes is… simply don’t! With two exceptions: If there’s a known security issue or a feature that is available in a newer version that we need for our site.

Our updates policy was “written by blood” after several incidents of updates that went wrong and caused unexpected headaches and time-waste, interrupting our operation and timelines. And yes, we could have avoided some of the stress with a [staging environment](https://premium.wpmudev.org/blog/benefits-of-staging-environments-in-wordpress-development/), but this wouldn’t have saved us the time & hassle if we still wanted to pursue the update to production.

WordPress has evolved a bit since then, and now we have auto-deactivation on plugin failures. However, that doesn’t apply for themes and deactivation of a mission-critical plugin for our website is still a big problem.

The bottom line is that if I, as a plugin developer and CEO of a company that helps thousands of plugin & theme developers grow their businesses, am concerned about breaking our site every time we update plugins or themes on our site, then that certainly means most users have no confidence in updating software in our space.

Lack of Staged Rollouts holds us and the entire WP ecosystem back and gives SaaS-based competing solutions a considerable advantage. WiX and Shopify users don’t need to think about updates at all! Updates just happen for them in the background, and their software is always up-to-date, security & feature-wise.

If you watched last week’s State of the Word, WordPress co-founder, Matt Mullenweg, clearly gets the importance of up-to-date software. Here’s Matt’s vision for WP updates:

**The only way I can imagine WordPress becoming a “set and forget” is if software updates can be more reliable and trustable, and that can only happen with Staged Rollouts.**

## WordPress.org: Here’s How You Can Introduce Staged Rollouts for the Plugin and Theme Repository

Similar to our implementation, two new meta options need to be added to every plugin and theme release in the WordPress.org database: `limit` and `uniques`.

The `limit` meta option editing can be exposed in the Advanced View for the logged owner (and maybe for other committers):

![WordPress.org Suggested Staged Rollouts Mechanism by Vova Feldman](https://freemius.com/blog/wp-content/uploads/2020/12/wordpress-org-suggested-staged-rollouts-mechanism-by-vova-feldman.png)

A developer will have a way to control the exposure of every release, as well as the ability to set a limit for the next release.

Since WordPress.org doesn’t store structured data for every website receiving updates from WordPress.org, instead of storing the latest version “seen” by a website in the WordPress.org database, the storage of the data can be delegated to the websites. This means that the `'update_plugins'` transient and the data sent to WordPress.org API when checking for updates will need to be enriched with a `last_served_update_version`.

Finally, the WordPress.org updates API endpoints can be enriched with the same logic we used for Freemius Staged Rollouts implementation. Just instead of relying on the `last_served_update_version` from the wp.org database, the mechanism will depend on the value sent from the website by core.

Easy-peasy, no?

## Let’s Bring Back Users’ Confidence to Hit The Update Button

We all want to see WordPress succeed and constantly grow bigger and better!

With so many resources going into Gutenberg, it’s clear that WordPress’ leadership acknowledges we have to make the platform way more accessible for the average non-techy Joe. The thing is that as long as [software updates can’t be trusted](https://wptavern.com/wordpress-auto-update-system-misfires-updating-live-sites-to-an-alpha-release), even with Gutenberg and all the amazing page builders we have available, a non-techy person will run away to Wix at their first broken update, and I couldn’t blame them.

I’m calling out to the founder of EDD, Pippin Williamson, WooCommerce CEO, Paul Maiorana, and the WordPress.org team: We have an opportunity to make the plugin & theme ecosystem much more stable for the greater WordPress community. Let’s enable users to keep their software secure & up to date with less fear & frustration. While it may not look like a high priority in the short term, I’m sure we’ll all benefit from it in the long run.