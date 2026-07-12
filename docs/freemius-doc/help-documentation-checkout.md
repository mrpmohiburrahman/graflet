---
title: "Checkout"
url: "https://freemius.com/help/documentation/checkout/"
source: "docs"
section: "Docs"
category: "Checkout"
scraped_at: "2026-04-09T19:58:37+06:00"
word_count: 512
---

The **Freemius Checkout** is a secure, embeddable checkout solution crafted to help software makers sell their products effortlessly. Whether you are selling SaaS, WordPress plugins, desktop apps, or web browser extensions, Freemius offers a seamless and secure payment experience for your customers, accepting global payments without writing custom code.

## Integrating the Freemius Checkout[​](#integrating-the-freemius-checkout "Direct link to Integrating the Freemius Checkout")

The Freemius Checkout provides multiple ways for customers to purchase your product, including:

- [Checkout Overlay](help-documentation-checkout-integration-overlay-checkout.md)
- [Hosted Checkout](help-documentation-checkout-integration-hosted-checkout.md)
- [In-Dashboard Upgrading in WP Admin](help-documentation-getting-started-making-your-first-sale.md#in-dashboard-upgrading-in-wp-admin) - *available for WordPress plugins and themes only*

### Processing a Purchase[​](#processing-a-purchase "Direct link to Processing a Purchase")

For WordPress products, the Checkout provides a license key immediately after a purchase and your customers can start using your product right away. See our [setup guide](help-documentation-wordpress.md).

For SaaS & Apps, you might often want to process the purchase on your end. It can be facilitated using webhooks or API calls along with the checkout's [redirections](help-documentation-checkout-integration-hosted-checkout.md#redirection-after-a-successful-purchase) or [callbacks](help-documentation-checkout-integration-freemius-checkout-buy-button.md#callbacks) feature. See our [SaaS & Apps setup guide](help-documentation-saas.md) for more details.

### Embedding or Linking the Checkout[​](#embedding-or-linking-the-checkout "Direct link to Embedding or Linking the Checkout")

You can embed Freemius Checkout in your website, email marketing, and social media using:

- The generated checkout links or overlay code snippet from the Freemius Developer Dashboard.

<!--THE END-->

- Or the [Freemius for WordPress plugin](help-documentation-wordpress-freemius-for-wordpress.md) if your customer-facing site is built on WordPress.

**Read the [Integration Guides](help-documentation-checkout-integration.md) to get started.**

## Key Capabilities[​](#key-capabilities "Direct link to Key Capabilities")

### Payment Methods[​](#payment-methods "Direct link to Payment Methods")

Securely accept credit cards and PayPal with full SCA and 3DS 2.0 compliance for European markets.

### Subscription Billing with Dunning[​](#subscription-billing-with-dunning "Direct link to Subscription Billing with Dunning")

Supports full subscription management, auto-renewals, and [failed-payment recovery mechanisms](help-documentation-marketing-automation-dunning-failed-payments.md) that help stabilize recurring revenue streams.

### One-off or Lifetime Purchases[​](#one-off-or-lifetime-purchases "Direct link to One-off or Lifetime Purchases")

Sell one-time or lifetime purchases alongside subscriptions. Useful to sell lifetime licenses for installable software or consumable units for SaaS products.

### Easy Upgrades & Downgrades[​](#easy-upgrades--downgrades "Direct link to Easy Upgrades & Downgrades")

Freemius Checkout supports [proration](help-documentation-checkout-features-proration.md) out of the box, allowing customers to upgrade or downgrade their plans seamlessly.

### Global-Ready Features[​](#global-ready-features "Direct link to Global-Ready Features")

- [Multi-currency](help-documentation-selling-with-freemius-multi-currency.md) supporting USD, EUR, and GBP.
- Available in multiple languages, including English, Spanish, German, French, Italian, and Dutch.
- Automated tax compliance: UK and EU VAT, US sales tax based on the buyer's geo-location.
- Various payment methods: Credit Cards, PayPal, and iDeal (Netherlands).

### Conversion Optimization Tools[​](#conversion-optimization-tools "Direct link to Conversion Optimization Tools")

To improve conversion rates, the checkout includes the following features:

- [Cart abandonment recovery](help-documentation-marketing-automation-cart-abandonment-recovery.md)
- [Exit-intent coupons](help-documentation-marketing-automation-special-coupons-discounts.md#exit-intent-coupon--1-hour-fomo)
- [Upsells](help-documentation-checkout-features-upsell-toggles.md)
- [Social-proofing](help-documentation-checkout-features-social-proofing-ui.md)

### Developer-Friendly & Customizable[​](#developer-friendly--customizable "Direct link to Developer-Friendly & Customizable")

- [Customizable features](help-documentation-checkout-customization-customizing-confirmation-dialog.md) to match your approach.
- Supports [advanced tracking and analytics integrations](help-documentation-checkout-features-tracking-analytics.md).
- Style the checkout to match your brand via [custom CSS](help-documentation-checkout-customization-applying-css-customization.md).
- Feature-rich [Buy Button API](help-documentation-checkout-integration-freemius-checkout-buy-button.md) for advanced use cases.

### Security & Compliance[​](#security--compliance "Direct link to Security & Compliance")

- [GDPR-ready](help-documentation-checkout-features-gdpr.md) and PCI compliant.
- Accessibility baked in out of the box.