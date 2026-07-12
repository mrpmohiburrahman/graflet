At some point, most WordPress plugin developers will ponder the possibility of transitioning to SaaS 🧳 For good reason: There are plenty of perks to consider, ranging from scalability and larger target audiences to platform independence and proprietary code. So, what are the signs that your plugin can (or can’t) take the leap?

[Freemius](index.md) is an eCommerce solution working with makers who sell SaaS products and WordPress plugins. As such, our founder and CEO Vova Feldman is deeply familiar with both software delivery models and has some sage advice on whether your WordPress plugin is better suited to the world of SaaS.

There are a few considerations, so buckle up. First stop…

## The Challenges of SaaS Products vs. Plugins

Not to be a negative know-it-all, but… promising paths pose potential problems 🧙

![Transitioning from a plugin to SaaS can pose challenges - GIF of people nodding](https://freemius.com/blog/wp-content/uploads/2023/08/transitioning-from-a-plugin-to-saas-can-pose-challenges-gif-of-people-nodding.gif)

SaaS products and WordPress plugins are horses of a different breed, and it pays to know what kind of rodeo you’re in for. Let’s examine the challenges.

### Architecture Design

I’ll let Vova take it away:

> From a technical perspective, developers need advanced skills to run a SaaS product. In contrast, WordPress plugins are built on existing code infrastructure — in other words, someone’s already done the heavy lifting for you. WordPress is the bowl full of cream; your job is to put the cherry — meaning, the plugin — on top.

SaaS doesn’t offer the luxury of building on an existing foundation. Yes, there are libraries for different coding languages that can simplify different use cases, but developing a SaaS product is usually more complex than this: “*You need to deal with architecture design challenges like data structures, algorithms, and more. When it comes to plugins, typically, you don’t have to worry about any of those things*.”

### Handling Server Downtime

The severity of server downtime hinges on how you structure your SaaS product. Taking the wheel when autopilot fails — which is bound to happen sometime — falls on you.

“*This is a whole field in itself, known as system administration*. *When there’s an issue with your plugin, it usually only affects one website. When SaaS goes down, your *entire* user base is affected*.”

And sometimes, those user bases can run into the millions…

### Learning to Scale

Compared to plugins, SaaS has a higher potential for fast growth. But rapid scaling can be tricky to keep up with…

> You need to understand databases, performance, and learn about scaling. Of course, you probably won’t need to do this immediately. But with a SaaS product, your ultimate goal will be attracting lots — even millions — of users. Your software has to stay well-oiled, effective, and fast. If it’s slow or inefficient, you’re going to lose customers.

![Rapid scaling is a challenge with SaaS - GIF from Jaws movie](https://freemius.com/blog/wp-content/uploads/2023/08/rapid-scaling-is-a-challenge-with-saas-gif-from-jaws-movie.gif)

The challenges of running a SaaS product aren’t the only potential hurdles to heed; sometimes, SaaS is simply not the correct tool for your intentions.

## Signs a SaaS Product Isn’t Your Best Bet

There are cases when executing your software product as a plugin is the more logical choice. Often, the bedrock provided by platforms like WordPress offers the best way of connecting the digital dots.

### Your Product Offers Once-Off Functionality

Services that — for example — help you migrate your website from one server to another or export information are used irregularly or once-off. Offering a recurring service, on the other hand, is a crucial characteristic of SaaS.

SaaS businesses rely on retaining customers over the long term to ensure a steady revenue stream. Products that offer ongoing value are more likely to keep customers engaged and subscribed. If the value is limited or one-time, customers might cancel their subscriptions after a short period.

## Subscribe and grab a free copy to start Mastering SEO on the WordPress.org Repository

Make the WordPress.org search algorithm work for you with actionable tips to rank your plugin higher.

![Mastering SEO on the WordPress.org Repository](https://freemius.com/blog/wp-content/plugins/fsblog-utilities/assets/img/svg/cheat-sheet-ebook.svg)

### Your Product Offers a Platform-Specific Solution or Depends on a Platform for Its Functionality

Suppose your plugin is adding functionality or solving a problem that’s specific to WordPress. Let’s use the example of a plugin that allows you to customize the WP Admin dashboard. It would make no sense to convert it to a SaaS because, as Vova puts it: *“You won’t be solving a problem because there’s no problem to solve.”*

Similar to solving issues, it’s also possible that your product wouldn’t be able to exist without a platform like WordPress in the first place.

The solution or functionality you’re offering may require information that sits in the WordPress database. While it’s not a rule and there are exceptions to that, one of the primary purposes of a SaaS product, however, is to offer something that can be used by anyone, regardless of the web platform/operating system they use.

“*If there are platform-specific requirements for your product, you’ll need to create a connection to add or enable that extra layer of functionality*. *There are cases where it’s possible to do this, but it doesn’t always make sense, and it’s a pretty technical topic.* ”

If you believe your product has SaaS potential but doesn’t *quite* cut the mustard, there may be a happy medium to fulfill your SaaSpirations.

## Your Product Is Better Suited As Semi-SaaS

Some products won’t serve their purpose as either pure plugins or pure SaaSes. In these cases, going the semi-SaaS route could be a viable option.

Semi-SaaS shouldn’t be construed as a hybrid that offers the perks of both SaaS products and plugins. Instead, it denotes a plugin that incorporates some of the characteristics of a SaaS product (and — sometimes — vice versa).

[![](https://freemius.com/blog/wp-content/uploads/2023/08/come-again.gif)](https://freemius.com/blog/wp-content/uploads/2023/08/come-again.gif)

Come again?

To illustrate, let’s discuss [BlogVault](https://blogvault.net/), a WordPress backups plugin that easily recovers websites when something goes wrong (and more).

BlogVault is a combo — or semi-SaaS — because the backup functionality itself is executed on the plugin that’s running on the website, while the backups themselves are processed through their service, which stores encrypted copies of the backups externally across multiple data centers.

A backups plugin like BlogVault is likely not a good fit for pure SaaS as it needs to have access to a website’s database and must have knowledge of and permissions for the website’s filesystem, which wouldn’t be possible as a generic solution (platforms like Wix or Webflow don’t offer that level of access).

At the same time, it also can’t be a pure WordPress plugin if it wants to offer its own cloud storage layer. Naturally, relying on the website’s hosting for storage is a big no-no for a backups plugin, as many of the low-tier hosting companies offer minimal storage. And even if there’s enough storage on the server itself, storing backups on the same server generates a single point of failure, which means if the server’s storage gets corrupted, it can impact the backup(s) and make them unusable when needed the most.

Now that we’ve listed the reasons your product should probably stay a plugin/become a semi-SaaS, let’s showcase:

## Signs Your Product Can Become SaaS

### You Offer a Platform-Agnostic Solution

Just like some products will perform better as plugins that offer a niche service or functionality within WordPress, others will perform better because they aren’t bound to a single system. Techopedia describes platform-agnostic products as follows:

“*Platform-agnostic is a concept that refers to the design attributes and philosophies of software products. A platform agnostic product runs equally well across more than one platform.”*

[![](https://freemius.com/blog/wp-content/uploads/2023/08/free-spirit.gif)](https://freemius.com/blog/wp-content/uploads/2023/08/free-spirit.gif)

In a SaaS of its own

If your product and most of its features are platform-agnostic, there’s potential for it to become a universal service or solution, and this is usually the first sign that it would do well as a SaaS. Of course, you’ll need to consider things like technical details, scalability, and server/serverless pros and cons, but if the initial indications are there, you’re well on your way to fulfilling your SaaSpirations 🤠

### Ingredient X 🤫

This is obvious, but a big deterrent of open-source software is that your code is available for all the world to see, use, and fork. If your product contains intellectual property like a proprietary AI algorithm or any other type of ‘special sauce’, you’re basically giving it away for free. Vova expands:

### Heavy Resource Consumption

Some products are heavy on server resources, and you can’t rely on WordPress websites to run them as plugins. An example of this is artificial intelligence. Think of an AI model that allows you to take a photo and remove the background, leaving only the primary item that you’d like to be present.

“*My friends from [Bazaart](https://www.bazaart.me/), a popular AI-powered photo and video editing app for iPhone, purchased special GPU-optimized machines that cost tens of thousands of dollars to optimize their AI models. Intellectual property aside, the point here is that it’s impossible to rely on traditional hosting services or web platforms like WordPress to run resource-heavy algorithms*.”

And if you integrate your plugin with an external service provider to bear the load? “*Then it’s not really your SaaS*,” Vova states. Essentially, you’ll be providing a plugin that facilitates a connection with another service, but you won’t be the SaaS provider.

[![](https://freemius.com/blog/wp-content/uploads/2023/08/not-mine.gif)](https://freemius.com/blog/wp-content/uploads/2023/08/not-mine.gif)

It doesn’t have to be this way

Despite their resource requirements, SaaS products do have an upper hand when it comes to know-how.

### Your Product Has Features That Thrive on Network Knowledge

A plugin, by design, is installed and works on a single website (leaving multi-site networks aside for simplicity). It doesn’t have an external “shared brain” allowing it to store info from multiple sources/websites. A SaaS product, on the other hand, can draw knowledge from millions of different websites.

Let’s use a plugin that’s purpose is to block brute force attacks as an example.

At any given moment, there are millions of bots trying to break into WordPress websites or find vulnerabilities in the background. They’re running from different servers, and the way the internet works is that every server has an IP address.

“*In a brute force attack, there are suddenly a large number of bots that are trying to attack your website*,” Vova says.

> Now, let’s say we have this plugin that identifies attacks and tries to block or mitigate them in some way. If it’s a pure plugin — meaning, its knowledge is based purely on the website it’s running on — it might be prompted to blacklist a server’s IP address after receiving, say, ten consecutive requests from it. But if millions of servers are attacking it at once with only a request or two from each server, it will have no way to protect against such an attack as those requests may be legitimate traffic.

Now, say the product is a SaaS that incorporates the above plugin.

If the SaaS is running on millions of websites, it has access to the combined knowledge of all of them. If there is a server that raises suspicions after repeated attacks on websites that use the plugin, the SaaS can blacklist that IP address across the entire network of websites that use it, instead of just blocking it on one specific site.

To summarise: If your product will benefit (read: get better at doing what it needs to do) from having access to and learning from a wider network, then that’s a big sign that SaaS is probably the way to go.

The final — and arguably the biggest — SaaS signal, however, isn’t explicitly about software.

### You Want to Offer Something Beyond Code and Functionality

SaaS can be utilized to create something new and unique. Think of search engines like Google, social media platforms like Facebook and Twitter, eCommerce platforms like Shopify, AI tools like ChatGPT, and communication platforms like Slack. All of them are SaaSes, and they offer a ready-made, seamless experience to customers. A SaaS product is a means to newness because it allows you to build an idea from scratch — one that often extends beyond the current landscape of software offerings.

Similarly, SaaSes are excellent for providing out-of-the-box solutions that save customers time and money or prevent a regulatory headache. Case in point — this is exactly what [Freemius](index.md) does:

Challenges, hurdles, and signs aside — I’d like to reemphasize my point from [WordPress Plugins vs. SaaS: What’s the Difference & Which to Choose](blog-wordpress-plugins-vs-saas-which-to-choose.md)?

## Choose Your Flavor!

While both WordPress plugins and SaaS products offer perks and perils, one is not superior/inferior to the other.

SaaS products may be more scalable, but they also require higher operating costs, resources, and advanced development skills to pull off. On the other hand, WordPress plugins have the support of the open-source community and offer a chance to fill a niche or address a specific pain point in the ecosystem. However, your code is publicly accessible, pushing updates is a headache, and WP infrastructure is considered to be outdated.

![Can your plugin transition to SaaS? GIF of Gordon Ramsey](https://freemius.com/blog/wp-content/uploads/2023/08/can-your-plugin-transition-to-saas-gif-of-gordon-ramsey.gif)

My hope is that this article gives you a roadmap that helps you find the straightest path to your ideal software product destination. Next up — in the final installment of our SaaS series — we’ll unpack how to convert your plugin to a SaaS product and how you can test the waters before diving in.