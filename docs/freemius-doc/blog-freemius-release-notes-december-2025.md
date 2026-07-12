This month’s release improves the day-to-day maker experience. Setup is simpler, controls are more flexible, and a set of iterative fixes smooth out common workflows.

These updates also set the stage for what’s coming in 2026.

## Weekly Reports With Clearer Performance Breakdowns

Weekly reports give you a quick overview of how your products performed over the past week.

As the grand finale for our [email rebranding project](blog-changelog-redesigned-customer-emails-with-modern-look-and-better-ux.md), we rebuilt the format from the ground up to make information easier to scan and more useful at a glance.

[![Weekly Reports with Detailed Performance](https://freemius.com/blog/wp-content/uploads/2026/01/weekly-reports-with-detailed-performance.jpeg)](https://freemius.com/blog/wp-content/uploads/2026/01/weekly-reports-with-detailed-performance.jpeg)

[Each weekly email now clearly highlights and breaks down](blog-changelog-a-fresh-clearer-weekly-reports-experience.md):

- Total sales
- First-time payments
- Renewals

This gives you quick, reliable insight into which plans, pricing structures, and billing cycles are performing best, without needing to dig through the Developer Dashboard.

We also added a direct link to the specific week’s report, so you can jump straight from the email into deeper detail when needed.

Combined with improved responsiveness across devices, the weekly report is now a cleaner, more actionable snapshot of your business.

## Product Setup Without Pricing or Integration Surprises

[We refined the new product form](blog-changelog-enhancement-to-the-type-of-products-supported-by-freemius.md) to eliminate confusion around product types and pricing.

Using a generic “plugin” label could lead to incorrect setup, such as higher fees (7% instead of 4.7%) or WordPress-only integrations being applied to SaaS products.

Makers also highlighted that the labels weren’t always enough to guide people toward the right setup. For example:

- Creators of Chrome extensions weren’t sure which type to pick
- Figma plugins were accidentally categorized as WordPress plugins, requiring manual corrections

The updated flow now starts with a clear, high-level product category, so makers only see the options that apply to what they’re selling:

- SaaS
- Apps & Software
- WordPress Products
- Bundles & Membership

[![New Product Form with Clear Category](https://freemius.com/blog/wp-content/uploads/2026/01/new-product-form-with-clear-category.jpeg)](https://freemius.com/blog/wp-content/uploads/2026/01/new-product-form-with-clear-category.jpeg)

Once a category is selected, the form surfaces relevant product types (such as plugins, extensions, or add-ons), ensuring the correct pricing and integrations are applied from the start.

[![New Product Form with Category-Specific Types](https://freemius.com/blog/wp-content/uploads/2026/01/new-product-form-with-category-specific-types.jpeg)](https://freemius.com/blog/wp-content/uploads/2026/01/new-product-form-with-category-specific-types.jpeg)

After creating a product, makers are taken straight to the Setup Checklist, keeping onboarding smooth and moving things forward without unnecessary detours.

[![New product Setup Checklist](https://freemius.com/blog/wp-content/uploads/2026/01/new-product-setup-checklist.jpeg)](https://freemius.com/blog/wp-content/uploads/2026/01/new-product-setup-checklist.jpeg)

We also added unsupported product categories, such as physical products, services, or marketplaces.

These options surface a clear notice explaining that they can’t be sold via Freemius, helping prevent invalid setups that cause headaches down the line.

The result is a cleaner setup flow, fewer misconfigurations, and less back-and-forth with support.

## GDPR Marketing Opt-In Control for SaaS Checkouts

Many SaaS products handle marketing consent during registration, not at purchase.

Until now, the Freemius Checkout could prompt buyers for consent again, adding one more required click until a choice was made.

[![SaaS Checkout GDPR Opt-In](https://freemius.com/blog/wp-content/uploads/2026/01/saas-checkout-gdpr-opt-in.jpeg)](https://freemius.com/blog/wp-content/uploads/2026/01/saas-checkout-gdpr-opt-in.jpeg)

Based on feedback from a SaaS maker, Freemius now gives makers [explicit control over the marketing opt-in UI in the Checkout](blog-changelog-checkout-improvements-gdpr-opt-in-control-localization-and-ux-fixes.md#new_feature_to_control_marketing_opt_in_ui). Depending on how consent is handled elsewhere in your product, you can choose to:

- Show the opt-in as before
- Hide the opt-in entirely and rely on consent collected during registration
- Default the opt-in to “No”, removing the required decision step at checkout

**We’ve also fixed an important case:** if a buyer has already opted in, they won’t be asked again — preventing needless prompts and opt-outs.

The result is a checkout flow that better matches how SaaS products operate, with flexibility to prioritize marketing reach or conversion efficiency.

## Design Update for License Download and Recovery Mini-App

The license download and recovery tool now matches the rest of the [Freemius rebrand](blog-freemius-rebrand-website-developer-dashboard-redesign.md). The update focuses on clearer visuals and better consistency, while keeping the experience and functionality the same.

The tool lets buyers recover their licenses and download links on their own, with an email sent automatically — a small change that quietly cuts down on avoidable support tickets.

[![Redesigned license recovery tool](https://freemius.com/blog/wp-content/uploads/2026/01/redesigned-license-recovery-tool.jpeg)](https://freemius.com/blog/wp-content/uploads/2026/01/redesigned-license-recovery-tool.jpeg)

[![Sample Email for License Recovery Tool Users](https://freemius.com/blog/wp-content/uploads/2026/01/sample-email-for-license-recovery-tool-users.jpeg)](https://freemius.com/blog/wp-content/uploads/2026/01/sample-email-for-license-recovery-tool-users.jpeg)

## Clearer Feedback When WordPress SDK Integration Fails

If a WordPress SDK integration can’t be confirmed, the setup flow now points out [common issues and links to helpful docs](blog-changelog-improved-sdk-integration-check-ux.md), making it easier to spot missed steps or configuration problems.

[![Improved Feedback with Common Issues & Docs for WordPress SDK Failures](https://freemius.com/blog/wp-content/uploads/2026/01/improved-feedback-with-common-issues-and-docs-for-wordpress-sdk-failures.jpeg)](https://freemius.com/blog/wp-content/uploads/2026/01/improved-feedback-with-common-issues-and-docs-for-wordpress-sdk-failures.jpeg)

Shaped by support and community feedback, the update makes first-time setup smoother and helps cut down on related support requests.

## Steady Improvements Across the Platform

These updates may not headline the release, but they polish everyday workflows, address edge cases, and improve reliability across key parts of the platform.

**Checkout and Payments**

- [Minor bug fixes and stability improvements](blog-changelog-checkout-enhancements-localization-fixes-cart-stability-updates.md)
- [Zero-value subscription invoices are now sent to buyers](blog-changelog-subscription-zero-value-invoices-are-now-sent-to-buyers.md)
- [Improved invoice and license exports](blog-changelog-backend-qol-improvements-invoice-wrapping-license-exports.md)
- [Improvements for renewals and upgrades](blog-changelog-checkout-improvements-for-renewals-upgrades.md)

**Emails and Deliverability**

- [Enhanced DKIM-aware email customization](blog-changelog-enhanced-dkim-aware-email-customization-flow.md)
- [Minor DKIM UI update](blog-changelog-minor-ui-polishing-to-the-dkim-configuration-section.md)
- [Weekly report email regression fix](blog-changelog-weekly-report-email-layout-fix-for-banner-rendering.md)

**Developer Experience and SDKs**

- [New LiteSDK license activation API now supports bundles](blog-changelog-improved-license-activation-api-with-full-bundle-support.md)
- [WordPress SDK clone resolution bug fixed](blog-changelog-fix-for-rare-license-migration-edge-case-in-the-wp-sdk.md)

**Customer Portal**

- [Bug fix improving styling reliability](blog-changelog-customer-portal-ui-customization-fixes.md)

**Developer Dashboard and Admin**

- [Fixed issues in store settings UI for non-owner team members](blog-changelog-fixed-store-settings-ui-for-non-owner-team-members.md)
- [Resolved error when listing sites by version number](blog-changelog-api-fix-resolved-504-errors-when-querying-sites-by-version.md)
- [Various Developer Dashboard enhancements](blog-changelog-developer-dashboard-update-improved-checkout-link-generation-cleaner-ui-bug-fixes.md)

**Compliance**

- [Strengthened GDPR-related handling and privacy controls across more regions](blog-changelog-strengthened-gdpr-handling-and-privacy-controls-across-more-regions.md)

## Refinements That Add Up and Build Momentum for 2026

This release reflects ongoing product development driven by real usage and feedback. Each improvement builds on the last, and together they make Freemius easier to work with and more predictable in everyday use.

As always, keep sharing ideas and feedback. It helps us decide where to go next.