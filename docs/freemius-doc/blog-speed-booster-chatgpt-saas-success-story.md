For the better part of a decade, Bram van der Giessen worked on software where performance problems have nowhere to hide.

Most recently, that meant streaming: keeping video running smoothly across devices, browsers, and old set-top boxes that many people still rely on.

Earlier this year, Bram stepped out on his own to build something for himself. It wasn’t long before that same instinct for spotting performance issues followed him somewhere unexpected: his ChatGPT window.

The longer a conversation ran, the more the browser struggled. For someone used to chasing performance issues for a living, it was hard to leave alone.

His solution became [Speed Booster for ChatGPT](http://gptspeedbooster.com): a browser extension that started by making long ChatGPT conversations usable again. It has since grown to 60,000 users and is evolving into a comprehensive AI productivity toolkit running as a paid product using Freemius, with licensing, payments, and global tax compliance handled in the background.

## The problem hiding in plain sight

What Bram found in the browser console was surprisingly straightforward.

Whenever someone sent a new prompt, the browser re-rendered the entire conversation instead of just handling the latest message. Ten messages in, that’s barely noticeable. Sixty messages in, the browser is dragging a growing mountain of content behind every new prompt.

> Even on my modern MacBook it would be slow… but on older hardware, it was almost unusable.

Since it was a browser-side problem, Bram could do something about it.

## Turning a script-sized idea into something people could use

Before building anything, Bram did some digging to see if someone had already solved it.

Reddit threads and developer forums showed he wasn’t the only one running into the problem. Other users had traced the slowdown to the same rendering issue, and a few had shared scripts to work around it.

But scripts only help the people comfortable running them.

Bram saw room for something simpler: a fix people could install through a trusted browser store and use without thinking about the technical side.

So he built a [Chrome](https://chromewebstore.google.com/detail/finipiejpmpccemiedioehhpgcafnndo?utm_source=item-share-fms) and Firefox extension — also available on Edge and other Chromium-based browsers — that improved the ChatGPT experience without asking users to fiddle with scripts, settings, or technical workarounds.

He launched it free, assuming it was a small utility for a specific kind of power user.

> I never thought this many people would be looking for a solution to this issue. I just thought it was a little tool.

Bram was happy to be proven wrong.

In roughly two months, Speed Booster had passed 10,000 installs. Even more telling: many of those users were coming back every day.

[![Speed Booster for ChatGPT user reviews in Freemius SaaS success story article](https://freemius.com/blog/wp-content/uploads/2026/06/speed-booster-for-chatgpt-user-reviews-in-freemius-saas-success-story-article.png)](https://freemius.com/blog/wp-content/uploads/2026/06/speed-booster-for-chatgpt-user-reviews-in-freemius-saas-success-story-article.png)

## Shipping fast, then listening closely

The first version worked, but it wasn’t the full fix yet.

It improved how messages were rendered, but older messages were still sitting in memory, hidden from view, and not fully unloaded. On a newer machine, that made a difference. On older hardware, it still wasn’t enough to alleviate the lag.

And users told Bram as much.

So he went back in and rebuilt the core behavior. Speed Booster stopped keeping the whole conversation loaded and rendered only the most recent messages by default. Users could still scroll back and load older messages when needed, and configure how much of the conversation stayed visible.

For people working inside long ChatGPT threads every day, especially on older machines, the difference was immediate.

### [![](https://freemius.com/blog/wp-content/uploads/2026/06/word-image.png)](https://freemius.com/blog/wp-content/uploads/2026/06/word-image.png)

### The catch with building inside another product

Browser extensions live in someone else’s house. That means every ChatGPT update can move the furniture.

Since launching Speed Booster, Bram has had to respond to platform changes that affect how his extension works.

A layout update might move something the extension relies on. A renamed UI element can break an assumption in the code. Even a small ChatGPT change can create an edge case Bram has to track down.

His support channel became an early warning system.

Users would email him when something changed — sometimes before Bram had even received the same ChatGPT update himself. Those messages also surfaced stranger cases: conversations in Chinese or Russian, branched threads, coding sessions with unusual tokens, and workflows he hadn’t originally accounted for.

Each one helped him make the product sturdier and changed how he thinks about building.

Bram is a self-described perfectionist. But Speed Booster for ChatGPT taught him the lesson most solo builders eventually have to learn the uncomfortable way:

Ship the simplest, most useful version, get it into real hands, and let feedback show you what matters.

## Turning a free tool into a paid product (without burning early users)

A few months in, the “small free tool” was taking up hours of Bram’s day. It had long since stopped being a side project in any meaningful sense.

If Bram wanted to keep supporting Speed Booster, he needed a way to make the time sustainable without shutting casual users out.

That led him to a freemium setup: the extension would stay free for lighter use, while people relying on it every day could unlock Pro with a small one-time payment.

He landed on $7.99 deliberately. Subscriptions make sense for many products, but at this stage, Speed Booster was still a focused utility solving one painful problem. A one-time payment felt simpler, fairer, and easier for users to say yes to.

The bigger question was what to do about the 10,000 people who’d been using it for free from the start.

> *Even if 1% of them were unhappy and left a bad review, the whole thing would collapse. So I grandfathered everyone in — ‘you have it for free, you don’t need to worry, I’ll make you a Pro user right away… permanently, and for free.’*

The response from the community was overwhelmingly positive — instead of feeling punished for being early, users felt recognised and appreciated.

[![Speed Booster for ChatGPT user reviews in Freemius SaaS success story article](https://freemius.com/blog/wp-content/uploads/2026/06/speed-booster-for-chatgpt-user-reviews-in-freemius-saas-success-story-article-1.png)](https://freemius.com/blog/wp-content/uploads/2026/06/speed-booster-for-chatgpt-user-reviews-in-freemius-saas-success-story-article-1.png)

## The two-week search for the right monetization layer

Once Bram knew he wanted to charge for Pro, the next question was how to do it without adding friction for users or extra admin for himself.

Checkout, licensing, activation, refunds, and tax handling all had to work cleanly in the background. Otherwise, he wasn’t just selling Speed Booster — he was signing up to build and support the whole commercial layer around it.

Finding the right setup took nearly two weeks, almost as long as he’d spent building the extension itself.

He tried several options first:

- [**Lemon Squeezy**](lemon-squeezy-alternative.md) came closest. It had a clean checkout, plenty of features, and licensing, but support was too slow for Bram’s needs. When he had questions, replies could take more than a week.
- [**Gumroad**](blog-best-gumroad-alternatives-free-paid.md) didn’t match the experience he wanted. Bram found the checkout unprofessional, the costs high, and the licensing setup too basic — essentially an uploaded file of license keys.
- **[Stripe](blog-stripe-transaction-fees-real-cost.md) and PayPal** were possible direct integrations, but once Bram read into global tax compliance, VAT, payment processing, and refunds, he wasn’t convinced they made sense for a solo developer selling globally.
- **Other tools** were part of the search, but he couldn’t find the combination he was looking for: frictionless checkout, licensing he wouldn’t have to manage himself, responsive support, and help with the messy operational layer around global software sales.

Then he found Freemius.

Freemius had the pieces Bram had been trying to line up separately: a proper [licensing system](software-licensing.md), [merchant of record coverage](merchant-of-record.md), [global tax handling](https://freemius.com/tax-compliance/), refunds, APIs, webhooks, and enough flexibility to build the frictionless activation flow he wanted.

The support response is what turned that technical fit into an easy decision. When Bram reached out, he says Freemius got back to him within 24 hours. After testing tools where support felt slow or distant, that was important.

## The commercial layer that let Bram keep building

For Speed Booster Pro, Bram wanted the paid upgrade to feel as simple as the extension itself.

Freemius’ APIs and webhooks let him build what he describes as a “magic” activation flow. When someone buys Pro, Freemius sends a webhook to Bram’s external application layer, which immediately generates a personalized onboarding email with detailed activation instructions and a single button.

> The person only has to click the activation button in the email — it goes back to Freemius to verify the license, and then it automatically activates everything. No copying and pasting license keys. Nothing like that.

Without that manual license-key step, activation-related support tickets have dropped to practically zero.

The Freemius [Developer Dashboard](help-documentation-getting-started-explore-the-developer-dashboard.md) also became part of his support workflow.

When someone writes in with a license issue, Bram looks them up, checks their activations, and solves the problem quickly. If a user has gone out of their way to help debug something tricky, he’s able to give them a few extra activations as a thank-you.

For a one-person operation, those small operational shortcuts add up.

The same was true for the bigger admin work around selling globally.

### The tax problem he didn’t want to own

Before choosing a [merchant of record](merchant-of-record.md), Bram looked at integrating directly with Stripe or PayPal. But once he started researching VAT, sales tax, registrations, filing obligations, refunds, and payment processing rules, the “simple” route looked anything but.

For a solo developer, direct payments would have meant owning another layer of admin. With Freemius acting as merchant of record, payments, tax handling, refunds, and compliance are handled in the background with the rest of the commercial layer.

Bram’s view is straightforward: because Freemius uses a [progressive rev-share pricing model](pricing.md), the cost scales with the product. If you’re not making money, you’re not carrying a big upfront platform cost. And if you are, the time saved on tax, payments, refunds, and admin is worth the fee.

## When a copycat crossed the line

A few months after launch, Bram was doing what many product builders do every so often: checking the competitive landscape.

He found another browser extension that looked familiar. Very familiar.

The layout and features closely matched Speed Booster. When he looked under the hood, Bram says roughly 90% of the code had been copied directly. The main change was that the copycat had swapped out the Freemius licensing API URL for their own before trying to sell it.

Competitors don’t bother Bram. In fact, he sees new tools appearing in the space as a sign that the problem is real.

But direct copying is different.

Fortunately, Bram had thought ahead and embedded small fingerprints in his code — subtle identifiers that could help prove authorship if someone copied his work.

He sent the evidence to Freemius. The team quickly investigated, terminated the copycat’s account, and stopped them from selling the product or any derivatives through Freemius.

> I got a reply from Freemius CEO Vova Feldman within 24 hours. After a couple of days they’d concluded their investigation. That gave me a lot of reassurance that Freemius takes this seriously and they want to protect the people they work with.

## From lag fix to AI productivity toolkit

As Speed Booster grows, Bram is seeing a different kind of message in his inbox.

At first, most emails were about fixing things: edge cases, platform changes, broken behavior, and performance issues on specific setups.

But once the core lag problem was under control, users started asking for more practical workflow features. They weren’t only trying to make ChatGPT faster anymore but also trying to make their AI work easier to manage.

One request keeps coming up: folders.

For users with dozens of chats spread across projects, clients, research threads, and coding sessions, ChatGPT’s native sidebar feels crowded. They want a way to group conversations into folders and subfolders, then find them again without scrolling through a long list of titles.

Exports are coming up too. Users want to save conversations as PDF, Markdown, or plain text, whether for archiving, sharing, documentation, or moving useful work into another tool.

[![](https://freemius.com/blog/wp-content/uploads/2026/06/word-image-1.png)](https://freemius.com/blog/wp-content/uploads/2026/06/word-image-1.png)

Bram is also looking at improved search — including search inside message content — and potential support for other LLMs like Claude, Gemini, and Grok.

> *I’m excited about where Speed Booster is going next. Thousands of professionals originally found it because they were searching for a way to make ChatGPT faster, but the feedback I’m getting now goes beyond performance.*
> 
> *People want better ways to manage their AI work. That’s why Speed Booster for ChatGPT is evolving from a performance fix into a broader ChatGPT productivity toolkit.*
> 
> *My goal is to give power users a better workspace for ChatGPT, and to keep building it with the community. Every user can share feedback, shape the roadmap, and follow what’s next at* [*gptspeedbooster.com*](http://gptspeedbooster.com)*.*

## [![](https://freemius.com/blog/wp-content/uploads/2026/06/word-image-2.png)](https://freemius.com/blog/wp-content/uploads/2026/06/word-image-2.png)

## One developer, one problem, 60,000 users later

Speed Booster for ChatGPT is still a one-person operation. Bram answers the support emails, watches for ChatGPT changes, ships the updates, and turns user requests into new features.

Even as the product grows, it still has the feel of something built close to the problem: practical, responsive, and shaped by the people using it.

For other developers sitting on an idea they haven’t shipped yet, Bram’s advice is simple: start with the basic version, validate it quickly, get real feedback early, and listen closely once it starts coming in.

He knows that’s easier said than done. As a perfectionist, he had to fight the urge to keep polishing in private. Speed Booster taught him that waiting until something is perfect can become another way of never finding out if people need it.

There’s another lesson in the story too: choose your foundation carefully.

Payments, licensing, activation, tax compliance, refunds, IP protection — all the machinery around a product can become a product of its own if you let it.

For Bram, finding the right supporting infrastructure with Freemius meant he could keep investing time where it mattered: improving Speed Booster and supporting the 60,000 people who rely on it.

[*Speed Booster for ChatGPT*](https://gptspeedbooster.com/) *is free to install, with a Pro upgrade available, for* [*Chrome*](https://chromewebstore.google.com/detail/speed-booster-for-chatgpt/ggpkgkdedgpcnoadmpmfmckhnmggalml) *and Firefox. Freemius readers get an exclusive 20% discount on Speed Booster Pro using the code FREEMIUS20 at checkout.*