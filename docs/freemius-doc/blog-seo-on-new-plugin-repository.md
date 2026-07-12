The new WordPress plugin repository was [officially released](https://make.wordpress.org/plugins/2017/03/28/the-new-directory-is-mostly-live/), replacing the old “legacy” one. Many community members (including me) feel that most of the [issues that were addressed during the feedback phase](https://make.wordpress.org/meta/2016/07/12/plugin-directory-v3-open-beta/#comment-8395) were unfortunately ignored, but one thing that was significantly improved for sure is the search.

It is still lagging way behind the search capabilities of designated search services like Addendio, but it’s much better than its predecessor.

![New repository for plugins](https://freemius.com/blog/wp-content/uploads/2017/03/New-repository-for-plugins-1024x530.png)

The much-anticipated update to the plugins’ search is a HUGE thing. Not only does it obviously affect the WordPress.org plugin repository search, it also changes the search in the WordPress Admin dashboard on ALL of the millions of WordPress sites out there (27% of the web).

Many developers in the WordPress community aren’t aware of the power of SEO in WordPress.org directory, but if you think about it, most of the traffic to your plugin or theme’s listing is coming from search. Here are the top 3 channels:

**WordPress.org** – people see the plugin repository as a trusted collection of plugins and themes, many “plugin hunting expeditions” are starting right there. If you take a look at the screenshot of the new plugins repo homepage you’ll easily notice that the focus is the search. Just the header with the search is using about 40% of the fold.

**WP Admin Dashboard** – if someone already has WordPress installed, there’s nothing easier than just searching for plugins and themes directly from it. This search is based on the same search mechanism that WordPress.org is, so searching for a specific term will yield the same results on both locations:

![WordPress.org repo search results](https://freemius.com/blog/wp-content/uploads/2017/03/WordPress.org-repo-search-results.png)

And the same search term: ‘Backup Plugin’ from within the WordPress admin dashboard:

![Admin dashboard plugin search results](https://freemius.com/blog/wp-content/uploads/2017/03/Admin-dashboard-plugin-search-results-1024x408.png)

**Google (and other search engines)** – every time we have a problem we ask our good friend, Mr. Google, to help us out. Since WordPress.org is THE authority regarding all things WordPress, and it possesses a massive backlinks collection from high quality sites, searching anything related to WordPress on Google favors results from WordPress.org, by default. Hence, we are really back right to the same source again 🙂

It’s undeniable that WordPress.org’s search mechanism significantly influences the user experience for finding new free themes and plugins. For this reason, and because it’s highly relevant for developers who want to get their products to market, we created an eBook to help you fully take advantage of everything the WordPress.org search algorithm has to offer. Download it for free:

## Subscribe and grab a free copy to start Mastering SEO on the WordPress.org Repository

Make the WordPress.org search algorithm work for you with actionable tips to rank your plugin higher.

![Mastering SEO on the WordPress.org Repository](https://freemius.com/blog/wp-content/plugins/fsblog-utilities/assets/img/svg/cheat-sheet-ebook.svg)

## Why should you care?

The answer is quite simple – if you have a plugin or theme listed under WordPress.org, undoubtedly, it’s your main user acquisition channel. If you want to get more users installing your software, luckily, you have full control over the marketing content you include in your readme.txt file. So instead of spending days, weeks, months on polishing features (although those are obviously important, too)… you can potentially spend less than a day optimizing your readme.txt file and get a very significant boost in traffic to your listing, which will directly increase your acquisition rate.

Unlike Google’s super-secret-proprietary search algorithm, the WordPress.org plugin repository is an open-source project (and thanks to [Daniel Iser](https://twitter.com/daniel_iser) who reminded me that yesterday and triggered this post about it). The new plugin repository is actually running on WordPress, therefore, as a derivative, it’s also licensed under the GPL. This gives us a unique opportunity to simply peek under the hood of the search logic and line up the key elements developers should focus on, to rank higher on the WP.org SERP (Search Engine Result Page).

Here’s the plugin repository’s source code, if you are interested: [https://meta.trac.wordpress.org/browser/sites/trunk/wordpress.org/public\_html/wp-content/plugins/](https://meta.trac.wordpress.org/browser/sites/trunk/wordpress.org/public_html/wp-content/plugins/)

The new search engine is based on [Elasticsearch](https://en.wikipedia.org/wiki/Elasticsearch), routed via a [wrapper layer on Automattic’s wordpress.com](https://meta.trac.wordpress.org/browser/sites/trunk/wordpress.org/public_html/wp-content/plugins/plugin-directory/libs/site-search/jetpack-search.php#L225). Which, as a side note, means that Automattic has a full visibility of all the searches on the repo (is anyone identifying a conflict of interests with all the .org data streamed directly over to WordPress.com, or is it just me?). I’m not going to dive deep in the technological part, but for those of you who are curious – just like most modern full-text search engines, Elasticsearch is also based on the open-source [Apache Lucene project](https://lucene.apache.org/). The key differentiator of Elasticsearch is that it can be distributed on multiple servers and has a RESTful API.

So your partner in crime (that’s me), dove into the plugin repository search class and the [Elasticsearch API documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html) to turn that logic into actionable items.

Elasticsearch is highly flexible and incorporates a bunch of mathematical formulas to weigh the different fields that are counted when a search takes place. So, having a BSc in Math and BSc in CS under my belt was a great foundation for understanding how the search works behind the scenes. I’m not going to detail the exact calculations, but I will tell you which fields and parameters matter most.

## The New Plugin Repository Search Algorithm Structure

The first phase of the algorithm pulls a collection of matching plugins, based on the following fields:

- Title
- Excerpt (short description)
- Description (including FAQ, changelog, everything…)
- Tags
- Slug
- Author name
- Contributor names

From what I heard (never validated), those were also most of the fields that the legacy algorithm was relying on, prior to the Elasticsearch update.

The second phase of the new algorithm refines the result rankings based on:

- Last update date
- Compatibility with the latest core version
- Number of active installs
- % of resolved support tickets
- Average rating

This is all new criteria that didn’t really matter before – so read it carefully!

### Make Sure You Have All the Relevant Keywords Covered!

The new search requires ALL keywords to appear somewhere in your readme.txt file. So for example, if you have a plugin that does *backups* and you didn’t mention the word “images” anywhere in your readme.txt file’s content, then a user’s search in the .org repo for “backup images” will not include your plugin in the search results, at all!

Reference: [https://meta.trac.wordpress.org/browser/sites/trunk/wordpress.org/public\_html/wp-content/plugins/plugin-directory/libs/site-search/jetpack-search.php#L794](https://meta.trac.wordpress.org/browser/sites/trunk/wordpress.org/public_html/wp-content/plugins/plugin-directory/libs/site-search/jetpack-search.php#L794)

### Exact Phrases Are Ranked Higher

The new algorithm favors exact phrases more than just a match of all the keywords. So for example, if a user is searching for “star author ratings”, a plugin that has that exact phrase in the same field (e.g. description field) will outrank a plugin that has “star ratings” in one field and “author” in another (assuming that the rest of the fields are identical).

One strategy to tackle the long-tail search phrases is doing in-depth keywords research for your plugin, focusing on phrases with at least three words. After you craft this list, do the following:

1. Run the search in the plugin’s directory.
2. Copy the slug of the plugin that was returned as the first result.
3. Open the readme.txt file of that plugin by browsing to https://plugins.svn.wordpress.org/{slug}/trunk/readme.txt (replace {slug} with the slug from step #2).
4. Search the readme file for the exact match of the search phrase. If you can’t find it – that’s great! Mark the phrase and move on to the next phrase.

After you have your list ready, you can start incrementally squeezing those unique phrases into the changelog, which means that you’ll start ranking as one of the top plugins for those searches.

## Grab a free copy of our Cheat Sheet for Selling Plugins and Themes

A growth roadmap with concise, actionable tips for every milestone of WordPress product development.

![blue book with the title “Cheat Sheet for Selling Themes and Plugins by Freemius” written on it](https://freemius.com/blog/wp-content/plugins/fsblog-utilities/assets/img/svg/cheat-sheet-ebook.svg)

## The Age of The Power Slugs Is Over

Having a lucrative slug that matches a commonly searched phrase was priceless real estate before the search algorithm change. The reason it was priceless is because of the way it worked: a plugin that had a slug such as “backup” was ranking first when users were searching for “backup”.

I raised that as an issue in a discussion about the directory’s search with Mika and Otto at the contributors day at Philly, two years ago. Anyways, this is no longer the case. The slug is now just another field in the search algorithm, together with others like the title, excerpt, description, and more. Moreover, it has less “power” than the others I mentioned.

Reference: [https://meta.trac.wordpress.org/browser/sites/trunk/wordpress.org/public\_html/wp-content/plugins/plugin-directory/libs/site-search/jetpack-search.php#L774](https://meta.trac.wordpress.org/browser/sites/trunk/wordpress.org/public_html/wp-content/plugins/plugin-directory/libs/site-search/jetpack-search.php#L774)

## The Plugin’s Title Has The Highest Impact

The title of your plugin weighs more than all the other fields that I mentioned in the first phase of the search algorithm. Even more than the slug. Therefore, make sure that your top 2-3 keywords are part of the title.

I know many developers think that the brand of the product should be the title of the plugin and that’s it, but that’s a big SEO mistake, and now it’s also backed up with the evidence. If you’d like to include the brand in the title – no problem! But start with the important keywords. For example, there’s a very popular backup plugin, titled “Duplicator”. The only reason it is ranked 5th when [searching for “backup”](https://wordpress.org/plugins/search/backup/) is because results 1-4 have “backup” in their title.

![backup results](https://freemius.com/blog/wp-content/uploads/2017/03/backup-results-1024x528.jpg)

Moreover, I would recommend using “WordPress” as part of the title. It might seem redundant when searching within the context of the repo, but it will increase your listing’s ranking on external search engines like Google since the title is embedded within an H1 header which is highly important for search engines.

So here’s my power formula for a high ranking plugin titles:  
***WordPress {functionality/description} Plugin – {brand}***

Here are a few examples:

- WordPress Gallery Plugin – AwesomeGallery
- WordPress Backup Plugin – AwesomeBackup

When the plugin is an integration with another service here’s a slightly different naming template:  
***{serviceName} for WordPress Plugin – {brand}***

Here are a few examples:

- Google Search Console for WordPress Plugin – AwesomeSearch
- SendGrid for WordPress Plugin – AwesomeEmails

## Translations & Geo-Location

When running a search in a non-English WordPress.org version or within a non-English WP Admin, the algorithm considerations will mainly be based on the given translation of that plugin to that language. So for example, if a Russian user searches for “Рейтинг виджет” (which stands for “rating widget” in English) in ru.wordpress.org, since only one plugin has both of those keywords in their Russian translation, [only this single plugin will appear in the results](https://ru.wordpress.org/plugins/search/%D0%A0%D0%B5%D0%B9%D1%82%D0%B8%D0%BD%D0%B3+%D0%B2%D0%B8%D0%B4%D0%B6%D0%B5%D1%82/) even though there are hundreds of rating plugins in the repo.

So translating your plugin’s internal strings is great for accessibility, but if you play this card right and focus some of your translation efforts towards the readme.txt marketing material, this could drive your SEO off the charts!

It’s important to mention that since many users are searching in English anyway, which means that the algorithm will probably not find a match for those tokens in the translated version, it also relies on the English translation, but with very small weight. This means that if the same Russian user is searching for “rating widget” in English, and for some reason, the phrase exists both in the Russian translation and in the English version of the fields, it can give you a little edge in rankings.

Bottom line – translations are now more important than ever!

Reference: [https://meta.trac.wordpress.org/browser/sites/trunk/wordpress.org/public\_html/wp-content/plugins/plugin-directory/libs/site-search/jetpack-search.php#L720](https://meta.trac.wordpress.org/browser/sites/trunk/wordpress.org/public_html/wp-content/plugins/plugin-directory/libs/site-search/jetpack-search.php#L720)

## Author & Contributors… Also Matter!

It’s a little weird in my opinion, but that’s the way it works, and it can give you an edge. If you have a gallery plugin, and another plugin which I’ll call “competitor” has the exact same marketing material, same number of active installs and resolved tickets, you can potentially sign-up with a new WordPress.org user, use “gallery” as the username, and list that user as a contributor to your readme.txt file. Your plugin will outrank the competitor. Crazy – but that’s how the engine works.

Reference: [https://meta.trac.wordpress.org/browser/sites/trunk/wordpress.org/public\_html/wp-content/plugins/plugin-directory/libs/site-search/jetpack-search.php#L835](https://meta.trac.wordpress.org/browser/sites/trunk/wordpress.org/public_html/wp-content/plugins/plugin-directory/libs/site-search/jetpack-search.php#L835)

## Updating Frequency On the New Plugin Repository Is Important, but Less Than Before

The plugin’s last update date matters, but you’ll only get penalized if you haven’t updated your plugin for 180 days. Therefore, make sure you release an update at least every six months.

Reference: [https://meta.trac.wordpress.org/browser/sites/trunk/wordpress.org/public\_html/wp-content/plugins/plugin-directory/libs/site-search/jetpack-search.php#L941](https://meta.trac.wordpress.org/browser/sites/trunk/wordpress.org/public_html/wp-content/plugins/plugin-directory/libs/site-search/jetpack-search.php#L941)

One of the “tricks” for getting more users to install your plugin before the change was actually releasing frequent updates. The reason for that is because of tags. There are multiple locations in WordPress.org and also inside the plugins search in the WP Admin dashboard, where users were exposed to linkable tags(there were even more of those in the past). So for example, if your plugin had a widget and you added ‘widget’ as one of your tags in the readme.txt file, every time you would release a new version of the plugin users who clicked the widget tag (which was the most popular one) would see your plugin first. That’s because the tag results view was ordered by the last update in a descending order. These mechanics rewarded developers that were constantly releasing updates. So instead of developing for months and releasing a mega-version, the better practice was creating continuous, incremental patches to the plugin. We were doing that for years in our plugins, and it worked great.

Long story short, the days of the tags are over. The default order of tags is now “relevancy” as the default search results order. Moreover, the ‘last update’ field was removed from the search results. Here’s an example for the “rating” tag:

[https://wordpress.org/plugins/tags/rating/](https://wordpress.org/plugins/tags/rating/)

As someone who has been “playing” in the plugin/apps/extensions marketplaces ecosystem since 2010, I had the chance to develop and market extensions for WordPress, Blogger, Shopify, WiX, Tumblr, Squarespace and Weebly. I was always highlighting how awesome the WordPress.org plugin repository is because it gives a chance for new and upcoming plugins to shine. All the other marketplaces were ranking new extensions based on active installs, number of reviews, and Avg. rating, which practically means that if the marketplace/repository is already well established and has a large inventory, it’s really hard to get any visibility.

WordPress had that unintentional tags mechanism that gave the new devs an opportunity as long as they keep releasing new versions. From the looks of it at the moment – those days are gone. I hope that the people who lead the WordPress.org plugins repo (Ahm… Samuel Wood aka Otto) read this and rethink changing the tags view back to the previous sorting, or maybe opening up a new category, because otherwise new plugins are basically going to be buried and won’t have any chance to get any organic exposure.

**Update: June 28, 2018 (thanks Angus)**  
The new repository limits to 5 tags so choose those wisely! This is also the case for the search algorithm. If you specify more than 5 tags in your readme.txt file only the first 5 ones will be used.

## Compatibility with New WordPress Versions

The “Tested up to” readme.txt header that hints about the compatibility of your plugin with WordPress core latest version is now counted in the search rankings – but only for [Major and Minor versions](http://semver.org/) (core “patches” compatibility doesn’t affect the rankings). So if your plugin is tested up to 4.7.0 and the latest release is 4.7.3, you are not going to be penalized. But, if your plugin is only supported up to 4.6.x you will get a lower ranking score. So the call-to-action here is simply to test your plugin before every minor release and to update the “Tested up to” field in the readme.txt file.

Reference: [https://meta.trac.wordpress.org/browser/sites/trunk/wordpress.org/public\_html/wp-content/plugins/plugin-directory/libs/site-search/jetpack-search.php#L963](https://meta.trac.wordpress.org/browser/sites/trunk/wordpress.org/public_html/wp-content/plugins/plugin-directory/libs/site-search/jetpack-search.php#L963)

## Active Installs

Plugins with over 1,000,000 active installs will get the highest rank for that search component. While plugins with fewer downloads (99.9% of the plugins) will compete on search rankings, based on who has more installs.

Unfortunately, this means that if you are starting a new plugin in an already popular category such as backups, prepare to be ranked somewhere after the 20th page of the search results when people search for a “backup” plugin.

Reference: [https://meta.trac.wordpress.org/browser/sites/trunk/wordpress.org/public\_html/wp-content/plugins/plugin-directory/libs/site-search/jetpack-search.php#L973](https://meta.trac.wordpress.org/browser/sites/trunk/wordpress.org/public_html/wp-content/plugins/plugin-directory/libs/site-search/jetpack-search.php#L973)

> **Update:** Greg Brown, the engineer that developed the search of the new plugins’ directory pinged me on PostStatus Slack with a fresh update. They solved [a bug in their algorithm](https://meta.trac.wordpress.org/ticket/2604), so now more active installs mean a higher boost on that search criteria.

## Answering Support Tickets

The percentage of answered support tickets on WordPress.org is now a part of the search algorithm. On the one hand, it’s a good way to incentivize developers to answer more tickets. On the other hand, many plugins host their support outside of the WordPress.org plugin repository (for various good reasons), and they will now officially be penalized by the plugin repository for that. This is one of the things that I think should be reconsidered, due to the great arguments presented by many plugin developers like **James Laws from [Ninja-Forms](https://ninjaforms.com/)**, in favor of 1:1 email support.

Another interesting point is if you have a new plugin released to the repo, as long as you don’t have any support tickets submitted the algorithm will default that criteria as if you have only answered 50% of your support tickets…

So the quick tip here is to ask a friend to start a ticket right after the plugin is live and to quickly resolve it to get to 100%.

Reference: [https://meta.trac.wordpress.org/browser/sites/trunk/wordpress.org/public\_html/wp-content/plugins/plugin-directory/libs/site-search/jetpack-search.php#L991](https://meta.trac.wordpress.org/browser/sites/trunk/wordpress.org/public_html/wp-content/plugins/plugin-directory/libs/site-search/jetpack-search.php#L991)

## A Plugin’s Average Rating Means a LOT

If before the new search we all knew that ratings are important for the decision-making when users were on the hunt for a plugin and wanted to get one with a decent reputation, now it’s incorporated deeply in the search results and even factored with a HUGE impact on your rankings. More than the active installs and the other criteria that I mentioned earlier, in phase II of the algorithm.

Also, if your plugin is fresh out of the oven, make sure to get at least one quick 5-star review! (tip: you can ask a friend to download the plugin and review it for you) If you don’t, the search algorithm will treat your plugin as if it has an average rate of 2.5 stars. That’s a really-really low rate.

Reference: [https://meta.trac.wordpress.org/browser/sites/trunk/wordpress.org/public\_html/wp-content/plugins/plugin-directory/libs/site-search/jetpack-search.php#L1000](https://meta.trac.wordpress.org/browser/sites/trunk/wordpress.org/public_html/wp-content/plugins/plugin-directory/libs/site-search/jetpack-search.php#L1000)

## Search Updates Frequency

I’m not sure how often the plugins directory is being indexed by the Elasticsearch, but presuming that the data is reindexed on changes (that’s the logical way) from what I’ve found in the code, WordPress.org caches the results from the service for 10 minutes. So if you push a change to your readme.txt, you’ll need to wait at least 10 minutes to see any change in the search rankings.

Reference: [https://meta.trac.wordpress.org/browser/sites/trunk/wordpress.org/public\_html/wp-content/plugins/plugin-directory/libs/site-search/jetpack-search.php#L290](https://meta.trac.wordpress.org/browser/sites/trunk/wordpress.org/public_html/wp-content/plugins/plugin-directory/libs/site-search/jetpack-search.php#L290)

## What Should Be Your Focus First?

There are only two parameters in the new search that you don’t have direct control over – active installs and the average rate. The good news is that even if you are in your early stages, and still have a very small user base – the average rate has a higher search impact than the number of active installs. So make sure you keep your users happy and also apply a [mechanism for increasing your 5-star reviews](blog-how-we-increase-our-wordpress-plugin-reviews-by-700-percent.md).

If I would need to rate the importance of the different components involved in the new search (that you have control over), here’s the full list starting with the most important:

01. Title
02. Excerpt (short description)
03. Description (including FAQ, changelog, everything…)
04. Tags
05. Slug
06. Author name
07. Contributors names
08. Translations
09. Releasing an update every 180 days
10. Tested up to (Compatibility with latest core version)
11. Resolving support tickets

## Taking Action

All of those algorithm parameters and criteria are under YOUR control! So do your keywords research, optimize your readme.txt marketing content, and rank higher. I know that coding new cool features may be more fun 🙂 but this can have a way bigger impact on your growth at the end of the day.

If you take action on this today, you can start observing an immediate growth in your downloads/installs tomorrow. You can use [Plugin Rank](https://pluginrank.com/) to monitor your plugin ranking for different keyword results (you can also monitor your competitors!). And if you do want to visually see how your SEO tweaks affect your plugin’s growth in real-time (WordPress.org doesn’t show active installs over time), check out [Freemius Insights](wordpress-insights.md). Here’s an example of an effective growth chart from the Freemius dashboard showcasing a growth in acquisition after an SEO optimization done by Ahmad Awais on one of his plugins:

> Been SEO optimizing my [#WordPress](https://twitter.com/hashtag/WordPress?src=hash) plugin and tracking it with [@freemius](https://twitter.com/freemius) — Exceptional growth, data does help [pic.twitter.com/UL0ZY1iEBs](https://t.co/UL0ZY1iEBs)
> 
> — Ahmad Awais (@MrAhmadAwais) [March 21, 2017](https://twitter.com/MrAhmadAwais/status/844190657220673536)

**Have fun SEO-ing!**