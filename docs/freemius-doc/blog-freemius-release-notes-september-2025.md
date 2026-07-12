From a brand new JavaScript SDK and React Starter Kit to a fully redesigned documentation hub, this release marks a huge step forward for developers building with Freemius.

Let’s explore September’s releases:

## The Freemius JavaScript SDK and React Starter Kit Have Landed

SaaS makers, this one’s for you.

Until now, integrating Freemius into a JavaScript- or React-based app meant working directly with the [API](https://docs.freemius.com/api) — powerful. Not rocket science, but comes with a learning curve.

That’s changed in a big way. The new [**Freemius JavaScript SDK**](help-documentation-saas-sdk-js-sdk.md) and [**React Starter Kit**](help-documentation-saas-sdk-react-starter.md) significantly reduce the time and effort needed to integrate Freemius into any JavaScript or React-based SaaS or app.

[![sample pricing page](https://freemius.com/blog/wp-content/uploads/2025/10/sample-pricing-page.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/10/sample-pricing-page.jpeg)

What’s new:

- SDK for JavaScript or TypeScript powered backends like Node.js, Bun, Deno, etc.
- A React Starter Kit that ships with fully typed APIs and ready-made React components — including paywalls, pricing tables, and a built-in customer portal — to speed up implementation even further.
- A [Next.js integration guide](help-documentation-saas-sdk-framework-nextjs.md), created by our VP of Engineering, [Swashata Ghosh](https://www.linkedin.com/in/swashata?originalSubdomain=in), to help teams hit the ground running.
- A foundation for future adapters — more SDKs for additional frameworks will be developed based on demand (you can [make a request](https://freemius.nolt.io/) today), expanding Freemius’ coverage across the SaaS ecosystem.
- **Plus,** a [Next.js starter template](https://github.com/Freemius/ai-chat-nextjs-example) to kick start the development of your Saas with Freemius billing and user management integrated into the system.

[![sample SaaS subscription page](https://freemius.com/blog/wp-content/uploads/2025/10/sample-saas-subscription-page.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/10/sample-saas-subscription-page.jpeg)

This release transforms what used to be a manual integration process into a guided, ready-to-deploy setup. By providing an SDK tailored to the world’s most common SaaS technologies, Freemius is making [SaaS monetization](help-documentation-saas-saas-integration.md) more accessible than ever for modern app developers.

In simpler terms: it’s now as fast and easy for JavaScript and React developers to monetize with Freemius as it’s always been for [WordPress plugin makers](help-documentation-wordpress.md).

You’ll find comprehensive documentation for the SDK and Starter Kit in the newly redesigned [Freemius Docs hub](help-documentation-saas-sdk.md).

And, wouldn’t you know it, that’s what we’re diving into next:

## Freemius Documentation Website: Faster, Performant, and Live

This one’s been a long time coming…

And it’s a ***huge*** one!

Our [**documentation website has been completely rebuilt**](help.md) as part of a long-term investment in usability and consistency.

[![Freemius documentation home page in light mode](https://freemius.com/blog/wp-content/uploads/2025/10/freemius-documentation-home-page-in-light-mode.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/10/freemius-documentation-home-page-in-light-mode.jpeg)

More than aesthetics, this is the start of a [**unified documentation experience**](blog-changelog-freemius-documentation-website-freshly-redesigned-and-live.md). Whether you’re selling WordPress plugins or scaling a SaaS, Freemius Docs are becoming faster, clearer, and more context-aware with every update.

What’s new:

- **Static architecture** for dramatically faster performance
- **Real-time search** that no longer relies on WordPress — every query is instant
- A **modernized, fully branded design** that matches the rest of the Freemius ecosystem

<!--THE END-->

[![an instant real-time search](https://freemius.com/blog/wp-content/uploads/2025/10/an-instant-real-time-search.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/10/an-instant-real-time-search.jpeg)

- **AI-powered assistance:** with one click, you can open ChatGPT and discuss any doc directly, from code snippets to implementation examples

<!--THE END-->

[![Page showing an option to open ChatGPT for a direct discussion with any document](https://freemius.com/blog/wp-content/uploads/2025/10/page-showing-an-option-to-open-chatgpt-for-a-direct-discussion-with-any-document.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/10/page-showing-an-option-to-open-chatgpt-for-a-direct-discussion-with-any-document.jpeg)

- **Restructured documentation** that now includes an entire new section for the JavaScript SDK and React Starter Kit
- Improved code snippets, a new dark mode 🤩, all built to make the developer experience smoother than ever

[![Freemius documentation home page in dark mode](https://freemius.com/blog/wp-content/uploads/2025/10/freemius-documentation-home-page-in-dark-mode.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/10/freemius-documentation-home-page-in-dark-mode.jpeg)

The redesigned Docs also introduce smarter content segmentation. Down the line, this will become even more intelligent. Your view of the Docs will automatically adjust based on what you build in your Developer Dashboard, even if it’s a mixture of WP and SaaS.

The new hub also lays the groundwork for upcoming improvements, like separate “Guides” and “Docs” sections, and tighter integration with Freemius’ API documentation portal.

## Improved Clarity for Customer Portal Temporary Passwords

This update is a great example of how feedback makes the Freemius experience better for newcomers to the community.

When a customer makes their first purchase through Freemius, they’re automatically granted access to the [**Customer Portal**](customer-portal.md). That access comes via email, along with a password they use to sign in for the first time. After logging in, they’re required to set a new one.

**Note:** [Customer portal link & credentials](blog-changelog-customize-customer-portal-links-in-transactional-emails.md) are optional for SaaS and can be turned off.

Someone in the Post Status community raised a valid concern:

The email included that password in plain text, and without clear labeling, it raised concerns from users and security researchers about whether Freemius was sending permanent credentials.

To prevent confusion and ease security concerns, [**we’ve updated the email copy**](blog-changelog-improved-clarity-for-customer-portal-temporary-passwords.md) to explicitly say **“Temporary password.”** The behavior hasn’t changed, but the clearer language makes expectations obvious and reduces unnecessary stress.

[![Email showing updated text with “Temporary password”](https://freemius.com/blog/wp-content/uploads/2025/10/email-showing-updated-text-with-temporary-password.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/10/email-showing-updated-text-with-temporary-password.jpeg)

> This is really cool. During a Fresh Perspective product review, I encountered some confusion with the way Freemius generates a temporary password and sends it in plain text in an email.
> 
> Wellp, the Freemius team fixed it. Now, all Freemius users benefit! [https://t.co/Y79oVeTXmX](https://t.co/Y79oVeTXmX)
> 
> — Jeff (@jeffr0) [September 22, 2025](https://twitter.com/jeffr0/status/1970143337693761849?ref_src=twsrc%5Etfw)

## Overlay Checkout: Skip the Confirmation Step for SaaS

We’ve made the post-purchase flow more intuitive for SaaS and app users.

Previously, completing a checkout via Freemius triggered a confirmation dialog along with a button to proceed. This made sense for downloadable software: users receive an email, grab the ZIP, and activate with a license key.

But for SaaS, this extra step added friction. After a successful payment, users expect immediate updates inside the app, whether that’s upgraded plan info, new credits, or access to additional features. That confirmation screen just got in the way.

Freemius now lets SaaS makers [**skip the confirmation dialog entirely**](blog-changelog-skip-confirmation-dialog-in-overlay-checkout.md), streamlining the experience and reducing redundant UX.

[![SaaS plan settings page with skip confirmation option](https://freemius.com/blog/wp-content/uploads/2025/10/saas-plan-settings-page-with-skip-confirmation-option.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/10/saas-plan-settings-page-with-skip-confirmation-option.jpeg)

You can manage this behavior in your Plan settings, or configure it on a case-by-case basis depending on the flow you want. It’s especially useful for apps that show custom confirmation messages, toasts, or visual upgrades directly inside the product.

[https://freemius.com/blog/wp-content/uploads/2025/09/checkout-skip-dialog-demo.mp4](https://freemius.com/blog/wp-content/uploads/2025/09/checkout-skip-dialog-demo.mp4)

## Hosted Checkout Redirect: Trial Support + Smarter Parameters

When a buyer completes a purchase via the hosted checkout, many SaaS makers choose to redirect them back into their app, typically to a billing or dashboard page where the purchase is reflected immediately.

This redirect flow now works [**seamlessly for trial signups**](blog-changelog-hosted-checkout-redirect-trial-support-new-parameters.md), too.

We’ve also added new redirect parameters that tell your app exactly what just happened: whether the user started a trial, upgraded a plan, changed their payment method, or something else entirely.

[![SaaS plan settings customization page](https://freemius.com/blog/wp-content/uploads/2025/10/saas-plan-settings-customization-page.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/10/saas-plan-settings-customization-page.jpeg)

For trials, we now pass metadata about:

- Whether it’s a free or paid trial
- The trial’s scheduled end date
- The user ID, subscription ID, and purchase details

This gives your SaaS app real-time context without needing to call the Freemius API. That means:

- Faster UI updates
- Cleaner billing displays
- Fewer seconds waiting for backend sync

And because there’s no need to fetch this data from our API, your post-checkout experience is *2–3 seconds faster*, meaning no lag or extra load time.

So, whether you want to show a “Pro trial active” badge, unlock usage-based features, or just skip an API call — now you can do it all instantly, right after checkout.

## Custom Bulk Pricing: Flexibility for Any Use Case

Freemius now supports [**customizable bulk pricing units**](blog-changelog-support-for-custom-bulk-pricing-smarter-pricing-ui-and-api-page-improvements.md) — a major unlock for both SaaS and WordPress products.

In the WordPress ecosystem, bulk licenses typically cover fixed increments: 1 site, 5 sites, 10 sites, 20 sites, etc. Over the years, we standardized these tiers based on what most developers actually sold. Custom quantities like 6, 9, or 123-site licenses were rare, and if needed, we’d handle them manually in the backend.

But SaaS changed the game. Makers are now selling tokens, API calls, usage credits, etc. These quantities range from 1 to 10 million and static pricing tiers just can’t keep up.

That’s why we’ve introduced a simple but powerful update:

You can now define any quantity of units when setting up bulk pricing. Whether you’re selling 99 credits, 7 license activations, or 432 API calls, you’re in full control.

[![Freemius with customizable bulk pricing units](https://freemius.com/blog/wp-content/uploads/2025/10/freemius-with-customizable-bulk-pricing-units.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/10/freemius-with-customizable-bulk-pricing-units.jpeg)

[![bulk pricing page with unit labels for SaaS or WP products](https://freemius.com/blog/wp-content/uploads/2025/10/bulk-pricing-page-with-unit-labels-for-saas-or-wp-products.jpeg)](https://freemius.com/blog/wp-content/uploads/2025/10/bulk-pricing-page-with-unit-labels-for-saas-or-wp-products.jpeg)

The unit label (e.g. “sites” or “credits”) adapts to your product type — giving WordPress plugin sellers the familiar terms they’re used to, while SaaS founders get flexible, token-based quantity controls.

## Bug Fixes, Polish, and Quiet Wins

Not every improvement makes a splash, but these behind-the-scenes fixes help Freemius run smoother, faster, and with fewer hiccups so you can build stronger and sell smarter.

**Checkout:**

- [Improved validation for opt-in redirection URLs](blog-changelog-improved-validation-for-opt-in-redirection-urls.md)
- [Fix for incorrect cart recovery emails triggered during payment method updates](blog-changelog-fix-for-incorrect-cart-recovery-emails-during-payment-method-update.md)

**Emails:**

- [Clearer messaging around the affiliate payment cooling-off period](blog-changelog-clarifying-affiliate-payment-cooling-off-period-in-emails.md)
- [Improved formatting for pro-forma invoices](blog-changelog-improved-formatting-in-pro-forma-invoices.md)

**Docs and Webhooks:**

- [Enhancements to API documentation, schema, and webhook clarity](blog-changelog-enhancements-to-api-documentation-schema-webhooks.md)

**Developer Dashboard:**

- [Fix for manual license assignment](blog-changelog-fix-for-manual-license-assignment-in-developer-dashboard.md)
- [Resolved table alignment regression](blog-changelog-fix-for-table-alignment-regression-in-developer-dashboard.md)
- [Improved responsiveness and notification handling](blog-changelog-dashboard-responsiveness-and-notification-fixes.md)
- [Fixed license table bug showing duplicate subscriptions](blog-changelog-bug-fix-in-license-table-showing-duplicate-subscriptions.md)

## Until Next Time — Keep Shipping, We’ll Keep Polishing

Whether you’re selling site licenses, credits, subscriptions, or something custom in between, these updates are here to make your workflow faster and your buyers’ journey smoother.

Got feedback or a [feature request](https://freemius.nolt.io/)? Drop us a [note](https://freemius.com/cdn-cgi/l/email-protection#14777b7a607577605472667171797d61673a777b79), a [DM](https://x.com/freemius), or a Slack message if you’re a community member — we’re building this with you.