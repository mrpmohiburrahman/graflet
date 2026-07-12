This month brings meaningful refinements across the customer buying journey and the internal tools you rely on. Upgrades are simpler, checkout flows are more flexible, billing details are clearer, and several long-standing edge cases around attribution, testing, and recovery finally got the attention they needed.

Let’s dive into what has improved.

## Upgrade from Single Products to Bundles Seamlessly

For makers running multiple products, this upgrade path has been a real pressure point. Customers who wanted to move into a [bundle](help-documentation-wordpress-selling-bundles-and-memberships.md) often hit friction and the workarounds weren’t always intuitive.

This new flow removes upgrade friction, reduces support back-and-forth, and creates a much clearer path for customers who start with one product and later discover the value of a full bundle.

If a customer owns any product included in a bundle, they can upgrade directly through [checkout](help-documentation-checkout.md) without juggling keys, emailing support, or re-activating anything.

[![Creating a bundle product in Developer dashboard](https://freemius.com/blog/wp-content/uploads/2025/12/Creating-a-bundle-product-in-Developer-dashboard.jpg)](https://freemius.com/blog/wp-content/uploads/2025/12/Creating-a-bundle-product-in-Developer-dashboard.jpg)

[This update comes with:](blog-changelog-introducing-seamless-license-upgrades-from-products-to-bundles.md)

- **Automatic** [**prorated discount**](https://freemius.com/help/documentation/checkout/proration/) — customers only pay the difference for the bundle
- **No new license to manage** — the original key becomes the bundle key
- **Instant access to all bundle products** — existing [website activations](help-documentation-wordpress-license-utilization.md) remain intact

## [![Freemius checkout with automatic prorated discount](https://freemius.com/blog/wp-content/uploads/2025/12/Freemius-checkout-with-automatic-prorated-discount.jpg)](https://freemius.com/blog/wp-content/uploads/2025/12/Freemius-checkout-with-automatic-prorated-discount.jpg)

## WordPress SDK 2.13.0 Brings Full Checkout Power Into WP Admin

If you rely on in-dashboard selling, this update is a big quality-of-life boost. The [checkout inside WP admin now works as smoothly as the on-site version](blog-changelog-freemius-wordpress-sdk-v2-13-0-released.md), so customers can buy or upgrade without leaving the dashboard.

[![the checkout page inside WP admin](https://freemius.com/blog/wp-content/uploads/2025/12/the-checkout-page-inside-WP-admin.jpg)](https://freemius.com/blog/wp-content/uploads/2025/12/the-checkout-page-inside-WP-admin.jpg)

On top of that, you now get full control over the checkout’s configuration.

Want to adjust billing-cycle selectors, tweak the UI, or fine-tune behavior for custom pricing pages? The new filter lets you shape the in-dashboard checkout to match exactly how you want to sell.

This keeps the whole experience contained and removes a chunk of friction from your flow.

## Freemius for WordPress Plugin Makes Checkout Integration Almost Effortless

[Freemius for WordPress plugin](help-documentation-wordpress-freemius-for-wordpress.md) started as a personal tool built by Xaver, the creator of [Mailster](https://mailster.co/). After showing it to our CEO, Vova Feldman, at WordCamp Asia, we sponsored its development so makers could have a simple, reliable way to integrate Freemius checkout into their marketing sites.

Now it’s officially available to everyone and any block-based button in WordPress [can become a fully functional Freemius checkout button](blog-changelog-simplify-freemius-checkout-integration-with-the-new-wordpress-plugin.md).

[![turning block-based button to a Freemius checkout button](https://freemius.com/blog/wp-content/uploads/2025/12/turning-block-based-button-to-a-Freemius-checkout-button.jpg)](https://freemius.com/blog/wp-content/uploads/2025/12/turning-block-based-button-to-a-Freemius-checkout-button.jpg)

Here’s what it does:

- Turns any block-based button into a Freemius checkout button
- Makes WP-based pricing pages and landing pages dead simple to wire up
- Removes the need to write or maintain integration code
- Significantly smooths the buying experience

You can watch a quick video demonstrating how to set it up:

## Cleaner Invoice Details and Clearer Product Attribution

Up until now, [customer invoices](help-documentation-users-account-management-orders-history.md#generate-a-printable-invoice) always showed “on behalf of” using your maker details, even when the purchase was for a specific product or brand. Many makers asked to flip that logic, so invoices now pull **from the product first** and only fall back to the maker name when needed.

[![customer invoice with clear details and product attribution](https://freemius.com/blog/wp-content/uploads/2025/12/customer-invoice-with-clear-details-and-product-attribution.jpg)](https://freemius.com/blog/wp-content/uploads/2025/12/customer-invoice-with-clear-details-and-product-attribution.jpg)

As part of these [improved invoice details](blog-changelog-improved-invoice-details-and-product-attribution.md), we also fixed a few related quirks:

- Invoice headers for [SaaS & Apps](help-documentation-saas.md) no longer show product slugs
- Product URLs use the product URL first and only fallback to the maker’s billing URL if it’s not set
- [Custom license unit labels](help-documentation-saas-customize-license-unit-label.md) show properly in the item description

This makes everything cleaner and more consistent for customers who buy from multi-product makers.

## Easier Testing for Custom Payment Recovery URLs

If you’ve played with the [custom payment recovery URL](help-documentation-marketing-automation-dunning-failed-payments.md#customizing-payment-method-update-links) feature we released recently, you may have noticed that testing the flow wasn’t as smooth as it could be. And because this feature is all about handling failed payments, it’s only natural to want a fast, reliable way to confirm everything works as expected.

To fix that, we’ve added a [new “Test Payment Recovery” button](blog-changelog-easier-testing-for-custom-payment-recovery-url-integration.md) in the UI that lets you trigger the flow instantly. No workarounds are required!

[![new test payment recovery button](https://freemius.com/blog/wp-content/uploads/2025/12/new-test-payment-recovery-button.jpg)](https://freemius.com/blog/wp-content/uploads/2025/12/new-test-payment-recovery-button.jpg)

One click opens your recovery URL and launches a mocked payment-recovery checkout flow, giving you the buyer’s view and a confirmation message that your integration is working.

[![integration to support custom payment recovery URL confirmation](https://freemius.com/blog/wp-content/uploads/2025/12/integration-to-support-custom-payment-recovery-URL-confirmationn.jpg)](https://freemius.com/blog/wp-content/uploads/2025/12/integration-to-support-custom-payment-recovery-URL-confirmationn.jpg)

## Improved Affiliate Attribution for Cross-Store Purchases

Before, if someone clicked an affiliate link for Product A but bought Product C, the commission was earned, but the payout view still tied it to Product A, which made [attribution](help-documentation-affiliate-platform-affiliate-program-activation.md#sales-attribution) confusing.

[This update fixes that](blog-changelog-fixes-and-enhancements-to-affiliate-exports-and-cross-store-or-account-attribution.md). Cross-store and cross-account commissions now show clearly in the Payouts tab, with the correct product represented, so you can see exactly where each commission came from.

[![Affiliate Program showing commission origins](https://freemius.com/blog/wp-content/uploads/2025/12/Affiliate-Program-showing-commission-origins.jpg)](https://freemius.com/blog/wp-content/uploads/2025/12/Affiliate-Program-showing-commission-origins.jpg)

We also fixed an issue with [affiliate](help-documentation-affiliate-platform.md) exports cutting off records, so CSV downloads now include your full affiliate list.

## Developer Dashboard Gets a New Onboarding Video

We’ve been putting more focus into the first-time user experience, and this update adds a short [walkthrough video to help new makers get up to speed faster](blog-changelog-developer-dashboard-gets-ui-fixes-and-a-new-video-walkthrough-for-easier-onboarding.md)[.](blog-changelog-developer-dashboard-gets-ui-fixes-and-a-new-video-walkthrough-for-easier-onboarding.md) If your product setup isn’t complete yet, you’ll see a guided overview of the key steps and where everything lives in the [dashboard](help-documentation-getting-started-explore-the-developer-dashboard.md).

[![New onboarding video in Developer dashboard](https://freemius.com/blog/wp-content/uploads/2025/12/New-onboarding-video-in-Developer-dashboard.jpg)](https://freemius.com/blog/wp-content/uploads/2025/12/New-onboarding-video-in-Developer-dashboard.jpg)

It’s a small touch, but it makes those first few minutes with Freemius a lot smoother.

## Fresh New Design for the Freemius Review App

Our Review App has gotten a [long-needed visual refresh](blog-changelog-fresh-new-design-for-the-freemius-review-app.md). Since the review flow starts from the email Freemius sends on your behalf, the design your customers land on matters.

The old version worked, but it felt a little dated. The new look is cleaner and fits better with the rest of the Freemius experience.

[![redesigned Freemius Review App](https://freemius.com/blog/wp-content/uploads/2025/12/redesigned-Freemius-Review-App.jpg)](https://freemius.com/blog/wp-content/uploads/2025/12/redesigned-Freemius-Review-App.jpg)

It’s a meaningful upgrade that gives customers a more modern, trustworthy space to leave feedback and helps you collect higher-quality reviews.

## Improved Sender Address for Transactional Emails

If you’re sending [transactional emails](help-documentation-marketing-automation-transactional-emails.md) using an address that falls into one of these cases:

- [DKIM authentication](help-documentation-marketing-automation-email-deliverability.md#domainkeys-identified-mail-dkim) has not been completed
- You’re using a generic provider like Gmail or Outlook
- The [sender address](help-documentation-marketing-automation-email-settings.md) doesn’t match your authenticated domain

…your emails are more likely to get blocked or land in spam — which isn’t great when customers rely on them for invoices, renewals, or updates.

[![Emails sections in the Developer dashboard](https://freemius.com/blog/wp-content/uploads/2025/12/Emails-sections-in-the-Developer-dashboard.jpg)](https://freemius.com/blog/wp-content/uploads/2025/12/Emails-sections-in-the-Developer-dashboard.jpg)

To prevent important messages from getting lost, [Freemius now sends transactional emails](blog-changelog-enhanced-handling-of-sender-addresses-for-transactional-emails.md) from [\[email protected\]](https://freemius.com/cdn-cgi/l/email-protection) whenever any of the above apply. Customers will see **&lt;[\[email protected\]](https://freemius.com/cdn-cgi/l/email-protection)&gt; {{ productTitle }} via Freemius**, and your Reply-To address stays the same, so replies still go directly to you.

If you’re already using your own domain and it’s DKIM-authenticated, your emails will continue using your configured sender.

## Our License Recovery Now Works for Migrated Licenses

Previously, some [migrated licenses](help-documentation-migration.md) weren’t included in the license-recovery flow, so customers never got the expiration notices. Now, those licenses [trigger the same “your license is about to expire” email sequence](blog-changelog-our-license-recovery-now-works-for-migrated-licenses.md), along with a checkout link to renew just like licenses purchased through Freemius.

[![License recovery email for migrated license](https://freemius.com/blog/wp-content/uploads/2025/12/License-recovery-email-for-migrated-license.jpg)](https://freemius.com/blog/wp-content/uploads/2025/12/License-recovery-email-for-migrated-license.jpg)

## Quiet Fixes, Polished Edges, and Small Wins That Add Up

These updates won’t steal the spotlight, but together they smooth out workflows, prevent edge-case headaches, and keep everyday operations running cleanly.

**Developer Dashboard**

- [Added simpler flow for setting unlimited license quotas](blog-changelog-smarter-license-quota-ui-plans-page-fixes.md#the_license_quota_ui_got_smarter)
- [Fixed Plans page actions for non-admin teammates](blog-changelog-smarter-license-quota-ui-plans-page-fixes.md#bug_fix_in_the_plans_page)
- [Fixed saving issues in Affiliate settings](blog-changelog-smarter-license-quota-ui-plans-page-fixes.md#fix_deployed_for_affiliate_settings_save_issue)
- [Improved clarity of GDPR and marketing-consent details](blog-changelog-enhanced-user-marketing-gdpr-ui-and-streamlined-sdk-test-license-creation.md#better_marketing_gdpr_ui_under_users)
- [Streamlined test-license creation during SDK onboarding](blog-changelog-enhanced-user-marketing-gdpr-ui-and-streamlined-sdk-test-license-creation.md#faster_license_creation_for_sdk_integration)

**Checkout**

- [Improved resilience for VAT number verification in checkout](blog-changelog-enhanced-resilience-for-vat-verification-in-checkout.md)
- [Fixed a layout glitch in embedded checkout flows (WP SDK 2.13)](blog-changelog-checkout-layout-bug-fix-for-wordpress-sdk-2-13.md)
- [Fixed payment-method recovery flow in Checkout JS SDK 1.4.1](blog-changelog-fix-for-payment-method-recovery-flow-in-checkout-js-sdk-1-4-1.md)

**Marketing Automation**

- [Improved clarity and layout in cancellation emails](blog-changelog-improved-subscription-cancellation-email.md)

**Customer Portal**

- [Hid sensitive details for foreign licenses](blog-changelog-customer-portal-now-hides-sensitive-details-for-foreign-licenses.md)
- [Disabled exit-intent popups in upsell flows](blog-changelog-exit-intent-disabled-in-customer-portal-upsell-flow.md)
- [Fixed incorrect product labels in affiliate application forms](blog-changelog-corrected-product-labeling-in-affiliate-application-form.md)

**API / Backend**

- [Fixed license expiration not updating after first PayPal payment](blog-changelog-fix-for-license-expiration-not-updating-after-initial-paypal-payment.md)
- [Improved API filter support and corrected error messages](blog-changelog-api-improvements-filter-support-error-message-fix.md)
- [Updated fallback statement descriptor for clearer bank entries](blog-changelog-updated-generic-statement-descriptor-for-broader-software-support.md)
- [Expanded WP.org product slug limit for better compatibility](blog-changelog-expanded-wordpress-product-slug-limit-for-better-compatibility.md)

## Another Month of Smoother Flows, Stronger Systems

A lot of this month’s work came from real conversations with you — little things you pointed out while setting up a bundle, testing checkout, reviewing invoices, or just trying to make your workflow smoother. They may seem small on the surface, but they’re the fixes you feel every day.

If you notice more rough edges or something that slows you down, [keep calling it out](https://freemius.com/cdn-cgi/l/email-protection#e3808c8d97828097a3859186868e8a9690cd808c8e). It really does help us figure out what needs attention next.