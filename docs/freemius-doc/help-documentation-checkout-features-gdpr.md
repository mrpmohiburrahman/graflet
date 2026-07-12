---
title: "Freemius Checkout GDPR and Privacy-Related Compliance"
url: "https://freemius.com/help/documentation/checkout/features/gdpr/"
source: "docs"
section: "Docs"
category: "Checkout"
scraped_at: "2026-04-09T19:58:37+06:00"
word_count: 493
---

As a [Merchant of Record](merchant-of-record.md), we (Freemius) take GDPR and privacy compliance seriously. The Freemius Checkout exposes the following user interfaces (UI) to help you comply with applicable regulations when using our services.

note

Please note that the UIs will display only when required based on the buyer's location or billing details.

## Marketing Consent UI[​](#marketing-consent-ui "Direct link to Marketing Consent UI")

This interface is designed to obtain explicit consent from users for marketing communications. The information is saved in Freemius, and you can view it in the Developer Dashboard under the specific user's profile.

By default, the UI will be shown to all EU-based buyers and buyers from other countries where similar privacy regulations are in place. The UI does not include any default selection, meaning all new users must explicitly opt in to receive marketing communications.

For existing buyers, we populate the radio button based on their previous consent status. If the buyer has already opted in, we do not display the UI to streamline the checkout process.

The behavior of this UI can be customized using the [`gdpr`](help-documentation-checkout-integration-freemius-checkout-buy-button.md#gdpr) parameter of the Checkout. It supports the following values:

- `default`: Show the UI only to new buyers from applicable regions. The radio button will have no default value.
- `opt_out`: Same as `default`, but the radio button will be pre-selected to `No` for new buyers. This helps reduce friction during checkout while still complying with regulations. The trade-off is that you will likely see lower opt-in rates for marketing communications.
- `hidden`: Hide the UI completely; for new buyers, their marketing consent will not have any value (set to `null`). Use this option when you do **not** want Freemius to collect marketing consent from your buyers at all.

Example of Customizing the GDPR Parameter

```js
checkout.open({
  gdpr: 'hidden',
});
```

## EU 14-Day Cooling-Off Waiver UI[​](#eu-14-day-cooling-off-waiver-ui "Direct link to EU 14-Day Cooling-Off Waiver UI")

This interface informs EU-based buyers about the [14-day cooling-off period](https://en.wikipedia.org/wiki/Cooling-off_period_%28consumer_rights%29) waiver for digital products (both SaaS and downloadable software such as WordPress products). It ensures that buyers are aware of their rights and the implications of purchasing digital goods.

Due to regulatory requirements, this UI cannot be customized and will show up automatically for EU-based buyers unless your product's refund policy exceeds the regulatory requirement.

How Refund Policy Affects This UI

The text automatically adjusts based on your product type and configured [refund policy](help-documentation-selling-with-freemius-refund-policy.md).

Specifically, if you have configured a [Double Guarantee](help-documentation-selling-with-freemius-refund-policy.md#flexible---double-guarantee) refund policy for more than 14 days, this UI will be automatically hidden since your policy provides buyers with greater protection than the 14-day minimum.

## Cart Reminder Notice UI[​](#cart-reminder-notice-ui "Direct link to Cart Reminder Notice UI")

This interface is shown to buyers from regulatory regions and allows them to opt out of [cart reminder emails](help-documentation-marketing-automation-cart-abandonment-recovery.md) sent by Freemius on behalf of merchants.

In certain locations, depending on local regulations, the cart is disabled by default and buyers must explicitly opt in to enable it.