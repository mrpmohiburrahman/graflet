[Changelog](https://freemius.com/changelog/) / Checkout phase2 final rollout with some bug fixes

Following our [rollout schedule](blog-changelog-checkout-reskinning-preparing-the-phase2-version-for-production-rollout.md), we’ve made the new Checkout design the default in production. From today onwards the new checkout design will show up, regardless of the status of the CSS migration.

[![](https://freemius.com/blog/wp-content/uploads/2024/08/Cover-image-1024x576.png)](https://freemius.com/blog/wp-content/uploads/2024/08/Cover-image.png)

If you aren’t using custom CSS or have already migrated your custom CSS, then you are all set. Otherwise, we request you to do that as soon as possible. Please read our [changelog](blog-changelog-checkout-reskinning-preparing-the-phase2-version-for-production-rollout.md) and [documentation](https://freemius.com/go/checkout-css-customization/) for help with the CSS migration.

If for some reason you still want to use the legacy checkout, you can use the JavaScript parameter `checkout_style: 'legacy'`. But please note, you have until September 29th, 2024, after which the legacy Checkout will be completely removed.

### Enabling the monthly switch by default

While introducing the upsell concept, we made the annual/monthly upsell switch hidden when the Checkout already loads in the “annual” billing cycle.

[![](https://freemius.com/blog/wp-content/uploads/2024/08/checkout-annual-upsell-1024x482.png)](https://freemius.com/blog/wp-content/uploads/2024/08/checkout-annual-upsell.png)

Following our maker’s feedback and discussing some cases, we understand it can be a bit confusing for some specific cases. Especially when:

1. The checkout is loaded from the WordPress SDK – Since users can miss the billing cycle when clicking some promotional notice coming from the plugin/theme itself.
2. The checkout is in license renewal/upgrade mode – A user may want to change the billing cycle from annual to monthly or vice-versa.

Hence for the two cases, we are now showing the switch by default. Additionally, you can always use the `show_monthly_switch` parameter and choose to show it all the time.

You can find more about all the new configuration options [here](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md#fs-phase2-checkout).

### Other bug fixes

- Fixed the positioning of the [exit intent modal](help-documentation-marketing-automation-special-coupons-discounts.md#exit_intent_coupon_1_hour_fomo).
- Fixed refund policy UI showing up incorrectly in some edge cases.