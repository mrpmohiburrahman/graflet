In a shocking turn of events, Digital River abruptly [laid off over 100 employees](https://www.kare11.com/article/news/local/digital-river-closing-minnesota-headquarters/89-71b3be97-2359-422c-a9b2-3dbec793a846) and [filed for insolvency](https://news.ycombinator.com/item?id=41856330), leaving software creators in the lurch, unable to access their hard-earned revenue.

From solo developers to established software companies, businesses of all sizes are feeling the impact. Some have a few hundred dollars trapped, while others are locked out of over $150,000.

If you’ve been affected, here’s what happened — and what you can do next.

## The MyCommerce Crisis: What Happened?

“They just cut off everything, and I can’t do anything. The website just says the account is deactivated with no clear explanation,” shares Milan Petrovic, a developer who’s been using MyCommerce for 16 years, highlighting the abrupt nature of this shutdown. “Currently, I have about $5,000 stuck with them.”

[![Email from Digital River about insolvency](https://freemius.com/blog/wp-content/uploads/2025/01/email-from-digital-river-about-insolvency.png)](https://freemius.com/blog/wp-content/uploads/2025/01/email-from-digital-river-about-insolvency.png)

The email Milan received from MyCommerce

This collapse didn’t happen overnight. Here’s how events unfolded:

- **July 2024**: The first red flag appeared when MyCommerce began missing scheduled payments to vendors
- **August 2024**: Sudden contract changes introduced, extending payment terms from 15 to 60 days
- **September 2024**: Additional fees implemented, including:
  
  - A new $100 monthly platform fee
  - $185/hour client support fees
  - $20 charge per chargeback
  - Various undisclosed “miscellaneous” fees
- **January 2025:** Final insolvency announcement and service suspension

This turn of events left many MyCommerce users outraged and considering lawsuits, according to experiences shared on [YCombinator’s Hacker News](https://news.ycombinator.com/item?id=41847953):

“They owe my company $90,000 for the July/August payment. A class action lawsuit seems to be the only viable option. While $90,000 might not be a large sum for a lawyer to take on individually, if it’s multiplied by 100 or 1000 cases, it becomes much more significant.”

## Why Software Makers Got Burned

The MyCommerce shutdown reveals several critical risks that many software creators overlooked. Looking back, Milan reports there were multiple warning signs:

1. **Drastic contract changes:** MyCommerce unexpectedly introduced significantly higher service fees — including customer support interactions:”The changes they introduced were quite drastic. They introduced a platform fee of $100 monthly, which was completely new. Then they added a $185/hour client support fee,” says Milan.
   
   Another MyCommerce user shared similar experiences: “We’re with them since 2005. Things started going south in August. July payment was due on August 15 but never came. A few days afterwards, they sent an email that they were changing contract terms and that payments would now be sent 60 days instead of 15 days after the month.
   
   Sadly, I didn’t switch to another payment processor immediately that day — accountants were on holiday, we were investigating our options,” complains this small family business owner, who’s currently owed $20,000 by Digital River.
   
   Many, however, did start looking for alternatives almost immediately:  
   ![A Hacker News visitor asking for recommendations](https://freemius.com/blog/wp-content/uploads/2025/01/a-hacker-news-visitor-asking-for-recommendations.png)
2. **Declining service quality:** Although Milan can’t be 100% sure it’s due to MyCommerce’s declining service quality, he noticed fewer sales were coming from the platform.”There was a decline in sales over the last year, especially in subscription renewals… I didn’t investigate much because I had relatively constant or even increasing website traffic, but sales were definitely lower,” Milan shares.
   
   And it wasn’t only about the sales. Customer support agents seem to have gone MIA as well — there was either an unhelpful “we don’t know” or no response at all.
   
   “It seems to take a week or more for any response to a ticket. Their new platform terms come into effect today, and they have absolutely buried the scale of their new monthly fee (US$100/month for me — unsure if it varies per customer). None of the emails mention the fee amounts. Customer support couldn’t tell me the fee amounts,” another Hacker News user shares.
3. **Industry whispers:** A tell-tale sign that something is wrong is your service provider’s competitors suddenly racing to your inbox.”Since mid-last year, I’ve been getting regular emails from various other companies — PayPro Global, Cleverbridge, and Fangis – offering to have me switch to them due to MyCommerce’s problems,” says Milan.
   
   Although these red flags didn’t lead to Milan quitting MyCommerce altogether, he started thinking about moving to another merchant of record:
   
   “At that time, I had already contacted Vova to discuss Freemius, as I wanted to move one of my plugins to Freemius as a test. If that went well, I planned to migrate all plugins…,” shares Milan.
   
   “So far, I’ve managed to do this with five plugins, but I still have 10-11 waiting. The worst part is that the plugins with the highest sales are still on the old system, and they’re the most complicated ones to convert,” he adds and explains why this process is complicated for him (especially when put in such a position where he has to handle things in a hurry!)
   
   “Most WordPress plugin developers, before switching to Freemius or another platform, typically use standard WordPress systems like Easy Digital Downloads or WooCommerce. This makes their transition somewhat simpler. My problem is that I had a 100% custom-developed system for my website, including MyCommerce integration and similar features,” concludes Milan.

## Urgent Action Plan for MyCommerce Users

With accounts suddenly deactivated and support channels unresponsive, affected software creators need to act swiftly to protect their businesses and maintain customer relationships.

![You have to have a backup plan gif](https://freemius.com/blog/wp-content/uploads/2025/01/you-have-to-have-a-backup-plan-gif.gif)

What’s the plan now?

Here’s an action plan based on insights from Milan and industry best practices:

### 1. Immediate Steps

- **Secure your data**: If you still have account access, export all customer data, sales reports, and transaction histories immediately
- **Document everything**: Save all communication, contracts, and payment records
- **Review your licensing system**: Assess whether your licensing system is dependent on MyCommerce’s infrastructure

Luckily, Milan has access to his customer data, thanks to saving it all outside of MyCommerce.

“Fortunately, I wasn’t directly tied to them except for payments. I handled my own licensing. They just processed payments and such. I have all my user data, except for payment method details — I only know if they used Visa or Mastercard, but nothing beyond that. I have all the important contact information for all customers,” he explains.

### 2. Customer Communication Strategy

Based on our interviewed developer’s experience, here’s how to handle customer communication:

- Send immediate notifications to all users, especially those with active subscriptions
- Consider offering incentives for migration (such as discount coupons)
- Be transparent about the situation while maintaining confidence in your solution

Milan is planning to send out an email to his users and implement some churn prevention strategies: “This is especially important for people with active subscriptions since these can’t continue. I plan to send each of them a discount coupon when they switch to the Freemius version.”

He adds he’s expecting some users to stop using his product: “I’m hoping it won’t be too bad, but I expect maybe 50% might not want to continue after all this because usually with major changes like this, users aren’t very understanding,” notes Milan, emphasizing the importance of careful customer communication.

### 3. Technical Migration Steps

The complexity of migration varies depending on your setup:

- For standard WordPress implementations using Easy Digital Downloads or WooCommerce, migration is relatively straightforward
- Custom implementations require more planning and typically take 3-4 days per software product
- Consider running parallel systems during transition to maintain service continuity

That was Milan’s plan, too:

“I would let old licenses remain active in their current form. This means each plugin essentially has two versions — one with Freemius and one without. People with existing licenses use the version without Freemius, while new purchases get the Freemius version. It’s no longer possible to buy the old versions anyway.”

## Protecting Your Software Business

The MyCommerce crisis offers crucial lessons about safeguarding your software business. Here’s what we’ve learned from developers who experienced this firsthand:

1. **Watch for early warning signs:** Pay attention to subtle changes in your payment processor’s behavior to recognize any signs that things might be going south for the company. The mismatch between website traffic and actual sales performance that Milan experienced was also an early indicator of underlying issues.
2. **Ownership structure matters:** Consider the company behind your payment processor. “The good thing about Freemius is that it’s not owned by some mega-corporation whose goal is essentially to extract as much money as possible while investing as little as possible in the whole system. That’s generally the goal of corporations.”
3. **Keep your freedom:** Maintain control over critical business components and avoid using platforms with customer lock-ins, so that you don’t lose all your data in case something like this happens. Freemius offers a simple way to [export your data](blog-freemius-release-notes-december.md) (like licenses and websites) into a clean, well-structured CSV file.

![Protect your business gif](https://freemius.com/blog/wp-content/uploads/2025/01/protect-your-business-gif.gif)

How will you protect your business from unexpected situations like this?

**Pro tip:** Create a quarterly health check routine for your payment processor: monitor processing times, support responsiveness, fee changes, and most importantly, any unusual patterns in your sales data versus site traffic. While you can’t predict every crisis, you can spot the warning signs early enough to take protective action.

## Next Steps: Moving Forward

While this situation is certainly unpleasant and challenging, there are clear paths forward.

Freemius offers a specialized migration path for affected businesses, with particular attention to:

- Data import and transition
- [Subscription management](subscriptions.md)
- Customer experience preservation
- [License key handling](software-licensing.md)
- Revenue continuity

The migration process is streamlined while ensuring minimum disruption to your business operations. **If you’re planning to switch to a new vendor, we’ve prepared a detailed step-by-step guide on [how to migrate from MyCommerce to Freemius](blog-how-to-migrate-from-mycommerce-to-freemius.md) — pain-free!**

## Looking Ahead

Class action discussions are already underway between Digital River and software makers who have their money stuck with MyCommerce. However, affected businesses shouldn’t wait to see how events develop before taking action.

“It’s really hard to predict what could happen to any business tied to internet operations,” Milan concludes, reminding us that while we can’t prevent every crisis, we can choose partners wisely and maintain preparedness for unexpected changes.

Need help migrating your software business to a new vendor? Contact our team at [\[email protected\]](https://freemius.com/cdn-cgi/l/email-protection) for help — we’ll build a personalized transition plan and get you back on your feet in no time.