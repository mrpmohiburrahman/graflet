What started as [payment delays and forced contract changes](https://www.theregister.com/2024/10/15/digital_river_runs_dry_hasnt/) in mid-2024 has escalated into full-blown insolvency for MyCommerce. This leaves software makers without access to earnings and scrambling for answers.

For years, MyCommerce was a trusted merchant of record for makers, but the cracks started showing when its parent company, Digital River, began struggling financially.

They quietly extended payout periods and altered contracts without consent. To rub salt in the wounds, vendors who expected payouts every 15 days suddenly had to wait 60 days or more, [only to discover that funds were never coming](https://news.ycombinator.com/item?id=41847953).

These events were just the early symptoms of a more serious disease…

## The MyCommerce Fallout: Why You Need to Move Fast

On Sunday, 26th January, MyCommerce shut down completely, without warning.

Accounts were locked, checkout pages stopped working, and all access to sales data vanished. Even worse, vendors were notified in a surprise email, with no chance to withdraw their pending earnings.

[Milan Petrovic](https://x.com/milangd), founder of [Dev4Press](https://www.dev4press.com/), was one of the many long-time MyCommerce users caught in the e-commerce crossfire. He relied on the platform as a stable revenue stream for 16 years — until everything collapsed overnight. Read his full story and [how MyCommerce and Digital River’s insolvency unfolded](blog-digital-river-mycommerce-shutdown-guide.md).

“I logged in on Saturday, and everything was fine. Payments were processing, my next payout was scheduled. Then, on Sunday, I got an email saying MyCommerce was gone. I couldn’t log in, my checkout pages were broken, and my $5,000 in pending earnings was frozen.”

Milan had already [migrated five plugins from MyCommerce to Freemius](help-documentation-getting-started.md) and was planning to gradually shift his full portfolio in 2025.

But with MyCommerce’s sudden implosion, he’s in your boat and has no choice but to accelerate migration plans to avoid these impending dangers:

### Key Risks of Delaying Migration From MyCommerce

If you’re still holding out hope for a resolution, consider these points:

- **Loss of access to critical business data**: MyCommerce locked vendors out of their dashboards, making it impossible to retrieve customer data or sales history
- **Frozen funds with no recourse**: Some vendors have reported losing [tens of thousands of dollars](https://news.ycombinator.com/item?id=41847953), and with insolvency proceedings underway, the likelihood of getting paid is slim
- **Mass subscription cancellations**: Milan witnessed a wave of subscription terminations just before the shutdown — a clear indicator that MyCommerce had already stopped processing payments well before the implosion of Digital River

With MyCommerce in freefall, the only logical move is to act ASAP. And we’re here to help you expedite things to regain control of your revenue and business.

> Freemius makes it possible to migrate seamlessly from MyCommerce in just a weekend.

## Preparing for Migration: What You Need Before the Big Weekend

For any platform migration, preparation is key.

A rushed process can lead to lost data, customer confusion, and damaging downtime. Here’s how to set yourself up for a smooth transition to Freemius from MyCommerce.

### Migration Kick-Off

Email [\[email protected\]](https://freemius.com/cdn-cgi/l/email-protection#f0838580809f8284b0968295959d998583de939f9d) with your details and a Freemius migration lead will follow up with a custom step-by-step migration plan from MyCommerce.

### Take the Preliminary Assessment

Every migration is unique. To tailor the process to your needs, we conduct a preliminary assessment:

- Are you migrating freemium, premium-only, or both?
- What types of products do you sell? (SaaS, plugins, themes, add-ons)
- Do you have a licensing system in place? If yes, share an example license key and confirm if it’s stored in the WordPress database upon activation
- Should expired licenses be reactivated post-migration, or should activation be restricted?
- How many active auto-renewing subscriptions do you have, and which payment processors do you use? (Stripe, PayPal, etc.)
- Do you have any restricted pages that only active license holders can access?
- How urgent is your migration? In this case, we’re guessing it’s **super** urgent!
- What is your average monthly sales volume? (To determine high-volume pricing eligibility.)

Your responses help us ensure **a frictionless transition**.

### Set Up Your Freemius Account

The next step is creating your [Freemius account](help-documentation-getting-started.md). Simple enough!

![Freemius signup page for migration from MyCommerce](https://freemius.com/blog/wp-content/uploads/2025/01/freemius-signup-page-for-migration-from-mycommerce.png)

Milan had already explored platforms like Paddle, FastSpring, and 2Checkout but found their sign-up processes overly complicated and lacking transparency in pricing and features.

Speaking with founder and CEO [Vova Feldman](https://x.com/vovafeldman) about technical integration, licensing, and support sealed the deal, and he decided to give the platform a go.

**![Freemius Checkout overlay code for migration from MyCommerce](https://freemius.com/blog/wp-content/uploads/2025/01/freemius-checkout-overlay-code-for-migration-from-mycommerce.png)**

Milan’s first integration experience convinced him that Freemius was the right choice for the rest of his portfolio.

### Identify Essential Data to Transfer

Since MyCommerce allowed full data exports before shutting down, makers who backed up their information early — like Milan — are at a huge advantage.

> If you still can — back up everything and store the following before it’s too late:
> 
> - XML purchase records
> - Customer contact details
> - Invoice history

Unfortunately, subscriptions cannot be transferred because they’re tied to MyCommerce’s payment processor. Makers migrating to Freemius must manually onboard their existing customers.

**Luckily, this is not as laborious as it sounds:** Our quick-to-act support team is on hand to — well — lend a hand.

### Inform Your Customers

Communication is non-negotiable during migration.

Without transparent updates and valid reasons for migrating, customers may think you’re hiding critical information from them or that your store has shut down entirely.

- **Announce the migration** via email and update your pricing page
- **Offer discounts** to encourage existing customers to repurchase via Freemius:  
  ![Freemius discounts and coupons in Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2025/01/freemius-discounts-and-coupons-in-developer-dashboard.png)
- **Set up a landing page** explaining the transition with FAQs and include support options

“I put up a notice for products not yet migrated. It reassured my customers and reduced support tickets,” Milan says.

With the data collected (holding thumbs for you!) and the preparation sorted, it’s all systems go.

## Migration Day 1: The Transition Begins

Day 1 is all about exporting, structuring, and importing.

### Exporting Your Data from MyCommerce to Freemius

If you’ve already backed up your MyCommerce data, you’re ahead of the game.

The next step is prepping it for export — because raw files alone won’t help if they’re not structured properly.

Milan had the foresight to store XML transaction files locally on his own servers, which meant he retained full customer details. “I always kept local backups. When MyCommerce locked me out, those files saved me.”

Not all vendors were as prepared. Now that accounts are locked, API endpoints have stopped working, making it impossible to retrieve real-time data exports at this time.

For those lucky few who have their precious data, here’s how to structure export files:

- Ensure customer details, purchase records, and invoices are cleanly formatted
- Separate one-time purchases from subscriptions. Since MyCommerce subscriptions can’t be transferred, this will help you manually onboard customers faster
- Check for gaps in data. If you’re missing transaction details, invoice history or email records might help reconstruct lost sales

If you didn’t back up your data and the lock-out situation remains, your recovery options are limited. But there are a few things you can try:

- **Check invoice records in email history** — you may be able to manually rebuild purchase logs
- **Retrieve customer details from payment processors** (if you have records in PayPal or Stripe)
- **Contact existing customers** to request proof of purchase if they need support

### Importing Customer and Licensing Data into Freemius

Freemius offers two ways to import data: [**API-driven automation**](help-documentation-migration.md) [or](help-documentation-migration.md) [**manual entry**](help-documentation-migration.md).

- **Manual entry:** Useful if your product catalog isn’t large or needs restructuring, and probably the only import method available to MyCommerce makers since API endpoints are defunct.
- **API import:** More efficient if you have extensive data to transfer (and weren’t locked out of a platform you trusted with your software’s critical data).

Even before the MyCommerce collapse, Milan took the hands-on migration route:

“I had to recreate my products in Freemius because MyCommerce’s pricing structure didn’t map perfectly. It took some time, but it was worth it for the flexibility. Plus, the Freemius support team was with me every step of the way.”

Regardless of the method, you must ensure **customer details, license keys,** and **purchase history** are correctly mapped.

### Configuring Payment Gateways and Checkout

MyCommerce offers [15](https://account.mycommerce.com/home/wiki/Billing%20and%20Displayable%20Currencies%20and%20Payment%20options)[+ payment methods](https://account.mycommerce.com/home/wiki/Billing%20and%20Displayable%20Currencies%20and%20Payment%20options), including region-specific options.

But, as mentioned, there’s an issue: all subscriptions are locked to MyCommerce’s platform, making them impossible to transfer.

At face value, MyCommerce’s payment flexibility looks great. Dig deeper and you’ll find it also comes with hidden costs**.** Vendors have to choose between two pricing models:

- **Model A**: €2.95 + 5% of per product transaction
- **Model B**: 14.90% of per product transaction (min charge: €2.50)

On top of this, MyCommerce tacked on extra surcharges in 2024:

- $100 platform fee
- $185/hour client support fee
- $20 per chargeback
- 2% affiliate fee per sale
- And several other fees

> These hidden fees and new surcharges were one of the things that pushed me to start searching for a replacement last year. — Milan Petrovic

Thankfully, there’s a silver lining for makers looking to jump ship:

After manually adding your products (**with our help if you need it!**), Freemius simplifies the rest of the configuration through Stripe, PayPal, and credit card support and an [intuitive, transparent checkout setup](blog-how-to-improve-checkout-conversion-rates.md):

Milan notes a key difference in how MyCommerce and Freemius handle customer payment accounts:

> With MyCommerce, every purchase generated a separate account — even if the customer used the same email. This was frustrating and led to subscription cancellations. Freemius, on the other hand, unifies customer accounts, making renewals and purchases seamless.

With your data exported, imported, and payments configured, you’re ready to address glitches and bugs that may have been missed.

## Migration Day 2: Testing, Optimization, and Going Live

The heavy lifting is done but the work isn’t over.

Day 2 focuses on fine-tuning your migration, resolving edge cases, and making sure customers experience a seamless transition.

### Test Everything!

Before you switch fully to Freemius, conduct a comprehensive system check to confirm that:

- **License activations work as expected** – Test activations for both new and existing customers
- **Payments are processed correctly** – Verify that Stripe, PayPal, and any other configured payment gateways function properly
- **Freemius’ Developer Dashboard is fully operational** – In contrast to MyCommerce’s outdated dashboard design, the [refreshed Developer Dashboard has been enriched with analytics and insights](blog-release-notes-real-time-analytics-and-multi-store-dashboard.md) to give makers more freedom and control. Make sure to familiarize yourself with the comprehensive details of your new dashboard
- **Product settings and pricing are correct –** MyCommerce’s pricing structure differs from Freemius, so ensure that all migrated products reflect the intended pricing and licensing terms

Lastly, ensure customers can easily manage licenses, renewals, and invoices using [Freemius’ Customer Portal](customer-portal.md) (which greatly reduces your overall support load).

### Handle Edge Cases

MyCommerce’s sudden shutdown left gaps that need manual intervention.

- **Manually re-onboard customers with lost subscriptions**: Since MyCommerce doesn’t allow direct subscription transfers, consider offering existing customers discounts to encourage them to re-subscribe or re-purchase via Freemius, like Milan:”When MyCommerce collapsed, I knew I had to act fast to keep customers from leaving. I offered exclusive renewal discounts which helped me retain a big chunk of my user base.
  
  “Makers who’ve migrated to Freemius have the opportunity to strengthen customer loyalty and drive revenue growth through:
  
  - [targeted coupons](blog-freemius-release-notes-december.md#enhancements_for_migrated_products:~:text=drive%20revenue%20growth.-,Targeted%20Coupons%20for%20Migrated%20Customers,-Transitioning%20to%20Freemius)
  - [transparent checkout calculations](blog-freemius-release-notes-december.md#enhancements_for_migrated_products:~:text=safeguarding%20against%20misuse.-,Checkout%20Calculation%20Updates%20Built%20for%20Migrated%20Makers,-Whether%20fine%2Dtuning)
- **Handle past-due renewals** – Some customers may have been due for a subscription renewal when MyCommerce went offline. Communicating with them proactively can prevent churn and restore lost revenue
- **Prepare for more customer support requests** – Milan noted he received more inquiries than expected after the transition. Use your FAQ page in tandem with an automated email sequence to address common migration concerns and ease the workload on your support team

### Finalize the Transition

With everything tested and edge cases addressed, you’re ready to fully detach from MyCommerce.

- **Update all website links** to direct customers to Freemius-powered checkout pages
- **Revise documentation** to reflect the new licensing, purchasing, and customer management systems
- **Communicate the transition to customers** through emails, blog posts, and support notices
- **Remove any remaining MyCommerce integration from your site** – check for old scripts, checkout links, and API calls that could create confusion

By this point, your migration is complete, but you’ll have to wait a tad longer for that celebratory drink and well-deserved downtime…

## What to Do After Migration From MyCommerce

Now that your store is fully operational on Freemius, monitor customer response and address concerns. A smooth migration is a huge win, but customer experience will ultimately define its success.

- **Communicate proactively**: Listen to feedback, actively engage on social media, and create another email sequence that addresses user queries and concerns after they’ve had time with the new system. Enrich your existing FAQ with these additions.
- **Encourage repurchases**: If customers lost subscriptions in the migration, double down on offering incentives to bring them back
- **Keep an eye on support requests**: Create stock answers for the queries you receive most. MyCommerce customers will have feedback about the new system, so be ready to guide and help them quickly

### Resources and Support

Our team, documentation, and makers’ community will help you refine your setup and maximize your revenue.

- **Explore our documentation** – Everything you need to fine-tune your Freemius integration is available in our [knowledge base](https://freemius.com/help/documentation/)
- **Join our makers’ community** – Learn from 1600+ like-minded makers who have successfully migrated and scaled their businesses with Freemius
- **Need help?** Our support team is here to assist with any questions as you optimize your store

## Why Freemius? The Freedom and Control to Grow on Your Terms

Your migration isn’t just about escaping MyCommerce — it’s about creating a better future for your software business.

We believe in:

✅ **Transparency**: No hidden fees, no confusing payout structures. Just [clear, fair revenue sharing](pricing.md) and full visibility into your earnings.

✅ **Freedom and control**: You own your customer data — and [have full access to it](blog-freemius-release-notes-january-2025.md#data_liberated) — helping you set your pricing and **grow your business without limitations.**

✅ **Built for makers, by makers**: We understand the challenges of selling software because we’ve been there too. That’s why we’ve built a platform that handles the heavy lifting so you can focus on innovation.

✅ **A thriving community:** You’re not in this alone. Join a network of successful software makers building and scaling their businesses with Freemius.

Make the switch, take control, and start selling on a platform built for your success.