More clarity, more control, less admin. That’s the theme for May.

New additions include support for iDEAL (the go-to payment method in the Netherlands), reverse invoices by email, and a cleaner, collapsible Earnings page that puts your take-home front and center.

There’s a lot going on under the hood, too. So let’s lift it:

## Going Dutch: iDEAL Checkout Is Live

The Netherlands’ most popular payment method is [now available in your hosted checkout](blog-changelog-new-payment-method-in-freemius-checkout-ideal-for-netherlands.md)!

This matters because buyers are more likely to complete a purchase when the checkout feels familiar. With iDEAL, Dutch customers see a checkout that feels local: their language, their currency, and their preferred payment method are front and center.

This familiarity builds trust and reduces drop-off at checkout. And in a digitally mature, flourishing economy like the Netherlands, that means more completed sales and higher revenue.

Here’s what Dutch buyers will see:

- A checkout localized in Dutch, with EUR pre-selected
- iDEAL shown as the default payment option
- A seamless, QR-powered flow that lets them pay via their banking app

[![Freemius Checkout supports iDEAL for Netherlands payments](https://freemius.com/blog/wp-content/uploads/2025/05/Freemius-Checkout-supports-iDEAL-for-Netherlands-payments.jpg)](https://freemius.com/blog/wp-content/uploads/2025/05/Freemius-Checkout-supports-iDEAL-for-Netherlands-payments.jpg)

Behind the scenes, iDEAL pairs with [SEPA mandates](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/79b492e8058c493b8f45ae544857fee7.html) to support recurring payments so that subscriptions still renew without a hitch.

**Note:** iDEAL is currently only available in the hosted checkout. If adoption meets expectations, we plan to expand support to overlay and in-dashboard checkouts later this year.

## The Freemius Checkout Gets a Boost in Accessibility

The EU Accessibility Act [comes into effect in June](https://accessible-eu-centre.ec.europa.eu/content-corner/news/eaa-comes-effect-june-2025-are-you-ready-2025-01-31_en), and we’re moving to meet — and exceed — its requirements.

This month, we’ve [upgraded the license and billing cycle dropdowns](blog-changelog-enhanced-checkout-accessibility-billing-selector-logic-and-ideal-flow-fixes.md) in the checkout to behave like native elements:

- Fully keyboard accessible
- Tab into elements, navigate with arrow keys, hit space/enter to select
- Escape to close

[https://freemius.com/blog/wp-content/uploads/2025/05/checkout-dropdown-ui-a11y.mp4](https://freemius.com/blog/wp-content/uploads/2025/05/checkout-dropdown-ui-a11y.mp4)

The Freemius Checkout becomes part of your site when embedded, so its accessibility matters for your compliance too. These updates move us closer to full compliance — and next up is the Customer Portal.

### Smarter Defaults for the Billing Cycle Selector

The Freemius Checkout supports two UI approaches for billing cycles:

*A compact toggle-style upsell:*[![Freemius Checkout toggle upsell feature](https://freemius.com/blog/wp-content/uploads/2025/05/Freemius-Checkout-toggle-upsell-feature.jpg)](https://freemius.com/blog/wp-content/uploads/2025/05/Freemius-Checkout-toggle-upsell-feature.jpg)

*An extended dropdown or list selector:*

[![Freemius Checkout dropdown selector](https://freemius.com/blog/wp-content/uploads/2025/05/Freemius-Checkout-dropdown-selector.jpg)](https://freemius.com/blog/wp-content/uploads/2025/05/Freemius-Checkout-dropdown-selector.jpg)

Until now, the **monthly billing option** only appeared if:

- You explicitly set the `show_monthly` flag
- Or loaded the checkout with a monthly plan preselected

Following feedback from our makers, we’ve updated the logic:

The monthly billing option is now shown by default unless a different cycle is explicitly set or `show_monthly` is set to `false`. This change makes the upsell toggle and dropdown more intuitive, predictable, and user-friendly right out of the box.

## Payout Emails Now Include Reverse Invoices

If your billing info’s set correctly, there’s no need to send us an invoice — we’ve already sent one your way. That’s the magic of a reverse invoice.

Last month, you found them on your [Earnings page](blog-freemius-release-notes-april-2025.md#no_more_manual_invoicing_for_payouts_seriously).

This month, they’ve made it to your inbox and are [automatically included in payout emails](blog-changelog-payouts-email-now-includes-the-reverse-invoice.md) so you don’t have to hunt them down come tax time.

We’ve also trimmed the fat from payout emails. Now they include only what you need: your earnings and a clear, downloadable invoice. No dashboard detours required.

[![New Freemius payout emails reverse invoices included](https://freemius.com/blog/wp-content/uploads/2025/05/New-Freemius-payout-emails-reverse-invoices-included.jpg)](https://freemius.com/blog/wp-content/uploads/2025/05/New-Freemius-payout-emails-reverse-invoices-included.jpg)

Unfortunately, there were a few hiccups during rollout and some makers didn’t receive reverse invoices in the latest round of payouts. To protect the experience, we’ve introduced a fallback: if invoice generation fails, the system reverts to the previous email format.

The good news is that those glitches are mostly behind us now, and delivery is running smoothly.

**Note:** Some countries have specific invoicing requirements that our reverse invoice feature may not fully support. If that’s the case for you, you’ll need to keep issuing invoices as required by your local laws. If you notice any gaps compared to the invoices you usually issue, please [reach out to support](https://freemius.com/cdn-cgi/l/email-protection#e5969095958a9791a583978080888c9096cb868a88) and let us know. Your feedback will help us prioritize which localizations to add next — even though this process will take time.

### One Small Edge Case, One Fix in Progress

Bank wire users, we owe you one. Or at least the right address.

In countries like Nepal, banks often require a formal invoice as proof before clearing incoming funds. To help with that, we pulled the billing address from the bank account details on file.

This backfired for software makers relying on FinTech services like Wise or Revolut.

Since these services use proxy accounts, invoices ended up showing *their* company address instead of yours.

Not ideal.

We’ve [just fixed the logic](blog-changelog-reverse-invoice-bug-fixes.md) and reissued any incorrect invoices. Thanks to the makers who flagged this — you made the system smarter for everyone.

## Earnings Page UI Tweak: More Focus on the Numbers You Care About

Not too long ago, we adjusted our [pricing model](pricing.md) to better serve [SaaS and App](freemius-for-saas.md) makers.

Now, we’ve given the [Earnings page a refresh](blog-changelog-new-ui-for-the-new-commission-rate.md) to match, because if there’s one place you shouldn’t have to dig ***for*** earnings, it’s the page ***about*** earnings.

[![Updated Freemius payment information Earnings page](https://freemius.com/blog/wp-content/uploads/2025/05/Updated-Freemius-payment-information-Earnings-page.jpg)](https://freemius.com/blog/wp-content/uploads/2025/05/Updated-Freemius-payment-information-Earnings-page.jpg)

You’ll still find the big block breaking down pricing, taxes, fees, and payout schedules (newly updated to reflect our current commission model). It’s a legacy addition we made to help new makers understand where every cent goes.

But let’s be honest: once you’ve seen it, you’ve seen it.

When the payment breakdown information becomes second nature, makers can now collapse it to keep earnings front and center. The page also remembers your preference, so if you collapse it once, it stays out of your way next time too.

## The (Infamous?) Blog Pop-Up Now Comes With a Dismiss Button

You know the one — the real-time pop-up on our blog showing live product sales through Freemius.

It’s there to showcase how active (and varied) our ecosystem is. Plus, it gives our makers’ products the spotlight, complete with a link to the pricing or home page. Win-win, right?

Well… not for everyone.

We’ve heard the feedback over the years: *“Cool feature, but why can’t I turn it off?”*

Now you can.

[![blog popup being closed](https://freemius.com/blog/wp-content/uploads/2025/05/sales-popup.gif)](https://freemius.com/blog/wp-content/uploads/2025/05/sales-popup.gif)

We’ve added a dismiss button, and your choice sticks across visits so you can scroll through changelogs or blog deep-dives without interruption.

It’s a small UX upgrade, but another step toward making our blog as smooth and friction-free as the rest of the Freemius experience.

## Not All Heroes Wear Headlines

Behind the scenes, we’ve been squashing bugs, tightening UI details, and tuning the machine. No big fanfare — just the kind of polish that keeps Freemius running like it should.

Here’s what shipped quietly in the background:

**Checkout and billing:**

- [New loading spinner — sleeker and faster](blog-changelog-checkout-ui-ux-improvements-2.md#:~:text=Updated%20Loading%20Spinner)
- [Entitlement UI is now hidden when multi-unit support is disabled](blog-changelog-checkout-ui-ux-improvements-2.md#:~:text=Smarter%20License%20Selector%20for%20SaaS%20%26%20Apps)
- [Fixed UI glitches and translation issues on Free plan checkouts](blog-changelog-various-checkout-improvements-2.md#:~:text=Free%20Plan%20Checkout%3A%20Polished%20and%20Perfected)
- [PayPal fault tolerance added to hosted payment method updates](blog-changelog-various-checkout-improvements-2.md#:~:text=Smarter%20PayPal%20Dunning)

**Developer Dashboard and DX:**

- [Affiliate Program ID now visible in the Developer Dashboard](blog-changelog-ui-ux-bug-fixes-in-the-developer-dashboard-and-customer-portal.md)
- [Fixed edge-case bug when transferring product ownership](blog-changelog-fixed-bug-in-transferring-product-ownership.md)
- [Special coupon UI no longer breaks when clearing input](blog-changelog-bug-fix-special-coupon-ui-in-the-developer-dashboard.md)

**Licensing:**

- [License key now correctly included in all license-related webhook events](blog-changelog-title-bug-fix-in-webhooks-license-key-now-included-in-all-license-events.md)

**Customer Portal**

- [Password reset flow got a UX tune-up](blog-changelog-ui-ux-bug-fixes-in-the-developer-dashboard-and-customer-portal.md#:~:text=For%20the%20Customer%20Portal)

## Built with Care, Tuned by Your Feedback

This release may not have launched a major feature, but it’s packed with practical wins — the kind that make software selling smoother, faster, and less of a headache. From better UX to smarter billing defaults, every improvement was shaped by makers like you.

Keep the feedback coming because we’re always listening!

[DM us on X](https://x.com/freemius) or [drop us a mail](https://freemius.com/cdn-cgi/l/email-protection#50333f3e2431332410362235353d3925237e333f3d).