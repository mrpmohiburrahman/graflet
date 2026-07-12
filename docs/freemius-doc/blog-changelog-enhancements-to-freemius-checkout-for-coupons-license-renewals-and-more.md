[Changelog](https://freemius.com/changelog/) / Enhancements to Freemius Checkout for Coupons, License Renewals, and More

This week, we’ve implemented fine-tuned adjustments and enhancements to the Freemius Checkout, with a particular focus on coupon handling and migrated license renewals.

### Coupon discount for migrated license update with active subscription

When updating a license, a new subscription may be created. If time remains on the current license before it expires, a pro-rated discount is applied to the renewal process up-front.

If a coupon is entered during this process, the coupon amount for the first payment of the renewal is adjusted to account for the [pro-rated discount](help-documentation-selling-with-freemius-proration.md). Previously, this adjustment was not clearly disclosed in the UI, leading to some confusion.

[![](https://freemius.com/blog/wp-content/uploads/2024/11/checkout-coupon-migrated-license-active-subscription-1024x706.png)](https://freemius.com/blog/wp-content/uploads/2024/11/checkout-coupon-migrated-license-active-subscription.png)

The UI has now been enhanced to show the exact breakdown of the coupon, ensuring clarity for the buyer. After the first payment, buyers will see that they will receive the full coupon discount on all future renewals.

Please note: This behavior only applies to migrated licenses with active subscriptions. For standard license upgrades, where a buyer opts to upgrade their license to a higher pricing tier or plan, the full coupon discount is applied, even on the first payment of the new subscription.

### Coupon discount for migrated license extension with expired subscription

Another case occurs when a migrated license is extended after its associated subscription has been canceled.

Previously, we incorrectly displayed a relative coupon discount in these cases. However, since these cases involve no pro-rated discount, and a new subscription is created to renew in 30 days or 1 year (depending on the billing cycle), a full coupon discount is now applied.

[![](https://freemius.com/blog/wp-content/uploads/2024/11/checkout-coupon-migrated-license-expired-subscription-1024x656.png)](https://freemius.com/blog/wp-content/uploads/2024/11/checkout-coupon-migrated-license-expired-subscription.png)

The UI has been updated to reflect the full coupon discount in these cases.

### Coupon discount for migrated license update without subscription

Depending on the platform a license was migrated from, some licenses may not be associated with any subscription.

[![](https://freemius.com/blog/wp-content/uploads/2024/11/checkout-coupon-migrated-license-no-subscription-1024x706.png)](https://freemius.com/blog/wp-content/uploads/2024/11/checkout-coupon-migrated-license-no-subscription.png)

For these cases, we apply pro-rated adjustments and a relative coupon discount. The UI has been updated to accurately display this information.

The reason we provide a pro-rated adjustment, rather than treating it like an expired subscription, is that we lack information on the original subscription. We offer the benefit of the doubt to encourage migration.

### Renewals discount for migrated license updates

We have a mechanism to offer [renewal discounts](https://freemius.com/help/documentation/search/renewal/#can_i_offer_a_discount_on_license_renewals) for products in general.

[![](https://freemius.com/blog/wp-content/uploads/2024/11/freemius-checkout-renewal-discount-license-update-1024x758.png)](https://freemius.com/blog/wp-content/uploads/2024/11/freemius-checkout-renewal-discount-license-update.png)

For migrated licenses, this renewal discount is applied during license updates as an incentive for migrating from a legacy platform to Freemius. This renewal discount may be relative to the first payment, depending on whether a pro-rated discount is applied. A UI bug that occasionally prevented the accurate display of this discount in certain edge cases has been resolved.

The enhancements above are part of our ongoing improvements to better support migrated subscriptions. If you’d like to migrate your product to Freemius and benefit from these features, please [get in touch](help-documentation-migration.md).

### Additional fixes for licenses and coupons

[![](https://freemius.com/blog/wp-content/uploads/2024/11/freemius-checkout-license-billing-cycle-1024x367.png)](https://freemius.com/blog/wp-content/uploads/2024/11/freemius-checkout-license-billing-cycle.png)

- For license renewals, the correct billing cycle of the license is now selected in Checkout, instead of defaulting to “Annual.” Upsell options are displayed in these cases to give buyers the option to adjust their billing cycle.

<!--THE END-->

[![](https://freemius.com/blog/wp-content/uploads/2024/11/freemius-coupon-absolute-value-current-customer-651x1024.png)](https://freemius.com/blog/wp-content/uploads/2024/11/freemius-coupon-absolute-value-current-customer.png)

- We resolved a bug where a coupon with multi-currency absolute discount values, if entered via URL parameter (or loaded from our [JS SDK](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md)) for a license restricted to “Current Customer,” was not loading correctly.

### General bug fixes

- A UI glitch affecting tablet mode has been fixed. This issue only appeared when Checkout was loaded in full-page mode, a new feature introduced in our latest latest [SDK release](https://github.com/Freemius/wordpress-sdk/releases/tag/2.9.0).