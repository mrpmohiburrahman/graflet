---
title: "Add Event listeners & Analytics Tracking in the Checkout"
url: "https://freemius.com/help/documentation/checkout/features/tracking-analytics/"
source: "docs"
section: "Docs"
category: "Checkout"
scraped_at: "2026-04-09T19:58:37+06:00"
word_count: 541
---

Freemius Checkout provides multiple ways to track user interactions and purchases for advanced analytics and conversion tracking.

## Tracking purchases with Google Analytics and Facebook[​](#tracking-purchases-with-google-analytics-and-facebook "Direct link to Tracking purchases with Google Analytics and Facebook")

The easiest way to track purchase conversions with external analytics and conversion tracking tools like Google Analytics is by leveraging the `purchaseCompleted` callback.

Here is an implementation example:

```javascript
checkout.open({
  // ...
  purchaseCompleted: function (response) {
    // This code is for paid trial only. To track free trials, you can check for response.trial object.
    var isTrial = null != response.purchase.trial_ends,
      isSubscription = null != response.purchase.initial_amount,
      total = isTrial
        ? 0
        : (isSubscription
            ? response.purchase.initial_amount
            : response.purchase.gross
          ).toString(),
      productName = 'Product Name',
      storeUrl = 'https://your-site.com',
      storeName = 'Store Name';

    // Facebook Pixel tracking code.
    if (typeof fbq !== 'undefined') {
      fbq('track', 'Purchase', {
        currency: response.purchase.currency.toUpperCase(),
        value: total,
      });
    }

    // The new GA4 gtag based tracking code.
    if (typeof gtag !== 'undefined') {
      gtag('event', 'purchase', {
        transaction_id: response.purchase.id.toString(), // Transaction ID. Required.
        affiliation: storeName, // Affiliation or store name.
        value: total, // Grand Total.
        shipping: 0, // Shipping.
        tax: 0, // Tax.
        currency: response.purchase.currency.toUpperCase(), // Currency.
        items: [
          {
            item_id: response.purchase.plugin_id.toString(), // SKU/code.
            item_variant: response.purchase.plan_id.toString(), // SKU/code.
            item_name: productName, // Product name. Required.
            item_category: 'Plugin', // Category or variation.
            price: total, // Unit price.
            quantity: 1, // Quantity
            currency: response.purchase.currency.toUpperCase(), // Currency.
          },
        ],
      });

      gtag('event', 'page_view', {
        page_title: '/purchase-completed/',
        page_location: storeUrl + '/purchase-completed/',
      });
    }
  },
  // ...
});
```

tip

To leverage this method via the WordPress In-dashboard/Admin checkout, utilize the [checkout/purchaseCompleted](help-documentation-wordpress-sdk-filters-actions-hooks.md#checkoutpurchasedcompleted) filter method.

## Advanced Event Tracking[​](#advanced-event-tracking "Direct link to Advanced Event Tracking")

You can leverage the `track` callback handler to act upon different checkout actions taken by the user. Here's how you can use it including the list of the currently supported events:

```javascript
checkout.open({
  // ...

  track: function (event, data) {
    const product = data.product;
    const user = data.user;
    const plan = data.plan;
    // More data may be available depending on the event type.

    switch (event) {
      case 'load':
        // Checkout loaded.
        break;
      case 'currency-changed':
        // Currency changed.
        break;
      case 'licenses-inc':
        // Licenses # increased.
        break;
      case 'licenses-dec':
        // Licenses # decreased.
        break;
      case 'billing-cycle-updated':
        // Billing cycle update.
        break;
      case 'email-updated':
        // Email address set or updated.
        break;
      case 'coupon-updated':
        // Coupon set or updated.
        break;
      case 'paypal-express-checkout':
        // PayPal express checkout started.
        break;
      case 'review-order':
        // User moved to review mode, i.e., they already filled up their payment method details and ready to confirm the purchase.
        break;
      case 'cooling-off-waiver-toggled':
        // Cooling-off waiver toggled (only relevant for EU buyers).
        break;
      case 'complete':
        // Purchase completed.
        break;
      case 'exit-intent-shown':
        // Exit intent shown.
        break;
      case 'exit-intent-promotion-ended':
        // Exit intent promotion ended.
        break;
      case 'exit-intent-discount-applied':
        // Exit intent discount applied.
        break;
      case 'exit-intent-discount-canceled':
        // Exit intent discount denied.
        break;
      case 'coupon-added':
        // Coupon successfully applied to the Checkout.
        break;
      case 'coupon-removed':
        /**
         * Coupon removed from the Checkout either due to deliberate removal or because the coupon is no longer applicable to the current checkout.
         *
         * @see https://freemius.com/help/documentation/selling-with-freemius/coupon-discount/#creating-same-coupon-with-discounts-for-different-plans
         */
        break;
      case 'coupon-updated':
        /**
         * Coupon updated in the Checkout because of some action that affected its applicability or discount value.
         *
         * @see https://freemius.com/help/documentation/selling-with-freemius/coupon-discount/#creating-same-coupon-with-discounts-for-different-plans
         */
        break;
    }
  },

  // ...
});
```