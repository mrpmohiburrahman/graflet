Freemius is built for momentum so your software can ship faster, adapt smarter, and scale without friction.

This release brings back high-impact features (hello there, billing cycle selector), unlocks smoother upgrade flows for SaaS, introduces automated reverse invoices to take the edge off admin, and quietly delivers a 30% speed boost to the mobile app.

**Focused improvements, shaped by your feedback. Tangible impact for your products.**

Here’s what’s new:

## No More Manual Invoicing for Payouts. Seriously.

As the [merchant of record](freemius-for-saas.md#:~:text=What%20separates%20Freemius%0Afrom%20other%20merchants%20of%20record%3F), Freemius is essentially a reseller of your software and is officially your sole customer.

This setup used to mean that makers had to issue payout invoices as proof of funds.

That extra admin? Consider it gone.

We now [automatically generate payout invoices](blog-changelog-new-feature-reverse-invoices-for-your-payouts.md) on your behalf — formatted exactly as if you’d issued them yourself, just without the manual lift.

[![Automatically generated payout reverse invoices by Freemius](https://freemius.com/blog/wp-content/uploads/2025/04/automatically-generated-payout-reverse-invoices-by-freemius.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/04/automatically-generated-payout-reverse-invoices-by-freemius.jpeg)

You’ll find these ready-to-go documents in:

- The **payout confirmation emails**, and
- The **Earnings page** in your Developer Dashboard

[![Payout reverse invoices in the Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2025/04/payout-reverse-invoices-in-the-freemius-developer-dashboard.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/04/payout-reverse-invoices-in-the-freemius-developer-dashboard.jpeg)

But we didn’t stop there…

### Proforma Invoices: Proof Before the Payout (*Coming Very Soon!*)

Because no maker wants to be mistaken for a money launderer, we’re rolling out **proforma invoices**: official documents sent *before* a payout lands in your account.

They give you an early estimate of how much to expect, and are perfect for:

- avoiding compliance delays and fraud flags.
- satisfying source-of-funds requests from banks.
- keeping your accountant happy.

You’ll get them automatically in a dedicated email once your next payout is calculated. No requests, no chasing paperwork. Just everything you need, before you need it.

**⚠️ Heads up:** Both **proforma** and **final payout invoices** are only available if you’ve completed your **billing information** in Freemius. It’s optional for now, but will soon be required for legal and financial compliance — so if you haven’t filled it in, now’s a good time.

## Block Duplicate Subscriptions With a Simple Toggle

**Picture this:** a user upgrades their plan, but thanks to a bug, a spotty connection, or a delayed webhook, the upgrade doesn’t show right away.

They assume something went wrong. There’s no charge in their bank account yet. So… they try again.

Suddenly, they’ve paid twice — or more — for the same product.

That’s stressful for them. It’s also a refund request for you. Or a chargeback. Or worse: a fraud flag. And even if it only happens once in a hundred checkouts, that one instance can still ruin your day.

That’s why we added a simple, powerful guardrail:

[*![Block duplicate subscriptions automatically with Freemius](https://freemius.com/blog/wp-content/uploads/2025/04/block-duplicate-subscriptions-automatically-with-freemius.jpeg)*](https://freemius.com/blog/wp-content/uploads/2025/04/block-duplicate-subscriptions-automatically-with-freemius.jpeg)

With a quick toggle, you can prevent users from purchasing multiple subscriptions for the same product. If someone tries to subscribe again when they already have an active plan, they’ll see a friendly message before the payment goes through:

[![Friendly message at Freemius Checkout to block duplicate subscriptions](https://freemius.com/blog/wp-content/uploads/2025/04/friendly-message-at-freemius-checkout-to-block-duplicate-subscriptions.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/04/friendly-message-at-freemius-checkout-to-block-duplicate-subscriptions.jpeg)

Consider it a friendly bouncer at the door of your checkout

This feature was originally built with SaaS makers in mind, but it’s helpful across the board.

## Hosted Checkout Success URL: Real-Time Redirects and Upgrades

Our [hosted checkout](help-documentation-selling-with-freemius-hosted-checkout.md) is simple, flexible, and no-code. But until now, it had one major gap: no way to instantly update your SaaS after a user completed a purchase.

If your server is down or your webhook logic hits a bug… well, your user’s still stuck staring at the same plan they’re trying to change.

Not exactly the seamless UX you were going for.

To put the “instant” back in “gratification”, we’ve introduced a [Checkout Success Redirect URL](blog-changelog-new-feature-redirect-after-successful-checkout.md) setting for hosted checkouts.

[![Hosted Freemius Checkout real-time redirects configuration](https://freemius.com/blog/wp-content/uploads/2025/04/hosted-freemius-checkout-real-time-redirects-configuration.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/04/hosted-freemius-checkout-real-time-redirects-configuration.jpeg)

Here’s what’s now possible:

- Define a custom redirect URL for your hosted checkout
- Redirect buyers immediately after a successful purchase
- Receive secure, signed context about the transaction
- Validate the data in your SaaS to confirm the purchase
- Instantly update the customer’s plan and unlock features
- Ensure the flow is secure, so your SaaS knows the request came from Freemius, not some random script

**It’s the best of both worlds:** a real-time experience for the user, with webhook-based redundancy as a fallback. *(Our advice: implement both for maximum reliability.)*

We’ve updated our [SaaS integration docs](help-documentation-selling-with-freemius-hosted-checkout.md#redirection_after_a_successful_purchase) to walk you through the setup.

While this was built with SaaS in mind, it works just as well for other use cases, such as redirecting to a thank-you page or post-purchase upsell screen. It also pairs nicely with our license-free SaaS integrations, where you don’t need to store license keys at all.

## Upgrade and Downgrade Links — No License Key Needed

For makers offering self-serve plan management, we’ve introduced a more secure, scalable way to handle upgrades and downgrades for paying customers.

Previously, this required storing license keys, which is something we strongly advise against.

Our new solution? [A secure Freemius API that generates checkout-ready links](blog-changelog-new-api-endpoint-to-generate-license-upgrade-links.md) using only the license ID. This is perfect for powering billing pages inside your SaaS, without compromising on security.

Here’s what you can do with it:

- Create upgrade and downgrade links without storing sensitive license keys
- Serve logged-in users with license-specific links
- Dynamically generate checkout URLs tied to a specific license
- Customize the link with `checkout.js` parameters (like plan ID, pricing, or quantity)
- Embed the flow directly into your billing section

This works for **any** Freemius license — not just SaaS. As long as the customer is already identified, it’s a smoother, safer way to let users manage their plans without exposing sensitive keys or adding friction.

## Leave No Maker Behind! A Smarter Billing Cycle Selector for Checkout

As part of our [checkout revamp](blog-new-freemius-checkout-drive-conversions-increase-sales-price.md#phase_two), we removed the original billing cycle selector to help declutter the experience.

The update improved overall conversion performance, but it came at a cost for some makers, especially those without full pricing pages who rely heavily on the Freemius Checkout for conversions.

After the cleanup, buyers were defaulted to a single plan (like Annual) and often missed other options — like Lifetime — simply because they weren’t highlighted as before.

We heard you.

And the [billing cycle selector is back!](blog-changelog-new-feature-billing-selector-ui-for-checkout.md) Redesigned to work better for those who activate it.

[![Freemius Checkout billing cycle selector](https://freemius.com/blog/wp-content/uploads/2025/04/freemius-checkout-billing-cycle-selector.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/04/freemius-checkout-billing-cycle-selector.jpeg)

The new version:

- Fits seamlessly into the revamped checkout
- Automatically displays as buttons when two billing cycles are available
- Shows all three billing cycles by default in an expanded layout
- Offers an optional dropdown layout for makers who prefer a more compact view
- Is fully optional and customizable — no forced changes

[![Freemius Checkout billing cycle selector three-plan default](https://freemius.com/blog/wp-content/uploads/2025/04/freemius-checkout-billing-cycle-selector-three-plan-default.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/04/freemius-checkout-billing-cycle-selector-three-plan-default.jpeg)

[![Freemius Checkout billing cycle selector three-plan dropdown](https://freemius.com/blog/wp-content/uploads/2025/04/freemius-checkout-billing-cycle-selector-three-plan-dropdown.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/04/freemius-checkout-billing-cycle-selector-three-plan-dropdown.jpeg)

***Left:* Vertical billing cycle list | *Right:* Dropdown billing cycle list for Freemius Checkout**

We don’t see edge cases as outliers. Even when most makers benefit, we pay close attention to the exceptions, especially when they impact revenue. We’ll always be committed to building for every maker, not just the average.

[![Annual lifetime upsells disabled when activating Freemius billing cycle selector](https://freemius.com/blog/wp-content/uploads/2025/04/annual-lifetime-upsells-disabled-when-activating-freemius-billing-cycle-selector.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/04/annual-lifetime-upsells-disabled-when-activating-freemius-billing-cycle-selector.jpeg)

Important note: Enabling the billing cycle UI will automatically disable annual and lifetime upsells

## The Mobile Experience Now Loads 30% Faster

We didn’t shout about it last time — but we probably should have.

As part of our recent improvements to the [Developer Dashboard’s mobile app experience](blog-freemius-release-notes-march-2025.md#a_fully_responsive_developer_dashboard_built_for_mobility), we quietly optimized caching behind the scenes.

The result? **Initial app load times are now roughly 30% faster when opening the mobile dashboard:**

[**![Freemius mobile dashboard app loads 30 percent faster](https://freemius.com/blog/wp-content/uploads/2025/04/freemius-mobile-dashboard-app-loads-30-percent-faster.jpeg)**](https://freemius.com/blog/wp-content/uploads/2025/04/freemius-mobile-dashboard-app-loads-30-percent-faster.jpeg)If you’re managing your business on the go, those extra seconds add up, whether you’re checking sales, reviewing customers, or pulling reports mid-meeting.

A dedicated page for the mobile app is in the works. In the meantime, you can find more context in [last month’s changelog](blog-changelog-various-mobile-and-pwa-improvements-for-the-developer-dashboard.md), which covers additional mobile polish.

## ICYMI: It’s Not Just the Showstoppers That Are Being Shipped…

Beyond the headline features, we’ve quietly shipped a ton since the last release — fixes, enhancements, and behind-the-scenes improvements that keep Freemius fast, smooth, and reliable for the makers who count on it.

Here’s a quick rundown if you feel like digging in:

- [New Version of the JS SDK](blog-changelog-freemius-checkout-improvements-with-a-new-version-of-the-js-sdk.md)
- Bulk Licenses, Payments Table & App Experience Improvements:
  
  - [Bulk Licenses for SaaS & App Products](blog-changelog-bulk-licenses-payments-table-app-experience-improvements-notification-controls.md#:~:text=Bulk%20Licenses%20for%20SaaS%20%26%20App%20Products)
  - [Payments Table Improvements for Migrated Payments](blog-changelog-bulk-licenses-payments-table-app-experience-improvements-notification-controls.md#:~:text=Payments%20Table%20Improvements%20for%20Migrated%20Payments)
  - [Notification Settings for Failed Renewal Recovery Emails](blog-changelog-bulk-licenses-payments-table-app-experience-improvements-notification-controls.md#:~:text=Notification%20Settings%20for%20Failed%20Renewal%20Recovery%20Emails)
- [App Documentation Improvements](help-documentation-selling-with-freemius-app-integration.md)
- [Removal of Developer Data from Webhook Payloads](blog-changelog-optimizing-webhook-payloads-removal-of-developer-data.md)
- [Fixed Loading of Abandoned Licenses in the Developer Dashboard](blog-changelog-fixed-loading-of-abandoned-licenses-in-the-developer-dashboard.md)
- Checkout UI/UX Improvements:
  
  - [VAT Number Validation](blog-changelog-checkout-ui-ux-improvements.md#:~:text=VAT%20Number%20Validation%20UX%20Improvement)
  - [Fixed Text in Money-Back Guarantee](blog-changelog-checkout-ui-ux-improvements.md#:~:text=Fixed%20Text%20in%20Money%2DBack%20Guarantee)
  - [Fixed Padding Issue in Checkout’s Postal Code Input](blog-changelog-checkout-ui-improvements.md#:~:text=Fixed%20Padding%20Issue%20in%20Zip/Postal%20Code%20Input)
  - [Removed Money-Back Guarantee UI from Free Plans](blog-changelog-checkout-ui-improvements.md#:~:text=Removed%20Money%2DBack%20Guarantee%20UI%20from%20Free%20Plans)
- [Fixed Subscription Cancellation Bug](blog-changelog-fixed-issue-with-subscription-cancellation.md)
- Developer Dashboard UI Improvements:
  
  - [Enhancements to Subscription and Payment Tables](blog-changelog-developer-dashboard-ui-improvements.md#:~:text=Enhancements%20to%20Subscription%20and%20Payment%20Tables)
  - [Offline UI Improvements](blog-changelog-developer-dashboard-ui-improvements.md#:~:text=Offline%20UI%20Improvements)
- [Fixed 2FA Input Issue with Samsung Keyboard](blog-changelog-fixed-2fa-input-issue-with-samsung-keyboard.md)
- [Fixed Missing Delete Button in Customer Portal](blog-changelog-customer-portal-bug-fix-missing-delete-button-on-website-page.md)

As always, every fix and feature, big or small, is shaped by the makers building with Freemius every day.

## Momentum and Progress, Powered by Your Voice

Everything in this release was shaped by real conversations with real makers, and we’re grateful for every suggestion, bug report, and feature request you send our way.

From smoother upgrade flows to faster mobile access and smarter billing experiences, we’re continuing to evolve Freemius into the most flexible, founder-friendly platform for selling software, whether you’re building SaaS, plugins, apps, or something in between.

Got feedback or ideas? [Reach out](https://x.com/freemius) — [we’re listening](https://freemius.com/cdn-cgi/l/email-protection#3a5955544e5b594e7a5c485f5f57534f4914595557)!