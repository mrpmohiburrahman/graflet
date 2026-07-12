I’ve been working on my WordPress plugin, [RatingWidget](https://wordpress.org/plugins/rating-widget/ "RatingWidget for WordPress"), for a while. It was clear to me from the beginning that the number of reviews and average rating were playing a crucial part in the success of the plugin. Having said that, it took me over four years to figure out the right formula to get more 5-star positive reviews.

### **First Strategy – Extraordinary Support**

At the early stages of the plugin, my strategy for positive reviews was providing extraordinary support. I decided that I would do my best to help every user of the plugin for free. Most users in the WordPress ecosystem don’t expect that, which yielded a decent amount of positive 5-star reviews.

### **Strategy #2 – Asking a favor back**

I often found that users, while grateful, didn’t always leave feedback. Sometimes I would help users for hours, only to receive a simple “thank you”. In fact, a recent study shows that [less than 1% of WordPress plugin users leave reviews](https://www.matteoduo.com/review-to-install-ratio-wordpress-plugins/), which confirms my experience. While my conscience wasn’t suffering, I knew that I needed more returns for my investment. Therefore, I put myself into the user’s position. I realized that I have only  reviewed a product in the following cases:

1. 5-star review: when it’s a phenomenal product that provided outstanding value for me.
2. 1-star review: I usually don’t bother to do it at all, but if a product breaks something, or does something extremely negative, I might unleash my anger with a negative review.
3. If a friend I trust needs help spreading the word about a good product.

As a result of handling complex tickets, a closer relationship develops with the users and they gain trust. Thus, after a few months, I decided to reshape my strategy and be a little more aggressive. Instead of just expecting the users to review the plugin after an exceptional support ticket, I started to ask the users for a favor back–as if I’m their trusted friend.

This favor was as simple as asking the user for a review in order to help us spread the word:

> Awesome! Happy we could help you out. Btw. If you have a moment, I would very much appreciate if you could quickly rate the plugin on WP, just to help us spread the word (don’t forget to click the Post button to submit the rating):
> 
> http://wordpress.org/support/view/plugin-reviews/rating-widget#postform

I was concerned about it first, but it was a great move. Users were excited to help us back and many have written amazing reviews–mainly related to our high quality of support. It increased our review generation to 1-2 reviews per week. We still use this approach today which generates our best reviews.

### **Making Reviews Rain – Automation**

About two month ago, when we were starting to put the Freemius blog in place, I was playing around with different social sharing plugins. One of the plugins I tested was [Mashshare](https://wordpress.org/plugins/mashsharer/). After using it for a week, I got the following message in the admin dashboard:

![Mashshare Plugin Review Notice](https://freemius.com/blog/wp-content/uploads/2015/05/mashshare-review-notice.png)

As simple this message was – I was amazed! Why didn’t I think about it before? It’s so obvious, and all modern mobile apps are doing that. Conceptually, mobile apps and plugins are very similar ecosystems. Asking for a review right from the app is part of the fundamentals of mobile app marketing, especially when there’s a marketplace involved.

Inspired by Rene’s plugin, I decided to explore that direction and optimize it. We decided to A/B Test two main things:

1. The trigger – **WHEN** is the best time asking for a review
2. The ask – **HOW** exactly to ask the user for the review

#### Testing the Trigger

We tested two types of triggers for the message:

**Time-Based Trigger**

The more time a  plugin is used and active on a site; it makes sense that the user gets some benefit from the plugin. Thus we decided that time would be a great trigger to test. We tested three time-spans, by asking the user to review our plugin after a week, after a month and another one after three months.

**Value Based Trigger**

Our plugin is a 5-star rating widget, and the main value it provides to our users is engagement with readers. This value can be easily quantified by number of votes the blog owner’s posts has received. As more votes are received by the site, the plugin becomes more valuable for the site owner. Therefore, we tested triggering the “review our plugin” notification when the number of votes on the site crossed some limit. In the case of Mashshare, the value base trigger could be the number of socially shared posts. In every plugin the value proposition is different, so you, the plugin developer, have to figure out how to quantify your plugin’s main benefits into numbers.

**What worked the best?**

We could test both of the approaches in less than a month, since we had many users that been using the plugin for various periods, with various amount of votes.

Once we added the “review our plugin” notification, we immediately started to receive more reviews.  Not surprisingly, the value based trigger performed way better. And it makes a lot of sense! When someone uses your plugin, it doesn’t necessary means that they are happy with it just because it’s installed. On the other hand, the users that are getting value from your plugin, (and you can show them how much it is valuable for them)– are way better candidates to vouch for you. For example, in our case, if a high traffic site installs RatingWidget, it can gain thousands of visitors’ votes in just a few days. Showing a message that says “Wow – you just received your 10,000 vote!” is hundred times better than “Wow – you are using our plugin for 3 days!”.

To improve our chances of “winning the customers trust”, we decided to trigger the review request notification three times. After 10 votes, after 100 votes and after 1,000 votes. If the user still doesn’t think our plugin is valuable enough for a review after he gains 1,000 visitor votes, we simply give up. 🙂

#### Testing the Tone

As a business owner with customer support, I fanatically follow [HelpScout’s awesome blog](https://www.helpscout.net/blog/ "HelpScout's Blog"). If you are not familiar with their blog–I encourage you to check it out! While the founders are fellow TechStars and good friends of mine, one of my main takeaways from Nick, Denny and Jared is – ***always adding a personal touch***. Showing the people behind the company, on our case – behind the plugin. But, since I’m also a data-driven person, I wanted to test that assumption with different message phrasing. Here’re the two versions that we tested:

**Formal / Company tone:**

> Hi, you just crossed the X votes on RatingWidget – that’s awesome! If you have a moment, please help us spread the word by reviewing the plugin on WordPress.
> 
> *~ The RatingWidget team*
> 
> – Leave a review
> 
> – Maybe later
> 
> – I already did

**Personal / Human tone:**

> Hey, I noticed you just crossed the X votes on RatingWidget – that’s awesome! Could you please do me a BIG favor and give it a 5-star rating on WordPress? Just to help us spread the word and boost our motivation.
> 
> *~ Vova Feldman*
> 
> – Ok, you deserve it
> 
> – Nope, maybe later
> 
> – I already did

Even though the first message looks more professional, the second friendly and personal version performed a little better. But, the differences were not big.

Here’s how our final notification looks:

[![RatingWidget Plugin Review Notice](https://freemius.com/blog/wp-content/uploads/2015/05/rating-widget-review-notice.png)](https://freemius.com/blog/wp-content/uploads/2015/05/rating-widget-review-notice.png)

**Summary**

After adding “ask for plugin review” notification in the admin dashboard, and optimizing with A/B testing for six weeks, we managed to increase our monthly reviews by 700%. From 4-8 monthly reviews to 56 reviews per month, and most of them are 5-star reviews!

That being said, the quality of the new reviews is pretty low, usually very short and concise “Great plugin” type reviews. Since reviews and average rate have a direct effect on your plugin’s evaluation by new users, and the distribution on the repository, it’s better to get all 5-star reviews you can and not being picky about it. 🙂

If you have a good plugin and you are still not asking for reviews – I encourage you to start testing it ASAP.