This release brings clear, polished improvements you can rely on. We’ve made the checkout smoother to reduce drop-offs, updated invoices to lower support needs, and released OpenAPI-powered API docs to make integrations easier and faster.

Whether you’re scaling a SaaS or selling plugins and other software, we’ve made Freemius more predictable, customizable, and maker-friendly than ever.

Let’s get into June’s updates:

## Launching Our New API Documentation: A Massive Step Toward SaaS Maturity

**Our new API documentation is live and you** [**can explore it right now**](https://docs.freemius.com/api)**! 🍾**

[**![Freemius's new API documentation](https://freemius.com/blog/wp-content/uploads/2025/07/freemiuss-new-api-documentation.jpeg)**](https://freemius.com/blog/wp-content/uploads/2025/07/freemiuss-new-api-documentation.jpeg)

Until now, most Freemius-powered WordPress products have relied on our SDK to handle things automatically, with a handful of documented snippets available for custom use cases.

But as we expand deeper into SaaS, a modern, well-documented API becomes essential — not just for flexibility, but for integration, automation, and even AI-readability.

We’ve overhauled our API infrastructure from the ground up, embracing the [OpenAPI specification](https://spec.openapis.org/oas/v3.0.0.html) as our new standard. This means:

- All current API endpoints are now fully documented to help SaaS makers build the custom integrations they envision
- All future API development will follow the OpenAPI protocol — no more stale, manually maintained docs
- Plus, we’ve [added detailed documentation](https://docs.freemius.com/api/deployments) to help with advanced automation around version deployments and getting latest updates

### A Developer’s Playground (Or Sandbox)

You can **already** browse every API endpoint in our [live docs](https://docs.freemius.com/api), view code examples in multiple languages (like JavaScript, NodeJS, PHP or cURL), and simulate or send real requests using bearer tokens.

Want to retrieve a subscription? Cool. See every parameter, expected response, and possible error before you write a line of code.

It’s all powered by OpenAPI, which means docs stay automatically synced with our codebase. No more guesswork or outdated pages.

This structure also makes our platform infinitely more compatible with AI tooling. Here’s why this is a massive win for Freemius makers of all types:

#### Built for Modern Makers (and Machines)

OpenAPI’s specification means our new docs aren’t just human-friendly — they’re IDE- and AI-friendly too.

What this means in practice:

- **Type-safe operations:** No more guessing what a response looks like. With OpenAPI, modern languages can validate your requests and responses at compile time, meaning fewer errors, faster debugging.
- **Live previews inside your IDE:** Use extensions like [vscode-openapi](https://marketplace.visualstudio.com/items?itemName=42Crunch.vscode-openapi) to browse endpoint details without ever leaving your code editor.
- **Instant client SDKs:** Generate language-specific SDKs using tools like [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator). No boilerplate, and no drift.
- **AI-ready structure:** Our docs can be fed directly into tools like ChatGPT or Cursor (using advanced protocols like [MCP](https://github.com/ReAPI-com/mcp-openapi)) to generate accurate, context-aware code snippets and automation flows, paving the way for code generation, smart assistants, and low-friction integrations.

**An example for ChatGPT:**

- **Prompt:** &gt; Please read the OpenAPI spec from this link –  [https://freemius.com/help/documentation/api/openapi.yaml](help-documentation-api-openapi.yaml.md) – and help me write TypeScript code to get a list of payments from the API.
- **Results:** [https://chatgpt.com/share/686a405e-37c0-8004-b0b3-ae33cb2e72a1](https://chatgpt.com/share/686a405e-37c0-8004-b0b3-ae33cb2e72a1)

Feels like magic? Here’s a pro tip from [Swashata Ghosh](https://www.linkedin.com/in/swashata?originalSubdomain=in) (Freemius VP of Engineering) to take the magic even further. **“**If you let chatGPT think deep it does much better job for you: [https://chatgpt.com/share/686a40c5-5154-8004-b302-e7c04dd225b0](https://chatgpt.com/share/686a40c5-5154-8004-b302-e7c04dd225b0)”

Our new API documentation is so much more than an update. It’s the foundation of our SaaS future and practically a product in its own right, built to power software businesses of all kinds.

## Checkout Enhancements: Polish, Power, and Post-Purchase Control

Two key upgrades lead the way for the Freemius Checkout this cycle, both designed to improve transparency, trust, and flexibility for SaaS and other software products.

### Smarter Discount Calculations, Less Buyer Confusion

We’ve added [a small line of text](blog-changelog-smarter-saas-friendly-discount-calculation-renewals-ui-and-other-checkout-improvements.md#:~:text=Improved%20Line%20Item%20to%20Show%20Renewal%20Price) and solved a big point of confusion.

Previously, buyers weren’t always sure if their discount would carry over at renewal, causing avoidable confusion, unnecessary support tickets, and lost conversions.

[![Freemius Checkout showing a “Renews at \[amount\]” line](https://freemius.com/blog/wp-content/uploads/2025/07/freemius-checkout-showing-a-renews-at-amount-line.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/07/freemius-checkout-showing-a-renews-at-amount-line.jpeg)

Renewal pricing has now been brought forward to where buyers actually need it, and the Freemius Checkout now clearly shows a **“Renews at \[amount]”** line, even when the renewal amount matches the discounted price.

This small but meaningful update brings greater clarity to the checkout experience and forms part of our ongoing effort to make Freemius more transparent and SaaS-savvy by design.

### Checkout Success Redirection — Now for All Product Types

[Originally built for SaaS flows](blog-freemius-release-notes-april-2025.md#hosted_checkout_success_url_real_time_redirects_and_upgrades), this feature quickly drew requests from WordPress makers looking for the same flexibility.

We listened!

***All*** makers can now redirect users to a custom page after checkout, whether it’s a dashboard, onboarding flow, thank-you screen, or upsell. The redirect also passes along helpful metadata, like the plan ID and user info, so you can personalize the experience from the moment a buyer converts.

[![Developer dashboard with post-checkout redirect option](https://freemius.com/blog/wp-content/uploads/2025/07/developer-dashboard-with-post-checkout-redirect-option.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/07/developer-dashboard-with-post-checkout-redirect-option.jpeg)

This is a perfect example of how our shift into SaaS benefits everyone, bringing modern capabilities to WordPress and other software ecosystems.

## Visual Polish with Purpose: Modernizing Freemius One Touchpoint at a Time

Another important part of our continued push to modernize the Freemius experience: visually, functionally, and everywhere it matters.

### Cleaner, Smarter Maker Emails (With More on the Way)

The old emails were showing their age, so we’ve begun rolling out sleeker ones, [starting with maker-facing messages](blog-changelog-another-batch-of-freemius-emails-gets-a-makeover.md).

[![cart recovery email for makers](https://freemius.com/blog/wp-content/uploads/2025/07/cart-recovery-email-for-makers.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/07/cart-recovery-email-for-makers.jpeg)

These aren’t just prettier templates. They’re clearer, more consistent with our current design language, and built to reflect the evolving maturity of the Freemius platform.

[![trial email for makers](https://freemius.com/blog/wp-content/uploads/2025/07/trial-email-for-makers.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/07/trial-email-for-makers.jpeg)

Buyer-facing emails are up next, but since many makers have customized them to match their brand, we’re rolling them out more gradually to avoid breaking anything.

Upon rollout, makers have the option to preview and tweak new designs before flipping the approval switch. Until then, your existing styles will stay exactly as they are.

### Modernized Invoices, From Font to Function

More than a facelift! The [redesigned buyer invoices are](blog-changelog-rebranded-customer-invoices-are-live.md) [**live**](blog-changelog-rebranded-customer-invoices-are-live.md) and more informative, accurate, and aligned with the evolving Freemius experience.

[![redesigned buyer invoice](https://freemius.com/blog/wp-content/uploads/2025/07/redesigned-buyer-invoice.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/07/redesigned-buyer-invoice.jpeg)

Here’s what’s new:

- **Account #, license ID**, and a **masked license key**, making it easier for buyers and support teams to connect purchases with licenses
- A new **“Additional Discounts”** row to account for edge cases like price adjustments or special promos
- **Product-specific support emails** now appear directly on the invoice
- **Monospace font for the numeric values** on invoices, improving alignment and readability across all totals and line items
- **Removed trailing zeroes** after decimal points (e.g. “20.00%” is now “20%”), so tax percentages look cleaner and more natural
- **Aligned currency symbols** in the totals section for a cleaner, more professional layout

[![Invoice section showing additional discount and support email](https://freemius.com/blog/wp-content/uploads/2025/07/invoice-section-showing-additional-discount-and-support-email.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/07/invoice-section-showing-additional-discount-and-support-email.jpeg)

Some of [these improvements](blog-changelog-refined-customer-invoices-with-discount-accuracy-and-better-readability.md) were sparked by real feedback from our makers (shoutout to [Florian](blog-florian-daugalies-success-story.md)!), and all of them are part of our continued push to bring more clarity and polish to our digital footprint.

## DX Win: Smoother Manual License Creation

Another chip off the “manual hassle” block to ensure the lives of our makers keep getting easier!

You can now assign a newly created license to any of the user’s websites directly in the UI. This also means you don’t need to send license keys manually anymore.

Small change = huge time saver.

[![Developer dashboard with license-to-site assignment option](https://freemius.com/blog/wp-content/uploads/2025/07/developer-dashboard-with-license-to-site-assignment-option.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/07/developer-dashboard-with-license-to-site-assignment-option.jpeg)

## Bit by Bit, a Better Freemius

Here are a bunch of smaller fixes and improvements that make Freemius smoother, smarter, and a little more delightful to use:

**Checkout:**

- [Smarter discount calculations for SaaS pricing](blog-changelog-smarter-saas-friendly-discount-calculation-renewals-ui-and-other-checkout-improvements.md#smarter_discount_calculation)
- [Improved mobile responsiveness in hosted checkout](blog-changelog-smarter-saas-friendly-discount-calculation-renewals-ui-and-other-checkout-improvements.md#responsiveness_improvements_in_hosted_checkout)
- [Clearer error for single-subscription limit for SaaS](blog-changelog-improved-error-message-for-single-subscription-limitation.md)
- [Bug fix for upgrade link generation API](blog-changelog-api-fixes-for-license-upgrade-and-deployment-update-endpoints.md#bug_fix_for_checkout_upgrade_link_generation_api)
- [Localized card icons for a more native feel](blog-changelog-checkout-card-icon-localization.md)

**Developer Dashboard:**

- [Removed outdated Skype support option from plans](blog-changelog-removed-skype-as-support-option-from-the-plans.md)
- [Fixed staged rollout bug in deployment](blog-changelog-api-fixes-for-license-upgrade-and-deployment-update-endpoints.md#bug_fix_for_deployment_update_api_endpoint)
- [Improved UI/UX and internal link structure](blog-changelog-ui-ux-and-internal-links-improvement-of-the-developer-dashboard.md)
- [Fixed bug in Event Log filtering](blog-changelog-better-events-filtering-and-mobile-ui-for-the-developer-dashboard.md#events_table_filtering)
- [Earnings page now mobile-friendly and tracks payouts on the go](blog-changelog-better-events-filtering-and-mobile-ui-for-the-developer-dashboard.md#responsiveness_improvements)

**Miscellaneous:**

- **Reverse invoices:** Squashed bugs and improved [reliability across the board](blog-changelog-reverse-invoice-bug-fixes.md)
- **Custom license units**: [New doc](help-documentation-selling-with-freemius-customize-license-unit-label.md) shows you how to customize your license unit labels
- **Deployment automation UI**: Improved WordPress deployment screen [now surfaces automation options more clearly](blog-changelog-improved-wordpress-deployment-screen-ui-and-misc-documentation-and-ui-updates.md)
- **Dunning:** Fixed an [edge case bug](blog-changelog-fixed-payment-method-update-bug.md) with updating payment methods in the dunning flow
- **Payout invoices**: [Fixed](blog-changelog-fixed-authentication-issue-with-tokenized-invoice-url.md) tokenized invoice link authentication issue
- **Customer portal**: Fixed issue with “[Remember Me](blog-changelog-license-creation-and-customer-portal-login-ui-issues.md#customer_portal_login_remember_me_option)” login option

## Progress Lives in the Details, and It’s Powered by You

We’ve been quietly consistent with leveling up not just the tools you use, but the way you use them. Clearer flows, cleaner interfaces, and smarter defaults.

This round of updates reflects a Freemius that’s becoming more polished and more cohesive, one touchpoint at a time, each progressive step expanding our digital footprint.

From API docs that scale with your SaaS ambitions to cleaner invoices, smarter checkout flows, and sleeker, better-looking touchpoints, every update reflects your feedback, needs, and the maturity of our platform.

Keep the ideas, bug reports, and requests coming. They shape what’s next.