From completing our Data Liberation Project to introducing powerful tools in the Freemius Checkout and WordPress SDKs, we’ve addressed key maker requests while staying ahead of trends in the software ecosystem.

With updates like dual plugin version activation, enhanced pricing pages, and IntelliSense for smoother integration, we’re simplifying workflows and helping make your software more appealing to users.

Discover how Freemius’s latest additions help grow your software business:

## Affiliate Payouts Export: Completing the Data Liberation Project!

This update marks the conclusion of our [Data Liberation Project](blog-changelog-enhancements-to-the-users-export-from-the-developer-dashboard.md), giving software makers full freedom and control over their important business data.

Currently, Freemius makers need to handle affiliate payouts manually (more on this in a second).

For some, this is manageable. But as the number of affiliates grows, the process can quickly become time-consuming. Manually copying and pasting details like affiliate names, PayPal emails, and payout amounts is tedious and inefficient.

**The good news?** With just a click, makers can now [export affiliate payout details in bulk](blog-changelog-new-feature-affiliate-payouts-download.md), including names, emails, and amounts. Once exported, the file can be customized (e.g., renaming columns) and uploaded to PayPal or any other system to streamline payouts.

![Freemius one click affiliate payouts export](https://freemius.com/blog/wp-content/uploads/2025/01/freemius-one-click-affiliate-payouts-export.jpeg)

**Looking ahead:** Later this year, we plan to fully automate affiliate payouts. Once live, Freemius will take care of everything — from calculations to transfers — eliminating the need for copy-pasting, manual exports, or uploads, so makers can focus on what matters most.

### Data… Liberated!

With the completion of our Data Liberation Project, there’s even more to celebrate. Makers now have a complete suite of tools and data, giving them freedom to grow on their own terms by accessing key business information whenever they need it.

Here’s everything that’s now exportable at your fingertips:

- [Payments](blog-changelog-introducing-new-feature-to-export-payments.md)
- [Subscriptions](blog-changelog-data-export-now-available-for-subscriptions.md)
- [Users](blog-changelog-enhancements-to-the-users-export-from-the-developer-dashboard.md)
- [Websites](blog-changelog-new-feature-to-export-sites.md)
- [Licenses](blog-changelog-new-export-feature-for-licenses-and-payments-export-enhancement.md)
- [Affiliate payouts](blog-changelog-new-feature-affiliate-payouts-download.md)

## The Affiliate Terms Page Gets a Makeover

As part of our ongoing rebrand and visual revamp, we’ve given the [Affiliate Terms page a fresh new look](blog-changelog-affiliates-terms-page-improvements-and-contact-form-bug-fix.md).

Previously, the design was functional but outdated. Now, the page features a sleeker layout, modern fonts, and a cleaner, sharper design that reflects our updated branding. It’s a small change, but one that underscores our commitment to delivering a better experience at every touchpoint.

![Redesigned dynamic Freemius Affiliate Terms page](https://freemius.com/blog/wp-content/uploads/2025/01/redesigned-dynamic-freemius-affiliate-terms-page.jpeg)

**Why does this matter?** Our dynamically generated affiliate terms provide flexibility by tailoring agreements to each product’s unique program.

The updated design enhances this functionality, offering a polished, professional presentation that builds trust and credibility with affiliates. This isn’t just about aesthetics — it’s about fostering greater confidence and engagement in your program.

## Transparency Without Complexity: Tax Information Included in Payments and Subscription Pages

Handling VAT and sales tax has always been seamless with Freemius. But for a long time, makers lacked granular visibility into the transaction level.

**Bottom line:** Transparency matters, even in a seamless process.

Recognizing the importance of visibility, we took an initial step toward greater transparency a few years ago by including aggregated tax data in payout emails. While these emails provide a high-level breakdown, specific tax details aren’t explicitly shown.

To build on that effort, we’ve added detailed tax information directly to the **Payments** and **Subscription** pages in the [Developer Dashboard](blog-release-notes-real-time-analytics-and-multi-store-dashboard.md):

![VAT sales tax information Freemius Payments and Subscription pages](https://freemius.com/blog/wp-content/uploads/2025/01/vat-sales-tax-information-freemius-payments-and-subscription-pages.jpeg)

- A **subtle tax icon** appears next to transactions where VAT or sales tax was collected. Hovering over the icon reveals whether it’s VAT or sales tax and the exact amount.
- **For subscriptions**, taxes are displayed as a percentage instead of an amount, since payments can vary (e.g., renewals versus first-time payments).

Additionally, the **Payments** table now includes the actual tax amount collected for each transaction, giving makers a full breakdown of the taxes Freemius handles.

![VAT sales tax information Freemius Payments and Subscription pages](https://freemius.com/blog/wp-content/uploads/2025/01/vat-sales-tax-information-freemius-payments-and-subscription-pages-1.jpeg)

With this clearer view of tax details, makers can feel confident knowing these complexities are managed with care and precision. It’s a simple yet significant step in maintaining transparency, helping everyone — whether you’re already using Freemius or considering it for your business.

## Freemius Checkout JS SDK v1.1.0: Smarter Integration with TypeScript IntelliSense

The [new Freemius JS SDK](blog-changelog-version-1-1-0-of-the-freemius-checkout-js-sdk.md) introduces a powerful update to make checkout integration faster and more intuitive for makers.

**TypeScript IntelliSense**: When integrating the checkout, IntelliSense automatically suggests and completes options as you type, giving you instant access to settings, functions, and capabilities — all within your code editor.

With this feature, makers can code on the fly without constant back-and-forth with documentation, streamlining development and minimizing errors. Whether you’re a seasoned developer or just starting with Freemius, this update will help you work faster, smarter, and with greater efficiency.

![TypeScript IntelliSense integration in Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2025/01/typescript-intellisense-integration-in-freemius-checkout.jpeg)

## WordPress SDK v2.10.1 Enhancements

### Parallel Activation of Both Free and Paid Plugin Versions

Originally, the Freemius SDK automatically deactivated a plugin’s free version when the paid version was activated (and vice versa), simplifying updates for users.

However, as makers sought greater flexibility, the demand to run both versions in parallel has grown over the years. Some even resorted to “hacking the system” to make it work, which often caused issues that required Freemius to step in and troubleshoot.

Running two versions presents significant complexities, including managing updates, ensuring compatibility, and avoiding conflicts. Even so, the main reason behind these requests was compelling enough for us to adapt our practices:

**Preserving WordPress.org active install counts**.

When a free version is deactivated, WordPress.org stops counting it as an active install. For example, if a 100 free users upgrade to the paid version at once, WordPress.org would show zero active installs, even though the plugin remains active on all 100 sites. This can impact visibility, perception, and ranking on WordPress.org.

With [SDK version v2.10.1](https://github.com/Freemius/wordpress-sdk/releases/tag/2.10.1), we now support running both versions in parallel. While not enabled by default, makers can configure the SDK to activate this setup:`$my_fs = fs_dynamic_init( [ // ... existing configuration options. 'parallel_activation' => [ 'enabled' => true, 'premium_version_basename' => 'premium-slug/filename.php', ], ] );`  
We don’t recommend this approach for optimal user experience, but we recognize the importance of flexibility in giving makers greater control over how they manage their products.

### Freemius Officially Supports WordPress Playground

**WordPress Playground** lets users try any plugin or theme with just a click — no installation required. It runs directly in the browser, allowing makers to set up their products so users can launch a full WordPress environment with the plugin pre-installed, all without the need for servers.

Freemius now officially supports this feature, demonstrating our commitment to evolving with the WordPress ecosystem. By automatically bypassing the opt-in process when a free version with the opt-in mechanism is activated, we ensure a smooth demo experience for users testing in this environment. Since these trials are one-time tests and users often use dummy emails, skipping the opt-in process eliminates unnecessary interruptions.

In addition to WordPress Playground, Freemius now supports other demo environments like TasteWP and InstaWP, which many makers use to showcase their plugins. This integration ensures potential buyers can explore plugins effortlessly, creating a better first impression that can lead to more conversions.

### Pricing Page Updates

![customizable Freemius pricing page enhancements](https://freemius.com/blog/wp-content/uploads/2025/01/customizable-freemius-pricing-page-enhancements.jpeg)

In the [previous release notes](blog-freemius-release-notes-december.md), we announced the new pricing page bundled into the SDK while acknowledging a few glitches that needed to be resolved. Since then, we’ve addressed key maker requests and polished the experience significantly.

What’s new:

**Control over displaying prices annually or monthly:** To maximize conversions, prices are shown in monthly increments by default, even for annual plans (e.g., $100/year is displayed as $8.33/month billed annually).

While smaller numbers are typically more appealing to potential customers, some makers prefer showing the full annual price upfront. To accommodate this, we’ve added a filter that lets you control how prices are displayed to align with your preferences.

**Improved product icon customization:** Makers can now override the product icon on the pricing page using a new filter, giving them greater control over their branding.

**Flexible pricing layouts:** By default, the new pricing page splits plans with multiple tiers (e.g., single site, 5 sites, 20 sites) into separate packages. This reflects the structure most makers in the software ecosystem use. For those who prefer the previous setup (a single plan with radio buttons for tier selection), we’ve added an option to revert to that layout.

**Simplified custom CSS:** Adding custom CSS is now easier than ever, thanks to a new filter. Makers can quickly tailor the pricing page to match their brand and style. While CSS customization was always possible, this update makes the process more intuitive.

## Your Software Success, Your Way

This release marks another step forward in giving makers the freedom to manage their software businesses with confidence and clarity.

With the completion of the Data Liberation Project and support for features like WordPress Playground, we’re continuing to refine and adapt to your needs. From simplifying affiliate payouts to customizing pricing layouts and enabling seamless demos, these updates empower you with flexibility and transparency to grow your business your way.

As always, we’re here to support you. If you have questions, feedback, or want to explore how Freemius can help you scale, [reach out to us](https://freemius.com/cdn-cgi/l/email-protection#91f2feffe5f0f2e5d1f7e3f4f4fcf8e4e2bff2fefc) via email or [drop us a DM on X](https://x.com/freemius).