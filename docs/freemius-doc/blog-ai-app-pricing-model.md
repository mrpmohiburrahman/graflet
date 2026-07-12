You built an AI app, people are using it, and now you need a pricing model that can survive real usage.

The problem? Most pricing guides are written for funded SaaS teams with predictable costs, bigger margins, and more room to experiment. AI apps are different. Every prompt, image, document, or workflow creates a cost, and your provider bills you whenever the product runs — whether that user is paying enough to cover it or not.

**Get the model wrong and your most engaged users become your most expensive ones.**

This guide looks at AI app pricing models through the lens that matters: how people use your product, what that usage costs you, and whether your pricing can absorb it.

You’ll compare subscriptions, credits, usage-based pricing, freemium, lifetime deals, and hybrid models, then choose a structure customers understand without letting inference costs eat your margins.

## TL;DR — What pricing model should I use for my AI app

**For most AI apps, the right answer is hybrid pricing:** a base subscription with a defined usage allowance and overage billing for customers who go beyond it.

- Flat subscriptions fail when power users consume disproportionate inference on a fixed fee
- One-time pricing fails when your backend keeps running after the sale

## Why inference costs make AI app pricing different from traditional software

Inference costs are the fees your AI model provider charges every time your app processes a prompt. Traditional software often gets cheaper to serve as it scales. AI apps do not work that way.

Every user interaction adds another compute cost to the bill, and a few power users can consume 8-10x more compute than the median customer (on the exact same plan).

[Naveen DA](https://www.linkedin.com/in/naveenda/), founder of [ResumeGrade](https://resumegrade.ai/), experienced the drain before he had a single paying user.

He launched his AI resume-review tool with a trial across two university departments and hit $80 in inference costs in the first month. Through caching and tighter model calls, he brought it down to $20.

That $60 gap is the difference between a product that can scale and one that loses a little more money every time people use it.

Other founders we spoke with had similar stories:

- One watched 8% of customers consume 61% of inference costs on a flat subscription
- Another launched a $19 lifetime add-on and lost 30% of revenue to power users within three months

This is why the first step in AI pricing is not choosing between subscriptions, credits, freemium, or usage-based. It’s finding the cost floor your pricing has to clear.

## Map your costs before you choose an AI app pricing model

Start by listing the costs behind your core user actions:

- Model/API fees per token, image, generation, call, or workflow
- Compute infrastructure
- Storage and retrieval
- Monitoring, logging, and support

To calculate your AI cost per user:

1. **Input cost** = input tokens per interaction × input price per token
2. **Output cost** = output tokens per interaction × output price per token
3. **Cost per user** = (input cost + output cost) × average interactions per month

For example, with $2 per million input tokens and $8 per million output tokens, a user generating 50,000 input tokens and 20,000 output tokens a month costs roughly $0.26/month in inference — before your margin buffer.

**Connect those costs to usage:**

What does one prompt, image, summary, or completed workflow cost? Multiply that by expected monthly usage per customer, and then add a buffer for retries, longer sessions, and your top 10% (heavy) users.

**That gives you a cost floor** — the minimum your pricing needs to cover before margin, growth, and product investment.

David Hunt, COO of [Versys Media](http://www.versysmedia.com/), works backward from target gross margin for his AI-powered initiatives:

> “If your underlying cost is $0.005 per 1,000 tokens and you want an 80% margin, your realized revenue needs to land around $0.025-$0.03 per 1,000 tokens.”

Make sure to keep that kind of token talk behind the curtain — builder lingo won’t compute with buyers. Use cost mapping to translate your internal math into customer-friendly units, clear usage limits, and pricing floors your model can survive.

Once those numbers are clear, the pricing models become easier to compare. Each one packages usage differently, exposes you to heavy-user risk differently, and shapes how customers understand value.

## The main AI app pricing models (with pros, cons, and examples)

### Seat- and subscription-based pricing

Subscription-based pricing charges customers a fixed recurring fee — monthly or annually — for access to the product, structured by seat count or account tier, with usage typically capped per plan.

Best for AI apps with predictable usage and natural usage ceilings, but only when caps are built in. Without a usage ceiling, flat subscription pricing is the fastest way to subsidize your heaviest users with revenue from your lightest ones. The risk isn’t the model itself; it’s leaving usage open-ended.

**Pros:**

- Predictable recurring revenue
- Familiar buying motion for SaaS customers
- Easy to package by seat, team, or account
- Works well when usage is capped or naturally consistent

**Cons:**

- Heavy users can wreck blended margins
- Average usage can hide expensive outliers
- “Unlimited” creates an open-ended cost liability
- Revenue stays fixed while inference costs keep moving

Put together, those cons create consequences:

[Aimen Hallou](https://www.linkedin.com/in/aimen-hallou-87335216b/), CTO of [Floxy](https://www.floxy.io/), saw how quickly they can bite after launching an AI-assisted data extraction feature on a flat subscription: 8% of customers were consuming 61% of inference costs.

> “Flat pricing on an AI product is not a business model. It is a slow-moving invoice you are sending to yourself.”

This problem is not limited to vibe coders or solo AI builders.

[GitHub Copilot was reportedly losing more than $20 per user per month](https://www.saastr.com/have-ai-gross-margins-really-turned-the-corner/) at its $10/month launch price. When Cursor moved to pooled credits in June 2025, [one team burned through a $7,000 annual subscription in a single day](https://www.ainews.com/p/cursor-faces-backlash-over-pro-plan-changes-and-surprise-usage-charges).

These are not freak incidents. They are what happens when flat pricing gives customers a simple monthly fee but gives the business no ceiling on AI usage.

If subscriptions still look like the right fit for your product, the answer is not to abandon them. It is to build guardrails into the plan before usage starts eating through the margin.

**How to make subscriptions work for your AI app:**

- **Usage caps** — a monthly limit per user so each plan has a clear cost ceiling
- **Overage pricing** — let customers exceed the cap at a defined per-unit rate
- **Model routing** — serve lighter queries with cheaper models
- **Fair-use limits** — protection against automation abuse or extreme usage patterns
- **Tiered access** — give higher plans more usage or better models so upgrades feel tied to real value
- **No “unlimited” without proof —** don’t offer unlimited AI access until you have at least three months of usage data confirming your unit economics support it

### Usage-based pricing (tokens, API calls, requests)

Usage-based pricing charges customers based on what they actually consume — per token, API call, image, document, or completed workflow — so the bill scales directly with activity.

Usage-based pricing is the fairest model for AI apps with variable workloads — revenue scales with costs and heavy users pay for what they actually consume. The model breaks down when customers can’t predict their spend and get surprised by the invoice.

**Pros:**

- Revenue scales directly with costs — no power-user subsidy problem
- Fairest model for high-variance workloads
- Small teams can start affordably, which encourages experimentation as needs grow

**Cons:**

- Customers may struggle to budget when small usage changes create noticeable price swings
- Requires real-time dashboards and alerts to maintain trust and transparency
- Non-technical audiences struggle with token or API-call framing

**How to make usage-based pricing work for your AI app:**

- **Choose a clear billing unit** — tokens for technical users; documents, images, or reports for non-technical users
- **Tie billing to workloads, not access** — charge for what the AI does, not for having AI available. “Unlimited AI access” is not a billing unit
- **Show real-time usage** — what they have used, what it costs, how close they are to any limit
- **Send pre-limit alerts** — warn customers before they hit thresholds
- **Add spending caps** — auto-pause or approval prompts before unexpected overages

### Credit- and package-based pricing

Credit-based pricing lets customers buy a block of usage upfront — credits, tokens, or a similar unit — and spend them as they go, at rates that vary by action type or model used.

Credit-based pricing is the right AI pricing model when the gap between your lightest and heaviest users is large.

Revenue is collected before inference costs arrive, which means you know what you’ve taken in before you’re surprised by what you owe. Customers buy a pack of credits and spend them on prompts, generations, documents, or workflows.

**Pros:**

- Predictable income even when usage spikes
- Works well for bursty, project-based usage such a creative initiatives; customers pay when they build, not when they don’t
- Natural fit for developer tools, API-based products, and builder-focused apps where credits already feel familiar
- Packages multiple AI capabilities under one currency, which is useful when your app has several different action types with different underlying costs

**Cons:**

- Friction for non-technical or consumer audiences
- Raw credit counts do not convert — requires clear outcome-based examples on pricing pages
- Credits can obscure the actual cost per outcome if conversion rates are not clearly communicated

Credits are easier to buy when the pricing page turns them into real outcomes. [Aimen Hallou’s](https://www.linkedin.com/in/aimen-hallou-87335216b/) team tested three landing page variations. Outcome-based pages converted 34% better than technical ones.

> “Buyers don’t care about what’s happening inside your infrastructure. They care about the output.”

[David Hunt](http://www.versysmedia.com/) adds: “100 credits typically covers around 300 chat conversations” tells a buyer something useful. A number of tokens tells them nothing.

**How to implement credit-based pricing for your AI app:**

- **Work backward from your target gross margin** — credits should cover model/API costs, variance, retries, and room for profit
- **Price around your heaviest realistic user** — not your median customer. Packages that work “on average” can still break under power users
- **Translate credits into outcomes on the pricing page** — documents processed, reports generated, images created, workflows completed. Keep tokens internal
- **Show what each package actually buys** — for example, “500 credits = about 100 resume reviews” or “1,000 credits = 50 research reports.”
- **Test outcome-based framing against technical framing before you commit** — especially if your audience is non-technical

### Value- and outcome-based pricing

Value-based pricing sets the price based on the outcome the AI delivers — a resolved ticket, a qualified lead, a processed document, or a measurable efficiency gain — rather than on usage or access.

Value-based pricing works when the AI delivers a measurable outcome the customer can verify and when that outcome is worth more than the compute it took to produce.

It shifts the conversation from “what does this cost?” to “what is this worth?” — but only holds up when ROI is clear, concrete, and auditable.

**Pros:**

- Supports higher prices when the AI creates measurable business value
- Aligns revenue with customer success, not just access or usage
- Can improve margin over time as model costs fall and output quality improves

**Cons:**

- Only works when the outcome is clear, measurable, and valuable enough to price against
- Starts failing when ROI is hard to prove, delayed, or disputed
- Requires more trust, reporting, and sales effort than simple usage-based pricing

**How to make value-based pricing work:**

- **Define the outcome before launch** — vague “time saved” or “productivity gained” claims create attribution disputes
- **Build measurement into the product** — both sides should be able to verify the result, not argue about it later
- **Use a base fee plus outcome component** — keep revenue predictable while still sharing in the upside
- **Set clear rules for attribution** — define what counts as a qualified lead, resolved ticket, accepted candidate, saved hour, recovered revenue, or completed workflow

### Performance-based and revenue-share models

Performance-based pricing ties payment to agreed customer outcomes or KPIs — revenue generated, tickets resolved, leads converted — so the vendor earns only when the product delivers a defined result.

Performance-based pricing works best as an add-on to a base fee, not as the whole model. Tying revenue entirely to outcomes sounds appealing — the customer only pays when the product delivers — but attribution disputes, seasonal distortion, and forecasting risk make it unreliable as a standalone structure.

The cleanest versions tie payment to outcomes that are easy to verify: leads generated, tickets resolved, revenue recovered.

**Pros:**

- Lowers purchase risk for the customer
- Aligns your revenue with customer outcomes
- Can support higher prices when the product creates measurable value
- Works well when the outcome is concrete and easy to audit

**Cons:**

- Requires strong tracking and attribution
- Revenue can become harder to forecast
- Seasonality can distort performance results
- Disputes are likely if “success” is not defined upfront

Some payment solutions offer versions of this at the platform level ([such as Freemius](pricing.md)). Its pricing is based on progressive revenue share, starting at 4.7% for SaaS and app makers and dropping as monthly revenue grows, down to 0.5% on revenue above $100k/month.

That works because the measured outcome — successful product revenue — is concrete and auditable.

**How to make performance-based pricing work:**

- **Define the paid outcome clearly** — resolved ticket, qualified lead, recovered revenue, accepted candidate, completed workflow
- **Use a base fee plus performance component** — do not make all revenue depend on perfect attribution
- **Build reporting into the product** — both sides should be able to verify the result
- **Agree on audit rules upfront** — define what counts, what does not, and how disputes are handled

### Freemium and trials

Freemium pricing offers a free tier with limited access — capped by usage, features, or time — to let customers experience product value before committing to a paid plan.

Freemium and free trials can work for AI apps, but only when free usage is tightly capped. Every free interaction still creates inference cost, and an open-ended free tier is an inference budget you haven’t charged anyone for yet.

Unlike classic software, there is no “free” in AI: someone is always paying for the compute.

[Naveen DA](https://www.linkedin.com/in/naveenda/) learned this with ResumeGrade: students were completing their entire job search inside the free limit and never converting. The product was offering too much value **for free**.

A solution is to offer a usage-limited free trial instead. A 14-day trial with unlimited access is a 14-day free inference budget.

> “A time-limited free trial trains users to sprint. A usage-limited trial trains them to stick around.” — [Aimen Hallou](https://www.linkedin.com/in/aimen-hallou-87335216b/)

**How to design a usage-limited trial that converts:**

- **Give users enough interactions to reach a real “aha” moment** — not enough to finish the entire job for free.
- **Make the limit visible throughout the experience** — use a progress indicator, not a scary warning banner.
- **Trigger the upgrade nudge after a successful outcome** — when the user has just seen value, not only when the credits run out.
- **Use the trial to prove the paid workflow** — the free version should show the value, not replace the paid plan.

### One-time license models

One-time license pricing charges customers a single upfront fee for access to the product or a defined output — one report, one export, one audit — with no recurring charge.

One-time pricing fails for most AI apps for a simple reason: revenue happens once, but inference costs continue every time the product runs.

It works only in the narrow cases where the AI job has a clear endpoint — one report, one audit, one export — and usage is bounded at the point of sale. If the customer pays once but can keep generating forever, you have created lifetime cost exposure without lifetime revenue.

David Hunt saw this after launching a $19 lifetime add-on. Within three months, the top 5% of users were running 5,000–10,000 calls per month, wiping out 30% of revenue against a one-time payment.

**Pros:**

- Easy for customers to understand
- Good fit for single-output tools
- Can reduce purchase hesitation
- Works well when usage is capped at the point of sale

**Cons:**

- No recurring revenue to cover ongoing inference
- Power users can drain margin long after purchase
- Lifetime access creates long-term cost exposure
- Hard to reprice once customers expect unlimited use

**How to make one-time pricing work for your AI app:**

- **Define exactly what is included —** one document, one report, one audit, one export, or a fixed credit bundle
- **Avoid “unlimited use forever” unless the underlying cost is close to zero**
- **Separate lifetime access from lifetime AI usage —** the customer can keep the product, but AI processing should still have limits
- **Add paid top-ups or upgrade paths —** let customers buy more credits, reports, files, or workflows when they need them

### Hybrid pricing models

Hybrid pricing is the safest default for most AI apps: a base subscription with a defined usage allowance, plus overage billing for customers who go beyond it.

A hybrid AI pricing model has three components:

1. **The base fee** — a flat monthly or annual subscription that grants core platform access and includes a defined AI usage allowance.
2. **The usage allowance** — the included amount of interactions, tokens, API calls, or credits per billing period before overages apply.
3. **Overage billing** — per-unit charges that apply once the allowance is exhausted, priced to cover the inference costs of your heaviest users.

Most builders land here after flat pricing exposes the same problem: predictable revenue doesn’t protect margins when usage costs are left open-ended.

[Ameet Mehta](https://www.linkedin.com/in/ameetcmehta/), co-founder of [VisibilityStack](https://www.visibilitystack.ai/), moved away from flat pricing after inference costs hit 47% of revenue in month three. He moved to a hybrid model with a lower base price plus credit packs, framing credits around outcomes rather than API calls. Users understood the value exchange immediately.

**Pros:**

- Predictable base revenue with margin protection at the heavy-user end
- Customers feel the base price is fair because they are not paying upfront for usage they may never need
- Avoids the backlash that hits “unlimited” plans once limits appear later
- Lets you serve light, average, and heavy users without forcing everyone into the same economics

**Cons:**

- More complex to communicate than a flat subscription
- Too many tiers, meters, or conditions can hurt conversions
- Overages need to feel fair, not punitive

**How to structure yours:**

- Base plan covers your average user’s inference spend, with margin built in
- Usage allowance is capped around normal usage, not your heaviest users
- Overages are priced to cover costs at the top of your distribution
- Three components maximum — if your pricing page needs a calculator, simplify

## Quick answer: The best AI app pricing models in 2026

Use the table below as a shortcut to pressure-test your own product: Is usage predictable, easy to measure, naturally capped, or tied to a clear outcome? Your answer points to the pricing model most likely to fit.

The breakdown and table give you the options, but the right AI pricing model for your product depends on how it performs under real usage. Use the framework below to match your pricing model to your costs, customers, and risk tolerance.

## Choosing the right AI app pricing model: A practical framework

### Step 1: Clarify your use case and answer three questions

**Q1: How variable is my per-user inference cost?**

Wide variance between users means credits or hybrid. Consistent, predictable usage points to subscription with caps.

**Q2: How predictable is my users’ usage pattern?**

Regular and consistent suits subscription. Sporadic, binge-then-quiet suits credits.

**Q3: How sensitive is my audience to usage limits?**

You get pushback on hard caps: soft limits with transparent overages. Comfortable with explicit limits: credits or usage-based.

### Step 2: Model your AI costs and margins

Measure average and 90th percentile usage per customer. Stress-test heavy adoption — a plan that works for 50 customers may fail when usage grows.

Run two checks before you set prices:

- **Floor check:** cost per interaction × median monthly usage × 2.5x. That is your minimum. If your planned price is below it, reprice before launch.
- **Power-user check:** what does your cost look like if your top 10 users each do 10x what you planned for? This is the number that breaks flat pricing.

Aim for 60%+ gross margin after model costs, compute, and support.

### Step 3: Select and calibrate your primary pricing model

Use seat-based pricing for stable daily use, usage-based for spiky workloads, hybrid when in doubt. Annual plans with 15-25% discounts improve cash flow and reduce churn.

The model is set. The next decision is how to structure it for customers.

### Step 4: Design tiers, limits, and add-ons

Draw the line between Basic and Pro on usage, not features. What does your median user do in a month? That defines Basic. What does your top 20% do? That defines Pro.

A concrete hybrid example:

- **Basic** — 100 interactions/month, $9/month
- **Pro** — 500 interactions/month, $29/month
- **Overages** — $0.05 per interaction above the allowance

Capacity gating beats feature gating. Start with two tiers. Add a third when usage data tells you where the boundary belongs.

**Common mistakes:**

- Gating features rather than usage — “Pro gets dark mode” is not a meaningful upgrade for most AI apps
- Too many tiers — a five-plan pricing page loses conversions
- Tiers that do not reflect real usage differences — if 80% of users are on Basic and never hit the limit, the boundary is in the wrong place

### Step 5: Test, measure, and iterate

Your first AI pricing strategy is a hypothesis, not a final answer. Run it for 3–6 months, then look at how real users behave against the assumptions you made.

Track:

- **Free-to-paid conversion** — are users reaching value before they hit the limit?
- **ARPU** — are customers paying enough to support the usage they create?
- **Gross margin after AI costs** — are model/API costs leaving enough room for support, product, and growth?
- **Churn by plan** — are specific tiers attracting the wrong users or creating surprise costs?
- **Upgrade rate after usage limits** — do limits encourage expansion, or do they feel like punishment?
- **Heavy-user concentration** — what percentage of users drives most of your inference costs?

Adjust usage levers before base price: caps, overages, fair-use limits, and included usage are easier to tune without disrupting the whole pricing page.

Change one variable at a time. If you adjust price, limits, overages, and trial rules together, you won’t know what worked.

Pricing gets easier once real usage data arrives. The costly mistakes usually happen earlier, when founders price for the average user and forget about the power users.

## Worked example: Pricing a new AI app in 2026

**Product:** An AI race-fueling planner for endurance runners that turns race distance, elevation, target pace, body weight, sweat rate, food preferences, and gut tolerance into a personalized fueling plan.

**Assumptions:**

- Median user creates 8 fueling plans or plan revisions per month
- Average blended model cost: $0.018 per plan/revision
- Raw inference cost: $0.14/month per median user
- With a 2.5x buffer: $0.36/month cost floor

In this example, a “plan/revision” means one meaningful AI action: generating a race-day fueling plan, adjusting it after a long run, or recalculating it for a different event. The real cost depends on input length, output length, model choice, retries, and any background calls.

- $7/month includes **20 plans or revisions**
- $0.25 per plan/revision above the allowance

Median user: **8 plans/revisions = $7 revenue vs ~$0.36 buffered cost floor**  
Power user: **80 plans/revisions = $22 revenue vs ~$3.60 buffered inference cost**

That structure keeps the base plan approachable for casual runners while making heavy usage pay for itself. For the first 90 days, monitor cost per plan, heavy-user concentration, upgrade rate, and overage usage. Adjust caps or overages before changing the base price.

Once the pricing logic is set, your billing stack has to turn it into something the product can track, enforce, and charge for. That leaves one practical question: build the billing layer yourself, or use a platform that already handles it?

## Choosing the right billing setup for your AI app pricing model

Your pricing model needs a billing setup that can handle the details behind it: subscriptions, credits, usage limits, trials, invoices, taxes, upgrades, downgrades, and customer self-service.

Common options include:

- **Direct payment processors** like Stripe, where you accept payments but build much of the AI-specific billing logic yourself
- **Merchant of Record platforms** like [Freemius](merchant-of-record.md) or Paddle, where payments, tax, invoicing, and compliance are handled through a managed selling layer
- **Built-in payment tools** like Lovable Payments, which can suit simple AI apps that need to start charging quickly inside their existing app-building platform

For a deeper comparison, see our guide to the [best payment solutions for AI-built apps](blog-best-payment-solutions-ai-built-apps.md), which breaks down when to use Freemius, Stripe, Paddle, Lovable Payments, and other options based on your app’s stage, pricing complexity, tax needs, and how much billing infrastructure you want to manage yourself.

## Sustainable AI app pricing: Build pricing that survives real usage and helps you scale

AI pricing will keep shifting as model costs change, new tools emerge, and customers get more comfortable with credits, usage limits, and hybrid pricing.

The goal is not to pick the perfect model forever. It is to choose one you can measure, explain, and adjust as usage data comes in.

Start with your cost floor, add clear usage limits, and keep the customer-facing value simple. If the numbers change later, be transparent. Show your math, give customers time to adjust, and avoid turning repricing into a trust problem.

If you need help choosing the right AI pricing model for your app, [get in touch with the Freemius team](pricing.md) and we’ll help you evaluate your pricing, margins, and usage structure before inference costs start eating into growth.

## FAQs

### What pricing model should I use for my AI app?

For most AI apps, the safest pricing model is hybrid: a base subscription with a usage allowance, plus overages or credit top-ups when customers go beyond it. It gives customers predictable access while protecting you from heavy-user inference costs.

### Why is AI app pricing different from SaaS pricing?

AI app pricing is different because every user action can create a direct compute cost. Every prompt, generation, document, image, or workflow can trigger another model/API bill, so pricing has to account for usage variance and heavy users, not just perceived value.

### What are inference costs in AI pricing?

Inference costs are the per-use fees charged when your AI app calls a model to process a prompt, image, file, document, or workflow. These costs usually depend on model choice, input size, output size, and the number of calls your app makes.

### Why is unlimited AI usage risky?

Unlimited AI usage is risky because revenue stays fixed while usage costs can keep rising. One heavy user on an uncapped plan can consume far more inference than dozens of light users, which is why “unlimited” needs caps, fair-use rules, or strong usage data behind it.

### Is freemium viable for AI apps?

Freemium can work for AI apps, but only when free usage is tightly limited. The free tier should help users reach an “aha” moment, not let them complete the entire job without paying. Usage-limited trials are usually safer than open-ended free plans.

### Should AI apps charge by tokens?

Most AI apps should not charge customers directly by tokens unless the audience is technical. Tokens are useful for internal cost modeling, but customers usually understand outcomes better: credits, documents processed, images generated, minutes transcribed, reports created, or workflows completed.

### When should I use credit-based pricing for an AI app?

Use credit-based pricing when usage is variable, bursty, or project-based. It works especially well for developer tools, API-based products, builder audiences, creative tools, and apps with multiple action types — as long as credits are translated into clear outcomes.

### When should I use usage-based pricing for an AI app?

Use usage-based pricing when the billing unit is obvious, measurable, and easy for customers to control, such as transcription minutes, images generated, API calls, documents processed, reports created, or workflow runs. It works best with real-time usage tracking, alerts, and spending caps.

### Are one-time licenses a good pricing model for AI apps?

One-time licenses are usually risky for AI apps with ongoing usage because revenue happens once while inference costs continue. They can work for finite AI jobs: one report, one document review, one audit, one export, or a fixed credit bundle.

### How do I calculate my AI app pricing floor?

Your pricing floor is the minimum your pricing needs to cover before margin, support, growth, and product investment. Use: **cost per interaction × expected monthly usage per customer × buffer for variance and heavy users**. A 2.5x buffer is a practical starting point.

### Do I need a Merchant of Record to sell an AI app?

You do not strictly need a Merchant of Record to sell an AI app, but it can make global pricing and billing much easier. A Merchant of Record handles the legal side of the sale, including applicable VAT, sales tax, invoices, payments, refunds, and compliance. For AI app makers selling internationally, an MoR like [Freemius](merchant-of-record.md) can reduce the operational burden so you can focus on pricing, usage limits, and product growth instead of tax workflows.