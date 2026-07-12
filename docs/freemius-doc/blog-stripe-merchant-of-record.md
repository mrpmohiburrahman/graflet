With the launch of Managed Payments, Stripe began acting as a [merchant of record](merchant-of-record.md) in April 2025, but only for a narrow subset of transactions. Its eligibility rules exclude more software businesses than they include.

That distinction is important because “Stripe merchant of record” gets thrown around loosely. Some founders are referring to Stripe Tax. Others mean the new Managed Payments in beta. Very few have mapped exactly where Stripe’s liability ends and their own begins. Yet that line determines how much compliance work ultimately lands on their desk.

So let’s draw the line clearly.

This article explains what each Stripe product covers, where Managed Payments’ eligibility requirements leave many software businesses exposed, and what changes operationally when you move to a full merchant of record.

## TL;DR — Is Stripe Managed Payments enough, or do you need a full merchant of record?

**Stripe Managed Payments may be enough if you:**

- Sell through Stripe Checkout or Payment Links
- Don’t use Stripe Connect or run a marketplace
- Operate within Managed Payments’ supported countries
- Only need Stripe to handle payments, tax remittance, fraud, and chargebacks

**A full merchant of record like Freemius is likely a better fit if you:**

- Use a custom or embedded checkout
- Sell through a marketplace, app store, or partner channel
- Operate outside Managed Payments’ supported regions
- Need software-specific features like licensing, dunning, subscription recovery, or cart abandonment
- Want one platform to handle both compliance and your software billing infrastructure

“Stripe merchant of record” means Stripe is the legal seller behind the transaction — not just the payment processor moving money between your customer and your business. But because of the way Stripe’s suite of products is set up, it’s not automatically your MoR.

**Standard Stripe is a payment processor.** It charges the customer’s credit card, moves the money, and sends a receipt. You remain the seller of record for every transaction, which means sales tax registration, VAT filing, PCI compliance, fraud, and chargebacks all sit on your side of the table.

**Stripe Tax adds tax calculation on top of that.** It applies the correct VAT amount or sales tax rate at checkout based on buyer location. That’s a real improvement over tracking rates in a spreadsheet, but like most tax-adding tools, it stops there. It doesn’t register you in a jurisdiction, file your tax returns, or take on liability if something goes wrong.

[![Stripe Tax dashboard screenshot](https://freemius.com/blog/wp-content/uploads/2026/07/stripe-tax-dashboard-screenshot.png)](https://freemius.com/blog/wp-content/uploads/2026/07/stripe-tax-dashboard-screenshot.png)

Source: Stripe website

If you sell into Europe, the [EU VAT rules for software sellers](https://freemius.com/blog/eu-vat-2024-us-software-sellers/) show just how much of that still lands on you.

[Hamid Ali](https://www.linkedin.com/in/hamidpeya/), founder and CEO of [WordLayouts](https://www.wordlayouts.com/), saw exactly where that line is after receiving a compliance notice for EU sales.

> Stripe is an exceptional payment processor, but as soon as you sell a digital product to someone in the EU, you take on tax liabilities that Stripe can help you calculate and process, but will never be legally responsible for. And that distinction will undoubtedly come back to you.

**Managed Payments is the only Stripe product where Stripe actually becomes the merchant of record solution.** For eligible transactions, Stripe becomes the legal seller: it remits sales tax and VAT in more than 80 countries, runs fraud prevention through Radar, handles chargebacks, and manages payment-related support requests

[![Stripe merchant of record - managed payments dashboard](https://freemius.com/blog/wp-content/uploads/2026/07/stripe-merchant-of-record-managed-payments-dashboard-e1783506923443.png)](https://freemius.com/blog/wp-content/uploads/2026/07/stripe-merchant-of-record-managed-payments-dashboard-e1783506923443.png)

Source: Stripe website

Put simply, Stripe runs the back office part: taxes, fraud claims, refund requests, chargebacks, and payment support.

But the word doing the heavy lifting is “eligible.” If your transactions meet every requirement, then yes, Managed Payments makes Stripe a merchant of record. Most SaaS businesses, however, run into at least one restriction.

## Where Stripe Managed Payments coverage ends

Managed Payments only applies to transactions that clear four separate eligibility checks: checkout method, business model, geography, and product type. Miss any one of them, and the transaction falls back to standard Stripe, where you remain the legal seller and retain the liability.

### Managed Payments only supports Stripe Checkout and Payment Links

For now, Managed Payments is limited to Stripe’s hosted payment flows: Checkout and Payment Links. It does not apply to Elements, custom payment flows, or integrations outside those two paths.

Stripe also reviews accounts before granting access, so this isn’t just a new feature you can enable during a coffee break. If you’ve built a custom checkout, qualifying means a real migration, not a configuration change.

So factor that engineering work into your decision before assuming Managed Payments is the simpler option.

### Marketplace and Connect-based businesses don’t qualify

Managed Payments doesn’t support platform business models built on Stripe Connect, including Express accounts and platform-managed accounts. . If you run a [marketplace model](blog-what-is-a-wordpress-marketplace.md) — even one where you process payments on behalf of other sellers — Managed Payments is off the table.

### Geographic eligibility is narrower than it looks

On the seller side, Managed Payments is available to businesses based in the US, Canada, most of Europe, Australia, Hong Kong, Japan, and Singapore.

There’s one important exception for the last two: Managed Payments doesn’t cover *domestic* tax compliance for them. Japan-based and Singapore-based sellers still handle parts of local compliance themselves.

Businesses based in countries like India, Brazil, South Korea, or Turkey aren’t currently eligible, regardless of how the rest of their setup qualifies.

Buyer location also affects eligibility. Transactions from customers in China, Russia, Iran, Cuba, North Korea, Syria, Kosovo, and a few overseas territories can’t be processed through Managed Payments.

### Subscriptions and billing still have separate costs

Subscriptions created through Stripe’s API as part of a custom billing flow aren’t supported. Subscriptions (e.g., monthly or yearly subscription) have to be created through Stripe Checkout, which can mean rebuilding a billing flow you already spent weeks getting right.

And here’s the part that surprises people: fraud protection is bundled into Managed Payments, but subscriptions aren’t. Recurring billing still requires Stripe Billing as a separate product with its own fees.

Your total cost depends on which Stripe products you stack together, not a single flat rate.

Even businesses that qualify for Managed Payments don’t get a [software-specific billing stack](blog-micro-saas-tech-stack.md#billing_and_monetization). It doesn’t manage license keys, retry failed subscription payments, recover abandoned carts, or provide a customer billing portal. Those capabilities still require separate tools or additional engineering.

That’s the gap a software-focused merchant of record model is designed to bridge.

## What a full merchant of record adds that Stripe doesn’t

A full MoR becomes the legal seller on **every transaction** (not a subset of them) and takes full responsibility for six specific categories that would otherwise live on your plate:

- **Tax collection and remittance:** Calculates [VAT](eu-vat-uk-vat-europe.md), [sales tax](us-sales-tax-and-economic-nexus.md), and GST at checkout, files returns, remits payment, and keeps up with changing regional tax rules so compliance updates don’t become your operational burden.
- **PCI DSS compliance:** Card data is handled within the MoR’s compliant infrastructure, so it never touches your systems.
- **Fraud management:** Fraud detection and blocking are managed as a service, not a configuration layer you need to tune and monitor.
- **Chargebacks and disputes:** The MoR works directly with card networks, handles evidence submission, and assumes liability for lost disputes.
- **KYC and AML compliance:** Identity verification and anti-money-laundering checks are handled as part of the MoR’s legal compliance obligations.
- **Customer data and privacy compliance:** Payment data handling is aligned with regulations such as [GDPR](help-documentation-checkout-features-gdpr.md) and CCPA as part of the infrastructure, rather than something you implement separately.

A payment processor like Stripe operates at the **transaction level**. That means expanding into new markets typically introduces additional configuration, tools, and compliance responsibility on your side.

A merchant of record operates at the **global commerce infrastructure level**. Global expansion doesn’t require rebuilding compliance per market because tax, liability, and regulatory handling are already embedded in the system.

The key pattern is that in the Stripe model, many capabilities exist as separate products or add-ons. Each introduces additional cost and operational overhead.

If you want to see how this compares in practice, here’s a breakdown of a [Stripe alternative](https://freemius.com/stripe-alternative) built for software monetization.

### Cost infrastructure differences

Standard Stripe charges a percentage plus a fixed fee per transaction, but the [effective cost often increases once additional services are included](blog-stripe-transaction-fees-real-cost.md).

Stripe Managed Payments bundles some of this, but subscription billing and other components may still be billed separately depending on setup.

A full MoR model typically replaces multiple standalone products with a single platform, though pricing structures differ between providers.

For example, Freemius uses a [tiered structure that decreases with volume](https://freemius.com/new-pricing/):

### Why “2.9% + $0.30” isn’t the real Stripe cost

The commonly cited Stripe rate is a baseline, not the full cost of operating globally. In practice, effective rates tend to increase once additional fees are included:

- Cross-border transactions
- Currency conversion
- Billing tools
- Fraud tooling
- Chargebacks and dispute handling

For example, David Hunt (COO at [Versys Media](https://versysmedia.com/)) reported an effective blended rate of **4.1–4.4%** once these factors were included.

[Tetiana Hnatiuk](https://www.linkedin.com/in/tetiana-hnatiuk-46355a164/) (COO at [Skylum](https://skylum.com/)) saw **5.5–7.0%** as international sales scaled and compliance tooling was layered on.

As Hunt puts it: “For non-trivial international SaaS, the ‘2.9%’ story is only the opening line. The real decision is whether you want to own that complexity or pay someone to absorb it.”

### The core difference between Stripe and a full merchant of record

A payment processor helps you move money.

A [merchant of record provider](blog-best-merchant-of-record-providers-saas-stage.md) removes entire layers of commerce infrastructure — tax, compliance, liability, and operational tooling — and replaces them with a single responsibility boundary.

A software-focused MoR like Freemius extends this further with infrastructure built specifically for software businesses, including [licensing](software-licensing.md), [cart abandonment recovery](cart-abandonment-recovery.md), and [checkout](checkout.md) flows designed around how software is actually sold, not assembled from a marketplace cart.

[![Freemius failed payment notice](https://freemius.com/blog/wp-content/uploads/2026/07/freemius-failed-payment-notice.png)](https://freemius.com/blog/wp-content/uploads/2026/07/freemius-failed-payment-notice.png)

An automated Freemius dunning notice, triggered instantly on a failed card charge.

The distinction isn’t just pricing or features. It’s where the operational responsibility sits and how much of it you want to carry as you scale.

## Four signs it’s time to move from Stripe to a full MoR

Businesses usually start looking beyond Stripe when the operational work around payments starts to outweigh the payment processing itself. If more than one of the below applies to your business, it’s often a signal that Stripe is no longer covering the full operational surface area you’ve outgrown.

**1. You operate outside Managed Payments coverage.** If your business or your customers fall outside Stripe’s Managed Payments coverage, you remain the legal seller for every transaction — tax registration, compliance, and liability stay with you in every market you enter.

A full merchant of record (MoR), such as Freemius, operates as the legal seller in 100+ countries, so global coverage is built in rather than something you assemble region by region.

**2. You rely on a non-hosted or custom checkout.** If your product uses Stripe Elements or a fully custom checkout flow, moving to Stripe Managed Payments typically requires rebuilding around Stripe’s hosted checkout experience.

A full MoR is usually designed to support more flexible integration patterns, including embedded or [platform-native checkout experiences](checkout.md), without forcing a redesign of your existing flow.

**3. Tax admin, disputes, and payment operations are taking meaningful time.** At scale, VAT registrations, chargeback handling, fraud review, and payment support become separate operational tracks — even if you’re using Stripe Tax and Radar.

A full MoR consolidates these responsibilities into a single operational layer that runs on your behalf.

[David Kemmerer](https://www.linkedin.com/in/davidkemmerer1/), co-founder and CEO of [CoinLedger](https://coinledger.io/), a crypto tax software, reached this point in his second year on Stripe, when international subscriptions grew to 37% of total revenue:

> Stripe was doing what it was designed to: processing payments. But we were growing more than we anticipated and it exposed us to international tax issues.

At that stage, the team was spending around 28 hours per month on tax and payment compliance work — between reviewing VAT invoices, coordinating with accountants, and managing related admin.

That’s more than three full working days each month spent on work that doesn’t contribute directly to product or growth.

**4. You need a full subscription and software monetization stack.** Capabilities like [dunning](help-documentation-marketing-automation-dunning-failed-payments.md), [license management](help-documentation-saas-integrating-license-key-activation.md), customer account access, and [cart recovery](help-documentation-marketing-automation-cart-abandonment-recovery.md) are not part of Stripe’s core product, and they’re not fully covered by Managed Payments either.

A software-focused MoR includes these as part of the platform, alongside [payment processing](blog-payment-processing-for-saas-guide.md), tax handling, and compliance, so the entire subscription lifecycle is managed in one place.

[![Freemius subscriptions dashboard](https://freemius.com/blog/wp-content/uploads/2026/07/freemius-subscriptions-dashboard.png)](https://freemius.com/blog/wp-content/uploads/2026/07/freemius-subscriptions-dashboard.png)

## What changes when you switch to a merchant of record

Switching to a merchant of record (MoR) is a big shift. It transfers legal and operational responsibility for the transaction to the MoR. Here’s what that looks like in practice.

### 1. Tax and compliance responsibility moves off your stack

With Stripe (or any payment processor), you are responsible for determining where you owe tax, registering in those jurisdictions, filing returns, and remitting payments.

With a full MoR, those obligations are handled within its coverage. That includes VAT, US sales tax nexus, GST, filings, and ongoing regulatory updates.

You no longer track thresholds or maintain tax registrations across markets — the MoR handles that.

### 2. Chargebacks and payment disputes are handled by the MoR

Refunds, chargebacks, and billing disputes become the responsibility of the MoR as the legal seller.

The MoR manages communication with card networks, submits evidence, and absorbs liability when disputes are lost.

### 3. Subscription billing runs as part of the system

Subscription operations such as renewals, [failed payment retries](blog-reduce-saas-failed-payments.md), and recovery flows are handled within the MoR layer.

Some software-focused MoRs also include dunning logic, customer billing portals, and cart recovery tools without requiring separate billing infrastructure.

For example, Freemius includes [subscription management, automated retries](help-documentation-marketing-automation-dunning-failed-payments.md#subscriptions), and a [Customer Portal](customer-portal.md) as part of its MoR offering, rather than requiring a separate billing stack.

![Freemius customer portal](https://freemius.com/blog/wp-content/uploads/2026/07/freemius-customer-portal.png)

### 4. The merchant on the transaction changes

The MoR becomes the legal seller on invoices and card statements.

Your branding typically still appears in the checkout and product experience — though how much depends on the MoR — but the transaction itself is attributed to the MoR entity.

This is primarily relevant for accounting, compliance, and customer-facing billing clarity.

### What does not change

Your core business remains the same in most meaningful ways:

- Your product, [pricing](blog-micro-saas-pricing-strategies.md), and positioning remain fully under your control
- You retain access to customer and transaction data required to run the business
- You still own customer relationships, product support, and all non-payment communication

### What you give up

A merchant of record reduces operational scope, but it also reduces control in specific areas.

You give up direct responsibility for certain aspects of checkout implementation and the direct legal merchant relationship with payment infrastructure.

In return, tax, compliance, disputes, fraud handling, and billing operations move outside your stack.

### The core trade-off

For many software businesses, the decision comes down to where you want complexity to live: inside your infrastructure, or outside it.

Once you’ve decided the trade is worth it, the next problem is practical: how do you move without losing the subscribers you worked so hard to get?

## Switching from Stripe to a full MoR without losing subscribers

Whether Stripe Managed Payments ruled you out or you simply want the full, software-focused solution, the success of a Stripe-to-MoR [migration](https://freemius.com/freemius-migration/) usually comes down to three things:

1. How you stage the rollout
2. How clearly you communicate the change
3. How much churn you anticipate upfront

Each one matters more than the technical migration itself.

### Stage the rollout

Start by routing all new signups through the MoR while keeping existing subscribers on Stripe until they complete a full billing cycle.

This avoids interrupting active subscriptions mid-cycle and gives you time to validate billing, tax handling, and support flows before a full cutover.

Once the system is stable, you can transition existing subscribers in batches aligned with their renewal dates.

### Communicate before they notice

Subscribers should hear about the change before it appears in their billing statement.

Tell subscribers what’s changing, including that a new name — the MoR’s rather than yours — will appear on their card statement. Without context, an unfamiliar charge descriptor can easily trigger confusion or chargebacks, even among loyal customers.

Give them:

- A clear timeline for the transition
- A simple way to update payment details if needed
- Reassurance that their subscription and access remain unchanged

### Plan for some churn, and soften it

Stripe payment methods are tokenized within Stripe’s infrastructure. Those tokens don’t transfer to a merchant of record, which means subscriptions need to be re-authorized and payment details re-entered.

That re-authentication step is where involuntary churn typically appears.

A common mitigation is to reduce friction or offset the effort, for example with a small renewal incentive or temporary extension during reactivation. The goal is to make the transition feel lighter than the effort required to drop off.

For practical ways to reduce churn and improve renewals during transitions like this, see this [guide on retention strategies.](blog-reduce-customer-churn-increase-subscriptions-renewal-rate.md)

### What carries over vs. what needs rebuilding

**Takeaway:** Your business logic transfers relatively well. What breaks is anything tightly coupled to Stripe’s infrastructure.

### Timeline and expectations

Migration timelines depend heavily on subscriber count and whether you align transitions with renewal cycles.

[CoinLedger](https://coinledger.io/) migrated roughly 4,800 active subscribers, with about **88% completing the transition within the first month**. That process required three pre-migration emails, a two-week in-app banner, and additional support coverage throughout the migration window.

Even so, they experienced around 5% permanent subscriber loss.

“If we didn’t do this, the loss would have been worse,” says Kemmerer.

A similar pattern appeared at [Floxy](https://www.floxy.io/), a proxy and web intelligence platform. CTO [Aimen Hallou](https://www.linkedin.com/in/aimen-hallou-87335216b/) reported an 8% loss during migration, attributing most of it to timing rather than execution:

> The 8% subscriber loss during migration was not a migration problem. It was the cost of a decision that, in hindsight, should have been made 6 months before, when we saw the red flags, and the subscriber base was less.

The pattern across both stories: migration churn is usually less about the mechanics and more about timing.

The longer you wait, the larger the subscriber base you need to transition and the higher the absolute friction, even when execution is solid.

## Start selling globally without the registration paperwork

[Selling globally](blog-accept-payments-globally.md) on standard Stripe scales compliance exposure faster than many founders realize. The issue is that nothing breaks noticeably at first — there’s rarely a clear warning. In many cases, the first signal is a tax notice, audit request, or unexpected liability.

Stripe Managed Payments is worth evaluating against your checkout setup, business model, and geography. It can be a meaningful upgrade if you meet its eligibility requirements across all required dimensions.

But if you don’t qualify — or if you need software-specific billing infrastructure that Stripe doesn’t provide — a full merchant of record removes those constraints entirely. It eliminates eligibility gating and offloads tax, compliance, and operational overhead, handing you back the hours you’d rather spend writing code.

Freemius operates as a merchant of record in 100+ countries with no checkout restrictions tied to eligibility. [See how Freemius handles tax compliance](https://freemius.com/tax-compliance/) or [explore the full subscription platform](subscriptions.md) before deciding what fits your setup.

## FAQ — Stripe, Stripe Tax, and Stripe Managed Payments

### Is Stripe a merchant of record?

Only in limited cases via Stripe Managed Payments, and only for transactions that meet its eligibility criteria. Standard Stripe and Stripe Tax are not merchant of record products. In those cases, you remain the legal seller of record.

### What’s the difference between Stripe Tax and Stripe Managed Payments?

Stripe Tax calculates VAT and sales tax at checkout but leaves registration, filing, and liability with you. Managed Payments goes further: for eligible transactions, Stripe becomes the legal seller and takes on tax remittance, fraud prevention, and dispute handling directly.

### Does Stripe Managed Payments work with marketplaces or Stripe Connect?

No. Managed Payments explicitly excludes Connect platforms, Express accounts, and any account controlled by a platform, regardless of business size and volume.

### Which countries does Stripe Managed Payments support?

Supported seller locations currently include the US, Canada, most of Europe, Australia, Hong Kong, Japan, and Singapore — though Japan and Singapore sellers still handle some domestic tax themselves.

On the buyer side, most global markets are supported, with a small number of restricted countries, such as China, Russia, and Iran, excluded from coverage.

### Do I lose customer payment data when I migrate to a merchant of record?

Yes. Stripe payment tokens are not portable to other systems, so customers typically need to re-enter payment details after migration.

To reduce churn, most migrations align transitions with billing cycles and communicate the change well in advance to minimize confusion and failed renewals.