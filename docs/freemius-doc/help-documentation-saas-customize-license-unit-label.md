---
title: "Customize License Unit Label"
url: "https://freemius.com/help/documentation/saas/customize-license-unit-label/"
source: "docs"
section: "Docs"
category: "Setup for SaaS & Apps"
scraped_at: "2026-04-09T19:58:42+06:00"
word_count: 159
---

SaaS and Applications have specific words to reference the units of measure (primary entitlement) for the digital product being sold, e.g.

- A SaaS product might sell “Seats”.
- Applications might sell “Activations”.

Freemius empowers SaaS and Application makers to customize the license unit label accordingly. To configure this:

1. Log in to the [Developer Dashboard](https://dashboard.freemius.com).
2. Navigate to the relevant product’s ***Settings*** page.
3. Locate the **Selling Unit** Label option and input the singular form of the unit (e.g., “Seat” or “Activation”). Our system will handle the rest.

The new label will be reflected in the checkout when customers are making purchases in the checkout dropdown.

Similarly, in the purchase confirmation email sent to the customer after a successful checkout.

note

Our system will always include the custom unit label in emails for Applications that require license activation by default. However, for SaaS products, this depends on whether you have chosen to [expose the license key to users](help-documentation-saas-integrating-license-key-activation.md#revealing-license-keys-to-customers).