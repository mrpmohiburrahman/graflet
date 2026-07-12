If you’re a relatively experienced WordPress plugin developer, you’ve most likely already asked yourself this question – possibly more than once.

If you’re a relatively new WordPress plugin developer, you’re probably asking yourself “Wait … why would I not want my plugin in the repository?!”

Both questions are valid because there are advantages and disadvantages to uploading a plugin to the official repository at WordPress.org, currently hosting [over 59,000 free plugins](https://wordpress.org/plugins/).

In this article, we’ll look at both sides of the debate, helping you understand both the fairly transparent advantages and the less obvious drawbacks, which may arguably have a greater impact on your WordPress business

It’s important to note at the outset that we’re taking a look at the repository here purely from the perspective of the developer – not the end user (although some user-centric factors do impact the developer in the long run).

Let’s start by examining its benefits.

## The Advantages of the WordPress Plugin Repository for Developers

Plugin developers enjoy a number of benefits from using the repository to host their plugins. Depending on whether you’re a professional plugin developer with lots of products, build plugins as a hobby or a side-hustle, or have another goal, each of these advantages may carry a different amount of weight for you.

### Gaining Trust with the Free Plugin Version for Easier Upsell

One critical requirement for use of the repository as a developer is that each plugin in the repository must be free to download and use. Upselling is permitted, but there are limits.

For example, you can create two versions of your plugin. The one hosted on the WordPress.org plugin repository must be free, but it also must be functional. So, you can create a basic version of your plugin that’s not as fully featured to upload to the repository, then offer the upsell to the user for the full-featured version, either for a one-time payment or on a subscription basis (AKA the [Freemium](https://en.wikipedia.org/wiki/Freemium) model).

There’s a benefit to developers willing to take these extra steps: you enjoy all the advantages of the repository for a free “light” version, and the opportunity to then upsell your premium version to free version users.

The working theory behind this setup is that users of your free version will be pleased with its functionality, and so they’re more likely to be willing to shell out cash to use the premium version. That set up itself is definitely a benefit to the developer as it facilitates closing the sale, and it greatly increases the size of the audience that’s been moved to that easier-to-convince spot in the buying cycle.

![Paying with a credit card](https://freemius.com/blog/wp-content/uploads/2016/05/money-card-business-credit-card-50987.jpeg)

More plugin users who would potentially be willing to upgrade to premium

### Exposure to a Broader Audience and an Active Community

That leads us to the second key benefit for developers using the repository: exposure to a vast and diverse audience. As [Scotch.io’s “How to Build a WordPress Plugin, Part 2”](https://scotch.io/tutorials/how-to-build-a-wordpress-plugin-part-2) points out, the repository is good for developers because you become “part of the WP community.”

That’s especially true when you consider that the WordPress community includes people from different countries who speak many languages: “It makes a lot of sense to have your plugin easily \[translatable] without having to touch its core coding.”

**Read more:** [How to Translate WordPress Plugins and Themes with Google API](https://freemius.com/blog/automatically-translate-plugins-themes/)

That community can also help speed up the process of debugging and future development – undeniably another benefit to using the repository.

Yes, sure developers can debug and refine their own plugins, but the process is a whole lot faster, smoother, and more thorough with the [assistance](http://www.themacro.com/articles/2016/05/why-the-best-give-away/) of a large, active user base.

That’s something that a lot of developers – especially those without premium versions to upsell – simply can’t replicate on a cost- or time-efficient basis. It’s just not practical.

### Easy Access to User Feedback

Then, too, there’s the tendency we all have to some degree: getting “code-blind” to our own work. Just like writers often can’t see their own typos or grammatical errors, developers can sometimes miss problems in their own plugins – problems an engaged group of users can more easily identify.

The repository can also offer a plugin developer access to timely and nuanced user feedback.

Speckyboy notes in [this article outlining some of the pros and cons of repository-hosted plugin development](https://speckyboy.com/2012/06/01/pros-and-cons-of-developing-plugins-while-hosting-them-at-the-wordpress-repository/):

> The Trac software solution which enables the Repository is actually quite adept at letting users comment on a plugin’s features. Plugin users will be able to directly interact with the developer of the code, and they can both comment on the features as well as review them using the basic commenting system which is as useful as it is intuitive.

When doing so is made easier, users are more likely to provide meaningful feedback, which can only make your work better. And if you’re wondering if you should offer some type of incentive to encourage this feedback, check out our thoughts on how to make sure [users perceive sharing their opinion worth it](https://freemius.com/blog/incentivize-user-feedback/).

### Help with Building Credibility and a Stable Userbase

Finally, there’s a built-in user perception for repository plugins that they’re higher quality and more trustworthy than plugins that aren’t listed there. (Whether that perception matches reality is another question – one we’ll explore later in this post.)

Users often equate inclusion in the repository with a stamp of approval from the platform. This can significantly boost their confidence in trying out new plugins, making them likelier overall that they’ll download, activate, and use your plugin.

## The Advantages of the WordPress Plugin Repository for Developers

So much for the advantages. Now, what are the drawbacks?

## Support Is A Heavy Load to Carry

By requiring the developer to provide the support to take action to “get” the requests, the repository is running a pull system, as opposed to one that “pushes” notifications to the developer.

If your plugin has just a few dozen downloads, and plugin development is only your hobby, this might not be a big deal. But if your plugin is your business, and/or you have several plugins, including a few particularly popular ones, a pull system can really wreak havoc on your productivity, schedule, and sanity.

Let’s face it: it can be a time-consuming process to offer support for free plugins, even if the developer wants to do it.

Underneath many developers’ complaints about the repository, there’s a perception of a lack of concern for the developer. Often, these developers’ criticisms are met with some version of “If you don’t want to spend time supporting a free plugin, avoid the repository. Release it on GitHub.”

Even if you don’t mind tackling a reasonable amount of support requests for free plugins, you’re still fighting what many believe to be an unfortunately designed platform for support. It places all the obligation on developers to monitor, which doesn’t necessarily work with your established workflows.

### The Review/Rating System Susceptible to Abuse

Many developers may agree that the current review and rating system is just too susceptible to manipulation by those with bad motives or those who simply didn’t understand what the plugin did or how to use it, and they never asked for support.

James Laws of [WP Ninjas](http://wpninjas.net/) put it well in an article at [ManageWP](https://managewp.com/improve-wordpress-plugins-repository):

> The problem is that there is no accountability when someone makes these ratings. Users say something is broken simply because it doesn’t work in their particular setup, but that isn’t always the case. Sometimes something else is broken in their setup, or they just don’t understand how to use the plugin properly.

### Quality Problems with Plugins

While users may perceive repository-hosted plugins as being of higher quality, that’s not necessarily true for developers. Many of them have commented on the presence of plugins of questionable quality in the repository.

One example of this perception can be found in the post “[What Lurks in the WordPress Plugin Repository?](https://premium.wpmudev.org/blog/what-lurks-in-the-wordpress-plugin-repository/)” which details the following issues (admittedly, in 2011 — but still relevant):

1. “More than half of the plugins in the repository are not compatible with WordPress 3.x”
2. “85% of the plugins I tested had PHP warnings, errors and notices”
3. “With a little bit of digging, I found a plugin in the repo with a weakness and was able to use it to hack a site and turn it into a drone”
4. “Only 32% of those 15,000+ plugins have been updated in 2011”
5. “… two-thirds of all plugins haven’t been updated this year, and one third haven’t been updated since 2009.”

Mika Epstein recently gave [a spectacular presentation about the entire review process](http://wordpress.tv/2016/03/29/mika-epstein-plugin-reviews-demystified-how-to-review-a-plugin/) from the POV of the volunteers (five, believe it or not – just five) who review plugins submitted for the repository (on average, 35 each day).

From this presentation, it’s clear that review is a long, arduous, and detail-oriented process designed to catch problems with code, as well as violations of the plugin guidelines such as name, trademark, etc.

Does it succeed in achieving these goals? Not entirely and not always. Of course, any system run by humans will be susceptible to some level of fallibility.

## Grab a free copy of our Cheat Sheet for Selling Plugins and Themes

A growth roadmap with concise, actionable tips for every milestone of WordPress product development.

![blue book with the title “Cheat Sheet for Selling Themes and Plugins by Freemius” written on it](https://freemius.com/blog/wp-content/plugins/fsblog-utilities/assets/img/svg/cheat-sheet-ebook.svg)

### The Review Process Itself

Mika’s presentation also lays out many of the issues with the review process.

Basically, with a team of five volunteer members and 35 plugins submitted on average each day, working on an outdated BBPress platform, it’s not reasonable to expect a speedy, streamlined, developer-oriented process.

The end result: [On the “add plugin” page on WordPress.org](https://wordpress.org/plugins/add/), you won’t find out how long you’ll wait, but you can see how many plugins are in line ahead of yours.

And, as the [Speckyboy post](https://speckyboy.com/2012/06/01/pros-and-cons-of-developing-plugins-while-hosting-them-at-the-wordpress-repository/) put it, “Automattic isn’t shy about imposing \[its] will on developers in the repository.”

It’s also worth noting that the process of uploading and submitting isn’t very user-friendly, especially to novices, which doesn’t encourage new developers to try out their skills and add to the WordPress experience in creative ways.

### Lack of Plugin Usage Data

Hosting your plugin on the WordPress plugins repository will not provide you with much statistics and data about who’s using your plugin and how. You will develop blindly, having to do only with the number of downloads, an estimate of the number of active installs, and occasional user feedback — if you manage to get the users to provide it.

This makes it practically impossible to make any intelligent, data-driven decisions.

As Chris Lema suggests – [when you have data](http://chrislema.com/problem-in-wordpress/) you are not “flying blind” and it can open your eyes to very important and urgent decisions that need to be made about your plugin. These decisions will usually benefit your users in terms of development and support, and eventually for your plugin’s marketing & pricing optimization process.

Here’s a quick hangout Matt Cromwell had with Chris Lema, discussing this topic, among other related ones.

Plugin developers hosting their plugins with the WordPress repository do have a legitimate way of obtaining their plugin’s data, as long as it’s done with the user’s consent & approval. [Freemius Insights](index.md#insights) can help with that by providing all of the missing pieces in a WordPress plugin’s data puzzle.

## Restrictions on Plugins

Finally, developers must contend with a long list of restrictions on plugins accepted for the repository.

As outlined in brief at [WordPress.org’s Plugin Directory information page for developer](https://wordpress.org/plugins/about/), those restrictions include:

1. Your plugin must be 100% GPL compliant (and that includes non-PHP assets, such as images & CSS, which are not derivatives of the WordPress code)
2. The developer must use the Subversion repository given by the plugin team for it to show up on the WP.org site – the directory “is a hosting site, not a listing site”
3. You must have a readme.txt file that’s readable and compatible with the [WP plugin readme file standard](https://wordpress.org/plugins/about/readme.txt)

There’s a [much longer list of guidelines and requirements](https://wordpress.org/plugins/about/guidelines/), including a prohibition on violating WordPress trademarks and another reminder that the team can remove plugins that possibly qualify as spam, illegal, or morally objectionable plugins.

## Conclusion

A perceived lack of awareness or consideration for the developer community’s perspective and needs underlies many of the drawbacks mentioned in this article.

Coupled with the perceived or actual problem with the quality of plugins accepted for the repository and the many requirements that get enforced, it’s no wonder that the repository loses its appeal to some developers.

So, what’s the solution?

If you’re a developer interested in making a quick contribution to the WordPress community with your code – you may want to consider GitHub, like [Coen Jacobs](https://coenjacobs.me/2012/06/19/moving-wordpress-plugins-github/):

> It basically is a remote repository where you can store your code. But GitHub offers more. You get a basic ticket system, wiki and a nice way to view (and share, if your repository is public) your code online.

Of course, [GitHub offers its own set of advantages](http://wptavern.com/wordpress-org-vs-github-for-hosting-wordpress-plugins-and-themes) and disadvantages to plugin developers, so you should consider the question critically before making a final decision.

But, if your intentions and plans in the WordPress plugin world are long-term & repeating – and maybe you’d also like to [monetize your plugin](blog-how-wordpress-plugin-developers-make-money.md) using the freemium model at some point – maybe the WordPress.org repository is right for you, despite all of its drawbacks.

Besides, as members of the WordPress community, we should press for [improvements to the repository](https://managewp.com/improve-wordpress-plugins-repository) to address its drawbacks and problems.

Want to keep learning about reaching new users with your plugin beyond just sharing the free version? You can sell your WordPress products in many ways, including your own website or a WP marketplace. Check out the [pros and cons of relying exclusively on a marketplace](blog-pros-cons-selling-wordpress-plugins-themes-non-exclusively.md) vs. diversifying your sales channels.