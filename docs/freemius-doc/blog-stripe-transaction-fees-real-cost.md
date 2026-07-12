Stripe advertises 2.9% + $0.30 per transaction. It’s clean, simple, and easy to budget around. But for software founders selling globally, actual Stripe transaction fees are often much higher.

Once you factor in international card fees, subscription billing, tax compliance tools, and dispute costs, the real rate for a typical software business lands closer to 7.4% — more than twice the headline figure.

Layer in currency conversion and overall rates can reach 11.4%. Many founders don’t discover the costs until they’re already deep into using Stripe for global sales.

We call this the Indie Tax: the cumulative, often invisible cost of building your online payments infrastructure on top of Stripe without accounting for everything that comes after launch. It shows up in your third-party tool subscriptions, your accountant’s hours, your support team’s time, and the revenue you lose to failed payments you never recovered.

In this post, we break down exactly where that gap comes from — fee by fee — and what it looks like for a software business. We’ll also cover what changes when you hand that entire layer to a merchant of record (MoR) instead.

## TL;DR — The real Stripe fee cost for software founders

- The advertised Stripe fee is 2.9% + $0.30. The effective rate for a maker running a full billing and compliance stack with global sales is closer to **6.9–7.3%** — more than twice the headline — rising to **8–11.4%** for sellers collecting in multiple currencies.
- What pushes it up: international card fees (+1.5%), Stripe Billing (+0.7%), Stripe Tax (+0.5%), optional fraud protection, dispute fees ($15/dispute), and FX conversion (1–4%).
- On top of that: time spent on tax reconciliation, dunning management, and customer billing support, none of which Stripe automates.
- The alternative is a merchant of record that absorbs the entire compliance and billing stack at a bundled rate that’s often comparable to Stripe’s true all-in cost, with none of the DIY required.
- **When this math applies:** The full Indie Tax typically materializes once you start selling globally, cross $10K MRR, and begin adding the tools Stripe’s core product doesn’t cover. Below that threshold, you’re likely running a subset of this stack and seeing a lower effective rate.

## Stripe fees at a glance: The total cost of Stripe at $10k/month

Stripe’s standard pricing uses a percentage (2.9%) plus a fixed amount ($0.30) on each successful card payment, but it’s only the starting point.

For a small business looking to accept payments primarily in one market, the rate is manageable. For software makers running recurring payments across multiple regions, the total cost looks different.

The table below models $10K MRR with ~300 transactions (average $33 each).

**This scenario assumes a full billing and compliance stack — subscription billing, tax calculation, invoicing, and fraud tooling.**

Founders using only a subset of these products will see a lower effective rate. The footnotes after the table explain when each line item applies to your setup.

*Stripe pricing varies in different countries. The calculations above are for Stripe US.*

### Footnotes on Stripe fees

**1 International card fee:** This scenario assumes 70% cross-border transactions at the low end and 95% at the high end.

For software products distributed globally, 70% is a reasonable working assumption, but your actual split depends on your audience.

If you sell primarily to a domestic market, your international card fee will be lower.

[![Stripe cards and wallets fees ](https://freemius.com/blog/wp-content/uploads/2025/08/stripe-cards-and-wallets-fees.png)](https://freemius.com/blog/wp-content/uploads/2025/08/stripe-cards-and-wallets-fees.png)

Source: Stripe pricing page

**2 Stripe Billing:** This fee applies to businesses using Stripe’s recurring billing product for subscriptions.

Not all software sellers use Stripe Billing directly. Many manage subscriptions through their eCommerce layer (for example, Easy Digital Downloads, a WordPress plugin for selling digital products) and only incur the base fee on each renewal.

[![Stripe pricing page](https://freemius.com/blog/wp-content/uploads/2025/08/stripe-pricing-page.png)](https://freemius.com/blog/wp-content/uploads/2025/08/stripe-pricing-page.png)

Source: Stripe pricing page

**3 Stripe Invoicing:** The 0.4% invoicing fee applies to standalone invoices sent outside of a subscription context — most common for B2B sales where a customer needs a formal invoice before paying.

Businesses running only subscription billing will not pay this on top of the 0.7% Billing fee. Both fees apply only to businesses using Stripe Billing *and* issuing standalone invoices separately.

[![Stripe Invoicing fee](https://freemius.com/blog/wp-content/uploads/2025/08/stripe-invoicing-fee.png)](https://freemius.com/blog/wp-content/uploads/2025/08/stripe-invoicing-fee.png)

Source: Stripe pricing page

**4 Stripe Radar:** Stripe offers two tiers of fraud protection and the price you pay depends on the tier and your Stripe plan.

**Radar (machine learning)** covers real time fraud scoring, device fingerprinting, proxy detection, SCA logic, and basic analytics.

It’s listed at $0.05/screened transaction, but this fee is waived for accounts on standard pricing — the majority of software founders pay nothing for it.

**Radar for Fraud Teams** adds custom rules, block and allow lists, adjustable risk thresholds, an AI-powered rules assistant, manual review queues, and advanced analytics.

On standard pricing, this costs $0.02/screened transaction. On custom pricing with negotiated volume discounts through the sales team, it’s $0.07/screened transaction.

[![Stripe Radar's machine learning and Radar for Fraud Teams pricing](https://freemius.com/blog/wp-content/uploads/2025/08/stripe-radars-machine-learning-and-radar-for-fraud-teams-pricing.png)](https://freemius.com/blog/wp-content/uploads/2025/08/stripe-radars-machine-learning-and-radar-for-fraud-teams-pricing.png)

Source: Stripe pricing page

**5 Dispute fees:** Stripe charges two separate fees with different refund rules for each:

1. **Dispute filing fee ($15):** Applied when a chargeback is opened against you. You pay this regardless of the outcome.
2. **Dispute countered fee ($15):** Applied when you submit evidence to contest a dispute. It is refunded if you win.

[![Stripe Disputes fees](https://freemius.com/blog/wp-content/uploads/2025/08/stripe-disputes-fees.png)](https://freemius.com/blog/wp-content/uploads/2025/08/stripe-disputes-fees.png)

Source: Stripe pricing page

**6 FX conversion:** This cost applies *only* if customers pay in a currency different from your payout account. A US seller collecting USD from international cardholders pays the international card fee (footnote 1) but not FX conversion.

FX costs also apply when you collect in foreign currencies (euros, GPB, AUD) and convert to your payout currency at settlement.

One thing many makers don’t notice: **Stripe calculates its 2.9% fee on the full transaction amount, including any sales tax, VAT, or GST your customer pays.**

If 25% of your sales include a 10% tax rate, Stripe’s fee is calculated on $10,250, not $10,000. That extra sliver is easy to miss until you reconcile a full month.

“Stripe is very transparent about its core fees, which is great. The challenge is that some of the other fees, things like handling taxes, failed payments, or compliance, aren’t so obvious when you’re starting out. They only reveal themselves as you grow, and that’s when they can really add up,” says [Vova Feldman](https://www.linkedin.com/in/vovafeldman/), CEO of [Freemius](index.md).

### How to find your actual Stripe rate

To see your true effective rate, open the Stripe Balance report at [dashboard.stripe.com/reports/balance](https://dashboard.stripe.com/reports/balance), select a reporting period, then apply this formula:

**Effective rate = SUM (Charges Fees + Dispute Fees + Additional Fees) ÷ SUM (Charges + Refunds + Disputes + Reversals)**

[![Stripe fees balance report dashboard](https://freemius.com/blog/wp-content/uploads/2025/08/stripe-fees-balance-report-dashboard.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/08/stripe-fees-balance-report-dashboard.jpeg)

This captures the full picture, including disputes, FX adjustments, and any Stripe add-ons active on your account.

For makers at $10K MRR, that’s hundreds of dollars lost every month. Florian Vizethum, founder of WordPress plugins like ClickWhale, discovered this as his business scaled:

“We used to manage three stores using Stripe through Easy Digital Downloads. That setup worked, but we had to add a few extra services on top to cover everything we needed.”

This is the first sign the Indie Tax is compounding. Let’s break down each layer.

## Stripe’s surface fees: International payments and FX

Stripe supports a wide range of payment methods — card payments, ACH direct debit, bank transfers, debit cards, Apple Pay, and Google Pay — which is part of why it’s popular for software products.

But once you start [accepting payments from international customers](blog-accept-payments-globally.md), the headline rate becomes just one component of the total cost.

### International card fees

Stripe adds an extra 1.5% for any card issued outside your home country.

For a SaaS or plugin with a globally distributed audience, that can represent a substantial portion of your transaction volume — and a meaningful recurring cost.

How much it affects you depends entirely on your customer mix. The best place to check: your Stripe Payment Methods report, which shows card origin by country.

### Currency conversion (FX) fees

If customers pay in a different currency than your payout account, Stripe applies a 1% conversion fee.

This is separate from the international card fee — a US seller collecting USD from a UK cardholder pays the 1.5% international card fee but not the FX fee.

FX kicks in when you’re actually converting between currencies at settlement.

For a seller collecting in multiple currencies, these two fees stack and both scale with revenue.

**This is where the Indie Tax starts accumulating.**

Each percentage point compounds against your total volume, and the bigger your international audience, the faster it adds up.

For more on managing this, see [why multi-currency pricing matters for software creators](blog-multi-currency-support-pricing-software-products.md).

## Hidden Stripe fees you may not anticipate: Refunds, failed payments, and tax compliance

Stripe fees are all documented, but they’re easy to underestimate when you’re focused on shipping. Here’s where the stack builds.

### Refund and chargeback fees

Stripe [charges $15 per dispute](blog-stripe-chargeback-fee.md), even if you win the case.

In practice, this means:

- **Don’t contest:** Lose the payment + $15 fee
- **Contest and win:** Get the funds back, but still pay $15 (the non-refundable filing fee)
- **Contest and lose:** Lose the payment + $30 total in fees (filing and counter-dispute)

A founder who contests every dispute and wins every one still pays $15 per dispute. That changes how you think about dispute volume — it’s never truly a zero-cost outcome.

Stripe also doesn’t refund the fee on the original transaction when a refund is issued.

Those costs accumulate quickly for subscription businesses where churn is a natural part of selling software. Plus, Stripe doesn’t include built-in chargeback protection, so managing disputes is your responsibility.

### Failed payment recovery

Stripe leaves [dunning](help-documentation-marketing-automation-dunning-failed-payments.md) (the process of recovering failed subscription payments) up to you. Without a built-in workflow or a third-party tool, you lose revenue every month to failed renewals that were recoverable — and nothing in the default dashboard flags how much.

[Nicky Zhu](https://www.linkedin.com/in/nicky-zhu-203073384/), AI Interaction Product Manager at [Dymesty](https://dymesty.com/), ran a micro-SaaS productivity tool for remote teams and discovered this the hard way:

> Stripe’s built-in Smart Retries recovered around 40% of salvageable churned payments. When I layered Churn Buster on top, that number jumped to 71%.
> 
> The surprise wasn’t the cost (the tool paid for itself within 60 days), but that nothing in the Stripe dashboard flagged it as a problem.

Florian had a similar experience:

“Stripe didn’t really offer the tools we needed for handling failed subscription payments or chargebacks. We brought in Churn Buster, which helped us recover failed renewals through [automated emails](help-documentation-marketing-automation.md). That part worked pretty well, but it added another $99/month to our costs.”

Here’s how to [reduce SaaS failed payments before they turn into hidden churn](blog-reduce-saas-failed-payments.md).

### Tax compliance

Selling globally means [dealing with VAT](eu-vat-uk-vat-europe.md), GST, and [US sales tax](blog-sales-tax-on-software.md).

Stripe Tax handles the calculation layer, but you’re still responsible for compliance — filing, monitoring economic nexus thresholds, and remitting to each jurisdiction — or finding a separate tool to do so. And it comes with an extra cost per transaction.

For Florian, that meant Quaderno:

“Handling taxes and invoicing was another big challenge. Since Stripe doesn’t deal with VAT or global sales tax out of the box, we used Quaderno and it did a fantastic job, but that was another $99/month to manage compliance and send proper invoices”

For his team, EDD + Stripe + Churn Buster + Quaderno added up to roughly $3,375/year in tool costs, not counting Stripe fees.

## The real indie tax: Time is money

The cost in dollars is only part of the picture. Stripe’s DIY model extracts a second tax in hours, and that one is harder to see on a dashboard.

### Billing admin and support

Even a well-automated Stripe setup creates ongoing operational work. Florian’s team ran a fully automated stack, but automation didn’t eliminate the need for human oversight:

“Managing Churn Buster campaigns, checking performance, and replying to customer emails when failed payments happened probably took our support team a few hours a week on its own.”

That’s roughly 10–15 hours per month spent on billing-related support before any other operational tasks.

### Tax reconciliation

Tax and reporting is where the hours accumulate fastest. Without invoice auto-reconciliation, every billing period means manual exports, cross-referencing, and variance checks.

Nicky Zhu ran into it when US economic nexus thresholds started triggering in states where she’d never physically operated:

“Tax reconciliation alone took roughly 6–8 hours a month. The workflow involved manually exporting data from Stripe, cross-referencing it against TaxJar reports, and then doing a quarterly review with an accountant. It was the most expensive $200/month I spent.”

Running multi-product operations, David Hunt, COO at [Versys Media](https://versysmedia.com/), saw a higher ceiling:

> At our peak complexity, we were spending 15–20 hours a month on payment-related admin, reconciling Stripe reports with accounting and bank payouts, untangling tax by country and product type, reviewing edge-case disputes and chargeback, and auditing dunning flows when recovery rates dipped.

### What that time actually costs

Every hour spent on payment admin is an hour not spent shipping features, improving onboarding, or talking to customers.

The range founders report is consistent:

- 6–8 hours/month for simpler, single-product setups
- 15–20 hours for multi-product operations selling across regions

That time doesn’t show up in your Stripe dashboard, but comes out of your product anyway.

### When this math applies to you

The 7%+ effective rate doesn’t happen overnight. Many software sellers start with basic Stripe payments and add tools as they grow. A rough rule of thumb:

- **Under $5K MRR, mostly domestic sales:** You’re likely paying Stripe’s base fees plus some international card fees. Your effective rate is probably closer to 3.5–5%, and the admin work is still manageable.
- **$5K–$20K MRR, selling globally:** This is where costs start to stack up. [Tax compliance](https://freemius.com/tax-compliance/), failed payment recovery, and dispute handling become harder to manage manually, so many founders start adding tools and services.
- **$20K+ MRR, multiple countries and currencies:** This is where the hidden costs become harder to ignore. Tax obligations expand, reconciliation takes more time, and your true cost can end up much higher than Stripe’s headline rate.

For many software businesses, the break-even point — where the combined cost of Stripe, add-on tools, and admin work starts to approach a merchant of record’s bundled fee — lands somewhere in the $5K–$20K MRR range.

## How Stripe compares to merchant of record alternatives: Fees side by side

[Stripe](https://freemius.com/stripe-alternative/) is a payment gateway and payment processor built to process payments (card payments, bank transfers, wire transfers) and settle them to your bank account.

What it doesn’t do is take responsibility for the business side of selling. With Stripe, you’re still responsible for sales tax, chargebacks, compliance, fraud prevention, and the other obligations that come with selling software globally.

A merchant of record (MoR) takes those responsibilities off your plate. The MoR becomes the legal seller of record and handles tax collection and remittance, compliance, chargebacks, and fraud management on your behalf.

**The practical difference:**

- With Stripe, you’re the merchant of record
- With Freemius, Paddle, or Lemon Squeezy, they are

Here’s how the main options compare for software sellers:

An important difference that’s not obvious from the rates is how fees are calculated.

Stripe, [Paddle](paddle-alternative.md), and [Lemon Squeezy](lemon-squeezy-alternative.md) take their cut from the *total* transaction amount, including the product price *and* any tax you collect. So, for a $100 product with 20% VAT, they’d calculate their fee from $120.

Freemius calculates its fee on the product price only. For that same $100 product, a 4.7% fee with Freemius would be $4.70 compared to the $6.50 charged by Paddle or Lemon Squeezy on the full $120.

“I know that, at first glance, merchant of record fees can seem high compared to Stripe’s headline rate. But when you calculate Stripe’s true cost — after adding tools for taxes, compliance, and revenue recovery — the difference is often marginal,” says Vova Feldman, CEO of Freemius.

Unlike flat rates that stay fixed regardless of volume, [Freemius uses volume-tiered pricing](blog-new-freemius-pricing-2025.md) — the rate scales down as revenue grows. Check out the [full pricing page](https://freemius.com/new-pricing/).

## What migrating away from Stripe looks like

The [migration](https://freemius.com/freemius-migration) is more straightforward than most founders expect, but it’s worth sizing the effort before you start.

Freemius offers two paths:

1. **Sync-first migration:** Your existing Stripe subscriptions keep renewing as normal while data mirrors across. Useful for validating the setup and license key continuity before committing.
2. **Full migration:** Freemius takes over renewals, tax, and dispute handling entirely. This is the only path that actually removes the compliance burden (the sync approach just splits it).

The main concern beforehand is whether subscriptions keep running smoothly and whether customers notice anything.

In practice, they don’t — if the migration is done correctly, license keys carry over, subscriptions renew as usual, and everything continues without interruption.

Florian migrated three separate EDD stores with different setups and saw immediate operational impact:

> We’ve eliminated those extra tools completely, which is a direct cost saving and a big time saving. Our support team spends less time managing billing-related issues, which means more time can go into product and customer experience.

David from Versys Media took a phased approach, routing EU and APAC revenue through an MoR while keeping Stripe for other products:

“Our internal finance time for that product dropped to a few hours a month. We had much clearer unit economics by country since the MoR provided clean, net reports. Our blended payment cost stabilized, even if the headline fee was slightly higher, because we were no longer bleeding value in hidden admin, tax and FX friction.”

Freemius also provides payment analytics alongside the billing layer — clean net reports by country and product, without having to manually reconcile against accounting exports.

That’s the part Nicky and Florian were spending 6–15 hours a month on.

## Stop paying the Indie Tax, keep more of your revenue

Stripe’s 2.9% is only part of the story. Add international fees, failed payments, and compliance overhead, and you’re looking at a real cost that can eat away around 7.5% of your revenue (plus the hours you spend keeping it all running).

**This is the Indie Tax:** not just the money, but the time and energy you lose maintaining a fragile stack of tools.

You didn’t build your product to become your own finance team. An MoR like Freemius takes that entire burden off your plate, so you can put those hours back into the product.

**Three signals it’s time to evaluate an MoR:**

- More than 30% of your customers are outside your home country
- You’re spending more than 5 hours a month on billing-related admin
- You’ve added more than one third-party tool to cover what Stripe doesn’t include

**“The moment we switched, we stopped worrying about taxes, chargebacks, and recovery flows. Everything just works now, and that’s priceless.”** — Florian Vizethum

Want to see what the full Freemius platform covers? Here’s our detailed guide to how a [merchant of record](merchant-of-record.md) works for software makers.

## FAQ: The real cost of Stripe for software businesses

### What is the real Stripe transaction fee for software businesses?

For software businesses selling globally, the real Stripe transaction fees are typically 7.2%–11.7%, not the advertised 2.9% + $0.30.

That advertised rate is based on a percentage fee plus a fixed fee per successful transaction, while the gap comes from international card fees (+1.5%), Stripe Billing (+0.7%), Stripe Tax (+0.5%), Radar fraud protection ($0.02/transaction), dispute fees ($15/dispute), and currency conversion (1%–4%).

### Why are Stripe fees so high?

Stripe’s base rate (2.9% + $0.30) is standard for the payments industry — it isn’t high by itself. The fees become high because Stripe is payment processing infrastructure, not a full commerce solution.

Tax compliance, recurring billing, failed payment recovery, and fraud protection are all additional services, each with its own cost. International payment fees (+1.5%) and currency conversion (1%–4%) apply automatically for cross-border sales.

When you stack everything a software business actually needs, the effective rate climbs to 7.8%–12.3%. The fees aren’t hidden — they’re just priced individually, which makes the total easy to underestimate at the start.

### Does Stripe charge fees on sales tax and VAT?

Yes. Stripe calculates its fee on the full transaction amount, including any tax collected. On a $100 product with $20 VAT, the 2.9% fee applies to $120, so you pay processing fees on money you’ll remit to a tax authority, not revenue you keep.

### How do Stripe’s fees compare to Paddle for software?

Stripe’s headline rate (2.9% + $0.30) is lower than Paddle’s (5% + $0.50), but Stripe charges separately for what Paddle includes: tax compliance (+0.5%), subscription billing (+0.7%), and $15 per dispute.

At $10K MRR selling globally, both platforms cost roughly the same in total. The difference is that Paddle bundles compliance; Stripe leaves it to you.

### Is Lemon Squeezy cheaper than Stripe for software sellers?

Lemon Squeezy’s headline rate (5% + $0.50) is higher than Stripe’s (2.9% + $0.30). The effective cost is comparable once you add the tools Stripe requires but Lemon Squeezy includes: tax compliance, subscription billing, and failed payment recovery. For sellers already running those tools on top of Stripe, the real rate difference is small.

### Which payment processor charges less for international software sales?

For sellers with 60%+ international revenue, merchant of record platforms (Freemius, Paddle, Lemon Squeezy) typically cost less than Stripe on an effective basis.

Stripe adds 1.5% for international cards plus FX conversion on top of its base rate; MoR platforms bundle international processing into a single fee. For primarily US-based audiences, Stripe’s base rate is competitive.

### What is a merchant of record and how does it affect my payment costs?

A merchant of record (MoR) is the legal entity that sells your product to the customer. When you use an MoR, they collect and remit taxes, handle chargebacks, manage fraud, and assume compliance liability.

When you use Stripe, you are the merchant of record — all of that stays with you. The cost difference shows up not in the headline rate but in the tools and time required to fill those gaps yourself.

### Can Freemius replace Stripe for SaaS and WordPress plugin sellers?

Yes. Freemius replaces Stripe plus the tools typically stacked on top of it — tax compliance, subscription billing, failed payment recovery, and software licensing — in a single platform built for SaaS, downloadable software, and WordPress plugins and themes.

### How do I calculate my actual Stripe effective rate?

Go to [dashboard.stripe.com/reports/balance](https://dashboard.stripe.com/reports/balance), select a 90-day period, and apply:

effective rate = SUM(Charges Fees + Dispute Fees + Additional Fees) ÷ SUM(Charges + Refunds + Disputes + Reversals).

This captures disputes, FX adjustments, and any Stripe add-ons. Most founders who run this calculation find their real rate is meaningfully higher than the advertised 2.9%.