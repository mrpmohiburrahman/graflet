May’s release is about reach.

RTL language support at checkout and in transactional emails gives makers selling in local markets a checkout and email experience that matches the rest of their product. Sticklight joins the growing list of AI builders with a one-prompt path to full Freemius monetization.

## RTL language support in Freemius Checkout

Global selling has always been the core Freemius value proposition — it’s how makers reach more buyers, in more markets, without the operational overhead.

Additional localization support had been on our radar for years, but adoption signals weren’t strong enough to move it up the roadmap.

That changed as Freemius [expanded beyond WordPress into broader SaaS](https://freemius.com/year-in-review-2025/). Talking to those makers made the necessity clear: starting local means starting in your language and your currency, and a checkout that doesn’t match breaks the experience where you can least afford it.

[Freemius Checkout now supports RTL (right-to-left) languages](blog-changelog-rtl-language-support-comes-to-freemius-checkout.md). Hebrew is the first language through, currently in beta.

To enable it, add the language=he parameter to your checkout configuration. Once the translation moves to full release, language=auto will surface Hebrew automatically for buyers in Israel.

[![Freemius Checkout in RTL language](https://freemius.com/blog/wp-content/uploads/2026/06/freemius-checkout-in-rtl-language.jpeg)](https://freemius.com/blog/wp-content/uploads/2026/06/freemius-checkout-in-rtl-language.jpeg)

For makers in markets where Stripe isn’t available, the case for localization is compelling. As a [merchant of record](merchant-of-record.md), Freemius lets sole proprietors start selling without needing to set up a company or navigate a Stripe Atlas-style LLC structure.

With that in mind, this is the first step in a broader localization effort covering the critical points in the buyer experience: checkout, currency, and transactional emails. To help guide these efforts, what’s the next language that you would like to see? [Let us know](https://dashboard.freemius.com).

## RTL support in email customization

Checkout is where the sale happens. But a consistent local experience doesn’t stop there — [transactional emails](help-documentation-marketing-automation-email-content-customization.md) are part of that same flow, and until now, the custom content section didn’t fully support RTL.

[RTL support is now available in Email Customization](blog-changelog-rtl-support-comes-to-email-customization.md), extending the same language flexibility beyond checkout. The feature automatically detects text direction when you enter RTL content. For mixed-language emails, you can explicitly set the **Custom Text Direction** option to force a specific direction.

[![Email Customization page supporting RTL](https://freemius.com/blog/wp-content/uploads/2026/06/email-customization-page-supporting-rtl.jpeg)](https://freemius.com/blog/wp-content/uploads/2026/06/email-customization-page-supporting-rtl.jpeg)

There’s also a new option to change the position of the custom section within the email, which is useful if you want fully localized instructions to appear before the original email content.

[![customizing sample RTL email](https://freemius.com/blog/wp-content/uploads/2026/06/customizing-sample-rtl-email.jpeg)](https://freemius.com/blog/wp-content/uploads/2026/06/customizing-sample-rtl-email.jpeg)

The current implementation is a first pass. Mixed-language emails in particular aren’t yet fully optimized, and further refinement will follow based on adoption and feedback. Reach out through support in the [Developer Dashboard](https://dashboard.freemius.com).

## Sticklight integration: Full Freemius monetization with a single prompt

In March, we said the [next integration would follow demand](blog-freemius-release-notes-march-2026.md#lovable_integration_full_freemius_monetization_with_a_single_prompt). Sticklight is it!

Sticklight is an AI-assisted app builder with a growing community of makers building and shipping SaaS products. The workflow will be familiar: an idea, a prompt, a working app.

What was missing was a simple path to full monetization.

Our [end-to-end Freemius integration guide for Sticklight](https://freemius.com/help/documentation/ai/sticklight/) works the same way our [Lovable integration](https://freemius.com/freemius-lovable-ai-integration/) does — one prompt to your AI agent sets up the complete monetization layer.

**1. Integrated pricing page and checkout, configured from your Freemius dashboard:**

[**![integrated pricing page](https://freemius.com/blog/wp-content/uploads/2026/06/integrated-pricing-page.jpeg)**](https://freemius.com/blog/wp-content/uploads/2026/06/integrated-pricing-page.jpeg)

**2. Feature gating. Users without an active plan are blocked at the feature level:**

[**![Feature gating for non-subscribers](https://freemius.com/blog/wp-content/uploads/2026/06/feature-gating-for-non-subscribers.jpeg)**](https://freemius.com/blog/wp-content/uploads/2026/06/feature-gating-for-non-subscribers.jpeg)

**3. In-app accounts page showing active subscriptions and payments, linked to the Customer Portal:**

[**![In-app accounts page showing active subscriptions and payments](https://freemius.com/blog/wp-content/uploads/2026/06/in-app-accounts-page-showing-active-subscriptions-and-payments.jpeg)**](https://freemius.com/blog/wp-content/uploads/2026/06/in-app-accounts-page-showing-active-subscriptions-and-payments.jpeg)

[Head over to our docs](https://freemius.com/help/documentation/ai/sticklight/) to get started. More integrations are on the way.

## The work behind the work

Not every fix gets a headline, but these ones came close — real bugs caught, rough edges smoothed, and a platform that continues to work better for everyone using it.

**Developer Dashboard**

- [Faster data loading across tables](blog-changelog-developer-dashboard-gets-faster-data-loading-and-safer-price-deletion.md)
- [Product settings page fixes](blog-changelog-fixed-product-settings-page-issues.md)
- [Multi-currency pricing UI fixed for non-USD plans](blog-changelog-fixed-multi-currency-pricing-ui-issues-for-non-usd-plans.md)
- [Payments table, Events menu, and earnings page currency filter restored](blog-changelog-fixed-payments-table-events-menu-and-earnings-page-ui.md)

**Checkout**

- [Bundle checkout preloading with license keys fixed for manual renewals and upgrades](blog-changelog-fixed-bundle-checkout-preloading-with-license-keys.md)

**Customer Portal**

- [Terms & conditions link in the affiliate form fixed for SaaS and app products](blog-changelog-fixed-terms-conditions-link-in-the-customer-portal-affiliate-form.md)

**Invoices**

- [Invoice discounts now render cleanly after a pricing update](blog-changelog-cleaner-invoice-discounts-after-pricing-updates.md)

**Billing**

- [Tax ID field extended to 18 characters, covering more regions, including China](blog-changelog-billing-form-now-supports-longer-tax-ids.md)

## Reaching further

Two features this month share the same logic: more makers, in more markets, with less friction. RTL support brings local-market makers a checkout and email experience that fits, and Sticklight gives a new community of builders a direct path to monetization.

The reach keeps broadening and we need your feedback to make sure it lands right — [let us know where to take it next](https://freemius.nolt.io/).