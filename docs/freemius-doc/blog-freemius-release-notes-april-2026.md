April’s release improves the experience on both sides of the transaction — for the makers building on Freemius and the buyers using their products. App makers get more native tooling. Analytics gets the filtering it needs. And a solid set of smaller improvements keeps everything underneath running as it should.

App makers often want buyers to have immediate access to their application after purchase.

Until now, making that happen required workarounds — download dialogs, redirecting buyers to external pages, manually customizing post-purchase emails, or writing custom JavaScript to surface links inside the Customer Portal.

Freemius now supports [configurable, labeled download links for apps](blog-changelog-new-custom-download-links-for-apps.md) as a first-class feature.

A new **Download Links** tab in the app’s **Settings** lets makers add as many links as needed, each with a label and a URL. This means separate links for different builds, versions, or assets, all managed from one place.

[![Freemius Customer Portal - Custom, labeled download links for apps ](https://freemius.com/blog/wp-content/uploads/2026/05/freemius-customer-portal-custom-labeled-download-links-for-apps.jpeg)](https://freemius.com/blog/wp-content/uploads/2026/05/freemius-customer-portal-custom-labeled-download-links-for-apps.jpeg)

Once configured, those links appear automatically in transactional emails after purchase and in the **Downloads** section of the Customer Portal (no custom code required).

[![Download links in post-purchase transactional buyer emails](https://freemius.com/blog/wp-content/uploads/2026/05/download-links-in-post-purchase-transactional-buyer-emails.jpeg)](https://freemius.com/blog/wp-content/uploads/2026/05/download-links-in-post-purchase-transactional-buyer-emails.jpeg)

Head to the [docs](help-documentation-saas-custom-download-links.md) to get it set up in minutes.

## Activations page in Customer Portal

When app makers used the Freemius API to handle license key activations outside of WordPress-native flows, buyers had no way to view or manage those activations from the Customer Portal.

Deactivating a license meant either using the app itself or contacting the maker directly, neither of which is a good buyer experience.

We’ve [introduced a new](blog-changelog-customer-portal-now-supports-app-activations-management.md) [**Activations**](blog-changelog-customer-portal-now-supports-app-activations-management.md) [page](blog-changelog-customer-portal-now-supports-app-activations-management.md) in the Customer Portal built specifically for app makers and their buyers.

Unlike the existing website views built for WordPress, the Activations page tracks devices and instances, which are the data points that matter in the app ecosystem.

From here, buyers can see every device or instance where their license is active.

[![Customer Portal Activations page](https://freemius.com/blog/wp-content/uploads/2026/05/customer-portal-activations-page.jpeg)](https://freemius.com/blog/wp-content/uploads/2026/05/customer-portal-activations-page.jpeg)

Clicking an item reveals the corresponding plan and offers a direct option to upgrade or downgrade. Buyers can also deactivate a license from a device, with a confirmation step before it takes effect.

[![Licenses by device in Customer Portal Activations page](https://freemius.com/blog/wp-content/uploads/2026/05/licenses-by-device-in-customer-portal-activations-page.jpeg)](https://freemius.com/blog/wp-content/uploads/2026/05/licenses-by-device-in-customer-portal-activations-page.jpeg)

Alongside the **Activations** page, the Customer Portal has been refined to remove irrelevant data for app and SaaS contexts.

The **Websites** and **Downloads** pages are WordPress-specific, and are now hidden when a store contains no WordPress or template products. The **Licenses** page is similarly hidden for stores with only SaaS products, since those don’t expose license keys to customers. These improvements carry through to system emails as well, keeping the experience consistent across every surface a buyer touches.

## Filtering in analytics charts

Analytics charts showing 20 or more series at once make it difficult to isolate what matters. A chart breaking down payments by country across every market is useful in aggregate but not when you’re trying to measure the impact of a campaign in a single region.

Freemius analytics charts [now support legend-based filtering](blog-changelog-analytics-charts-now-support-legend-based-filtering.md). Click any legend item to filter the chart to that selection. Select multiple items to compare them directly. The chart updates to show only the data you’ve selected.

[![Legend-based filtering in Freemius Developer Dashboard analytics charts](https://freemius.com/blog/wp-content/uploads/2026/05/legend-based-filtering-in-freemius-developer-dashboard-analytics-charts.jpeg)](https://freemius.com/blog/wp-content/uploads/2026/05/legend-based-filtering-in-freemius-developer-dashboard-analytics-charts.jpeg)

Geolocation is an obvious use case: filter the payments breakdown chart by one or a few countries to see exactly how a localized marketing effort is performing over time, without touching an export.

## Croatian language out of beta

Reaching buyers in their own language at checkout removes friction at the most critical point in the purchase flow.

After a brief beta period, Croatian (Hrvatski) is now [fully supported in Freemius Checkout](blog-changelog-freemius-checkout-now-fully-supports-hrvatski.md), brought to full release with help from the maker community.

Makers can set the checkout language parameter to `auto`, so buyers in Croatia see the checkout in their language automatically.

[![Croatian language in the Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2026/05/croatian-language-in-the-freemius-checkout.jpeg)](https://freemius.com/blog/wp-content/uploads/2026/05/croatian-language-in-the-freemius-checkout.jpeg)

The team has developed an efficient, AI-assisted process for generating new translations, with native speakers contributing to ensure accuracy. Croatian is the latest language to come through this pipeline (and it won’t be the last).

Native-speaking makers who want to see their language supported in checkout are [encouraged to reach out](https://freemius.com/cdn-cgi/l/email-protection#31525e5f4550524571574354545c5844421f525e5c) — the team will work it out with you.

## The maintenance crew

The features get the headlines, but the fixes and refinements underneath are what keep the platform dependable. This month’s smaller updates span payouts, checkout, the Customer Portal, and the Developer Dashboard.

**Payouts**

- [Billing information is now required before setting up a payout method](blog-changelog-billing-information-is-now-required-before-setting-up-a-payout-method.md)

**Checkout**

- [PayPal checkout outage resolved with added safeguards](blog-changelog-paypal-checkout-outage-resolved-with-added-safeguards.md)
- [Checkout trial title now includes product name](blog-changelog-checkout-trial-title-now-includes-product-name.md)
- [Fixed renewal notice regression for deleted pricing](blog-changelog-fixed-renewal-notice-regression-for-deleted-pricing.md)
- [Checkout quality of life fixes for navigation and bundle upgrades](blog-changelog-checkout-quality-of-life-fixes-for-navigation-and-bundle-upgrades.md)

**Developer Dashboard**

- [Bundle product form fixed with clearer product selection UX](blog-changelog-bundle-product-form-fixed-with-clearer-product-selection-ux.md)
- [Developer Dashboard QoL fixes for tables and email history](blog-changelog-developer-dashboard-qol-fixes-for-tables-and-email-history.md)
- [Better product settings UX, transfer flow updates, and SaaS refund improvements](blog-changelog-better-product-settings-ux-transfer-flow-updates-and-saas-refund-improvements.md)

**Customer Portal**

- [Updated default profile avatar](blog-changelog-updated-default-profile-avatar-in-customer-portal.md)
- [Customer Portal UX improvements for SaaS products](blog-changelog-customer-portal-ux-improvements-for-saas-products.md)

**API and backend**

- [Backend and API improvements for license validation and free plan detection](blog-changelog-backend-and-api-improvements-for-license-validation-and-free-plan-detection.md)

## Better in more places

A lot landed this month. Native download links for app makers, a full Activations page for app buyers, legend-based filtering in analytics, and Croatian language at checkout. Each one closes a real gap and together they make the platform more capable for the makers building on it.

What’s next is shaped by what you’re running into or thinking of — [so keep the feedback coming](https://freemius.nolt.io/).