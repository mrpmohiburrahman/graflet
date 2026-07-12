[Changelog](https://freemius.com/changelog/) / New Coupon Type for Migrated Customers and Other Coupon-Related Bug Fixes

At Freemius, we support [migrations](help-documentation-migration.md) from platforms like EDD, WooCommerce, Envato, and more. To help you maximize the benefits of the Freemius platform—such as tax compliance and subscription recovery—we recommend encouraging your buyers to update their licenses through Freemius.

[![](https://freemius.com/blog/wp-content/uploads/2024/11/coupon-config-migrated-customer-1024x774.png)](https://freemius.com/blog/wp-content/uploads/2024/11/coupon-config-migrated-customer.png)

To make this easier, we’ve introduced a new [coupon](help-documentation-marketing-automation-special-coupons-discounts.md#how_to_create_a_discount_coupon) type called **“Migrated Customers”**. This option allows you to target customers with a migrated license who have never purchased your product through Freemius, providing an incentive while minimizing the risk of misuse.

This feature was inspired by feedback from our community of makers. Thank you for your valuable suggestions! If you have more feedback or ideas to help us enhance our platform, please share them on our [feature board](https://freemius.nolt.io/).

### Other coupon related bug fixes

#### Exit intent popup bug fix

[![](https://freemius.com/blog/wp-content/uploads/2024/11/exit-intent-modal-1024x903.png)](https://freemius.com/blog/wp-content/uploads/2024/11/exit-intent-modal.png)

We identified an issue where the [exit intent coupon](help-documentation-marketing-automation-special-coupons-discounts.md#exit_intent_coupon_1_hour_fomo) modal would display even if the coupon configuration did not match the current pricing, currency, or billing cycle. This has now been resolved.

#### Issues with renewing migrated licenses

[![](https://freemius.com/blog/wp-content/uploads/2024/11/coupon-discount-relative-1024x777.png)](https://freemius.com/blog/wp-content/uploads/2024/11/coupon-discount-relative.png)

We also addressed several edge-case bugs related to renewing migrated licenses with coupons and applying renewal discounts to migrated subscriptions. The following improvements have been made:

- The system now extends the license with the full coupon discount if the migrated subscription is inactive.
- If the migrated subscription is active, it will be canceled with a prorated discount and the appropriate coupon discount.

Additionally, the UI will now display a detailed breakdown of coupon discounts to avoid any confusion.

If you want to migrate your product from any platform to Freemius, please get in touch with our [support](https://freemius.com/cdn-cgi/l/email-protection#6d1e181d1d021f192d0b1f08080004181e430e0200).