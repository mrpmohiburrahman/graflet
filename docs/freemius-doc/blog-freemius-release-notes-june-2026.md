June’s release is about localization, recovery, and refinement.

Makers get more ways to sell in the currencies and languages their buyers expect, more control over trial cancellation emails and license activations, and a set of enhancements that smooth out checkout, dashboard, portal, and backend flows.

## New currencies: PLN, CAD, AUD, and ILS

Most makers dream globally, but build locally first, where customers are closer, community is tighter, and feedback is faster.

That local-first pattern is what led to this update. The Israeli maker community in particular has been active and vocal, and the signal was clear: Hebrew speakers wanted to pay in Shekels, not just see a familiar language at checkout.

[![Freemius checkout in RTL with ILS pricing](https://freemius.com/blog/wp-content/uploads/2026/07/freemius-checkout-in-rtl-with-ils-pricing.jpeg)](https://freemius.com/blog/wp-content/uploads/2026/07/freemius-checkout-in-rtl-with-ils-pricing.jpeg)

Requests from other markets followed the same logic — Australian and Canadian makers wanted AUD and CAD, Polish makers wanted PLN.

[Freemius Checkout now supports four new currencies](blog-changelog-freemius-checkout-now-supports-pln-cad-aud-and-ils.md): Polish złoty, Canadian dollars, Australian dollars, and Israeli Shekels, alongside existing [USD, EUR, and GBP support](help-documentation-selling-with-freemius-multi-currency.md).

These are presentment currencies:

- A buyer in Poland sees and pays in Polish złoty, exactly as the maker configured it
- Freemius doesn’t hold a PLN balance behind the scenes — the payment is automatically converted and settled into the maker’s USD balance at the exchange rate at the time of the transaction
- One less currency to manage, with buyers still seeing the price in what’s familiar to them

[![Freemius checkout showing local currency](https://freemius.com/blog/wp-content/uploads/2026/07/freemius-checkout-showing-local-currency.jpeg)](https://freemius.com/blog/wp-content/uploads/2026/07/freemius-checkout-showing-local-currency.jpeg)

Adding currencies is easier too. We’ve revamped the Add Currency flow on the Plan page. Freemius copies your USD price over using the current conversion rate as a starting point, and you can adjust it from there.

[![Add currency flow on the Plans page](https://freemius.com/blog/wp-content/uploads/2026/07/add-currency-flow-on-the-plans-page.jpeg)](https://freemius.com/blog/wp-content/uploads/2026/07/add-currency-flow-on-the-plans-page.jpeg)

You can also leave currency unset. Buyers then get a dropdown near the total price and in the footer, letting them pick their currency themselves.

[![Currency selector in the Freemius checkout](https://freemius.com/blog/wp-content/uploads/2026/07/currency-selector-in-the-freemius-checkout.jpeg)](https://freemius.com/blog/wp-content/uploads/2026/07/currency-selector-in-the-freemius-checkout.jpeg)

Currency conversion currently runs through Stripe, with PayPal support in progress. On the payout side, nothing changes for existing GBP or EUR setups — you’ll just need a USD payout method in place to receive funds from the new currencies.

Want a currency that isn’t listed here? [Let us know](https://freemius.nolt.io/).

## RTL support moves out of beta, with Arabic and Serbian joining the list

A checkout that reads right-to-left, in a buyer’s own language, removes one more reason to hesitate at the moment of payment.

With that in mind, [RTL support at checkout](blog-changelog-rtl-language-support-comes-to-freemius-checkout.md) launched in beta in May, with Hebrew as the first language. After several rounds of feedback, both RTL and Hebrew are [officially out of beta and production-ready](blog-changelog-checkout-localization-update-rtl-out-of-beta-and-polish-now-available.md), with Polish moving to production alongside it.

Two more languages join the list, each opening the door to a new market:

- **Serbian (Srpski)** is generally available, extending that same local-checkout experience into the Balkans
- **Arabic** joins in beta (Modern Standard Arabic). It’s one of the most widely spoken languages in the world, making this a meaningful first step toward reaching MENA buyers

[![Freemius checkout sample in Arabic](https://freemius.com/blog/wp-content/uploads/2026/07/freemius-checkout-sample-in-arabic.jpeg)](https://freemius.com/blog/wp-content/uploads/2026/07/freemius-checkout-sample-in-arabic.jpeg)

Language switching is also noticeably faster, cutting what used to be a few-hundred-millisecond delay down to near-instant. [RTL loading gets a boost](blog-changelog-checkout-localization-update-faster-rtl-loading-arabic-beta-and-serbian-support.md) on top of that, with the layout shifting as soon as a buyer selects an RTL language.

Have a language your buyers need that isn’t here? [Let the team know](https://freemius.nolt.io/).

## Trial cancellation email joins Email Customization

A cancelled trial doesn’t have to be the end of the conversation with that buyer.

But until now, makers had no way to speak into that moment. They could customize purchase and subscription emails, [among others](https://freemius.com/help/documentation/emails/email-content-customization/), but not the one sent when a trial gets cancelled.

Take a buyer who starts a trial with a payment method attached, then cancels before it converts to paid. That’s the moment the [trial cancellation email](blog-changelog-trial-cancellation-email-added-to-email-customization.md) is built for, and it’s now live in the Email Customization section of the Developer Dashboard.

[![trial email customization page in the Developer dashboard](https://freemius.com/blog/wp-content/uploads/2026/07/trial-email-customization-page-in-the-developer-dashboard.jpeg)](https://freemius.com/blog/wp-content/uploads/2026/07/trial-email-customization-page-in-the-developer-dashboard.jpeg)

It’s a natural spot to re-engage a buyer who was close enough to try the product — a one-time discount or another incentive written into the email can be the difference between a lost trial and a second chance at conversion.

## Manage license activations directly from the Developer Dashboard

Customers have a self-service way to manage activations from the Customer Portal. They can see which devices are connected to their license and deactivate a specific one when needed.

Sellers had less control. From the Developer Dashboard, deactivating a license meant deactivating it everywhere at once. There was no way to remove access from one device without affecting the rest.

[That’s now changed](blog-changelog-app-makers-can-now-manage-license-activations-from-the-dashboard.md). Open **Users** in the Developer Dashboard, select a customer, and the new **Activations** section shows every device tied to their license, each with its own **Deactivate** button.

![License activations section](https://freemius.com/blog/wp-content/uploads/2026/07/license-activations-section.jpeg)

When a customer contacts you about one specific device, you can handle it directly from the dashboard instead of sending them back to the Customer Portal.

## Odds, ends, and edge cases

Some months the smaller fixes cluster around one theme. This month they’re scattered — a license expiration quirk, a couple of checkout edge cases, some dashboard polish — each one closing a gap somewhere in the platform.

**Developer Dashboard**

- [License expiration updates now also work correctly from the Subscription page](blog-changelog-fixed-license-expiration-updates-from-the-subscription-page.md), not just the Licenses page
- [Webhook permissions restored for the Developer role](blog-changelog-developer-dashboard-improvements-for-webhooks-plan-pricing-and-license-creation.md), plus Plan page UI fixes and a corrected unit label in the license creation dialog
- [Email Customization previews, data table loading, and documentation links](blog-changelog-improved-email-previews-faster-data-tables-and-better-documentation-links.md) all got faster and clearer — data tables in particular got a second pass after May’s initial speed-up

**Checkout**

- [Upsell UI, consumptive usage refund badge, and duplicate payment-failed email bugs fixed](blog-changelog-checkout-bug-fixes-and-consumptive-usage-refund-badge-update.md)

**Customer Portal**

- [Modal dialogs now stay within view](blog-changelog-customer-portal-modal-positioning-fixed-in-embed-mode.md) when the portal is embedded in a fixed-height container

**Backend and emails**

- [Trial lifecycle emails redesigned](blog-changelog-improved-trial-emails-and-backend-fixes.md) to match the current style, alongside fixes for a license deletion error and a rare cart webhook issue

## Local where it matters

Selling globally works better when the buying experience still feels local. This month’s release adds more currencies, more language coverage, stronger RTL support, and a better way to follow up when trials are cancelled.

Each update removes a bit more friction from the path between interest and purchase. [Tell us what would make that path smoother for your buyers next](https://freemius.nolt.io/).