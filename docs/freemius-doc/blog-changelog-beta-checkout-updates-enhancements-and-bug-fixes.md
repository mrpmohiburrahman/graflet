We are rolling out several enhancements and bug fixes for our beta checkout (internally code named as `phase2`). If you’ve missed the changelog/announcement post, you can find it [here](blog-changelog-beta-release-dual-column-checkout-with-upsells-and-social-proofing.md).

To give it a try, simply add `checkout_style=phase2` in the URL parameter or `checkout_style: 'phase2'` in the [JavaScript integration](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md).

Now let’s see what are the new changes.

### Fixed Coupons UI when changing between billing cycles and licenses

From the Freemius Developers Dashboard, you can create coupons with several configurations. For example, you can generate a coupon applicable only for a particular billing cycle or a specific number of licenses.

Previously while such coupons were active, changing the billing cycle or the licenses would not invalidate the coupon UI, keeping the old code in place.

[![Fixed coupons UI in Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2024/06/coupons-ui-fix-freemius-checkout.gif)](https://freemius.com/blog/wp-content/uploads/2024/06/coupons-ui-fix-freemius-checkout.gif)

We have fixed this UI regression. Now the coupon code line will disappear if the coupon is not applicable anymore. Instead, the user will have the option to re-enter a new coupon code. Changing the billing cycle or licenses back to the original value will show the applicable coupon again.

### Fixed the upsell price difference calculation logic

Previously we calculated the price difference in license and billing cycle upsells based on the “subtotal” price. We realized it could be misleading because there can be coupon discounts, taxes, pro-rated discounts, etc.

[![Upsell price difference logic fix in Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2024/06/upsell-price-difference-freemius-checkout-1024x419.png)](https://freemius.com/blog/wp-content/uploads/2024/06/upsell-price-difference-freemius-checkout.png)

The upsell price difference will be calculated based on **Today’s total** amount now.

### Specifying a review by providing an ID

With the new ability to feature a review right within the checkout, we’ve been auto-selecting a “featured” review with a 5-star rating. While this behavior will still be the default, you can now pass a new parameter `review_id` to specifically select the review you want to show.

[![Getting the ID of a review from Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2024/06/freemius-reviews-id-developer-dashboard-1024x403.png)](https://freemius.com/blog/wp-content/uploads/2024/06/freemius-reviews-id-developer-dashboard.png)

To know the ID of a review, kindly look at the `ID` column inside the Developer Dashboard.

### Fixed Renewals Discount line

We were incorrectly showing a percentage value in the renewals discount line, even if a fixed value was configured.

[![Renewal discount line with fixed value in Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2024/06/freemius-checkout-renewals-discount-badge.png)](https://freemius.com/blog/wp-content/uploads/2024/06/freemius-checkout-renewals-discount-badge.png)

We have now fixed it to follow the configuration you’ve set from the Developer Dashboard.

### Trimming large reviews

We are now trimming large reviews to keep the UI consistent.

[![Trimming large review - Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2024/06/freemius-large-review-trimmed-checkout-1024x541.png)](https://freemius.com/blog/wp-content/uploads/2024/06/freemius-large-review-trimmed-checkout.png)

The review will be shown in full when it is hovered on.

### Checkout Page mode

We’ve always had a `page` mode for the checkout, to support standalone checkout URLs.

For example you could open the checkout with `https://checkout.freemius.com/mode/page/plugin/:plugin_id/[/plan/:plan_id/]...` etc.

But it was never really “feature complete”.

[![Freemius checkout in page mode](https://freemius.com/blog/wp-content/uploads/2024/06/freemius-checkout-page-mode-1024x848.png)](https://freemius.com/blog/wp-content/uploads/2024/06/freemius-checkout-page-mode.png)

In this iteration, we are finally making it complete. The `mode/page` is an optional and backward-compatible parameter. It is applicable only when the checkout is opened directly (not from the SDK or JS integration). A `page` mode of the checkout means

1. The checkout will show up in two columns/horizontal layout by default. You can still use the parameters, for example, to force the `layout` to `vertical`.
2. If present a back button will be shown (more on it later).
3. The social proofing (money-back guarantee and reviews) will be shown by default. You can also disable them by using the appropriate parameter (as written [here](blog-changelog-beta-release-dual-column-checkout-with-upsells-and-social-proofing.md)).
4. The close and expand button with the header will not be shown.

To make it more user-friendly, we are showing the `page` view even when the checkout is opened with `mode/dialog` but not embedded in an iFrame. In time, you can even drop the `mode/dialog` or `mode/page` from the URL and it will load the correct mode automatically.

### Cancel-URL for the checkout

We have a new feature for the page mode, called the “cancel URL”, which can take the user back in case they want to cancel the purchase.

[![Freemius checkout back button with the cancel_url parameter](https://freemius.com/blog/wp-content/uploads/2024/06/freemius-checkout-back-button-1024x425.png)](https://freemius.com/blog/wp-content/uploads/2024/06/freemius-checkout-back-button.png)

- You can link the checkout from your website and the “Cancel URL” will be automatically picked up from the `Referer` header (if present).
- We have an explicit parameter `cancel_url` using which you can modify the URL.
- The icon will be automatically generated based on the favicon of the website. But you can override it with the `cancel_icon` URL.
- The link and the image will only work if they are `https`.
- The `hostname` (subdomain + domain) of the cancel URL will be shown in the button.

Please note they will not show up for the regular JS-based integration where the checkout opens in a popup/modal.

### Introduced a new option to always show the monthly/annual switch

While introducing the upsell concept, we intentionally removed the billing cycle UI and the ability to switch to lower billing cycles in the checkout. For example, when the checkout is loaded in the “Annual” billing cycle, the user cannot go to the “Monthly” billing cycle.

[![Always showing monthly switch - Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2024/06/freemius-checkout-monthly-switch-1024x361.png)](https://freemius.com/blog/wp-content/uploads/2024/06/freemius-checkout-monthly-switch.png)

But following partners feedback, we have introduced a parameter `show_monthly_switch` which will bring back the toggle as shown above. Set `show_monthly_switch=true` in the URL parameter or `show_monthly_switch: true` in the JS-integration.

### Improved the Exit Intent UI

We noticed that when the checkout is loaded with [JS-integration/buy button](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md) API, clicking the “No Thanks” button of the [exit intent popup](help-documentation-marketing-automation-special-coupons-discounts.md#exit_intent_coupon_1_hour_fomo) would not close the checkout.

[![Exit intent UI with promotional coupon - Freemius Checkout](https://freemius.com/blog/wp-content/uploads/2024/06/freemius-checkout-exit-intent-coupon-1024x936.png)](https://freemius.com/blog/wp-content/uploads/2024/06/freemius-checkout-exit-intent-coupon.png)

We have fixed this.

### Inline currency selector

This was a great feature suggestion from our partners.

[![Freemius checkout - Inline currency selector](https://freemius.com/blog/wp-content/uploads/2024/06/inline-currency-selector-freemius-checkout.gif)](https://freemius.com/blog/wp-content/uploads/2024/06/inline-currency-selector-freemius-checkout.gif)

If you support multiple currencies, then apart from showing the currency selector in the footer, we are also showing it right alongside the “Today’s total” line. This brings more visibility to it.

### Other bug fixes/notable changes

- Fixed the `title` parameter not being respected.
- We are now appending the plan title by default in the cart header. This can of course be changed with the `title`paramerer.
- We noticed and fixed some UI regression in the Safari browser.
- We have fixed various UI glitches/regressions.
- We have decided to drop the `subtitle` support. You can modify the `title` parameter to tweak it to your liking.

[Learn more »](blog-freemius-release-notes-june-2024.md)