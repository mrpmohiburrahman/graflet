Many WordPress plugin developers have started to pursue the add-ons model to monetize their plugin, especially after seeing the great success of WooCommerce, which was just [acquired for $30M by Automattic](http://wptavern.com/automattic-acquires-woocommerce "WooThemes Acquisition By Automattic"). So why not make your own add-ons plugin?

Great! You built your awesome free core plugin, pushed it to the .org repo for a few months, and you are now ready to start developing cool extensions! You have tons of ideas–features you heard from your friends, and requests you got from your core plugin users.

In a perfect world with unlimited resources, you could just develop every addon. Unfortunately, the real world works differently. Building a one-product-business is a pretty hard journey by itself and with add-ons it’s even more difficult, since you need to develop, market, and maintain multiple products.

### Starting with 20% add-ons that matter the most!

[As we recently covered](https://freemius.com/blog/premium-vs-add-ons-which-is-the-best-monetization-model-for-your-wordpress-plugin/ "Premium vs. Add-ons – Which is the Best Model for Your WordPress Plugin?"), the Pareto Principle, also known as the 80–20 Rule, applies to the add-ons model. During your extensions’ business lifetime, most likely that about 20% of the add-ons will provide over 80% of your revenues. Let’s call this power add-ons ***MVA*** – *Most Valuable Add-ons*.

Wouldn’t you want first to develop your MVA instead of working on add-ons that only a few people will use?

**Of course you would!**

It will reduce your support tickets, speed up your time to market, accelerate the progress to profitability, and will save you valuable time and money.

As you already know, our team’s flagship plugin is [RatingWidget](https://wordpress.org/plugins/rating-widget/ "RatingWidget for WordPress Plugin")–a freemium SaaS product which has nothing to do with Add-ons at all. So why do I write about add-ons?

For the past four years, we’ve been receiving tons of feature requests for our WordPress plugin–most of which didn’t make sense for us to implement in our core plugin. Recently, we had a team meeting discussing RatingWidget’s roadmap, and we decided to push these features via extensions during 2015. Since we are focused on Freemius, and spending less development time on RatingWidget, it was crucial for us to **figure out our *MVA* – BEFORE we develop them!**

### Thinking process…

One way to approach the challenge of finding the most valuable add-ons could be simply guessing – or using a gut feeling. However, this isn’t accurate approach unless you are a prophet.

A better method is to make decisions based on real users requests, support tickets, or other forms of customer feedback. The problem with that approach is that there’s a big difference between a user asking for a feature and having them say they’ll pay for it, and to actually getting that user to type his credit card and click the “Purchase” button.

### How to identify your most valuable add-ons without developing them?

Our decision was to leverage user feedback we collected, our gut intuition, and mock the add-ons marketplace as much as possible.

![RatingWidget Add-Ons Marketplace Mock](https://freemius.com/blog/wp-content/uploads/2015/06/ratingwidget-addons-marketplace.jpg)

### Step-by-Step

Enough with the long intro, here’s the recipe that worked for us:

1. We listed the top 15 features that we believed could be decent add-ons.
2. Then, we filtered these add-ons based on the following rule – if the feature wasn’t requested by at least 10 unique users, it was removed. That left us with 8 potential add-ons.
3. Then, I drafted very simple marketing taglines for these add-ons, focusing on the value proposition, and short descriptions explaining their functionality.  
   Example:  
   **Add-on title:** Facebook Likes  
   **Tagline:** Increase Your Posts’ Likes  
   **Description:**  Ask your visitors to like your Facebook Fans page after a 5-star rating.
4. To make sure users understand it’s all paid add-ons, we set a dummy price of $19.99 for all the extensions.
5. Our talented UI-magician, Stanley Macha, designed simple “card” style cover for each add-on.
6. Leo, our lead WP developer, created a new admin settings page for our WordPress plugin to facilitate this mock marketplace.
7. To make sure the position of the add-ons wouldn’t affect the results, Leo programmed the page to show a different random order of the add-ons on every website.

We wanted to track how many users were “interested” enough in the add-on by clicking its card. We also wanted to see how many were brave enough to click the purchase button–measuring the intent to buy. Moreover, why not to capture user emails to build our initial database of potential customers.

8. Since our plugin is on the WordPress.org repository and we strictly follow the guidelines, we couldn’t just “phone-home” and send that info back to our server. So every time a user clicked the add-on card or the *Purchase* button on the card, we opened a modal dialog box to ask his permission to share the intent.

![RatingWidget Mock Add-Ons Marketplace Dialogbox](https://freemius.com/blog/wp-content/uploads/2015/06/ratingwidget-addons-marketplace-dialogbox.jpg?v=1)

Since getting the stats was the whole point, picking the right wording for the message to keep high conversion rate was very tricky. The way we phrased it allowed us to send a different level of the info depending if the user clicked the primary or secondary button. We still kept the close button at the top right of the window in case the user was not interested to share any data.

After running the mock marketplace for two months, we figured out exactly what addons to start with. Moreover, we built a list of over 100 users who signed for the waiting list to purchase the add-ons. Here’re the stats we gathered for our top 3 most wanted extensions:

Clicked Purchase Clicked on add-on card Signed for waiting list Anonymously showed their interest **Reviews** 13 27 11 29 **Facebook Likes** 9 23 14 18 **Product Reviews** 11 17 18 10

### Summary

Looking back at our assumptions, the “gut feeling” approach was a great start to pick the initial add-ons for the mock. But, it wasn’t accurate. Prior to running the experiment, we were sure that the *Twitter Add-on* was supposed to be a big hit, but it didn’t even get to the *top 3*. Therefore, I’m very happy we didn’t just follow our hunch.

While the process we used looks very promising, it isn’t perfect. In theory, to perfectly test what would be the most popular paid add-ons, the method is to mock the whole experience, including the input of the credit card information (or PayPal), till the final purchase button click (the only component that should be fake in the process). Practically, the reason we didn’t do that, is because it would probably piss users off. Imagine yourself spending time filling credit card forms and eventually getting a message telling you the add-on is not ready yet. That would annoy me 🙂

**Anyhow, we still haven’t developed any of the add-ons. But we are empowered by solid data that will definitely save us many unnecessary development & support hours. We will start the development in 6 weeks, and I’ll keep you posted with the results.**