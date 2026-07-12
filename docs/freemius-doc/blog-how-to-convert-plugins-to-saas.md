Converting your plugin to Software as a Service could prove to be fanSaaStic for your product-making journey 😁 Seriously, though — SaaS offers developers an opportunity to service bigger markets and potentially grow their products into empires. Assuming you’re ready to take up the mantle of SaaS emperor 👑 how does one transition from a WordPress plugin to SaaS?

You’ve weighed up the considerations discussed in [WordPress Plugins vs. SaaS: What’s the Difference & Which to Choose](blog-wordpress-plugins-vs-saas-which-to-choose.md) and [Signs Your Product Has The Potential To Become a SaaS](blog-signs-wordpress-plugins-can-convert-to-saas.md).

Your SaaSpirations seem plausible and you’re keen to get the $aa$ party started, but what are the practical things you need to do? Freemius CEO and founder [Vova Feldman](https://twitter.com/vovafeldman) has been building SaaS startups since 2009 and knows the more extensive considerations + practical steps to transform a plugin to SaaS. In this article, he shares some handy pointers to help you facilitate the process.

**SIDE NOTE**: I’m not sure if you’re aware, but Freemius is, in fact, a SaaS. We cater to plugin, theme, and static software WordPress developers, but our offering also extends to SaaSpreneurs. You’re welcome to get in touch with us if you need some technical support while making the move from plugin to SaaS but in the meantime, we’ve put together the fundamental pieces of the puzzle to help you get going.

![wrestling announcer GIF in saas article](https://freemius.com/blog/wp-content/uploads/2023/09/wrestling-announcer-gif-in-saas-article.gif)

## Should You Start With a Plugin or SaaS?

Suppose your idea for a software product has not yet crystallized. In other words: If you have a SaaS-worthy concept, is it better to test it as a plugin first? Vova answers below:

As mentioned above, you (technically) don’t even need a website to distribute a plugin. With SaaS, it’s the complete opposite because a website is essential for delivering the software — there’s no way around it. To elaborate on the video: Whereas plugins don’t require dashboards for configuring settings on your end, SaaSes do. WordPress core already provides the infrastructure and APIs for creating those settings pages but with a SaaS, you’ll need to build a dashboard with product settings yourself.

Starting with a WordPress plugin is an effective way to validate if there’s demand for your product or service, too. “*Before you invest all the technical resources required for SaaS, you can just push out something, see how it goes, and iterate the product based on feedback,*” Vova explains. “*It helps you figure out if there’s a product-market fit before you take a massive leap of faith with little to no feedback to go on. Once you’ve established that, you can go ahead and transition or expand into a SaaS.*”

Of course, this doesn’t imply that WordPress or similar ecosystems should merely be treated as sandboxes for potential SaaS candidates, but:

> If you want to do something fast, it’s logical to opt for the easiest way. And if you know from the beginning that your product idea ticks all the right boxes for SaaS, build your plugin with that in mind. The way you code it will make for a more concrete and seamless structure if and when it’s time to transition to SaaS.

Back to the main premise: you’ve got a WordPress plugin, it’s performing well, and you’re confident it could shine as a SaaS…

## Converting Your WordPress Plugin to SaaS

### Determine the Architecture and Design of Your Service

“*I think this is the most fundamental, technical thing you’ll need to figure out to transition from a WordPress plugin to a SaaS*,” Vova says.

[In a previous SaaS article](blog-wordpress-plugins-vs-saas-which-to-choose.md), we discussed how distributed software *—* like WordPress plugins *—* works. In a nutshell, the software is sold as a product to users, who must download, install, and run it on their hosted server. It’s also the user’s responsibility to download and install updates and improvements to the plugin. This is the opposite of SaaS, which is served ‘ready to go’ and doesn’t have to be downloaded, thanks to being cloud-based. This seamlessness also means that SaaS automatically feeds through changes to the entire user base.

“*With WordPress plugins, every node — in other words, every website your plugin is running on — takes care of the resource requirements. If you suddenly have, for argument’s sake, a million users to serve after you’ve transitioned to SaaS, the consumption is much higher than before.*”

## Subscribe and grab a free copy to start Mastering SEO on the WordPress.org Repository

Make the WordPress.org search algorithm work for you with actionable tips to rank your plugin higher.

![Mastering SEO on the WordPress.org Repository](https://freemius.com/blog/wp-content/plugins/fsblog-utilities/assets/img/svg/cheat-sheet-ebook.svg)

### Separating User Interface from Business Logic

Following modern web development practices, your high-level architecture should have a clear separation between your SaaS’s UI and its BL, which can be achieved by using a RESTful or GraphQL API. This front-end/back-end decoupling provides the all-important flexibility to work with different technologies and change them as you go.

For example: You build your SaaS dashboard using ReactJS. If the go-to framework is no longer ReactJS three years from now and you decide to switch, you’ll be able to do so easily without the need to make any changes to the ‘brains’ of your SaaS.

### Server-less is More!

If you’re not experienced with servers and cloud computing, a great solution for the API implementation is going Serverless. It allows you to skip a lot of hassle and focus on building your SaaS’s ‘brains’ without thinking of the overhead, which simplifies ***everything***.

If you’re unfamiliar with Serverless, here’s the definition from IBM:

*“Serverless is a cloud computing application development and execution model that enables developers to build and run application code without provisioning or managing servers or backend infrastructure.”*

“*Amazon has a Serverless solution called Lambda. Cloudflare offers Workers. Google has its App Engine. And there are many more solutions out there that offer similar capabilities*,” Vova says.

### Optimize Your Architecture for Cost – You Have To!

While serverless is great, financial ramifications may arise — especially when it comes to scaling.

When your SaaS is still fresh and only has a few users, Serverless’s services will be much more affordable as they charge according to the number of requests (and you won’t have many). But when your resource consumption starts growing, a single, well-configured AWS EC2 with Nginx can run millions of requests per day at a very affordable price (which will be *way* cheaper than Serverless).

With plugins, you simply don’t have to consider resource consumption costs as you rely on the WordPress server’s resources to execute your plugin. But — as you’ll realize in time — when it comes to SaaS, incorporating financial optimization is a meaningful part of technical design. If the cost to support a SaaS customer is higher than what they’re willing to pay, you’re going to have a problem. No matter how amazing your SaaS is, the numbers have to check out. If they don’t, you’re doomed to fail.

![financial optimization is part of successful saas GIF of man jumping in pool](https://freemius.com/blog/wp-content/uploads/2023/09/financial-optimization-is-part-of-successful-saas-gif-of-man-jumping-in-pool.gif)

Not good

### Scale with Cloud Computing

> Unless your margin with Serverless is healthy to begin with, you’ll probably consider making a few transitions at some point when you start scaling. This will include things like setting up your own cloud servers, managing database and storage, load balancers, caching layers, and a whole bunch of other ‘fun’ 😅 technicalities.

Whether you start with cloud computing from the get-go or get there when you’re ready to scale…

### Recommended: Stick to Horizontal Scaling

If your servers run like APIs, they conform to a concept known as horizontal scaling. Vova explains:

To add to the above video: Suppose you’re on a single load balancer and you notice the consumption of your servers is getting exhausted/slowing down. Do I even need to say this is bad for business? 😅

“*Horizontal scaling is the recommended route for APIs. With vertical scaling, you’re just increasing the same server resources. The problem with vertical scaling is that at some point, and due to hardware costs that are not linear, every jump to higher resources gets more expensive — especially when the numbers are high. For example, it’s cheaper to run 192 servers with 16 GiB RAM than a single server with 3072 GiB RAM. So unless your SaaS does need a resource-intensive machine to run some special algorithms or big data mining, keep your API servers stateless and as light as possible so you can scale cost-effectively.”*

### Pricing Your SaaS

With WordPress plugins, the primary decision in setting your pricing is typically based on estimated support costs, market prices, and ongoing development. With SaaS, as mentioned before, you have to incorporate resource consumption as part of the equation.

For example, if you build a SaaS that offers some AI functionality that leverages ChatGPT, every request to ChatGPT comes with a cost. You can either add a margin on top of that or be transparent about your pricing — excluding the cost of ChatGPT requests — thereby delegating those costs directly to your SaaS customers.

> The math is relatively easy when there’s a clear price tag on your resources per user or requests (which is another benefit of serverless per request pricing), but when you start to manage servers, the math gets tricky. A single server can serve variable users and requests, but you still need to pay for the server whether it’s in use or not.

This is one of the reasons most SaaS products offer a monthly plan. As the SaaS owner, you have monthly server bills to cover, so it’s easier to get your customers aligned on the billing cycle.

### Should You Stick to PHP?

“*In terms of coding languages, you have a lot of freedom with SaaS. On one hand, freedom is good because it doesn’t impose any limitations on what you can do. On the other, you need to use that freedom responsibly and avoid making costly mistakes. Obviously, with plugins, you have no choice but to use PHP.”*

As to whether you should stick to PHP: there’s no clear-cut answer, and it depends on your needs. It’s up to you to decide if you’re going to keep your product in PHP or move to another language. It’s definitely not a must, and it’s possible to do this in parallel if you intend to build out the SaaS separately from your plugin. That said, moving over to a new coding language may be useful if it offers meaningful benefits. *“This is especially true for AI products, for which there are far better and more specialized languages than PHP,”* Vova says.

It’s even possible to mix two coding languages and have them in different places. If you go this route, you’ll need to figure out if (and how) the different languages will communicate with one another or whether they’ll take care of different functionalities with no cross-communication.

### You’ll Need a Dashboard

“*Users need access to a dashboard on your website where they can manage the product*,” Vova says. “*It’s a place where they can adjust personalized settings around your SaaS’s interface for themselves.”*

![freemius user dashboard](https://freemius.com/blog/wp-content/uploads/2023/09/freemius-user-dashboard.png)

The Freemius User Dashboard

### Set Up User Registration

As I’ve mentioned before, the nice thing about WordPress is the convenience; everything has been taken care of for the developer to start distributing their plugin, including user registration.

WordPress users can usually install your plugin on their website straight away, no questions asked. With SaaS, you need to design a user registration page for them to access your product, not to mention dealing with the responsibility of managing their private information as confidential data.

This leads us to the next point.

### Legal Terms and Privacy

When offering a SaaS, you are liable for PII (Personal Identifying Information), whether for free users or customers. It depends on what your service does, though you are most likely managing additional data that is stored on cloud solutions and shared with third-party services.

Gone are the days when you could just push a free version to WordPress.org and everything else was up to the user who installed the plugin on their website.

Therefore, it’s important to include terms of service, privacy and cookie policies, etc. that are aligned with the service you’re offering. Luckily, you won’t need a professional to set this up for you from the get-go: there are effective online generator tools that can help you get started 💯 Later, when you scale and legal implications become more serious, you should get a lawyer to help you iron out the fine print.

***Full Disclaimer:* The above is not legal advice, and neither myself nor Freemius can be held responsible for any unintended consequences that may arise from following it.**

### Consider Implications for Customers

When your product is SaaS, everything is stored and running on ‘your’ server: data, traffic, etc. You need to manage this effectively because any blunder on your side could lead to legal implications.

SaaS cancels out many of the no-strings-attached perks of plugins for customers, too. Instead of relying on a single WordPress plugin to add functionality to their website, they are suddenly dependent on a third party. “*This can be a good or bad thing — it depends. For example, by selling and managing licenses through an eCommerce SaaS like Freemius, a heavy load is taken away from the store’s server resources. And even if the store’s site is down, subscription renewals will be properly processed and logged.”*

However, Vova admits that convincing prospective users to trust a third party is not always easy.

> For users who are used to working with WordPress plugins, there’s a leap of faith that customers need to take before trusting that an external service is more stable than their own website. The service isn’t a part of their core business, and they have to trust that bringing in a third party to provide it instead of employing a dedicated team is a wiser decision. In other words, they need to believe there’s a bigger chance things will go wrong if they manage that aspect of their business themself.

There are many customer-related implications to keep in mind when transitioning to SaaS, but the independence and privacy factors loom large. “*I think if you convert your plugin to a SaaS completely, you’ll probably lose some of your existing customers. They may require the customizability that plugins offer as opposed to a hosted solution. With a SaaS, you lose some level of control, you’re restricted in what you can do, and you lose some flexibility*.”

By now, it should be clear that transitioning to SaaS is doable but certainly no walk in the park. Depending on your state of mind, the next section will either leave you feeling relieved or peeved 😅

## Subscribe and grab a free copy of our WordPress Plugin Business Book

Exactly how to create a prosperous WordPress plugin business in the subscription economy.

![The WordPress Plugin Business Book](https://freemius.com/blog/wp-content/plugins/fsblog-utilities/assets/img/svg/cheat-sheet-ebook.svg)

## You Could Build Your SaaS in WordPress

Although plugins and SaaS are different beasts, it’s possible for developers to build their SaaS products on WordPress. “*Doing so will save you some mechanisms, and it’s probably the more natural route for plugin developers who are already familiar with WordPress*,” Vova says. “*It spares the headache of building from the ground up.*”

There are many downsides to this approach and while it’s generally not the recommended route, it’s doable (we won’t get into the downsides at the risk of digressing from the article).

Time to come up for air! We’ve taken a deep dive into SaaS, and I’d like to leave you with one final — but important — consideration.

## SaaS Isn’t the Be-All or End-All

If the stars don’t align with your SaaSperations, there’s still plenty of room to make a success of your software journey.

Yes: SaaS is the logical route if you dream of creating something unique or have ambitions for exponential market growth. But WordPress plugins fill a special niche that SaaS can’t, and the joy of building a software product and growing a business with the WordPress community’s advice and support should never be underestimated. Figure out which software model best suits your intents and purposes, and be sure to make a kick-ass product once you’ve taken your pick.