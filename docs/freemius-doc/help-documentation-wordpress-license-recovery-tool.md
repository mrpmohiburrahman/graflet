---
title: "License Recovery Tool for WordPress Customers"
url: "https://freemius.com/help/documentation/wordpress/license-recovery-tool/"
source: "docs"
section: "Docs"
category: "Setup for WordPress"
scraped_at: "2026-04-09T19:58:45+06:00"
word_count: 297
---

Sometimes, customers may misplace their license keys or download links for your WordPress plugins or themes.

While this information can be found in [their account](https://customers.freemius.com), to help them recover this information quickly and easily using only their email address, Freemius offers a License Recovery Self-Service tool.

## How It Works[​](#how-it-works "Direct link to How It Works")

When a customer submits the form, Freemius automatically sends them an email on your behalf, containing download links for their purchased products along with all associated license keys.

This lightweight recovery flow gives your buyers a quick way to help themselves, which can significantly reduce routine support tickets.

## Setting Up Links[​](#setting-up-links "Direct link to Setting Up Links")

We offer two types of links to the license recovery tool.

### Product-Specific License[​](#product-specific-license "Direct link to Product-Specific License")

For a specific product, create a button or link using the URL pattern below:

```text
https://dashboard.freemius.com/license-recovery/{product_id}/{product_slug}/
```

For example, using a product with ID `11707` and slug `my-awesome-plugin`, the URL would be:

```text
https://dashboard.freemius.com/license-recovery/11707/my-awesome-plugin/
```

We recommend adding these links to your product's FAQ or support pages for easy access.

Where to Find Your Product ID and Slug

You can find the `product_id` and `product_slug` in your [Developer Dashboard](https://dashboard.freemius.com/) under the **Settings** page of the desired product.

- To get your `product_slug`, select the **Information** tab and check the `slug` field.
- To get your `product_id`, select the **API & Keys** tab and check the `ID` field under the **Product Keys** section.

### Developer Account-Wide License[​](#developer-account-wide-license "Direct link to Developer Account-Wide License")

If you prefer offering a unified recovery page for your entire developer account, use:

```text
https://dashboard.freemius.com/license-recovery/{developer_id}/
```

Where to Find Your Developer ID

Your `developer_id` is available via [your Profile page](https://dashboard.freemius.com/#!/profile/). Scroll to the bottom of the page under the **Keys** section.