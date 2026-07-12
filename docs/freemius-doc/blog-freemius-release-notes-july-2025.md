Big, sustainable growth often starts with small, consistent improvements, and July’s updates are full of them.

From localized checkouts and clearer webhook payloads to better support transparency and smarter pricing defaults, this month’s updates focus on removing friction where it counts.

The improvements are not just cosmetic. They’re designed to reduce support requests, improve buyer clarity, and give you more control over how your product is sold, scaled, and supported.

Let’s take a look at what’s new:

## Payouts, Prepped: Earnings, Invoices, and Peace of Mind

We’ve upgraded our payout process to give you more clarity *before* the money hits your account.

Starting this month, makers will receive a [scheduled payout email](blog-changelog-new-feature-monthly-scheduled-payout-email-with-pro-forma-invoice.md) on the 1st of each month, summarizing their expected earnings, along with a downloadable [pro forma invoice](blog-freemius-release-notes-april-2025.md#proforma_invoices_proof_before_the_payout_coming_very_soon) issued by us on your behalf.

[![Scheduled payout email sample](https://freemius.com/blog/wp-content/uploads/2025/08/scheduled-payout-email-sample.png)](https://freemius.com/blog/wp-content/uploads/2025/08/scheduled-payout-email-sample.png)

Why this matters:

- **More visibility:** You’ll know what to expect before payouts are processed (typically by the 10th).
- **Fewer surprises:** The email now includes destination details like PayPal or bank wire info, so you can flag any issues in advance.
- **Bank-friendly documentation:** In some regions, large inbound transfers from abroad may trigger account freezes or delays. The pro forma invoice acts as proof of expected payment, helping you unblock or pre-clear funds with your bank.
- **Supports compliance workflows:** Need to explain a cross-border transaction to a platform like Wise? The pro forma invoice makes it easier **(see image below).**

[![Sample paid invoice](https://freemius.com/blog/wp-content/uploads/2025/08/sample-paid-invoice.png)](https://freemius.com/blog/wp-content/uploads/2025/08/sample-paid-invoice.png)

Once the payout is completed, you’ll receive a follow-up email with the updated information and a link to the finalized [paid invoice](blog-changelog-new-feature-reverse-invoices-for-your-payouts.md).

## Milestones, Made to Share: Polished Emails That Celebrate Your Wins

From your first sale to your hundredth (and beyond!), our milestone emails now look sharper, read better, and feature built-in ways to share your journey publicly.

[![Sample milestone email](https://freemius.com/blog/wp-content/uploads/2025/08/sample-milestone-email.png)](https://freemius.com/blog/wp-content/uploads/2025/08/sample-milestone-email.png)

When you hit key milestones, [you’ll get more than a congratulatory message](blog-changelog-announcing-the-new-look-for-freemius-milestone-emails.md):

You’ll get a tailored mix of growth tips, feature suggestions, and — at your 1st and 100th sale — a one-click tweet button to share your win on X, with each post adding to a growing thread of makers celebrating their progress and inspiring others.

> 100 sales = proof you built something people actually want 🔥
> 
> Do you still catch yourself smiling at every “new sale” notification? 😊
> 
> Looking back, what would you tell yourself before sale #1?
> 
> Share it on the 🧵 [pic.twitter.com/iHpZ224QPi](https://t.co/iHpZ224QPi)
> 
> — Freemius (@freemius) [July 25, 2025](https://twitter.com/freemius/status/1948703636436988408?ref_src=twsrc%5Etfw)

## One-Time Discounts for Migrated Customers

Freemius has seen a surge in migrations in recent months. With that growth, we’ve discovered new patterns in subscription transitions.

**One common migration challenge:** we advise makers not to cancel legacy customer subscriptions for the previous payment platform to avoid churn. Even so, most makers still want to transition customers gradually over to Freemius.

To bridge that gap, we’ve introduced a [one-time discount to migrated customers](blog-changelog-one-time-discount-support-for-migrated-subscriptions.md) that applies exclusively to their first payment when re-subscribing through Freemius.

**Note:** The new discount applies **only to the first payment collected by Freemius**, not to renewals (there’s another simple option for that).

[![Freemius Checkout with the one-time discounts for migrated customers](https://freemius.com/blog/wp-content/uploads/2025/08/freemius-checkout-with-the-one-time-discounts-for-migrated-customers.png)](https://freemius.com/blog/wp-content/uploads/2025/08/freemius-checkout-with-the-one-time-discounts-for-migrated-customers.png)

**Bonus:** Customers will receive the usual proration discount **and** the new one-time discount, making the switch to Freemius more appealing for them and beneficial for you.

[![Freemius Checkout with migrated payment coupon applied](https://freemius.com/blog/wp-content/uploads/2025/08/freemius-checkout-with-migrated-payment-coupon-applied.png)](https://freemius.com/blog/wp-content/uploads/2025/08/freemius-checkout-with-migrated-payment-coupon-applied.png)

Freemius Checkout with migrated payment coupon applied

To avoid stacking discounts, the one-time coupon is calculated **only on the non-prorated portion** of the billing period. If a renewal discount is also set, customers will see a tooltip in the UI explaining how both discounts are applied:

[![Freemius Checkout tooltip explaining how the discounts are applied](https://freemius.com/blog/wp-content/uploads/2025/08/freemius-checkout-tooltip-explaining-how-the-discounts-are-applied.png)](https://freemius.com/blog/wp-content/uploads/2025/08/freemius-checkout-tooltip-explaining-how-the-discounts-are-applied.png)

Everything works seamlessly, even with imported subscription history, so you can encourage re-subscriptions through Freemius without permanently lowering your price, all while supporting a phased, churn-conscious migration strategy.

## Even More iDEAL: Now for Payment Method Updates Too

iDEAL, the most popular Dutch payment method, has been [supported in Checkout since May](blog-freemius-release-notes-may-2025.md#going_dutch_ideal_checkout_is_live). Now, it also works for [updating payment methods](blog-changelog-enhancements-to-ideal-support-in-freemius-checkout.md).

This means users can switch from credit card to iDEAL or from one iDEAL account to another via the Customer Portal.

[![Freemius Checkout showing how to switch payment methods including iDEAL](https://freemius.com/blog/wp-content/uploads/2025/08/freemius-checkout-showing-how-to-switch-payment-methods-including-ideal.png)](https://freemius.com/blog/wp-content/uploads/2025/08/freemius-checkout-showing-how-to-switch-payment-methods-including-ideal.png)

These updates also resolve edge cases with license renewals and improve error handling during interrupted payments. And in a digitally mature, flourishing economy like the Netherlands, that means fewer failed payments, fewer support tickets, more sales, and a much smoother experience for you and your customers.

## Built for SaaS: Ongoing Improvements That Keep You Building Better

As more SaaS and app makers join the Freemius platform, we’re getting valuable feedback on everything from onboarding to integration flows — and using those insights to continuously improve the experience.

### In-App Subscription Control

New API endpoints let software makers access data and cancel subscriptions directly from a license. This is especially useful for SaaS products where the preference is to manage subscriptions in-app rather than redirecting users to an external customer portal.

The new API endpoints:

- **Eliminate ambiguity** by automatically fetching the correct subscription when multiple subscriptions exist for a license (e.g., due to upgrades or billing changes)
- **Improve user control** through smooth cancellation flows directly in your SaaS, while still using Freemius for enforcement and fulfillment

A smoother dev experience, and a more cohesive experience for your users.

### A Sharper Setup Flow: Faster Starts for SaaS and Apps

We’ve fine-tuned the **Setup Checklist** to [improve the onboarding flow for SaaS and app products](blog-changelog-improved-onboarding-experience-for-saas-app-creators.md).

Based on maker feedback, we updated the step order, added missing items, and restructured the checklist to better guide you through product setup.

[![Setup checklist for SaaS and Apps](https://freemius.com/blog/wp-content/uploads/2025/08/setup-checklist-for-saas-and-apps.png)](https://freemius.com/blog/wp-content/uploads/2025/08/setup-checklist-for-saas-and-apps.png)

We’ve also added direct links to the [integration guide](https://freemius.com/help/documentation/setup-for-saas/saas-integration/) and [webhook setup hints](https://freemius.com/help/documentation/setup-for-saas/events-webhooks/) so you can dive into technical implementation when you’re ready.

[![Developer Dashaboard sidebar section highlighting the Setup Checklist](https://freemius.com/blog/wp-content/uploads/2025/08/developer-dashaboard-sidebar-section-highlighting-the-setup-checklist.png)](https://freemius.com/blog/wp-content/uploads/2025/08/developer-dashaboard-sidebar-section-highlighting-the-setup-checklist.png)

The checklist is always accessible from the sidebar, making it easy to revisit no matter where you are in the Developer Dashboard.

That said, we know visibility could be improved.

Right now, it’s easy to lose track of the checklist after clicking away, especially on larger screens where the button can be hard to spot. We’re working on improving that too, with a clearer, more persistent flow to help you stay focused on what’s next in product creation.

### Custom Unit Labels Now Show Correctly in the Customer Portal

Whether it’s sites, seats, credits, or any other entitlement, the [Customer Portal](customer-portal.md) now consistently displays the [correct license unit labels](blog-changelog-consistent-selling-unit-labels-across-customer-portal.md) at all UI touchpoints.

[![Customer Portal section showing correct license unit labels](https://freemius.com/blog/wp-content/uploads/2025/08/customer-portal-section-showing-correct-license-unit-labels.png)](https://freemius.com/blog/wp-content/uploads/2025/08/customer-portal-section-showing-correct-license-unit-labels.png)

You’ll primarily notice this improvement in the Upgrade/Downgrade flows of the **Licenses** and **Renewals & Billing** sections.

Buyers will clearly see the specific license unit they’ve purchased, with a [consistent and accurate label](help-documentation-saas-customize-license-unit-label.md) guiding them through the upgrade experience:

[![Customer Portal's Renewals & Billing section showing how to upgrade plan](https://freemius.com/blog/wp-content/uploads/2025/08/customer-portals-renewals-and-billing-section-showing-how-to-upgrade-plan.png)](https://freemius.com/blog/wp-content/uploads/2025/08/customer-portals-renewals-and-billing-section-showing-how-to-upgrade-plan.png)

This simple but important fix improves clarity for your users, reduces confusion around what they’ve purchased, and helps keep your product experience consistent and trustworthy.

## Enhanced Webhook Payloads for Product Deployment Events

Whether you’re releasing to all users, rolling out a beta, or gradually increasing rollout to a percentage of users, webhook payloads for deployments now include deeper details to support custom automations.

Specifically, [webhooks include](blog-changelog-enhanced-webhook-payloads-for-wordpress-products-deployment-events.md):

- File name
- Version number
- Release mode (unreleased, beta, released, incremental)

These improvements unlock more accurate automation triggers, like sending update notifications only when a version is officially released. Makers will also know exactly which build stage they’re working on, keeping systems in sync, users in the loop, and ensuring far fewer release surprises.

## Reducing Confusion in the Customer Portal’s Support Form

The Customer Portal includes a built-in form where users can choose a topic and submit a support ticket. These messages are routed directly to **you**, the maker — not to the Freemius team.

Previously, however, the confirmation message read something like:

*“Your message has been successfully sent to *our* support. We’ll get back to you as soon as possible.”*

That vague phrasing caused confusion, especially when users accessed the portal via [freemius.com](). Some users assumed they were contacting Freemius support directly.

To clear up that misunderstanding and better set expectations, [the confirmation message has been updated to include](blog-changelog-improved-support-contact-success-message-in-customer-portal.md):

- The **product name** the message is associated with
- The **exact email address** the message is sent to

[![Updated support form confirmation message in Customer Portal](https://freemius.com/blog/wp-content/uploads/2025/08/updated-support-form-confirmation-message-in-customer-portal.png)](https://freemius.com/blog/wp-content/uploads/2025/08/updated-support-form-confirmation-message-in-customer-portal.png)

Clearer for users, safer for your support reputation, and no confusion about who’s expected to reply.

## Your Pricing, Polished: Smarter Plan Setup for a Cleaner, Quicker Start

A few small tweaks make plan setup and pricing more intuitive, especially for SaaS and app makers:

### Simplifying New Plan Creation

- **Plan creation flow:** The order of inputs has been updated. You’ll now enter the **title first**, followed by the **unique name**, which is auto-generated from the title (e.g., “Business” → `business`). This saves time and clicks during plan creation.

<!--THE END-->

[![Updated plan creation flow in the Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2025/08/updated-plan-creation-flow-in-the-developer-dashboard.png)](https://freemius.com/blog/wp-content/uploads/2025/08/updated-plan-creation-flow-in-the-developer-dashboard.png)

- **Pricing configuration clarity:**
  
  - We’ve added a **“Pricing (US Dollars)”** header to better reflect the default currency and align with how other currencies are labeled (e.g., “Pricing (Euro)”). Previously, some users couldn’t immediately tell where their USD pricing was if they’d added additional currencies.
  - For **SaaS and app products**, what was previously labeled “Lifetime” is now correctly shown as **“One-off”** pricing. This better reflects real-world use cases like one-time API credit bundles or fixed data packages, without implying ongoing lifetime access, which is rare in SaaS.
  - For non‑WordPress product types, the **Description field** has been removed from the plan form to reduce clutter and confusion.

[![Plan creation section showing pricing configuration](https://freemius.com/blog/wp-content/uploads/2025/08/plan-creation-section-showing-pricing-configuration.png)](https://freemius.com/blog/wp-content/uploads/2025/08/plan-creation-section-showing-pricing-configuration.png)

## Numbers Now Localized in Checkout

Another meaningful stride toward a more globally intuitive experience: numbers now follow the [buyer’s selected locale at Checkout](blog-changelog-full-locale-support-in-checkout-numbers-currencies-now-localized.md), including within the cart and final review steps.

[![Freemius Checkout showing buyer's numeric format preference](https://freemius.com/blog/wp-content/uploads/2025/08/freemius-checkout-showing-buyers-numeric-format-preference.png)](https://freemius.com/blog/wp-content/uploads/2025/08/freemius-checkout-showing-buyers-numeric-format-preference.png)

Depending on the region, large numbers may use **commas** or **periods** differently — e.g., **1,000.50** in the US vs. **1.000,50** in much of Europe. Our checkout now detects the user’s locale and adapts to both language and numeric format preferences. Not just one or the other.

[![Freemius Checkout adapting to user's locale language](https://freemius.com/blog/wp-content/uploads/2025/08/freemius-checkout-adapting-to-users-locale-language.png)](https://freemius.com/blog/wp-content/uploads/2025/08/freemius-checkout-adapting-to-users-locale-language.png)

This enhancement makes transactions easier to parse and delivers a seamless, native, and familiar experience for buyers, helping you drive more conversions, no matter where your customers are.

## Fixes That Fly Under the Radar (But You’ll Feel the Difference)

Not all improvements need fireworks. These small fixes tidy up the corners of Freemius by squashing bugs, improving clarity, and smoothing out little snags that make a big difference over time.

**Checkout and Billing:**

- [Cart recovery coupons now respect all rule settings](blog-changelog-cart-recovery-coupons-now-respect-your-coupon-rules.md)
- [Fixed legal text alignment issue](blog-changelog-checkout-minor-ui-fix-alignment-of-the-legal-text.md)
- [Billing cycle selector now handles inconsistent plan data gracefully](blog-changelog-billing-cycle-selector-now-handles-plan-inconsistencies-gracefully.md)

**Customer Portal:**

- [Cart recovery no longer triggers during troubleshooting](blog-changelog-log-in-as-user-now-safer-for-debugging-without-triggering-cart-recovery.md)
- [Fixed unintended subscription cancellation when closing the cancel dialog](blog-changelog-fixed-unintended-subscription-cancellation-triggered-by-closing-dialog-in-customer-portal.md)

**Developer Dashboard:**

- [Smoothed out UI glitch when adding new team members](blog-changelog-fixed-ui-glitch-of-add-new-team-member-component.md)

**Deployment:**

- [Fixed incorrect version returned when using incremental releases](blog-changelog-deployment-api-fixed-incorrect-version-returned-for-latest-tag.md)
- [Deployment endpoints now behave reliably under all conditions](blog-changelog-deployment-endpoints-bug-resolved.md)

## Another Month, Another Leap Forward

That’s a wrap for July.

From behind-the-scenes bug fixes to workflow-enhancing updates, each change helps make Freemius more reliable, scalable, and intuitive for you — and more seamless for your customers.

Got feedback or a feature request? [DM us](https://x.com/freemius) or [reach out](https://freemius.com/cdn-cgi/l/email-protection#284b47465c494b5c684e5a4d4d45415d5b064b4745): we’re always listening.