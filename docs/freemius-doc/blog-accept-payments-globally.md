You can launch a SaaS and accept payments globally in a matter of hours. But every new market brings tax, invoicing, and compliance rules that your checkout does not handle by itself.

That is where a lot of solo founders and SaaS makers get caught out. Stripe, PayPal, and other payment processors help you accept payments, but they do not automatically make you compliant in every market you sell to.

A [merchant of record](merchant-of-record.md) does. An MoR becomes the legal seller for each transaction, calculates and collects tax at checkout, handles invoices and filings, and takes responsibility for the compliance layer behind the sale.

This article breaks down what SaaS makers need to know before selling software globally, so payments, tax, and compliance are covered before they become expensive problems.

## TL;DR — What does it take to accept payments globally?

- Selling software globally can create VAT, GST, sales tax, and invoicing obligations across multiple markets — sometimes before you have meaningful revenue in that country.
- A payment gateway processes transactions. A merchant of record (MoR) assumes legal tax liability, so your customers’ VAT becomes the MoR’s problem, not yours.
- To accept payments globally, you need multi-currency support, local payment methods (iDEAL, UPI, PIX, etc.), and digital wallets — not just card processing.
- Authorization rates are often higher with an MoR thanks to local acquiring — the ability to process payments through banking partners in a customer’s region. This makes transactions look more local to the issuing bank, which can reduce payment declines and improve conversion rates.
- Freemius operates as an MoR in 100+ countries, handling VAT, sales tax, fraud, and chargebacks, so software makers can start accepting payments globally from day one without a dedicated compliance team.

## The two layers of accepting global software payments: Processing and compliance

Accepting payments from international customers means solving two separate problems: getting the transaction through and staying compliant in the customer’s market. Most payment solutions only solve the first.

### Layer 1: Payment processing

Moving money from an international customer into your account: accepting cards, digital wallets like Apple Pay and Google Pay, and local methods like iDEAL (Netherlands), UPI (India), PIX (Brazil), and SEPA transfers.

It also means showing prices in the customer’s own currency instead of forcing a mental conversion. Gateways like [Stripe](https://freemius.com/stripe-alternative/), PayPal, and Adyen are built for exactly this layer.

### Layer 2: Tax and legal compliance

Calculating the correct VAT or digital services tax by customer location, remitting it to the right authority, filing on schedule, and tracking rule changes across jurisdictions.

For physical goods, this layer usually kicks in past a revenue threshold. For digital software, revenue thresholds are often not the deciding factor. In many markets, especially for non-resident sellers, tax obligations can begin with the first sale.

That reality caught [Colin Bartlett](https://www.linkedin.com/in/colinabartlett/), CEO and co-founder of [StatusGator](https://statusgator.com/), by surprise Stripe processed payments cleanly for a year, until a €19 invoice to a customer in Austria came back rejected because their finance team needed VAT details the checkout hadn’t collected.

I opened our Stripe records, our accounting software, and three tabs about EU VAT rules. Each one gave me a different answer. An hour later, after a lot of research, I still didn’t know how to answer.

Bartlett and his co-founder moved to a merchant of record soon after, not to fix one invoice, but because reconstructing VAT decisions from a year of Stripe exports wasn’t something they could redo fast if a tax authority ever asked.

Payments gateways generally stop at Layer 1. Bolting on a tool like Stripe Tax addresses tax calculation, but not the liability: you still register with each tax authority, file your own returns, and own the consequences of getting it wrong.

A merchant of record runs both layers under a single integration, which is the structural difference that matters once you’re selling outside your home country.

The next section explains why this second layer is non-negotiable for digital software and how it differs from physical goods and other digital products.

## Digital products VAT and sales tax: What software makers owe and when

For digital software, VAT and sales tax obligations depend on the customer’s location, buyer type, and local threshold rules.

**B2C sales:** Selling to consumers in the EU, UK, Australia, or Japan means charging VAT at the rate set by the customer’s country. For non-EU sellers there’s no minimum threshold: a US-based developer with one French subscriber is already technically liable for French VAT.

[**B2B reverse charge (EU)**](https://freemius.com/blog/eu-vat-reverse-charge-guide/)**:** For EU B2B sales, VAT can often be handled through reverse charge, where the customer accounts for VAT instead. But this only works if your checkout validates their VAT ID and applies the exemption at purchase.

This matters most for WordPress plugins, developer tools, and B2B SaaS, where a meaningful share of EU revenue can qualify for the exemption if validation runs at checkout.

[Hamid Ali](https://www.linkedin.com/in/hamidpeya/), founder of [WordLayouts.com](http://wordlayouts.com), ran into this when a customer requested a VAT-compliant invoice he couldn’t issue.

“I was using a regular payment processor and felt confident the setup was secure until a business client from Germany asked for a VAT-compliant invoice I couldn’t provide at the time. That’s when I realized I had an enormous tax compliance risk without even knowing it, and that my current payment setup wouldn’t be able to handle it.”

[**US sales tax**](blog-sales-tax-on-software.md)**:** Many states use economic nexus thresholds to decide when remote sellers must register, collect, and remit sales tax. The [most common threshold is around $100,000](https://www.avalara.com/blog/en/north-america/2025/06/states-eliminating-economic-nexus-transaction-thresholds.html) in annual sales per state, though some states also use transaction counts, and the rules vary by jurisdiction.

That means a moderately successful SaaS can trigger filing obligations across multiple states inside its first year, each with its own registration schedule.

Handling this without an MoR means:

- Registering with the EU’s [One-Stop Shop (OSS)](https://vat-one-stop-shop.ec.europa.eu/index_en) for quarterly B2C filings
- Tracking tax by customer location
- Generating compliant invoices for each market
- Repeating the process for the UK, Australia, and every US state where you’ve crossed a nexus threshold

Since January 2024, that exposure has become easier for tax authorities to detect. Under [CESOP](https://taxation-customs.ec.europa.eu/taxation-1/central-electronic-system-payment-information-cesop_en), the EU’s Central Electronic System of Payment Information, EU payment service providers — including Stripe and PayPal — must [report cross-border transaction data quarterly](https://freemius.com/blog/eu-vat-2024-us-software-sellers/#what_changed_with_eu_vat_compliance).

Non-compliance is no longer invisible to tax authorities. But when you sell through an MoR, that entire compliance layer transfers: registrations, tax collection, filings, liability. Your name never appears on a VAT filing.

We’ve covered the mechanics in more depth separately. See our guides on [EU VAT and UK VAT](eu-vat-uk-vat-europe.md) and [US sales tax and economic nexus](us-sales-tax-and-economic-nexus.md) if you’re scoping registration requirements market by market.

Tax exposure is one half of the problem. The other half is what it takes to actually get the payment through, and that starts with currency.

## How to accept payments globally: Currencies, local methods, acquiring, and recurring payments

Accepting payments globally requires more than enabling a few most popular payment methods. Customers in different regions prefer different payment methods, and a limited checkout can directly reduce conversion rates.

### Multi-currency pricing vs. multi-currency settlement

Many gateways support multi-currency transactions, letting customers pay in their local currency while you settle in USD. The problem is that the price shown at checkout is often still in USD, so the customer has to convert it manually.

Multi-currency *pricing* is different — the price shows in the customer’s own currency from first glance. A customer in Germany comparing €29/month to a competitor’s listing makes a direct decision; one staring at $31.47 is still doing math.

### Local payment methods SaaS customers expect by region

Credit card use varies by country, and in several major markets it isn’t the default way people pay online.

- iDEAL lets customers pay directly from their bank account and accounts for [over 70% of online payments in the Netherlands](https://www.mordorintelligence.com/industry-reports/netherlands-ecommerce-market)
- UPI dominates digital payments in India through a mobile-first, real-time interface
- PIX is Brazil’s fast-growing instant payment rail

[![iDEAL as the payment method at Freemius screenshot ](https://freemius.com/blog/wp-content/uploads/2026/06/ideal-as-the-payment-method-at-freemius-screenshot.png)](https://freemius.com/blog/wp-content/uploads/2026/06/ideal-as-the-payment-method-at-freemius-screenshot.png)

*In* [*Freemius Checkout*](checkout.md)*, iDEAL appears as a local payment option for Dutch customers, integrated directly into a fully localized checkout flow.*

A checkout offering only credit card payments via Visa and Mastercard gives customers in those markets no familiar option, and many won’t complete a purchase with a method they rarely use.

For recurring payments, SEPA Direct Debit plays a similar role across Europe, enabling bank-based subscription billing at typically lower cost than cards.

### Digital wallets, local acquiring

Apple Pay and Google Pay have become the default checkout for a large share of mobile commerce — one biometric tap replaces a 16-digit card form, and both also work through browser integration on desktop.

Acquiring (the system that handles and routes card payments between banks) matters just as much, but gets far less attention.

Standard payment gateways use a single acquiring setup for all transactions. As a result, payments are often processed outside the customer’s region, which can increase declines on international cards.

Merchant of record platforms with local acquiring licenses process payments through acquirers in the customer’s region. This makes the transaction appear local, improving approval rates and often reducing fees.

### Recurring payments across borders

International renewals fail more than domestic ones for three compounding reasons:

1. Banks flag recurring foreign charges more aggressively
2. Cards expire between billing cycles
3. [PSD2’s Strong Customer Authentication rules](https://finance.ec.europa.eu/publications/strong-customer-authentication-requirement-psd2-comes-force_en) can block a renewal if the initial charge lacked correct authentication

To reduce this failure rate:

1. Implement 3D Secure 2 on the initial charge to register the recurring relationship with the cardholder’s bank
2. Space out failed renewal retries over several days rather than attempting them immediately
3. Use account updater services that automatically fetch replacement card details when a card expires

Real-time rails like SEPA Instant and PIX sidestep the category entirely (no card expiry, SCA (strong customer authentication) step, or cross-border fee), which is why a meaningful Dutch, Indian, or Brazilian customer base produces steadier cash flow than card billing alone.

We go deeper on dunning and renewal mechanics in our [payment processing guide for SaaS](blog-payment-processing-for-saas-guide.md).

Supporting local currencies and multiple payment methods is only part of the equation. You also need to know whether a provider can handle the operational requirements that come with selling software internationally.

## What SaaS makers should look for in a global payments setup

The right global software payments setup should cover the full sales layer: transaction processing, tax compliance, subscriptions, invoicing, fraud prevention, reporting, and local payment methods.

Not every payment provider is built for software and the gaps surface fast once you sell internationally.

Check these six things before committing.

1. [**Tax compliance coverage**](https://freemius.com/tax-compliance/)**:** Some setups calculate, collect, and remit VAT on your behalf and assume legal liability; others hand you a report and leave registration, filing, and errors with you.
   
   Ask directly: Who is the registered seller listed on the customer’s invoice, you or the provider? If it’s you, the compliance work hasn’t actually left your desk.
2. [**Subscription-native billing**](subscriptions.md)**:** A payment gateway records a failed renewal and stops. A subscription platform triggers dunning — retries and emails that give the customer a chance to fix payment before cancellation.
   
   Run a failed-renewal test in the platform’s sandbox and count the automated retries and emails before cancellation; one or none means you’re likely building dunning yourself.
3. [**Software licensing integration**](software-licensing.md)**:** If your product ships with license keys, payment needs to talk to licensing. A lapsed subscription should deactivate the license; a renewal should extend it automatically.
   
   Check whether that sync runs natively or whether you’d need to build a webhook listener for it. The second option means manual cleanup on every refund, plan change, and trial conversion.
4. **Fraud prevention and PCI compliance requirements:** Cross-border transactions carry higher fraud rates, and most card networks flag a merchant account [once disputes cross 1% of monthly transactions](https://www.chargeblast.com/blog/chargeback-threshold).
   
   For a product with 1,000 subscribers, that’s 10 chargebacks before you’re under review and at risk of having online payment processing restricted or cut off entirely.
   
   Check whether fraud detection, tokenization, and 3D Secure are included by default or only available as paid add-ons.
5. **Consolidated reporting and automatic invoicing:** Once you’re collecting revenue across multiple currencies, you need a unified view to understand your business.
   
   Selling to EU businesses adds another requirement: compliant invoices carrying your and customer’s VAT number, the applicable rate, and the transaction currency.
   
   Pull a sample EU B2B invoice before you sign up. If either VAT number is missing, your customer can’t reclaim the tax and the support ticket lands on you.
6. **Effective pricing:** The advertised rate is never the full rate. A $100 international renewal through Stripe picks up 2.9% base, 0.7% for Stripe Billing, and 1.5% for the international card fee — 5.1% before currency conversion or tax tooling, [and it compounds from there](blog-stripe-transaction-fees-real-cost.md).
   
   Model your actual transaction mix — domestic vs. international split, what’s bundled vs. billed separately — before committing to a number on a pricing page.

The six checks above tell you what a global payments setup needs to do. The next section uses Freemius as an example of how this is implemented in practice.

## How SaaS makers accept payments in 100+ countries with Freemius

Selling through Freemius means selling through a merchant of record built for software makers. You sell the product; Freemius handles the payment, tax, invoicing, fraud, chargeback, and compliance work behind each sale in [100+ countries](https://freemius.com/tax-compliance/).

### Tax and compliance

Tax is calculated at checkout by buyer location, covering EU VAT, UK VAT, and US sales tax. Every transaction is classified B2B or B2C automatically.

If a customer adds a VAT ID after purchase, Freemius issues a partial refund and keeps the subscription running instead of canceling and rebilling, avoiding the duplicate gateway fees a full refund-and-repurchase triggers.

OSS filing runs on your behalf; you never register for VAT anywhere.

### Automated revenue recovery

When a payment fails, dunning retries the charge over the following days and emails the customer, who can switch payment methods to resolve it.

License keys deactivate on lapse and reactivate on renewal automatically, no webhook setup required. Cart abandonment recovery sends a three-email sequence to anyone who started checkout and didn’t finish, with zero configuration.

### Local payment coverage

Major cards, PayPal, and iDEAL, priced in the customer’s own currency — USD, EUR, GBP, AUD, CAD, ILS, or PLN. Checkout runs in English, Spanish, German, French, Italian, Dutch, Croatian, and Hebrew, with right-to-left support.

### What Freemius costs you

You pay a percentage of sales, and [the rate drops as you scale](https://freemius.com/new-pricing/):

For a side-by-side comparison against Paddle, FastSpring, and the rest of the MoR field, see our breakdown on [choosing an MoR by SaaS stage](blog-best-merchant-of-record-providers-saas-stage.md).

## Getting started: How to set up global payments for your software

To get started, simply create an account, add your product, set your pricing and currencies, and embed the checkout. Freemius handles tax calculation, collection, and remittance on every sale from there.

[![Freemius Dashboard - Plans overview](https://freemius.com/blog/wp-content/uploads/2026/06/freemius-dashboard-plans-overview.png)](https://freemius.com/blog/wp-content/uploads/2026/06/freemius-dashboard-plans-overview.png)

Embedding the checkout is the only step that might touch code and you have three options:

1. A [hosted link](help-documentation-checkout-integration-hosted-checkout.md) for a no-code solution
2. An [overlay](help-documentation-checkout-integration-overlay-checkout.md) to keep buyers on your site
3. The [JS API](help-documentation-checkout-integration-freemius-checkout-buy-button.md) for full control over the customer experience

The REST API and webhooks sync the subscription lifecycle with your existing systems for custom builds.

Makers building with AI tools have an even shorter path — see our guides on [adding payments to an AI app](blog-how-to-add-payments-ai-app.md) and [monetizing a Lovable app](blog-how-to-monetize-lovable-app.md).

[![Freemius Hosted Checkout](https://freemius.com/blog/wp-content/uploads/2026/06/freemius-hosted-checkout.png)](https://freemius.com/blog/wp-content/uploads/2026/06/freemius-hosted-checkout.png)

Most makers have this running in a few hours. From the moment it’s live, billing runs, license keys sync, VAT is handled, abandoned checkouts trigger recovery emails, and customers get a self-service portal to manage their own subscriptions.

[![Freemius Customer Portal](https://freemius.com/blog/wp-content/uploads/2026/06/freemius-customer-portal-1.png)](https://freemius.com/blog/wp-content/uploads/2026/06/freemius-customer-portal-1.png)

## SaaS global payments checklist

If you’re scoping a global payments setup, run it through this sequence first:

1. **Map your buyer mix:** List the countries where you have customers or expect meaningful volume in the next 12 months. That tells you which VAT regimes, currencies, and payment methods actually matter.
2. **Check who holds tax liability today:** On a payment gateway alone, you’re the registered party in every market where you’ve crossed a threshold, registered or not. That’s the gap to close first.
3. **Price your real transaction mix, not the headline rate:** Run a $100 domestic sale and a $100 international renewal through each provider’s full fee stack before comparing platforms.
4. **Confirm subscription-native features exist:** Dunning, license sync, and cart recovery are the difference between a payment processor and a billing system built for software.
5. **Migrate before you’re forced to:** Moving infrastructure under live subscriber load is harder than moving early, and staying on a gateway-only setup means compliance exposure that grows with every new market.

If any of this sounds like where you are right now, the fastest way out of it is infrastructure that already covers it.

[Set up Freemius](https://dashboard.freemius.com/register/) and open your checkout to the world.

## FAQ: Accepting international payments

### Do I need to register for VAT in every country I sell software to?

Not if you sell through a merchant of record. Without one, yes — digital services trigger VAT obligations from the first sale in most jurisdictions, since the EU, UK, Australia, and others apply no minimum threshold to non-resident sellers.

### What’s the difference between a payment gateway and a merchant of record?

A payment gateway processes transactions and moves money. An MoR is the legal seller, meaning it holds tax registrations, collects VAT, files returns, and owns compliance liability.

### Can I accept payments from international customers without a local business entity?

Yes, if you sell through an MoR. The MoR is the legal entity in each market, and you sell through them — no local office, bank account, or entity required anywhere they operate.

### What local payment methods do I need to support for global software sales?

Credit and debit cards plus PayPal cover a wide base everywhere. For the EU, add iDEAL and SEPA, for South Asia, UPI, for Latin America, PIX. Apple Pay and Google Pay matter most for mobile. Start with the markets driving the most traffic.

### How do recurring payments work for global software subscriptions?

Cross-border renewals need 3D Secure on the initial transaction, smart retry logic, and dunning sequences that catch involuntary churn. An MoR or purpose-built subscription payment platform handles all three by default; a generic gateway requires custom work for each.

### How do I handle global payouts — when and how do I get paid?

With a standalone processor, funds typically land within 2–7 business days depending on the payment gateway and country. With an MoR, the platform collects revenue and pays out on a defined schedule after deducting its fee. Confirm payout frequency and supported currencies before committing.