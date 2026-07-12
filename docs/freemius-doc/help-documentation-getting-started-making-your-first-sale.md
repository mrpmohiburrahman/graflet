---
title: "Making Your First Sale"
url: "https://freemius.com/help/documentation/getting-started/making-your-first-sale/"
source: "docs"
section: "Docs"
category: "Getting Started"
scraped_at: "2026-04-09T19:58:38+06:00"
word_count: 685
---

Welcome to your first steps selling through Freemius! This guide will help you set up and test your checkout/buy button to ensure everything is working perfectly before going live.

Freemius offers multiple ways for users to purchase your product:

- Hosted Checkout
- Checkout Overlay
- In-Dashboard Upgrading in WP Admin

## Hosted Checkout[​](#hosted-checkout "Direct link to Hosted Checkout")

Freemius provides direct checkout links to our hosted checkout, offering a no-code integration method.

### Access Checkout Links[​](#access-checkout-links "Direct link to Access Checkout Links")

1. In the **Plans** section of your Developer Dashboard.
2. Click the **Get Checkout** button next to each configured plan.
3. Select the **Production Link** option.

### Choose the Appropriate Link[​](#choose-the-appropriate-link "Direct link to Choose the Appropriate Link")

You'll see options for testing and live payments.

- **Sandbox Link:** Ideal for simulating purchases to ensure everything functions correctly.
- **Production Link:** Use this when you're ready to start accepting real payments.

### Use Cases for Checkout Links[​](#use-cases-for-checkout-links "Direct link to Use Cases for Checkout Links")

These checkout links are handy for many reasons. Here are a few ways you can use them:

- **Testing:** The testing link is the easiest way to test your checkout process.
- **Direct Sales:** Send custom plan links to specific customers.
- **Social Promotion:** Share checkout links directly on social platforms to streamline the buying process.
- **Plan Management:** Provide customers direct links for upgrades or renewals by combining [querystring parameters](help-documentation-checkout-integration-freemius-checkout-buy-button.md) to specify the license key, target update plan, and billing cycle.

## Checkout Overlay Dialog[​](#checkout-overlay-dialog "Direct link to Checkout Overlay Dialog")

For a native and seamless user experience, embed the checkout as an overlay on your website.

### Get the Buy Button Checkout Code[​](#get-the-buy-button-checkout-code "Direct link to Get the Buy Button Checkout Code")

1. In the **Plans** section.
2. Click **Get Checkout** button next to the desired plan.
3. Select the **Overlay Code** option.

### Embed the JavaScript Snippet[​](#embed-the-javascript-snippet "Direct link to Embed the JavaScript Snippet")

Copy the provided JavaScript code and paste it into your website's HTML where you want the Buy Button to appear.

tip

You can share this code with partners to place a Buy Button for your product directly on their site, reducing the steps to purchase.

tip

The overlay checkout snippet is platform-agnostic and can be used on any website. So, for example, even if you sell WordPress plugins, it doesn’t mean you have to use WordPress for your website to sell them.

One major advantage of using the Buy Button is how simple it is to create a fully functional eCommerce experience for any software product.

If your product is growing and needs a dedicated site, just build your new website using any platform or technology you prefer and embed the Freemius checkout code. That’s it! You now have a complete eCommerce solution, including licensing, payments, subscriptions, and more, all seamlessly integrated into your new site.

In contrast, other eCommerce solutions for WordPress products, like [WooCommerce](freemius-vs-woocommerce.md) or [Easy Digital Downloads](freemius-vs-edd.md), require running WordPress and their plugins on your site. This setup also stores all data in your WordPress site’s database, making it challenging and time-consuming to move a specific product to a new site.

Freemius offers greater flexibility, freeing you from these limitations and allowing you to integrate eCommerce functionality wherever you choose.

## In-Dashboard Upgrading in WP Admin[​](#in-dashboard-upgrading-in-wp-admin "Direct link to In-Dashboard Upgrading in WP Admin")

When you [integrate Freemius’ WordPress SDK](help-documentation-wordpress-integration-with-sdk.md) into your plugin or theme, the free version automatically includes a pricing table and a purchase button, enabling customers to purchase directly from their WP Admin dashboard. We call this *In-Dashboard Upgrading*.

The pricing and features on this table automatically sync with what you’ve configured in the **Plans** section of your Developer Dashboard, keeping everything up-to-date and consistent.

tip

If you’d like to hide a plan from the WP Admin pricing table, you can do so by toggling the **Is Hidden** switch in the **Plans** section.

For more information, check out the [complete Checkout API documentation](help-documentation-checkout-integration-freemius-checkout-buy-button.md) to explore additional customization options, like hiding the coupon section, loading the checkout with a specific billing cycle, and much more.